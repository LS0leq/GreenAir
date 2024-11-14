import customtkinter as ctk


class Sidebar:
    def __init__(self, root, switch_page_callback):

        self.appearance_mode_switch = None
        self.root = root
        self.frame = ctk.CTkFrame(root, width=200, corner_radius=0)
        self.frame.pack(side="left", fill="y")
        self.switch_page_callback = switch_page_callback
        self.create_buttons()
        self.create_stats_frame()
        self.appearance_mode_switch = ctk.CTkSwitch(
            self.frame, text="Dark Mode", command=self.toggle_appearance_mode,
        )
        self.appearance_mode_switch.select()
        self.appearance_mode_switch.pack(side="bottom", pady=(10, 20), anchor="s")

    def create_buttons(self):
        ctk.CTkLabel(self.frame, text="Menu", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=(20, 10))
        buttons = [("Kalkulator", "calculator"), ("Statystyki", "statistics"), ("Mapa powietrza", "map")]
        for text, page in buttons:
            ctk.CTkButton(
                self.frame, text=text, width=200, height=50, corner_radius=0,
                command=lambda p=page: self.switch_page_callback(p), font=("Helvetica", 12), hover=True,
                hover_color="black", border_width=2,
                border_color="black", bg_color="#262626", fg_color="#262626"
            ).pack(pady=5, anchor="n")

    def create_stats_frame(self):
        self.stats_frame = ctk.CTkFrame(self.frame, corner_radius=20, border_width=2)
        self.stats_frame.pack(side="bottom", pady=20, padx=20, fill="both")
        ctk.CTkLabel(self.stats_frame, text="Statystyki", font=("Arial", 14, "bold")).pack(pady=5)
        self.label_time = ctk.CTkLabel(self.stats_frame, text="", font=("Arial", 12))
        self.label_time.pack(pady=2)
        self.label_emissions = ctk.CTkLabel(self.stats_frame, text="", font=("Arial", 12))
        self.label_emissions.pack(pady=2)

    def update_time(self, text):
        self.label_time.configure(text=text)

    def update_emissions(self, text):
        self.label_emissions.configure(text=text)

    def toggle_appearance_mode(self):
        if self.appearance_mode_switch.get() == 1:
            ctk.set_appearance_mode("dark")
        else:
            ctk.set_appearance_mode("light")

