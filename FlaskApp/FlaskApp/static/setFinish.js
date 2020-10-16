var iframeelement = [];
var testWebsite = [];
var testWebsiteID = 0;
var recordValue = 0;
function doWork() {
  clearDb();
  time = performance.now();
  while (performance.now() - time < 10000);
    sendFinished();
  for (let i = 1; i <=50; i++){
      iframeelement[i] = document.getElementById('testiframe' + i);
      console.log(iframeelement[i]);
  }
      // testWebsite.push('https://9gag.com/');
      // testWebsite.push('https://adf.ly/');
      // testWebsite.push('https://www.aliexpress.com/');
      // testWebsite.push('https://www.amazon.com/');
      // testWebsite.push('https://www.aol.com/');
      // testWebsite.push('https://archive.org/');
      // testWebsite.push('https://www.blizzard.com/en-us/?ref=battle.net');
      // testWebsite.push('https://www.booking.com/');
      // testWebsite.push('https://www.bukalapak.com/');
      // testWebsite.push('https://conservativetribune.com/');
      // testWebsite.push('https://www.dailymotion.com/us');
      // testWebsite.push('https://www.deviantart.com/');
      // testWebsite.push('https://www.digikala.com/');
      // testWebsite.push('http://doublepimp.com/Account/LogIn');
      // testWebsite.push('https://www.espncricinfo.com/');
      // testWebsite.push('https://www.extratorrents-cc.com/');
      // testWebsite.push('https://blog.feedly.com/');
      // testWebsite.push('https://github.com/');
      // testWebsite.push('https://www.godaddy.com/');
      // testWebsite.push('http://3.15.200.178/index.php?q=https%3A%2F%2Fwww.google.com%2F');
      // testWebsite.push('https://us.hola.com/');
      // testWebsite.push('https://www.imdb.com/');
      // testWebsite.push('https://www.intuit.com/');
      // testWebsite.push('https://www.leboncoin.fr/');
      // testWebsite.push('https://www.livejasmin.com/en/girls/');
      // testWebsite.push('https://www.ltn.com.tw/');
      // testWebsite.push('https://www.mozilla.org/en-US/');
      // testWebsite.push('https://www.naver.com/');
      // testWebsite.push('https://www.nicovideo.jp/');
      // testWebsite.push('https://www.ntd.com/');
      // testWebsite.push('https://onedio.com/');
      // testWebsite.push('https://www.oracle.com/index.html');
      // testWebsite.push('https://www.outbrain.com/');
      // testWebsite.push('https://www.popads.net/');
      // testWebsite.push('https://www.researchgate.net/');
      // testWebsite.push('https://www.rt.com/');
      // testWebsite.push('https://www.scribd.com/');
      // testWebsite.push('https://soundcloud.com/');
      // testWebsite.push('https://www.spotify.com/us/');
      // testWebsite.push('https://stackexchange.com/');
      // testWebsite.push('https://steamcommunity.com/');
      // testWebsite.push('https://t.co/');
      // testWebsite.push('https://www.thesaurus.com/');
      // testWebsite.push('https://www.tokopedia.com/');
      // testWebsite.push('https://www.tribunnews.com/');
      // testWebsite.push('https://twitter.com/explore');
      // testWebsite.push('https://www.fandom.com/explore');
      // testWebsite.push('https://www.wittyfeed.tv/explore');
      // testWebsite.push('https://www.xvideos.com/');
      // testWebsite.push('https://www.yelp.com/');
      testWebsite.push('https://www.abs-cbn.com/');
      testWebsite.push('https://www.adobe.com/');
      testWebsite.push('https://allegro.pl/');
      testWebsite.push('https://aws.amazon.com/');
      testWebsite.push('https://www.apple.com/');
      testWebsite.push('http://askcom.me/');
      testWebsite.push('https://www.blastingnews.com/');
      testWebsite.push('https://www.breitbart.com/');
      testWebsite.push('https://www.businessinsider.com/');
      testWebsite.push('https://www.dailymail.co.uk/ushome/index.html');
      testWebsite.push('https://www.detik.com/');
      testWebsite.push('https://www.dictionary.com/');    
      testWebsite.push('https://hclips.com/');
      testWebsite.push('https://www.ebay.com//');
      testWebsite.push('https://www.riotgames.com/en');
      testWebsite.push('https://www.facebook.com/');
      testWebsite.push('https://www.gamepedia.com/');
      testWebsite.push('http://go.com/');
      testWebsite.push('https://www.goodreads.com/');
      testWebsite.push('https://hclips.com/');
      testWebsite.push('https://hotmovs.com/');
      testWebsite.push('https://www.instructure.com/');
      testWebsite.push('https://www.kompas.com/');
      testWebsite.push('https://www.liputan6.com/');
      testWebsite.push('https://www.livejournal.com/');
      testWebsite.push('microsoftonline.com');
      testWebsite.push('https://www.msn.com/');
      testWebsite.push('https://www.netflix.com/');
      testWebsite.push('https://www.nih.gov/');
      testWebsite.push('https://www.office.com/');
      testWebsite.push('https://www.alliance4creativity.com/where-to-watch/');
      testWebsite.push('https://ouo.io/');
      testWebsite.push('https://www.pinterest.com/');
      testWebsite.push('https://www.quora.com/');
      testWebsite.push('https://www.roblox.com/');
      testWebsite.push('http://rutracker.org/forum/index.php');
      testWebsite.push('https://www.skype.com/en/');
      testWebsite.push('https://sourceforge.net/');
      testWebsite.push('https://spotscenered.info/');
      testWebsite.push('https://www.zhihu.com/signin?next=%2F');
      testWebsite.push('https://store.steampowered.com/');
      testWebsite.push('https://www.theguardian.com/us');
      testWebsite.push('https://www.tistory.com/');
      testWebsite.push('https://torrentz2.eu/');
      testWebsite.push('https://www.baidu.com/');
      testWebsite.push('https://weather.com/');
      testWebsite.push('https://www.wikipedia.org/');
      testWebsite.push('https://xhamster.com/');
      testWebsite.push('https://yandex.ru/');
      testWebsite.push('https://zippyshare.com/');
      
  
      //exoclick.com
      //stackoverflow
      //facebook
      //https://www.tumblr.com/
      testWebsiteNumber = testWebsite.length;
      // console.log(testWebsite);
      iframeelement[testWebsiteID + 1].src = testWebsite[testWebsiteID];
}

function recordTime(){
  recordValue++;
  console.log(recordValue);
  if (recordValue > 50){
    sendFinished();
    // console.log("in",recordValue);
    console.log(iframeelement[testWebsiteID + 1])
    iframeelement[testWebsiteID + 1].parentNode.removeChild(iframeelement[testWebsiteID + 1]);
    console.log(performance.now());
    testWebsiteID++;
    if (testWebsiteID < 50){
      time = performance.now();
      while (performance.now() - time < 1000);
        loadNew();
    }
  }
  
}

function loadNew(){
  iframeelement[testWebsiteID + 1].src = testWebsite[testWebsiteID];
}


function sendFinished() {
  console.log("start send");
  const Http = new XMLHttpRequest();
  const url='http://3.15.200.178:8080/setFinished';
  Http.open("GET", url);
  Http.send();

  Http.onreadystatechange = (e) => {
    console.log(Http.responseText);
    console.log(testWebsiteID);
  }
}

function clearDb() {
  console.log("clearDb");
  const Http = new XMLHttpRequest();
  const url='http://3.15.200.178:8080/clearDb';
  Http.open("GET", url);
  Http.send();

  Http.onreadystatechange = (e) => {
    console.log(Http.responseText);
  }
}
