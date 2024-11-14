from src.main import *

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x600")
        self.root.title("Kalkulator - Emisja CO2")

        self.is_building_stage = False
        self.current_stage = 0

        self.selected_gender = ctk.StringVar(value="Wybierz")
        self.selected_age = ctk.StringVar(value="Wybierz")
        self.km_weekly = ctk.DoubleVar(value=0)
        self.selected_fuel = ctk.StringVar(value="Wybierz")
        self.house_area = ctk.DoubleVar(value=20)
        self.selected_heating = ctk.StringVar(value="Wybierz")
        self.bio_recycling_percent = ctk.DoubleVar(value=0)
        self.paper_recycling_percent = ctk.DoubleVar(value=0)
        self.plastic_metal_recycling_percent = ctk.DoubleVar(value=0)
        self.food_waste_percent = ctk.DoubleVar(value=0)

        self.build_stage()

    def build_stage(self):
        if self.is_building_stage:
            return
        self.is_building_stage = True

        for widget in self.root.winfo_children():
            widget.destroy()

        stage_methods = {
            1: self.stage1_basic_info,
            2: self.stage2_transport,
            3: self.stage3_home_emissions,
            4: self.stage4_waste_management,
        }

        stage_methods.get(self.current_stage, self.show_results)()
        self.is_building_stage = False

    def update_slider_label(self, slider_var, label):
        label.configure(text=f"{slider_var.get():.0f}")

    def stage1_basic_info(self):
        self.create_label("Kalkulator - Informacje podstawowe", 16)
        self.create_option_menu("Płeć:", self.selected_gender, ["Kobieta", "Mężczyzna", "Inne"])
        self.create_option_menu("Wiek:", self.selected_age,
                                ["Poniżej 18 lat", "18-30 lat", "31-45 lat", "46-65 lat", "Powyżej 65 lat"])
        self.create_next_button()

    def stage2_transport(self):
        self.create_label("Kalkulator - Transport", 16)
        self.create_slider("Ile km tygodniowo przejeżdżasz samochodem?", self.km_weekly, 0, 500)
        self.create_option_menu("Rodzaj paliwa:", self.selected_fuel,
                                ["Benzyna", "Diesel", "Gaz (LPG)", "Hybryda", "Prąd elektryczny"])
        self.create_next_button()

    def stage3_home_emissions(self):
        self.create_label("Kalkulator - Emisje domowe", 16)
        self.create_slider("Powierzchnia domu/mieszkania (m²):", self.house_area, 20, 300)
        self.create_option_menu("Rodzaj ogrzewania:", self.selected_heating, ["Prąd", "Gaz", "Węgiel", "Pompa ciepła"])
        self.create_next_button()

    def stage4_waste_management(self):
        self.create_label("Kalkulator - Odpady", 16)
        for var, text in [
            (self.bio_recycling_percent, "Jaką część odpadów BIO segregujesz (%)"),
            (self.paper_recycling_percent, "Jaką część odpadów papierowych segregujesz (%)"),
            (self.plastic_metal_recycling_percent, "Jaką część odpadów plastikowych i metalowych segregujesz (%)"),
            (self.food_waste_percent, "Jaką część jedzenia dziennie wyrzucasz (%)")
        ]:
            self.create_slider(text, var, 0, 100)
        self.create_button("Zakończ Kalkulator", self.show_results)

    def create_label(self, text, font_size=12):
        label = ctk.CTkLabel(self.root, text=text, font=("Arial", font_size))
        label.pack(pady=10)

    def create_option_menu(self, label_text, variable, options):
        label = ctk.CTkLabel(self.root, text=label_text)
        label.pack(pady=5)
        option_menu = ctk.CTkOptionMenu(self.root, variable=variable, values=options)
        option_menu.pack()

    def create_slider(self, label_text, variable, from_, to):
        label = ctk.CTkLabel(self.root, text=label_text)
        label.pack(pady=5)
        slider = ctk.CTkSlider(self.root, variable=variable, from_=from_, to=to)
        slider.pack()
        value_label = ctk.CTkLabel(self.root, text=f"{variable.get():.0f}")
        value_label.pack()
        variable.trace("w", lambda *args: self.update_slider_label(variable, value_label))

    def create_next_button(self):
        self.create_button("Dalej", self.next_stage)

    def create_button(self, text, command):
        button = ctk.CTkButton(self.root, text=text, command=command)
        button.pack(pady=20)

    def next_stage(self):
        if self.current_stage < 5:
            self.current_stage += 1
            self.build_stage()

    def calculate_emissions(self):
        emisja_transport = self.km_weekly.get() * 0.1
        emisja_dom = self.house_area.get() * 0.3
        emisja_odpady = sum([self.bio_recycling_percent.get(), self.paper_recycling_percent.get(),
                             self.plastic_metal_recycling_percent.get(), self.food_waste_percent.get()]) * 0.05
        return emisja_transport, emisja_dom, emisja_odpady

    def show_results(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        emisja_transport, emisja_dom, emisja_odpady = self.calculate_emissions()
        total_emissions = emisja_transport + emisja_dom + emisja_odpady

        summary_text = (
            f"=== Podsumowanie Emisji CO2 ===\n"
            f"Całkowita emisja CO2: {total_emissions:.2f} kg CO2 rocznie\n\n"
            f"--- Emisje z transportu ---\n"
            f"{emisja_transport:.2f} kg CO2 rocznie\n"
            f"✓ Rekomendacje: Przejście na transport publiczny, carpooling lub pojazdy elektryczne.\n\n"
            f"--- Emisje domowe ---\n"
            f"{emisja_dom:.2f} kg CO2 rocznie\n"
            f"✓ Rekomendacje: Izolacja budynku, pompy ciepła, zmiana źródła ogrzewania.\n\n"
            f"--- Emisje z odpadów ---\n"
            f"{emisja_odpady:.2f} kg CO2 rocznie\n"
            f"✓ Rekomendacje: Segregacja odpadów, zmniejszenie marnowania żywności.\n"
        )

        label_summary_title = ctk.CTkLabel(self.root, text="Wynik kalkulacji - Podsumowanie", font=("Arial", 18, "bold"))
        label_summary_title.pack(pady=10)

        frame_summary = ctk.CTkFrame(self.root)
        frame_summary.pack(pady=10, padx=20, fill="both", expand=True)

        label_summary = ctk.CTkLabel(frame_summary, text=summary_text, font=("Arial", 13), justify="left")
        label_summary.pack(padx=10, pady=10)

        advice_text = (
            "=== Eksperckie Wskazówki ===\n\n\n"
            "Transport: Carpooling lub korzystanie z transportu zbiorowego zmniejszy emisje.\n\n"
            "Ogrzewanie: Sprawdź efektywność urządzeń, rozważ instalację paneli słonecznych.\n\n"
            "Odpady: Zmniejszenie odpadów organicznych i segregacja ułatwiają ekologię."
        )

        frame_advice = ctk.CTkFrame(self.root)
        frame_advice.pack(pady=10, padx=20, fill="both", expand=True)

        label_advice = ctk.CTkLabel(frame_advice, text=advice_text, font=("Arial", 13), justify="left")
        label_advice.pack(padx=10, pady=10)

        self.create_button("Zakończ", self.end_quiz)

    def end_quiz(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.after(1000, lambda: EmissionCalculatorApp(self.root))