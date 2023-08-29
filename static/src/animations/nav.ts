declare const gsap: any
declare const Expo: any

const navToggler = document.getElementById("navToggler") as HTMLButtonElement
const navSm = document.getElementById("navSm") as HTMLDivElement
const navSmContainer = navSm.querySelector(".container")
// hanburger
const hamburger = navToggler.querySelector("#hamburger") as HTMLDivElement
const header = document.getElementById("navbar-sticky") as HTMLElement

export function navMenuSM() {
    const lineA = hamburger.querySelector('.line_a');
    const lineB = hamburger.querySelector('.line_b');
    const lineC = hamburger.querySelector('.line_c');
    // navigation open state
    let navOpen = false

    navToggler.addEventListener("click", () => {
        let tl1 = gsap.timeline({ paused: true, defaults: { duration: .2 } })
        let tl2 = gsap.timeline({ paused: true, defaults: { duration: .2 } })

        tl1.to(lineA, { translateY: 12 })
            .to(lineC, { translateY: -12 }, '-=.2')
            .to(lineB, { scale: 0 }, '-=.2')
            .to(lineA, { rotate: 45 })
            .to(lineC, { rotate: -45 }, '-=.2')
            .to(navSm, { clipPath: 'polygon(0 0, 100% 0, 100% 100%, 0 100%)', duration: .5 }, '-=.2')
            .to(navSmContainer, { translate: '0 0', opacity: 1, duration: .5 }, '-=.5')

        tl2.to(lineC, { rotate: 0 })
            .to(lineA, { rotate: 0 }, '-=.2')
            .to(lineB, { scale: 1 })
            .to(lineA, { translateY: 0 }, '-=.2')
            .to(lineC, { translateY: 0 }, '-=.2')
            .to(navSmContainer, { translate: '0 20%', opacity: 0.3, duration: .5 }, '-=.2')
            .to(navSm, { clipPath: 'polygon(0 0, 100% 0, 100% 0%, 0 0%)', duration: 0.5 }, '-=.3')

        console.log('click');
        console.log(navOpen);
        if (!navOpen) {
            tl1.play()
            tl1.addPause()
            navOpen = !navOpen
        }
        else {
            console.log('here');
            tl2.play()
            navOpen = !navOpen
        }
    })
}

export function headerHamburger() {
    let lastScroll = 0;

    window.addEventListener("scroll", () => {
        const currentScroll = window.scrollY;
        // timeline to hide nav and hamburger
        let tlHide = gsap.timeline({ paused: true, defaults: { duration: .2, Easings: Expo.EaseOut } })
            .to(header, { top: '-15%', })
        if (navToggler.offsetHeight) {
          tlHide.to(navToggler, { bottom: '-4rem' })
        }

        let tlShow = gsap.timeline({ paused: true, defaults: { duration: .2 } })
            .to(header, { top: '0%', })
        if (navToggler.offsetHeight) {
          tlShow.to(navToggler, { bottom: '4rem' })
        }

        if (currentScroll <= 0) {
            header.classList.remove("show");
            tlShow.play()
        }
        if (currentScroll > lastScroll && !header.classList.contains("hide")) {
            header.classList.remove("show");
            header.classList.add("hide");
            tlHide.play()
        }
        if (currentScroll < lastScroll && header.classList.contains("hide")) {
            header.classList.remove("hide");
            header.classList.add("show");
            tlShow.play()
        }
        lastScroll = currentScroll;
    });
}