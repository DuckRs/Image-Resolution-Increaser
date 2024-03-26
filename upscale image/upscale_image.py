import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageFilter, ImageEnhance
import os

class ImageResizer(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Image Resizer")
        self.geometry("300x150")
        self.resizable(False, False)

        self.select_button = tk.Button(self, text="Select Image", command=self.select_image)
        self.select_button.pack(pady=20)

        self.status_label = tk.Label(self, text="")
        self.status_label.pack()

    def select_image(self):
        file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("Image Files", "*.jpg;*.png;*.bmp")])
        if file_path:
            try:
                self.process_image(file_path)
                messagebox.showinfo("Success", "Image resized successfully!")
            except Exception as e:
                messagebox.showerror("Error", str(e))

    def process_image(self, file_path):
        im = Image.open(file_path)
        width, height = im.size

        new_width = width * 4
        new_height = height * 4

        im_denoised = im.filter(ImageFilter.MedianFilter(size=3))
        im_sharpened = im_denoised.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))
        im_corrected = ImageEnhance.Color(im_sharpened).enhance(1.5)
        im_resized = im_corrected.resize((new_width, new_height), resample=Image.BICUBIC)

        output_path = os.path.splitext(file_path)[0] + "_4k" + os.path.splitext(file_path)[1]
        im_resized.save(output_path)

        self.status_label.config(text=f"Image saved as: {output_path}")

if __name__ == "__main__":
    app = ImageResizer()
    app.mainloop()
