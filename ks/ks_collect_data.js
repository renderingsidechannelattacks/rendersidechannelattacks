var fs = require('fs');
var robot = require("robotjs");
// set no delay after keypress
robot.setKeyboardDelay(0);

function sleep(ms) {
  return new Promise(resolve => setTimeout(resolve, ms));
}

async function tableCallback(table){
    // this function works when table reading is finished
    var samples = [];
    // skip first row of index
    for(var i=0; i<table.length; i++){
      var row = table[i];
      var len = row[row.length-1];
      samples.push({
                  'word': '', 
                  'PRESS_TIME': [],
                  'LETTER': []
                }
      );
      for(var j=0; j<len; j++){
        samples[samples.length-1].PRESS_TIME.push(row[j+19]);
        // console.log(parseInt(row[j+4],10)+65);
        samples[samples.length-1].LETTER.push(String.fromCharCode(parseInt(row[j+4],10)+97));
      }
      samples[samples.length-1].word = samples[samples.length-1].LETTER.join('');
    }
    try{    
        //delay 10s
        // console.log('delaying 10s...please switch to search box');
        // await sleep(10000);
        // for each sample in sample, deal with time
        for (var i = 0; i<samples.length; i++){
            var LETTER = samples[i].LETTER;
            console.log(samples[i].PRESS_TIME);
            console.log(LETTER);
            //delay 10s
            console.log('delaying 2s...please start');
            await sleep(2000);
            // clear box            
            // await robot.keyToggle("a", "down", ["command"]);
            // await robot.keyTap("backspace");
            // await robot.keyToggle("a", "up", ["command"]);
            // start recording
            // TODO: send signal to aq server!
            // input word
            await input_word(samples[i].PRESS_TIME, LETTER);
            console.log('delaying 20s...please stop, save file');
            await sleep(20000);
            // stop recording
            // TODO: send signal to aq server!
        }
    } finally {
      console.log('finish');
    }
    console.log('read table finished');
}

function ConvertToTable(data, callBack) {
  data = data.toString();
  var table = new Array();
  var rows = new Array();
  rows = data.split("\n");
  for (var i = 0; i < rows.length; i++) {
      table.push(rows[i].split(",")); // one row, one word
  }
  callBack(table);
}

function Main(fileName){
  fs.readFile(fileName, function (err, data){
    var table = new Array();
    if (err) {
        console.log(err.stack);
        return;
    }
    ConvertToTable(data, tableCallback);
  });
}

// call by each word
async function input_word(PRESS_TIME, LETTER) {
  var realTime = [];
  try {
    await sleep(5000); // let FPS of canvas go steadily
    // send every key except the last key
    for(var i = 0; i<PRESS_TIME.length-1; i++){
        await robot.keyTap(LETTER[i]);
        realTime.push(Date.now());
        // await sleep(2000);
        await sleep(PRESS_TIME[i]);
    }
    // send last key
    await robot.keyTap(LETTER[PRESS_TIME.length-1]);
    realTime.push(Date.now());
    // await sleep(2000);
  } finally {
    //  path = 'data/' + WORD
    path = 'data/' + 'elections'
    if(!fs.existsSync(path))
      fs.mkdirSync(path) 
    fs.writeFile( path + '/' + realTime[0] + '.txt', realTime + '$' + LETTER, (err) => {
      if (err) throw err;
      console.log(LETTER.join('') + ' is saved!');
    });
  }
};

keystrokeFile = 'keystroke_dataset/data.csv'

Main(keystrokeFile);
