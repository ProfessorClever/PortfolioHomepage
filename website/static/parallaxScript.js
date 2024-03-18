let planet;
let stars;

document.addEventListener("DOMContentLoaded", function () {
    stars = document.querySelector(".parallax1");
    planet = document.querySelector(".parallax2");

    let zoomFactor = 1.2;

    stars.style.width = `${window.innerWidth * zoomFactor}px`;
    stars.style.height = `${window.innerHeight * zoomFactor}px`;

    window.addEventListener("mousemove", (e) => {
        let mouseX = e.clientX - window.innerWidth / 2;
        let mouseY = e.clientY - window.innerHeight / 2;

        

        stars.style.transform = `translateX(${(mouseX / -16) - (window.innerWidth - window.innerWidth * zoomFactor)-window.innerWidth/3}px) translateY(${(mouseY / -16) - (window.innerHeight - window.innerHeight * zoomFactor)-window.innerHeight/3}px)`;
        planet.style.transform = `translateX(${mouseX / 8}px) translateY(${mouseY / 8}px)`;
    });
});