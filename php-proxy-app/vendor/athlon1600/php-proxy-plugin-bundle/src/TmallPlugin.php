<?php


namespace Proxy\Plugin;

use Proxy\Plugin\AbstractPlugin;
use Proxy\Event\ProxyEvent;
use Proxy\Html;

class TmallPlugin extends AbstractPlugin {

    protected $url_pattern = 'login.tmall.com';

    public function onCompleted(ProxyEvent $event){

        $response = $event['response'];
        $output = $response->getContent();
//        $output = preg_replace('@(</title>)(\s*)@', \1 . '<meta name="referrer" content="no-referrer" />', $output);
        $output = preg_replace('@document.domain\s*=\s*[^;]*?;@', 'document.domain = \'3.221.81.120\';', $output);

        $response->setContent($output);
    }
}

?>