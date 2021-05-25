# Rendersidechannelattacks  
We design a novelty rendering contentionchannel. Specifically, we stress the browser’s rendering re-source with a stable, self-adjustable WebGL program and mea-sure the time taken to render a sequence of frames. The mea-sured time sequence is further used to infer any co-renderingevent of the browser.  
To demonstrate the channel’s feasibility, we design and im-plement a prototype, open-source framework, calledSIDER,to launch four attacks using the rendering contention channel,which are (i) cross-browser, cross-mode cookie synchronization, (ii) history sniffing, (iii) website fingerprinting, and (iv)keystroke logging.  
## Environment  
We deploy this project on Apache2 + Flask. We also show the demo on http://renderingsidechannelattacks.com:8080/ . 
## Deploy(Ubuntu Apache2 + Flask)
### install mod_wsgi
`sudo apt-get install libapache2-mod-wsgi python-dev`   
`sudo a2enmod wsgi  `  
### install Flask
`sudo apt-get install python-pip  `
#### we need use virtual environment  
`sudo pip install virtualenv `  
`source venv/bin/activate  `   
`sudo pip install Flask  `  
`sudo python __init__.py `  
### create apache
`sudo nano /etc/apache2/sites-available/html2markdown.conf ` 
Also we need change the ServerName, WSGIScriptAlia and PATH  
#### start virtual host
`sudo a2ensite html2markdown  `  
`sudo service apache2 restart  `  

## Deploy(Ubuntu PHP-Proxy)
<div class="text-blue mb-2">
will add this part later.
</div>

## Code repository
We have different versions code for collecting different data and we will show one version.  
rendersidechannelattacks/FlaskApp/FlaskApp/templates/ is for all html files and rendersidechannelattacks/FlaskApp/FlaskApp/static/ us for others like js files.  

### Proxy Server(escape option)
<div class="text-blue mb-2">
will add this part later.
</div>

### Cross-browser, cross-mode cookie synchronization
<div class="text-blue mb-2">
will add this part when I update the code.
1. Change 01 --> word
2. Automatic deployment
</div>

### History sniffing attack
In our basic collect version. The html file is rendersidechannelattacks/FlaskApp/FlaskApp/templates/aquarium/aquarium.html and js file is rendersidechannelattacks/FlaskApp/FlaskApp/static/aquarium.js /   
Functionality | Code | Description
------------ | -------------| -------------
Initialization | 1855-1876 | For different devices, give a similar workload.
Data Collection | 1890-1980 | Collecting data.
Denoising | 2042-2084 | Algorithm 1 Denoising.
Outlier Detection | 2094-2101 | Algorithm 2 Max-min Outlier Detection
DTW-M | 2127-2155 | Algorithm DTW

### Website fingerprinting attack
Share Initialization, Data Collection and Denoising part with History sniffing.
<div class="text-blue mb-2">
Will add model part
</div>

### Keystroke logging attack
#### Prerequisite
`npm install robotjs`

#### Procedure
1. modify in `ks_collect_data.js` line 107 to switch to the data file you like
2. close all chrome windows
3. open <http://3.221.81.120/gpu_attack.github.io/aquarium/aquarium.html> in a new chrome window
4. open <http://www.google.com/> in a new chrome window
5. select search box
6. run “node ks_collect_data.js”
7. **SWITCH TO GOOGLE SEARCH BOX!!!**
8. get the data!

#### Data

local: [timestamp] list, [key] list

server: [timestamp, how many seconds each frame takes up] list
