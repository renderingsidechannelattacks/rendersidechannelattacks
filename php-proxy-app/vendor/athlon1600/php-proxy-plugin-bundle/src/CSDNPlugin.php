<?php


namespace Proxy\Plugin;


use Proxy\Plugin\AbstractPlugin;
use Proxy\Event\ProxyEvent;
use Proxy\Html;


class CSDNPlugin extends AbstractPlugin {

    protected $url_pattern = 'csdn.net';

    public function onCompleted(ProxyEvent $event){

        $response = $event['response'];
        $output = $response->getContent();
//        $output = preg_replace('@(</title>)(\s*)@', \1 . '<meta name="referrer" content="no-referrer" />', $output);
        $output = preg_replace('@<\/title>\s*@', '</title><meta name="referrer" content="no-referrer" />', $output);
        $response->setContent($output);
    }
}

?>
