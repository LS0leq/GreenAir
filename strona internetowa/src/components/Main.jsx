import React from 'react';
import { Link as RouterLink } from 'react-router-dom';
import bgmain from '../img/mghero.png'
import bee from '../img/bee.webm'
import '../animations.css';

const Main = ({ carbonRef,infoRef }) => {
    const handleScroll = () => {
        carbonRef.current.scrollIntoView({ behavior: 'smooth' });
    };

    const handleScroll2 = () => {
        infoRef.current.scrollIntoView({ behavior: 'smooth' });
    };

    return (
        <div className="flex flex-col items-center justify-center min-h-screen gradient-background " style={{
            backgroundImage: `url(${bgmain})`,
            backgroundSize: 'cover',
            backgroundPosition: 'center',
        }}>
            <section
                className="flex flex-col items-center justify-center text-center p-8 rounded-lg  h-[85vh] w-[50vw] bg-green-200 bg-opacity-75 boxShadow"

            >
                <h1 className="text-4xl text-quinary font-bold mb-4  ">Zadbajmy o naszą planetę</h1>
                <p className="text-lg mb-6 text-quinary">
                    Dołącz do nas w walce o lepsze środowisko. Odkryj sposoby na życie w harmonii z naturą i wprowadź
                    ekologiczne zmiany, które przysłużą się przyszłym pokoleniom.
                </p>

                <button
                    onClick={handleScroll}
                    className="button-custom"
                >
                    <i className="fa-solid fa-tower-broadcast i"></i>Sprawdź jakość O2
                </button>

                <button
                    onClick={handleScroll2}
                    className="button-custom"
                >
                    <i className="fa-solid fa-circle-info i"></i>
                    Dowiedz się więcej
                </button>

                <a
                    href="/files/GreenAir.exe"
                    download="GreenAir.exe"
                    className="button-custom"
                >
                    <i className="fa-solid fa-download"></i>Pobierz aplikację na system Windows
                </a>


            </section>

            <div>
                <video
                    src={bee}
                    autoPlay
                    loop
                    muted
                    className="bee"
                >
                </video>
            </div>


        </div>


    );
};

export default Main;
