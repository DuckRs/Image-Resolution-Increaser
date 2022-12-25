import tkinter as tk
import subprocess
from tkinter import filedialog
from PIL import Image, ImageEnhance

# Create a function to open the file dialog and select an image file
def select_image():
    # Open the file dialog and get the selected file's path
    file_path = filedialog.askopenfilename()

    # Open the image and get its width and height
    im = Image.open(file_path)
    width, height = im.size

    # Calculate the new width and height to increase the resolution by a factor of 4
    new_width = width * 4
    new_height = height * 4

    # Denoise the image using the median filter
    im_denoised = im.filter(ImageFilter.MedianFilter(size=3))

    # Sharpen the image using the unsharp mask filter
    im_sharpened = im_denoised.filter(ImageFilter.UnsharpMask(radius=2, percent=150, threshold=3))

    # Correct the color balance using the color balance filter
    im_corrected = ImageEnhance.Color(im_sharpened).enhance(1.5)

    # Use the resize() method to increase the resolution
    im_resized = im_corrected.resize((new_width, new_height), resample=Image.BICUBIC)

    # Save the resized image
    im_resized.save('image_4k.jpg')

    # Open the output image using the default image viewer
    subprocess.run(['open', 'image_4k.jpg'])

# Create the GUI
root = tk.Tk()
root.title("Image Resizer")

# Create a button to open the file dialog
button = tk.Button(text="Select image", command=select_image)
button.pack()

root.mainloop()