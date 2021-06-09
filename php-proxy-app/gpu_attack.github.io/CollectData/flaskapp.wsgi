#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/home/ubuntu/Sites/php-proxy-app/gpu_attack.github.io/CollectData") 

from CollectData import app as application
application.secret_key = 'Add your secret key'
