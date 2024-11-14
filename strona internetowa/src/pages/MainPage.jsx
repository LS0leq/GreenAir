import React, { useState, useEffect, useRef } from 'react';
import Main from "../components/Main";
import Carbon from "../components/Carbon";
import EnvironmentMessage from "../components/EnvironmentMessage";
import { Footer } from "../components/Footer";
import heroFoto from "../img/hero-bgh.jpg";
import leafs1 from "../img/leafs-1.png";
import leafs2 from "../img/leafs02.png";

export function MainPage() {
    const [isVisibleLeaf1, setIsVisibleLeaf1] = useState(false);
    const [isVisibleLeaf2, setIsVisibleLeaf2] = useState(false);

    const [scrollY, setScrollY] = useState(0); // Stan do przechowywania pozycji przewijania

    const leaf1Ref = useRef(null);
    const leaf2Ref = useRef(null);
    const carbonRef = useRef(null);
    const infoRef = useRef(null); // Dodanie infoRef do referencji

    const handleScroll = () => {
        setScrollY(window.scrollY); // Ustawiamy nową wartość scrollY
    };

    useEffect(() => {
        window.addEventListener('scroll', handleScroll);

        return () => {
            window.removeEventListener('scroll', handleScroll);
        };
    }, []);

    const hideThreshold = 700;

    const leaf1Class = scrollY > hideThreshold ? 'slide-out-left' : isVisibleLeaf1 ? 'slide-in-left' : '';
    const leaf2Class = scrollY > hideThreshold ? 'slide-out-right' : isVisibleLeaf2 ? 'slide-in-right' : '';

    useEffect(() => {
        const observer = new IntersectionObserver(([entry]) => {
            if (entry.isIntersecting) {
                setIsVisibleLeaf1(true);
            }
        }, { threshold: 0.1 });

        const observer2 = new IntersectionObserver(([entry]) => {
            if (entry.isIntersecting) {
                setIsVisibleLeaf2(true);
            }
        }, { threshold: 0.1 });

        if (leaf1Ref.current) {
            observer.observe(leaf1Ref.current);
        }

        if (leaf2Ref.current) {
            observer2.observe(leaf2Ref.current);
        }

        return () => {
            if (leaf1Ref.current) {
                observer.unobserve(leaf1Ref.current);
            }
            if (leaf2Ref.current) {
                observer2.unobserve(leaf2Ref.current);
            }
        };
    }, []);

    return (
        <>
            <main className="relative">
                <Main carbonRef={carbonRef} infoRef={infoRef} />
                <img
                    ref={leaf1Ref}
                    src={leafs1}
                    alt="leafs"
                    className={`absolute bottom-[-20px] left-[-280px] rotate-45 w-1/3 ${leaf1Class}`}
                />
                <img
                    ref={leaf2Ref}
                    src={leafs2}
                    alt="leafs"
                    className={`absolute bottom-[-20px] right-[-280px] rotate-[-45deg] w-1/3 ${leaf2Class}`}
                />
            </main>

            <section
                ref={carbonRef}
                style={{
                    backgroundImage: `url(${heroFoto})`,
                    backgroundSize: 'cover',
                    backgroundPosition: 'center',
                    padding: '60px',
                }}
            >
                <Carbon />
            </section>

            <section ref={infoRef}>
                <EnvironmentMessage/>


            </section>

            <footer>
                <Footer/>
            </footer>
        </>
    );
}

export default MainPage;
