import customtkinter as ctk
import time
import os
import sys
from itertools import cycle
from PIL import Image
from components.sidebar import Sidebar
from pages.page_calculator import create_calculator_page
from pages.page_statistics import create_statistics_page
from pages.page_map import PollutionMapPage
from src.quiz import *


class EmissionCalculatorApp:
    def __init__(self, root):
        self.root = root
        self.start_time = time.time()
        self.tips = [
            "Czy wiesz, że jedna osoba może w ciągu roku zaoszczędzić 400 kg CO2, wybierając rower zamiast samochodu?",
            "Recykling jednej butelki szklanej oszczędza tyle energii, ile potrzeba do zasilenia komputera przez 30 minut.",
            "Rośliny domowe mogą poprawić jakość powietrza i zmniejszyć poziom CO2."
        ]
        self.tips_cycle = cycle(self.tips)
        self.current_tip = ctk.StringVar(value=next(self.tips_cycle))
        ctk.set_appearance_mode("dark")
        self.root.geometry("1000x600")
        self.root.title("Kalkulator Emisji CO2")
        self.root.resizable(False, False)
        self.current_page = None
        self.api_key = "fb9e5c164b6e64b6ea40f8d266f20499"
        self.sidebar = Sidebar(self.root, self.switch_page)
        self.create_widgets()
        self.update_stats()
        self.next_tip()

    def get_resource_path(self, relative_path):
        if hasattr(sys, "_MEIPASS"):
            return os.path.join(sys._MEIPASS, relative_path)
        return os.path.join(os.path.abspath(".."), relative_path)

    def create_widgets(self):
        label_title = ctk.CTkLabel(self.root, text="Witaj w kalkulatorze emisji CO2!", font=("Arial", 20, "bold"))
        label_title.pack(pady=10)
        self.page_frame = ctk.CTkFrame(self.root, corner_radius=15, width=750, height=500)
        self.page_frame.pack(side="right", padx=(10, 20), pady=10, fill="both", expand=True)
        self.switch_page("calculator")

    def switch_page(self, page_name):
        if self.current_page:
            self.current_page.pack_forget()
        if page_name == "calculator":
            self.current_page = create_calculator_page(self.page_frame, self.current_tip, self.next_tip, self.calculate)
        elif page_name == "statistics":
            self.current_page = create_statistics_page(self.page_frame)
        elif page_name == "map":
            self.current_page = PollutionMapPage(self.page_frame, self.api_key)
        self.current_page.pack(fill="both", expand=True)

    def update_stats(self):
        elapsed_time = int(time.time() - self.start_time)
        emissions = elapsed_time * 0.02
        self.sidebar.update_time(f"Czas działania:\n {elapsed_time} sekund")
        self.sidebar.update_emissions(f"Szacowana emisja CO2:\n {emissions:.2f} g")

        self.root.after(1000, self.update_stats)

    def next_tip(self, event=None):
        self.current_tip.set(next(self.tips_cycle))
        self.root.after(15000, self.next_tip)

    def calculate(self):
        QuizApp(self.root).next_stage()

if __name__ == "__main__":
    root = ctk.CTk()
    app = EmissionCalculatorApp(root)
    root.mainloop()