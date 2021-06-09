
<center>
# php-proxy-app

based on the origin project

make some modification according to our needs

--------

Web Proxy Application built on [**php-proxy library**](https://github.com/Athlon1600/php-proxy) ready to be installed on your server

![alt text](http://i.imgur.com/KrtU5KE.png?1 "This is how PHP-Proxy looks when installed")



## Web-Proxy vs Proxy Server

Keep in mind that sites/pages that are too script-heavy or with too many "dynamic parts", may not work with this proxy script.
That is a known limitation of web proxies. For such sites, you should use an actual proxy server to route your browser's HTTP requests through:  

https://www.proxynova.com/proxy-software/



#### config.php

This file will be loaded into the global Config class.

#### /templates/

This should have been named "views", but for historic purposes we keep it named as templates for now.

#### /plugins/

PHP-Proxy provides many of its own native plugins, but users are free to write their own custom plugins, which could then be automatically loaded from this very folder. See /plugins/TestPlugin.php for an example.
