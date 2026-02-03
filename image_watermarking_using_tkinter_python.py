# Image Watermarking Application using Tkinter
# Cross Watermark with Angle Slider + Background Image
# Compatible with Python 3.13 and latest Pillow

import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont


class WatermarkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Watermarking Tool")
        self.root.geometry("800x600")

        self.image = None
        self.watermarked_image = None
        self.tk_img = None

        # ================= BACKGROUND IMAGE =================
        self.canvas = tk.Canvas(root, width=800, height=600)
        self.canvas.pack(fill="both", expand=True)

        self.bg_image = Image.open("background.png")
        self.bg_image = self.bg_image.resize((800, 600))
        self.bg_tk = ImageTk.PhotoImage(self.bg_image)
        self.canvas.create_image(0, 0, image=self.bg_tk, anchor="nw")

        # ================= UI FRAME =================
        self.ui_frame = tk.Frame(self.canvas, bg="#ffffff", bd=2, relief="ridge")
        self.ui_frame.place(relx=0.5, rely=0.5, anchor="center")

        # Title
        title = tk.Label(
            self.ui_frame,
            text="Image Watermarking Using Tkinter",
            font=("Arial", 18, "bold"),
            bg="white"
        )
        title.pack(pady=10)

        # Buttons
        btn_frame = tk.Frame(self.ui_frame, bg="white")
        btn_frame.pack(pady=5)

        tk.Button(btn_frame, text="Select Image", command=self.load_image).grid(row=0, column=0, padx=10)
        tk.Button(btn_frame, text="Apply Watermark", command=self.apply_watermark).grid(row=0, column=1, padx=10)
        tk.Button(btn_frame, text="Save Image", command=self.save_image).grid(row=0, column=2, padx=10)

        # Watermark Text
        wm_frame = tk.Frame(self.ui_frame, bg="white")
        wm_frame.pack(pady=5)

        tk.Label(wm_frame, text="Watermark Text:", bg="white").grid(row=0, column=0, padx=5)
        self.wm_text = tk.Entry(wm_frame, width=30)
        self.wm_text.grid(row=0, column=1, padx=5)

        # Angle Slider
        angle_frame = tk.Frame(self.ui_frame, bg="white")
        angle_frame.pack(pady=5)

        tk.Label(angle_frame, text="Watermark Angle (0–90°):", bg="white").grid(row=0, column=0, padx=5)
        self.angle_slider = tk.Scale(
            angle_frame,
            from_=0,
            to=90,
            orient="horizontal",
            length=200,
            bg="white"
        )
        self.angle_slider.set(45)
        self.angle_slider.grid(row=0, column=1, padx=5)

        # Image Preview
        self.image_label = tk.Label(self.ui_frame, bg="white")
        self.image_label.pack(pady=10)

    def load_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image Files", "*.png *.jpg *.jpeg")]
        )
        if not file_path:
            return

        self.image = Image.open(file_path).convert("RGBA")
        self.display_image(self.image)

    def display_image(self, img):
        preview = img.copy()
        preview.thumbnail((400, 300))
        self.tk_img = ImageTk.PhotoImage(preview)
        self.image_label.config(image=self.tk_img)

    def apply_watermark(self):
        if self.image is None:
            messagebox.showerror("Error", "Please select an image first")
            return

        text = self.wm_text.get().strip()
        if not text:
            messagebox.showerror("Error", "Please enter watermark text")
            return

        angle = self.angle_slider.get()

        base = self.image.copy()
        width, height = base.size

        watermark_layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(watermark_layer)

        try:
            font = ImageFont.truetype("arial.ttf", 40)
        except IOError:
            font = ImageFont.load_default()

        bbox = draw.textbbox((0, 0), text, font=font)
        text_w = bbox[2] - bbox[0]
        text_h = bbox[3] - bbox[1]

        x_spacing = text_w + 100
        y_spacing = text_h + 100

        for y in range(-height, height * 2, y_spacing):
            for x in range(-width, width * 2, x_spacing):
                draw.text((x, y), text, fill=(255, 255, 255, 80), font=font)

        # Rotate by slider angle
        watermark_layer = watermark_layer.rotate(angle, expand=True)

        w, h = watermark_layer.size
        left = (w - width) // 2
        top = (h - height) // 2
        watermark_layer = watermark_layer.crop((left, top, left + width, top + height))

        self.watermarked_image = Image.alpha_composite(base, watermark_layer)
        self.display_image(self.watermarked_image)

    def save_image(self):
        if self.watermarked_image is None:
            messagebox.showerror("Error", "No watermarked image to save")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG Files", "*.png"), ("JPEG Files", "*.jpg")]
        )

        if file_path:
            self.watermarked_image.convert("RGB").save(file_path)
            messagebox.showinfo("Success", "Image saved successfully")


if __name__ == "__main__":
    root = tk.Tk()
    app = WatermarkApp(root)
    root.mainloop()
