var canvas = document.querySelector('canvas')
canvas.width = window.innerWidth;
canvas.height = window.innerHeight;

var c = canvas.getContext('2d');
var circleX = Math.random() * canvas.width;
var circleY = Math.random() * canvas.height
var circleRadius = Math.random() * 100

var clearScreen = function () {
    c.clearRect(0, 0, canvas.width, canvas.height)
};

var drawcicle = function(x, y, radius) {
    clearScreen();
    c.strokeStyle = 'black';
    c.lineWidth = 4;
    c.beginPath();
    c.arc(x, y, radius, 0, Math.PI * 2);
    c.stroke();
};

drawcicle(circleX, circleY , circleRadius);

var drawDot = function(event) {
    c.fillStyle = 'green';
    c.beginPath();
    c.fillRect(event.clientX, event.clientY, 5, 5);
}

canvas.addEventListener('click', drawDot);