document.addEventListener('DOMContentLoaded', function() {
    (async () => {
        const fingerprint = await fpCollect.generateFingerprint();
        const rowsFingerprint = [];
        rowsFingerprint.push('<tr><th>Attribute</th><th class="breakword">Value</th><tr/>');
        Object.keys(fingerprint).forEach(function(key) {
            if (key === 'canvas') {
                rowsFingerprint.push('<tr><td>' + key + '</td><td class="breakword"><img src="' + fingerprint[key].image + '"></td><tr/>');
            } else {
                rowsFingerprint.push('<tr><td>' + key + '</td><td class="breakword">' + JSON.stringify(fingerprint[key]) + '</td><tr/>');
            }
        });
        document.getElementById('fp').innerHTML = rowsFingerprint.join('');
        const xhr = new XMLHttpRequest();
        xhr.onreadystatechange = function() {
            if (xhr.readyState === 4 && xhr.status === 200) {
                const scannerResults = JSON.parse(xhr.responseText);
                const INCONSISTENT = 1;
                const UNSURE = 2;
                const CONSISTENT = 3;
                const resultToLabel = new Map([
                    [INCONSISTENT, 'Inconsistent'],
                    [UNSURE, 'Unsure'],
                    [CONSISTENT, 'Consistent']
                ]);
                const rowsScanner = [];
                rowsScanner.push('<tr><th>Test</th><th class="breakword">Result</th><th>Data</th><tr/>');
                Object.keys(scannerResults).forEach(function(key) {
                    let resultTest = scannerResults[key];
                    let color = 'green';
                    if (resultTest.consistent === INCONSISTENT)
                        color = 'red';
                    rowsScanner.push('<tr><td style="color:' + color + ';">' + key + '</td><td class="breakword" style="color:' + color + '">' + resultToLabel.get(resultTest.consistent) + '</td><td style="color:' + color + ';">' + JSON.stringify(resultTest.data) + '</td><tr/>');
                });
                document.getElementById('scanner').innerHTML = rowsScanner.join('');
            }
        };
        xhr.open('POST', '/bots/collectfp');
        xhr.setRequestHeader('Content-Type', 'application/json');
        fingerprint.uuid = uuid;
        fingerprint.url = window.location.href;
        xhr.send(JSON.stringify(fingerprint));
    })();
});
(function(i, s, o, g, r, a, m) {
    i['GoogleAnalyticsObject'] = r;
    i[r] = i[r] || function() {
        (i[r].q = i[r].q || []).push(arguments)
    }, i[r].l = 1 * new Date();
    a = s.createElement(o), m = s.getElementsByTagName(o)[0];
    a.async = 1;
    a.src = g;
    m.parentNode.insertBefore(a, m)
})(window, document, 'script', '//ant.antoinevastel.com/analytics.js', 'ga');
ga('provide', 'adblockTracker', function(tracker, opts) {
    var xhr = new XMLHttpRequest(),
        method = "GET",
        url = "//ant.antoinevastel.com/advertisement.js";
    try {
        xhr.open(method, url, false);
        xhr.send();
        ga('set', 'dimension' + opts.dimensionIndex, xhr.responseText != "var canRunAds=true;");
    } catch {
        ga('set', 'dimension' + opts.dimensionIndex, xhr.responseText != "var canRunAds=true;");
    }
});
ga('create', 'UA-43580478-4', 'auto');
ga('require', 'adblockTracker', {
    dimensionIndex: 1
});
ga('send', 'pageview');
const xhr2 = new XMLHttpRequest();
xhr2.open('POST', '/bots/datadome');
xhr2.setRequestHeader('Content-Type', 'application/json');
xhr2.send(JSON.stringify({
    d: Date.now()
}));