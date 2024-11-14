import { BrowserRouter, Routes, Route} from "react-router-dom";
import MainPage from "./pages/MainPage";
import ErrprPage from "../src/pages/404page";


function App() {
    return (
        <BrowserRouter>
                <Routes>
                    <Route path="/" element={<MainPage />} />
                    <Route path="/404" element={<ErrprPage/>} />
                    <Route path="/*" element={<ErrprPage/>} />
                </Routes>
        </BrowserRouter>
    );
}

export default App;
