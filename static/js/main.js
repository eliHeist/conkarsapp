import gsap from 'gsap';
import ScrollTrigger from 'gsap/src/ScrollTrigger';
gsap.set(".fly-up", { y: 200, clipPath: 'polygon(0 0, 100% 0, 100% 0, 0 0)' });
gsap.set('.fade-in', { opacity: 0, scale: 0.9 });
ScrollTrigger.batch('.trigger', {
    onEnter: (batch) => {
        const slideElements = batch[0].querySelectorAll('.fly-up');
        const fadeElements = batch[0].querySelectorAll('.fade-in');
        gsap.to(slideElements, { clipPath: 'polygon(0 0, 100% 0, 100% 100%, 0 100%)', y: 0, stagger: 0.2, duration: 1 });
        gsap.to(fadeElements, { opacity: 1, scale: 1, stagger: 0.2, duration: 0.5 });
    },
    start: '400px bottom',
    // markers: true
});
//# sourceMappingURL=main.js.map