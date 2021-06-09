<?php

namespace Proxy\Plugin;


use Proxy\Plugin\AbstractPlugin;
use Proxy\Event\ProxyEvent;

use Proxy\Html;

class IMDBPlugin extends AbstractPlugin
{

    protected $url_pattern = 'imdb.com';

//	// force old imdb layout!
//    public function onBeforeRequest(ProxyEvent $event)
//    {
//        $event['request']->headers->set('Cookie', 'PREF=f6=8');
//        $event['request']->headers->set('User-Agent', 'Opera/7.50 (Windows XP; U)');
//    }

    public function onCompleted(ProxyEvent $event)
    {

        $response = $event['response'];
        $url = $event['request']->getUrl();
//        console_log('IMDB onCompleted: '. $url);
//        console_log('youtube_plugin_before: '. $event['request']);

        $output = $response->getContent();

        // remove top banner that's full of ads
        $output = Html::remove("#header", $output);

        // do this on all youtube pages
        $output = preg_replace('@masthead-positioner">@', 'masthead-positioner" style="position:static;">', $output, 1);

        // data-thumb holds real image when it is available!
        $output = preg_replace_callback('/<img[^>]+data-thumb="(.*?)"[^>]*/is', function ($matches) {

            // may or may not have src= attribute
            $has_src = strpos($matches[0], 'src="') !== false;

            // proxified thumb url
            $thumb_url = whole_url($matches[1], false);

            if ($has_src) {
                // TODO: maybe remove data-thumb too?
                $matches[0] = str_replace('data-thumb', 'remove-this', $matches[0]);
                return preg_replace('/src="(.*?)"/i', 'src_replaced="1" src="' . $thumb_url . '"', $matches[0]);
            }

            return preg_replace('/data-thumb="(.*?)"/i', 'src_added="1" src="' . $thumb_url . '"', $matches[0]);
        }, $output);

        $IMDB = new IMDBDownloader();
        // cannot pass HTML directly because all the links in it are already "proxified"...
        $links = $IMDB->getDownloadLinks($url, "mp4 360, mp4");
//        console_log('IMDB_plugin_before: '. $url);

        if ($links) {

            $url = $links['url'];

            $player = vid_player($url, 640, 390, 'mp4');

            // this div blocks our player controls
//            $output = Html::remove("#theater-background", $output);

            // replace youtube player div block with our own
            $output = $output.$player;
//            $output = Html::replace_inner("#video-player__video", $player, $output);

        }

        // causes too many problems...
//        $output = Html::remove_scripts($output);

        $response->setContent($output);
    }
}

