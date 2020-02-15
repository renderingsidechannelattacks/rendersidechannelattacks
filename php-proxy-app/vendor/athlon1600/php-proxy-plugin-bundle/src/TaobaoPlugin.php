<?php


namespace Proxy\Plugin;


use Proxy\Event\ProxyEvent;
use Proxy\Html;
use Proxy\Plugin\AbstractPlugin;


class TaobaoPlugin extends AbstractPlugin {

    protected $url_pattern = 'taobao.com';

    public function onCompleted(ProxyEvent $event){

        $response = $event['response'];
        $output = $response->getContent();

//          $output = preg_replace('@["\']base["\']:\s*("\')(.*?)\1@', 'masthead-positioner" style="position:static;">', $output, 1);
        $output = preg_replace_callback('@["\'](base|path)["\']\:\s*(["\'])(.*?)\2@is', array($this, 'taobao_script_attr'), $output);
//        $str = preg_replace('@["\'](base|path)["\']\:\s*(["\'])(.*?)\2@is', '\3', $str);

        $response->setContent($output);
    }


    // replace  <link href=
    private function taobao_script_attr($matches){

        // could be empty?
        $url = trim($matches[3]);

//        $schemes = array('data:', 'magnet:', 'about:', 'javascript:', 'mailto:', 'tel:', 'ios-app:', 'android-app:', 'blob:');
//        if(starts_with($url, $schemes)){
//            return $matches[0];
//        }
        return str_replace($url, 'http:'.$url, $matches[0]);
//		return 'taobao_script_attr debug';
    }


}



?>

