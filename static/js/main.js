import { gsap } from 'gsap';
// slideshow
const slideshow = document.querySelector('#slideshow');
const slides = slideshow.querySelectorAll('.slide');
let currentSlide = 0;
console.log('Heloo');
function showSlide(n) {
    slides[currentSlide].classList.remove('active');
    slides[n].classList.add('active');
    currentSlide = n;
}
function nextSlide() {
    showSlide((currentSlide + 1) % slides.length);
}
const tl = gsap.timeline({ repeat: -1 });
tl.to(slideshow, { duration: 1, x: '-100%' });
tl.call(nextSlide);
tl.to(slideshow, { duration: 1, x: '0%' });
//# sourceMappingURL=main.js.map