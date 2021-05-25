# Rendersidechannelattacks  
we design a novelty rendering contentionchannel. Specifically, we stress the browser’s rendering re-source with a stable, self-adjustable WebGL program and mea-sure the time taken to render a sequence of frames. The mea-sured time sequence is further used to infer any co-renderingevent of the browser.  
To demonstrate the channel’s feasibility, we design and im-plement a prototype, open-source framework, calledSIDER,to launch four attacks using the rendering contention channel,which are (i) cross-browser, cross-mode cookie synchroniza-tion, (ii) history sniffing, (iii) website fingerprinting, and (iv)keystroke logging.  
## Environment  
We deploy this project on Apache2 + Flask. We also show the demo on http://renderingsidechannelattacks.com:8080/ . 
## Deploy(Ubuntu)
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

## Code repository
We have different versions code for collecting different data and we will show one version.  
rendersidechannelattacks/FlaskApp/FlaskApp/templates/ is for all html files and rendersidechannelattacks/FlaskApp/FlaskApp/static/ us for others like js files.  
In our basic collect version. The html file is rendersidechannelattacks/FlaskApp/FlaskApp/templates/aquarium/aquarium.html and js file is rendersidechannelattacks/FlaskApp/FlaskApp/static/aquarium.js /    
In the js file, The core part is on the line 1757 function onAnimationFrame()

### History sniffing attack
In our basic collect version. The html file is rendersidechannelattacks/FlaskApp/FlaskApp/templates/aquarium/aquarium.html and js file is rendersidechannelattacks/FlaskApp/FlaskApp/static/aquarium.js /   
Functionality | Code | Description
Initialization | 1855-1876 | For different devices, give a similar workload.
Denoising | ------------- | -------------
Denoising | ------------- | -------------
Denoising | ------------- | -------------
Denoising | ------------- | -------------

Denoising | ------------- 
Denoising | ------------- 
Denoising | ------------- 
Content from cell 1 | Content from cell 2
Content in the first column | Content in the second column

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
