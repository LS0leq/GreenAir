import customtkinter as ctk
from tkintermapview import TkinterMapView
import requests

class PollutionMapPage(ctk.CTkFrame):
    def __init__(self, parent, api_key):
        super().__init__(parent)
        self.page = ctk.CTkFrame(parent)
        self.api_key = api_key
        self.create_map_page()


    def show_pollution_alert(self, pollution_text):
        alert = ctk.CTkToplevel(self.page)
        alert.title("Informacja o zanieczyszczeniu")
        alert.geometry("800x300")

        label = ctk.CTkLabel(
            alert,
            text=f"Stan powietrza:\n\n{pollution_text}",
            font=("Arial", 12)
        )
        label.pack(pady=40)

        button = ctk.CTkButton(
            alert,
            text="Zamknij",
            command=alert.destroy
        )
        button.pack(pady=10)
    def on_map_click(self, event):
        lat, lon = self.map_view.get_position()

        pollution_data = self.get_pollution_data(lat, lon)

        self.map_view.delete_all_marker()

        if pollution_data:
            pollution_text = (
                f"CO (czad): {pollution_data['co']} µg/m³ - Wysoki poziom może prowadzić do problemów z oddychaniem.\n"
                f"NO (tlenek azotu): {pollution_data['no']} µg/m³ - Może powodować podrażnienia dróg oddechowych.\n"
                f"NO₂ (dwutlenek azotu): {pollution_data['no2']} µg/m³ - Może pogarszać stan astmy i innych chorób płuc.\n"
                f"O₃ (ozon): {pollution_data['o3']} µg/m³ - Może powodować kaszel i podrażnienia oczu.\n"
                f"PM2.5 (cząstki stałe): {pollution_data['pm2_5']} µg/m³ - Cząstki te mogą wnikać głęboko do płuc.\n"
                f"PM10 (większe cząstki): {pollution_data['pm10']} µg/m³ - Mogą powodować kaszel i problemy z oddychaniem."
            )
            self.map_view.set_marker(lat, lon, text=pollution_text)
            self.show_pollution_alert(pollution_text)

        else:
            self.map_view.set_marker(lat, lon, text="Brak danych o zanieczyszczeniach")
            self.show_pollution_alert("Brak danych o zanieczyszczeniach")

    def get_pollution_data(self, latitude, longitude):
        url = f"http://api.openweathermap.org/data/2.5/air_pollution?lat={latitude}&lon={longitude}&appid={self.api_key}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            data = response.json()
            pollution_data = data['list'][0]['components']
            return pollution_data
        except (requests.RequestException, KeyError) as e:
            print(f"Błąd pobierania danych o zanieczyszczeniach: {e}")
            return None

    def create_map_page(self):
        instruction_label = ctk.CTkLabel(
            self,
            text="Kliknij na mapie, aby sprawdzić stan powietrza w wybranym miejscu.",
            font=("Arial", 14, "italic"),
            text_color="white"
        )
        instruction_label.pack(pady=10)

        user_location = (52.2297, 21.0122)

        self.map_view = TkinterMapView(self, width=700, height=400, corner_radius=10)
        self.map_view.set_position(user_location[0], user_location[1])
        self.map_view.set_zoom(10)
        self.map_view.pack(pady=20)

        self.map_view.add_left_click_map_command(self.on_map_click)