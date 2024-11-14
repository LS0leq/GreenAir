export function Footer() {
    return (
        <footer className="bg-gray-800 text-white py-6 " >
            <section className="container mx-auto text-center">
                <h1 className="text-lg font-bold mb-4">GreenAir &copy; 2024</h1>
                <div>
                    <h2 className="text-md font-semibold mb-2">Dane kontaktowe:</h2>
                    <ul className="list-none space-y-2">
                        <li>
                            Adres mail: <span className="text-green-500">support@greenair.pl</span>
                        </li>
                        <li>
                            Nr telefonu: <span className="text-green-500">+48 800 888 999</span>
                        </li>
                        <li>
                            Adres: <span className="text-green-500">ul. Zielona 48, 00-123 Warszawa</span>
                        </li>
                    </ul>
                </div>


                <br/>
                <br/>
                <p>Website powered by <a href="https://lsoleq.pl" target="_blank" className="text-green-800">LS Oleq</a>
                </p></section>
        </footer>
    );
}

export default Footer;
