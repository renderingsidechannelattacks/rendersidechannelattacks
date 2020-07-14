# rendersidechannelattacks  
We study a new type of side channel in which a cross-origin adversary targets incremental rendering and measures the rendering performance between consecutive frames over time.  
This is the prototype, open-source framework, called SideR, and successfully launched three types of attacks, namely history sniffing, runtime website fingerprinting and keystroke logging, based on the framework.  
## environment  
We deploy this project on Apache2 + Flask. We also show the demo on http://renderingsidechannelattacks.com:8080/ . 
## deploy(Ubuntu)
### install mod_wsgi
sudo apt-get install libapache2-mod-wsgi python-dev  
sudo a2enmod wsgi  
### install Flask
sudo apt-get install python-pip  
#### we need use virtual environment  
sudo pip install virtualenv 
source venv/bin/activate   
sudo pip install Flask   
sudo python __init__.py 
### create apache
sudo nano /etc/apache2/sites-available/html2markdown.conf  
Also we need change the ServerName, WSGIScriptAlia and PATH  
#### start virtual host
sudo a2ensite html2markdown  
sudo service apache2 restart  
## collecting code part 
We have different versions code for collecting different data and we will show one version.  
rendersidechannelattacks/FlaskApp/FlaskApp/templates/ is for all html files and rendersidechannelattacks/FlaskApp/FlaskApp/static/ us for others like js files.  
In our basic collect version. The html file is rendersidechannelattacks/FlaskApp/FlaskApp/templates/aquarium/aquarium.html and js file is rendersidechannelattacks/FlaskApp/FlaskApp/static/aquarium.js /    
In the js file, The core part is on the line 1757 function onAnimationFrame()
##### init
On the line 1815, we will add which Website we want to test to the array. 
##### adjust workload
On the line 1853, we will make the WebGL project has balance workload for different computer before we collect data. 
##### collect data
On the line 1888, we collect data.
##### post data
On the line 2002, we send data to server.
##### History sniffing online analyze
On the line 2038, we have a online version for history sniffing analyze.
