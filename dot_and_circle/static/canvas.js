var canvas = document.querySelector('canvas');
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

var c = canvas.getContext('2d');
var circleX = Math.random() * canvas.width;
var circleY = Math.random() * canvas.height;
var circleRadius = Math.random() * 100;

var clearScreen = function () {
    c.clearRect(0, 0, canvas.width, canvas.height)
};

var drawCircle = function(x, y, radius) {
    clearScreen();
    c.strokeStyle = 'black';
    c.lineWidth = 4;
    c.beginPath();
    c.arc(x, y, radius, 0, Math.PI * 2);
    c.stroke();
};

drawCircle(circleX, circleY , circleRadius);

var checkDot = function(event) {
    checkIfDotLiesInTheCircle('/dot_and_circle/check', event, drawDot);
};

var drawDot = function(event, response) {
    console.log(response);
    c.beginPath();
    c.fillStyle = 'red';
    if(response === 'True') {
        c.fillStyle = 'green';
    }
    c.fillRect(event.clientX, event.clientY, 5, 5);
};

var checkIfDotLiesInTheCircle = function (url, event, callback) {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (xhttp.readyState == 4 && xhttp.status == 200)
            callback(event, xhttp.response);
    };
    var params ="?"+
        "radius="+circleRadius+"&"+
        "xCircle="+circleX+"&"+
        "yCircle="+circleY+"&"+
        "xPoint="+event.clientX+"&"+
        "yPoint="+event.clientY;
    xhttp.open('GET', url+params, false);
    xhttp.setRequestHeader("Content-type", "application/json");

    xhttp.send(params);
}

canvas.addEventListener('click', checkDot);