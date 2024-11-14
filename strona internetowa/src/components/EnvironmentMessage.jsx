import React from 'react';
import note from '../img/note.png';
import bgnote from '../img/bgnote.png';

const EnvironmentMessage = () => {
    return (
        <div className="relative flex  justify-center items-center h-screen bg-cover bg-center bg-no-repeat"
             style={{
                 backgroundImage: `url(${bgnote})`,
                 backgroundSize: 'cover',
                 backgroundPosition: 'center',
                 padding: '60px',
             }}
             >

            <div className="   text-center mb-20  max-w-xl h-[100vh] animate-fadeIn"
                 style={{
                     backgroundImage: `url(${note})`,
                     backgroundSize: 'cover',
                     backgroundPosition: 'center',
                     padding: '60px',
                 }}>
                <h1 className="text-4xl font-bold  text-green-700 p-10 animate-slideIn mt-20">Nasza planeta potrzebuje pomocy!</h1>
                <p className="text-xl mb-5 text-green-950 opacity-0 animate-fadeInDelay animate-delay-1000 p-5">
                    Problemy środowiskowe, przed którymi stoimy, są ogromne. Od zmiany klimatu po zanieczyszczenie, nasza planeta
                    jest ciągle zagrożona. Jednak nie wszystko stracone.
                </p>
                <p className="text-lg text-green-950 opacity-0 animate-fadeInDelay animate-delay-2000">
                    Dzięki naszej aplikacji, chcemy wprowadzić zmiany. Oferujemy narzędzia, które pomogą w redukcji odpadów,
                    wspieraniu recyklingu i promowaniu zrównoważonych praktyk, aby wspólnie podjąć kroki ku czystszemu,
                    zielonemu światu. Dołącz do nas i zrób różnicę!
                </p>
            </div>
        </div>
    );
};

export default EnvironmentMessage;
