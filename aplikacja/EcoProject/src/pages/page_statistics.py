import customtkinter as ctk
import matplotlib.pyplot as plt
from io import BytesIO
from PIL import Image

def create_statistics_page(parent):
    page = ctk.CTkFrame(parent)
    stats_text = (
        "1. Transport odpowiada za około 24% emisji CO₂ globalnie.\n"
        "2. Sektor energetyczny generuje 42% światowych emisji CO₂.\n"
        "3. W 2022 roku największymi emitentami CO₂ były: Chiny, USA, i Indie.\n"
        "4. Globalna emisja CO₂ w 2022 roku wyniosła około 37 miliardów ton.\n"
        "5. Każdy mieszkaniec Ziemi emituje średnio 4,8 tony CO₂ rocznie."
    )
    ctk.CTkLabel(page, text="Globalne statystyki emisji CO₂", font=("Arial", 16, "bold")).pack(pady=10)
    ctk.CTkLabel(page, text=stats_text, font=("Arial", 12), justify="left").pack(pady=5, padx=20)

    countries = ["Chiny", "USA", "Indie", "Rosja", "Japonia"]
    emissions = [10.06, 5.41, 2.65, 1.47, 1.15]
    fig, ax = plt.subplots(figsize=(5, 4))
    ax.bar(countries, emissions, color=["#FF6F61", "#6B5B95", "#88B04B", "#F7CAC9", "#92A8D1"])
    ax.set_title("Emisja CO₂ w 2023 roku (mld ton)")
    ax.set_ylabel("Emisja CO₂ (mld ton)")
    ax.set_xlabel("Kraje")

    buffer = BytesIO()
    fig.savefig(buffer, format="png", bbox_inches="tight")
    buffer.seek(0)
    plot_image = Image.open(buffer)
    plot_ctk_image = ctk.CTkImage(plot_image, size=(500, 350))
    ctk.CTkLabel(page, image=plot_ctk_image, text="").pack(pady=10)
    return page