var interval = null;
function startCheck() {
  interval = setInterval(checkFinished, 500);
}

function checkFinished() {
  console.log("checking");
  const Http = new XMLHttpRequest();
  const url='http://3.15.200.178:8080/checkFinished';
  Http.open("GET", url);
  Http.send();

  Http.onreadystatechange = (e) => {
    res = Http.responseText;
    console.log(res);
    if(res === 'True') {
      clearInterval(interval);
      whenFinishedDo();
    }
  }
}

function whenFinishedDo(){
  document.getElementById('show').innerHTML = "Finished";
}
