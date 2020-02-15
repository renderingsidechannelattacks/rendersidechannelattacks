<?php


namespace Proxy;


class JavaScript{

//    public static function parse_scripts($html){
//        $html = preg_replace('/<\s*script[^>]*>(.*?)<\s*\/\s*script\s*>/is', '', $html);
//        return $html;
//    }




    /*****************************************************************
     * Javascript parser - main parsing function
     *
     * The specific parts that need proxying depends on which javascript
     * functions we've been able to override. On first page load, the browser
     * capabilities are tested to see what we can do client-side and the results
     * sent back to us. This allows us to parse only what we have to.
     * If $CONFIG['override_javascript'] is disabled, all commands are parsed
     * server-side. This will use much more CPU!
     *
     * Commands to proxy only if no override at all:
     *	 document.write()
     *	 document.writeln()
     *	 window.open()
     *	 eval()
     *
     * Commands to proxy, regardless of browser capabilities:
     *	 location.replace()
     *	 .innerHTML=
     *
     * Commands to proxy if the extra "watch" flag is set
     * (the browser doesn't support the .watch() method):
     *	 location=
     *	 x.location=
     *	 location.href=
     *
     * Commands to proxy if the extra "setters" flag is set
     * (the browser doesn't support the __defineSetter__() method):
     *	 .src=
     *	 .href=
     *	 .background=
     *	 .action=
     *
     * Commands to proxy if the extra "ajax" flag is set
     * (the browser failed to override the .open() method):
     *	 XMLHttpRequest.open()
     ******************************************************************/

