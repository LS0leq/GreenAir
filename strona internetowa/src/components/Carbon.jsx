import React, { useState } from 'react';

const Carbon = () => {
    const [data, setData] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
    const [selectedCity, setSelectedCity] = useState('');
    const [selectedState, setSelectedState] = useState('');
    const [cityToSearch, setCityToSearch] = useState('');
    const [stateToSearch, setStateToSearch] = useState('');
    const [color, setColor] = useState("green");

    const country = "Polska";

    const countriesAndCities = [
        {
            country: "Polska",
            state: "Pomorskie",
            cities: ["Bytów", "Gdańsk", "Gdynia", "Kościerzyna", "Pogórze", "Sopot"]
        },
        {
            country: "Polska",
            state: "Mazowieckie",
            cities: ["Warszawa", "Radom", "Płock"]
        },
        {
            country: "Polska",
            state: "Kujawsko-Pomorskie",
            cities: ["Bydgoszcz", "Grudziądz", "Inowrocław", "Nakło nad Notecią", "Świecie", "Toruń", "Wilcze", "Włocławek"]
        },
        {
            country: "Polska",
            state: "Małopolskie",
            cities: ["Kraków", "Muszyna", "Myslenice", "Niepolomice", "Nowy Targ", "Olkusz", "Rabka-Zdroj", "Sucha Beskidzka", "Uście Gorlickie", "Zabierzów", "Zaborze"]
        },
        {
            country: "Polska",
            state: "Łódzkie",
            cities: ["Ksawerów", "Kutno", "Lask", "Łódź", "Pabianice", "Piotrków Trybunalski", "Radomsko", "Zgierz"]
        },
        {
            country: "Polska",
            state: "Lubelskie",
            cities: ["Biała Podlaska", "Chełm", "Lublin", "Łódź", "Łuków", "Radzyń Podlaski", "Zamość"]
        },
        {
            country: "Polska",
            state: "Lubuskie",
            cities: ["Lubsko", "Nowa Sól", "Olbrachcice", "Zielona Góra"]
        },
        {
            country: "Polska",
            state: "Opolskie",
            cities: ["Lubsko", "Nowa Sól", "Olbrachcice", "Zielona Góra"]
        },
        {
            country: "Polska",
            state: "Podlasie",
            cities: ["Białystok", "Grajewo", "Nowa Świdziałówka", "Suwałki"]
        },
        {
            country: "Polska",
            state: "Śląskie",
            cities: ["Bielsko-Biała", "Goczałkowice-Zdrój", "Jastrzębie-Zdrój", "Katowice", "Lubliniec", "Międzybrodzie Żywieckie", "Orzesze", "Racibórz", "Rybnik", "Sosnicowice", "Sosnowiec", "Tychy", "Zawiercie"]
        },
        {
            country: "Polska",
            state: "Podkarpackie",
            cities: ["Boguchwała", "Dębica", "Jarosław", "Krempna", "Krosno", "Mielec", "Nisko", "Przemyśl", "Rudna Wielka", "Rymanów-Zdrój", "Rzeszów", "Sanok", "Tarnobrzeg"]
        },
        {
            country: "Polska",
            state: "Świętokrzyskie",
            cities: ["Kępie", "Kielce", "Łagów", "Małogoszcz", "Skarżysko-Kamienna", "Starachowice", "Wodzisław", "Wymysłów"]
        },
        {
            country: "Polska",
            state: "Warmińsko Mazurskie",
            cities: ["Działdowo", "Ełk", "Gołdap", "Olsztyn", "Ostróda", "Wygryny"]
        },
        {
            country: "Polska",
            state: "Zachodnio Pomorskie",
            cities: ["Darłowo", "Kołobrzeg", "Szczecin", "Szczecinek"]
        }
    ];

    const mapStateToAPI = (state) => {
        const mapping = {
            "Mazowieckie": "Mazovia",
            "Małopolskie": "Lesser%Poland%Voivodeship",
            "Pomorskie": "Pomerania",
            "Łódzkie": "Lodz%Voivodeship",
            "Lubelskie": "Lublin",
            "Lubuskie": "Lubusz",
            "Opolskie": "Opole%Voivodeship",
            "Śląskie": "Silesia",
            "Podkarpackie": "Subcarpathian%Voivodeship",
            "Świętokrzyskie": "Swietokrzyskie",
            "Warmińsko Mazurskie": "Warmia-Masuria",
            "Zachodnio Pomorskie": "West%Pomerania"
        };
        return mapping[state] || state;
    };

    const fetchData = async (city, state) => {
        const stateCode = mapStateToAPI(state);
        if(city=="Warszawa"){
            city="Warsaw";
        }
        const API_URL = `http://api.airvisual.com/v2/city?city=${city}&state=${stateCode}&country=POLAND&key=102d3598-ce56-4825-a71b-60d520a6535e`;

        setLoading(true);
        setError(null);

        try {
            const response = await fetch(API_URL);
            if (!response.ok) throw new Error(`Błąd: ${response.status} ${response.statusText}`);
            const result = await response.json();
            setData(result.data);

            const aqi = result.data.current.pollution.aqius;
            setColor(aqi <= 50 ? "green" : aqi <= 100 ? "yellow" : aqi <= 150 ? "orange" : aqi <= 200 ? "red" : "dark");
        } catch (error) {
            setError(error.message);
        } finally {
            setLoading(false);
        }
    };

    const handleSearch = () => {
        if (selectedCity && selectedState) {
            setCityToSearch(selectedCity);
            setStateToSearch(selectedState);
            fetchData(selectedCity, selectedState);
        } else {
            setError("Proszę wybrać województwo i miasto.");
        }
    };

    return (
        <div className="p-12 max-w-3xl mx-auto bg-white rounded-xl shadow-md space-y-4 flex flex-col md:flex-row mt-9 h-[70vh]">
            <div className="md:w-1/2 space-y-4">
                <h1 className="text-2xl font-bold text-center">Wybierz województwo i miasto</h1>
                <div className="mb-4">
                    <h2 className="text-lg">Kraj: {country}</h2>
                </div>
                <div>
                    <label htmlFor="state" className="block text-lg">Województwo:</label>
                    <select
                        id="state"
                        value={selectedState}
                        onChange={(e) => {
                            setSelectedState(e.target.value);
                            setSelectedCity('');
                        }}
                        className="border p-2 rounded"
                    >
                        <option value="">Wybierz województwo</option>
                        {countriesAndCities
                            .filter(item => item.country === country)
                            .map(item => (
                                <option key={item.state} value={item.state}>{item.state}</option>
                            ))}
                    </select>
                </div>
                <div>
                    <label htmlFor="city" className="block text-lg">Miasto:</label>
                    <select
                        id="city"
                        value={selectedCity}
                        onChange={(e) => setSelectedCity(e.target.value)}
                        className="border p-2 rounded"
                    >
                        <option value="">Wybierz miasto</option>
                        {countriesAndCities
                            .find(item => item.state === selectedState)
                            ?.cities
                            .map(city => (
                                <option key={city} value={city}>{city}</option>
                            ))}
                    </select>
                </div>
                <button onClick={handleSearch} className="mt-4 px-4 py-2 bg-blue-500 text-white rounded">
                    Sprawdź jakość powietrza
                </button>
                {error && <div className="text-red-500 mt-4">{error}</div>}
            </div>

            <div className="md:w-1/2 space-y-4">
                {loading && <div className="text-center text-lg">Ładowanie danych...</div>}
                {data && (
                    <div>
                        <h2 className="text-xl font-semibold">Aktualne dane dla {cityToSearch}, {stateToSearch}</h2>
                        <p className="text-lg">
                            AQI: <span className={color}
                        >{data.current.pollution.aqius}</span>
                        </p>
                        <p className="text-lg">Temperatura: {data.current.weather.tp}°C</p>
                        <p className="text-lg">Wilgotność: {data.current.weather.hu}%</p>
                        <p className="text-lg">Ciśnienie: {data.current.weather.pr} hPa</p>
                        <p className="text-lg">Czas: {new Date(data.current.weather.ts).toLocaleString()}</p>
                        <div className={`bg-${color}-500 text-white p-2 rounded`}>
                            {color.charAt(0).toUpperCase() + color.slice(1)} powietrze
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

export default Carbon;
