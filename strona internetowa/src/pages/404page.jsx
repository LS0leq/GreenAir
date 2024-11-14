import Error from "../components/Error";
import Footer from "../components/Footer";

export function LoginPanel() {
    return (
        <>

            <main className="error-container">
                <Error/>

            </main>
            <footer>
                <Footer/>
            </footer>
        </>
    );
}

export default LoginPanel;