    public static function parse_scripts($input) {

        # Unless we know we don't need to, apply all the browser-specific flags
        $flags = array('ajax', 'watch', 'setters');

        # Start parsing!
        $search = array();

        # Create shortcuts to various search patterns:
        #	  "before"	  - matches preceeding character (string of single char) [ignoring whitespace]
        #	  "after"	  - matches next character (string of single char) [ignoring whitespace]
        #	  "id"		  - key for identifying the original match (e.g. if we have >1 of the same key)
        $assignmentPattern	= array('before'	  => '.',				  'after' => '=');
        $methodPattern			= array('before'	  => '.',				  'after' => '(');
        $functionPattern		= array('after' => '(');

        # Configure strings to search for, starting with always replaced commands
        $search['innerHTML'][] = $assignmentPattern;
        $search['location'][]  = array('after' => '.', 'id' => 'replace()');
        # ^ This is only for location.replace() - other forms are handled later

        # Look for attribute assignments
        if ( in_array('setters', $flags) ) {
            $search['src'][]			= $assignmentPattern;
            $search['href'][]			= $assignmentPattern;
            $search['action'][]		= $assignmentPattern;
            $search['background'][] = $assignmentPattern;
        }

        # Look for location changes
        # location.href will be handled above, location= is handled here
        if ( in_array('watch', $flags) ) {
            $search['location'][] = array('after' => '=', 'id' => 'assignment');
        }

        # Look for .open() if either AJAX (XMLHttpRequest.open) or
        # base (window.open) flags are present
        if ( in_array('ajax', $flags) || in_array('base', $flags) ) {
            $search['open'][] = $methodPattern;
        }

        # Add the basic code if no override
        if ( in_array('base', $flags) ) {
            $search['eval'][]		= $functionPattern;
            $search['writeln'][]	  = $methodPattern;
            $search['write'][]	= $methodPattern;
        }

        # Set up starting parameters
        $offset			= 0;
        $length			= strlen($input);
        $searchStrings = array_keys($search);

        while ( $offset < $length ) {

            # Start off by assuming no more items (i.e. the next position
            # of interest is the end of the document)
            $commandPos = $length;

            # Loop through the search subjects
            foreach ( $searchStrings as $item ) {

                # Any more instances of this?
                if ( ( $tmp = strpos($input, $item, $offset) ) === false ) {

                    # Nope, skip to next item
                    continue;

                }


                # Closer to the currently held 'next' position?
                if ( $tmp < $commandPos ) {

                    $commandPos = $tmp;
                    $command = $item;

                }

            }

            # No matches found? Finish parsing.
            if ( $commandPos == $length ) {
                break;
            }

            # We've found the main point of interest; now use the
            # search parameters to check the surrounding chars to validate
            # the match.
            $valid = false;

            foreach ( $search[$command] as $pattern ) {

                # Check the preceeding chars
                if ( isset($pattern['before']) && str_checkprev($input, $pattern['before'], $commandPos-1) === false ) {
                    continue;
                }

                # Check next chars
                if ( isset($pattern['after']) && ( $postCharPos = str_checknext($input, $pattern['after'], $commandPos + strlen($command), false, true) ) === false ) {
                    continue;
                }

                # Still here? Match must be OK so generate a match ID
                if ( isset($pattern['id']) ) {
                    $valid = $command . $pattern['id'];
                } else {
                    $valid = $command;
                }

                break;

            }

            # What we do next depends on which match (if any) we've found...
            switch ( $valid ) {

                # Assigment
                case 'src':
                case 'href':
                case 'background':
                case 'action':
                case 'locationassignment':
                case 'innerHTML':

                    # Check our post-char position for = as well (could be equality
                    # test rather than assignment, i.e. == )
                    if ( ! isset($input[$postCharPos]) || $input[$postCharPos] == '=' ) {
                        break;
                    }

                    # Find the end of this statement
                    $endPos = analyze_js($input, $postCharPos);
                    $valueLength = $endPos - $postCharPos;

                    # Produce replacement command
                    $replacement = sprintf('parse%s(%s)', $command=='innerHTML' ? 'HTML' : 'URL', substr($input, $postCharPos, $valueLength));

                    # Adjust total document length as appropriate
                    $length += strlen($replacement);

                    # Make the replacement
                    $input = substr_replace($input, $replacement, $postCharPos, $valueLength);

                    # Move offset up to new position
                    $offset = $endPos + 10;

                    # Go get next match
                    continue 2;


                # Function calls - we don't know for certain if these are in fact members of the
                # appropriate objects (window/XMLHttpRequest for .open(), document for .write() and
                # .writeln) so we won't change anything. Main.js still overrides these functions but
                # does nothing with them by default. We add an extra parameter to tell our override
                # to kick in.
                case 'open':
                case 'write':
                case 'writeln':

                    # Find the end position (the closing ")" for the function call)
                    $endPos = analyze_js($input, $postCharPos);

                    # Insert our additional argument just before that
                    $input = substr_replace($input, ',"gl"', $endPos, 0);

                    # Adjust the document length
                    $length += 5;

                    # And move the offset
                    $offset = $endPos + 5;

                    # Get next match
                    continue 2;


                # Eval() is a just as easy since we can just wrap the entire thing in parseJS().
                case 'eval':

                    # Ensure this is a call to eval(), not anotherfunctionendingineval()
                    if ( isset($input[$commandPos-1]) && strpos('abcdefghijklmnopqrstuvwxyz123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ_', $input[$commandPos-1]) !== false ) {
                        break;
                    }

                    # Find the end position (the closing ")" for the function call)
                    $endPos = analyze_js($input, $postCharPos);
                    $valueLength = $endPos - $postCharPos;

                    # Generate our replacement
                    $replacement = sprintf('parseJS(%s)', substr($input, $postCharPos, $valueLength));

                    # Make the replacement
                    $input = substr_replace($input, $replacement, $postCharPos, $valueLength);

                    # Adjust the document length
                    $length += 9;

                    # And move the offset
                    $offset = $endPos + 9;
                    continue 2;


                # location.replace() is a tricky one. We have the position of the char
                # after . as $postCharPos and need to ensure we're calling replace(),
                # then parse the entire URL
                case 'locationreplace()':

                    # Validate the match
                    if ( ! preg_match('#\Greplace\s*\(#', $input, $tmp, 0, $postCharPos) ) {
                        break;
                    }

                    # Move $postCharPos to inside the brackets of .replace()
                    $postCharPos += strlen($tmp[0]);

                    # Find the end position (the closing ")" for the function call)
                    $endPos = analyze_js($input, $postCharPos);
                    $valueLength = $endPos - $postCharPos;

                    # Generate our replacement
                    $replacement = sprintf('parseURL(%s)', substr($input, $postCharPos, $valueLength));

                    # Make the replacement
                    $input = substr_replace($input, $replacement, $postCharPos, $valueLength);

                    # Adjust the document length
                    $length += 9;

                    # And move the offset
                    $offset = $endPos + 9;

                    continue 2;

            }

            # Still here? A match didn't validate so adjust offset to just after
            # current position
            $offset = $commandPos + 1;

        }

        # Ignore document.domain
        $input = str_replace('document.domain', 'ignore', $input);

        # Return changed
        return $input;

    }

}


