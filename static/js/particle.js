
// particle


const canvas = document.getElementById("canvas1");
const ctx = canvas.getContext("2d");
canvas.width = canvas.parentElement.clientWidth;
canvas.height = canvas.parentElement.clientHeight;
let particleArray = [];

// Get mouse position
let mouse = {
    x: null,
    y: null,
    radius: 80
};

window.addEventListener('mousemove', function(event) {
    mouse.x = event.x - canvas.getBoundingClientRect().left;
    mouse.y = event.y - canvas.getBoundingClientRect().top;
});

function drawImage() {

    let imageWidth = png.width || png.naturalWidth;
    let imageHeight = png.height || png.naturalHeight;

    const data = ctx.getImageData(0, 0, imageWidth, imageHeight);
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    class Particle {
        constructor(x, y, color) {

            this.x = x + canvas.width / 2 - png.width * 2;
            this.y = y + canvas.height / 2 - png.height * 2;
            
            this.color = color;
            // this.size = 2;
            // this.size = 1.5;
            // this.size = 0.9;
            this.size = 1;
            this.baseX = this.x;
            this.baseY = this.y;
            this.density = (Math.random() * 10) + 2;
        }
        draw() {
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.closePath();
            ctx.fillStyle = this.color;
            ctx.fill();
        }
        update() {
            let dx = mouse.x - this.x;
            let dy = mouse.y - this.y;
            let distance = Math.sqrt(dx * dx + dy * dy);
            let forceDirectionX = dx / distance;
            let forceDirectionY = dy / distance;
            var maxDistance = 80;
            var force = (maxDistance - distance) / maxDistance;
            if (force < 0) force = 0;
            let directionX = (forceDirectionX * force * this.density) * 0.9;
            let directionY = (forceDirectionY * force * this.density) * 0.9;

            if (distance < mouse.radius + this.size) {
                this.x -= directionX;
                this.y -= directionY;
            } else {
                if (this.x !== this.baseX) {
                    let dx = this.x - this.baseX;
                    this.x -= dx / 5;
                }
                if (this.y !== this.baseY) {
                    let dy = this.y - this.baseY;
                    this.y -= dy / 5;
                }
            }
            this.draw();
        }
    }

    function init() {
        particleArray = [];
        for (let y = 0, y2 = data.height; y < y2; y++) {
            for (let x = 0, x2 = data.width; x < x2; x++) {
                if (data.data[(y * 4 * data.width) + (x * 4) + 3] > 128) {
                    let positionX = x * 4;
                    let positionY = y * 4;
                    let color = "rgb(" + data.data[(y * 4 * data.width) + (x * 4)] + "," + data.data[(y * 4 * data.width) + (x * 4) + 1] + "," + data.data[(y * 4 * data.width) + (x * 4) + 2] + ")";
                    particleArray.push(new Particle(positionX, positionY, color));
                }
            }
        }
    }

    function animate() {
        requestAnimationFrame(animate);
        ctx.fillStyle = 'rgba(0, 0, 0, 0.2)';
        // ctx.fillStyle = 'rgba(255, 255, 255, 0.2)';

        ctx.fillRect(0, 0, canvas.width, canvas.height);
        for (let i = 0; i < particleArray.length; i++) {
            particleArray[i].update();
        }
    }

    init();
    animate();

    window.addEventListener('resize', function() {
        canvas.width = canvas.parentElement.clientWidth;
        canvas.height = canvas.parentElement.clientHeight;
        init();
    });
}

// Load image and run drawImage
var png = new Image();
png.src = "data:image/png;base64,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";
png.onload = function() {
    ctx.drawImage(png, 0, 0);
    drawImage();
};

