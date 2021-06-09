/*
 * Fired when use's mouse enters the location where the image will be replaced with a 3s gif
 * output in current page console a prompt
 */
$(document).ready(function($) {
    // console.log('Hello Developer');
    var times = 0;
    $("body").on("click",function(){
        console.log(window.performance.now());
        console.log("click");
    });
    $("body").on(
        {
            mouseenter: function () {
                // console.log(times++);
                console.log(window.performance.now());
                console.log('hover');
            }
        }
        ,
        ".yt-shelf-grid-item, \
        .yt-lockup-tile .yt-lockup-thumbnail, .expanded-shelf-content-item .thumb-wrapper, \
        .video-list-item, \
        ytd-thumbnail.ytd-grid-video-renderer, \
        ytd-thumbnail.ytd-video-renderer, \
        ytd-thumbnail.ytd-newspaper-mini-video-renderer, \
        ytd-thumbnail.ytd-compact-video-renderer"
    );

});


/* 
 * Fired when a tab's visibility is changed (minimized or swith to another tab in the same window)
 * output in current page console a prompt
 */
// console.log("visProp");
// to support older version browsers, add prefixes
function getVisibilityState() {
    var prefixes = ['webkit', 'moz', 'ms', 'o'];
    if ('visibilityState' in document) return 'visibilityState';
    for (var i = 0; i < prefixes.length; i++) {
        if ((prefixes[i] + 'VisibilityState') in document)
            return prefixes[i] + 'VisibilityState';
    }
    // otherwise it's not supported
    return null;
}


var visProp = getVisibilityState();
// console.log(visProp);
var evtname = visProp.replace(/[V|v]isibilityState/, '') + 'visibilitychange';
// console.log(evtname);
document.addEventListener(evtname, function () {
    console.log("visibilitychanged");
    console.log("NOW: " + document[visProp]);
},false);



/*
 listen input in the site
 */
document.addEventListener('input', logKey);

function logKey(e) {
    console.log(window.performance.now());
    console.log(e.target.value);
  // log.textContent += ` ${e.code}`;
}







