from PIL import Image
import customtkinter as ctk
import sys
import os


def get_resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath(".."), relative_path)


def create_calculator_page(parent, tip_var, next_tip_callback, calculate_callback):
    page = ctk.CTkFrame(parent)
    image_path = os.path.join(os.path.dirname(__file__), '..', '..', 'resources', 'image.png')
    image_path = os.path.abspath(image_path)
    image_path = get_resource_path(image_path)
    sticky_image = Image.open(image_path).resize((400, 350), resample=Image.Resampling.LANCZOS)
    sticky = ctk.CTkImage(sticky_image, size=(400, 400))

    sticky_note_label = ctk.CTkLabel(
        page, image=sticky, textvariable=tip_var,
        font=("Arial", 15, "italic"), wraplength=200,
        compound="center", fg_color="transparent", text_color="black"
    )
    sticky_note_label.pack(pady=20, padx=20, side="right", anchor="se")
    sticky_note_label.bind("<Button-1>", next_tip_callback)

    calculate_button = ctk.CTkButton(
        page,
        text="Kliknij, by obliczyć!",
        font=("Arial", 18, "bold"),
        width=300,
        height=70,
        corner_radius=15,
        fg_color="#4CAF50",
        hover_color="#45A049",
        text_color="white",
        border_width=1,
        border_color="black",
        command=calculate_callback
    )
    calculate_button.pack(pady=40, anchor="center")
    return page
