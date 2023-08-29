import './main.scss';
import './gsap/gsap.min'
import './gsap/ScrollTrigger.min'

import { navMenuSM, headerHamburger } from './animations/nav'
import { scrollAnims } from './animations/animations'
import { carouselInit, CarouselSlider } from "./animations/carousel";

declare const homepage:boolean

navMenuSM()
headerHamburger()
scrollAnims()

try {
    if (homepage) {
        // Carousel.switchSlides()
        carouselInit()
        CarouselSlider.switchSlides()
        setInterval(CarouselSlider.switchSlides, 20000)
    }
} catch (error) {
    
}