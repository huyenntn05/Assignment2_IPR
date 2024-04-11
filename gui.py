import tkinter as tk
import cv2
from tkinter import filedialog
from PIL import Image, ImageTk
from image_processing import apply_low_pass_filter, apply_high_pass_filter

# Kích thước cố định cho ảnh hiển thị
IMAGE_WIDTH = 400
IMAGE_HEIGHT = 400

def select_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        image = cv2.imread(file_path)
        return image

def process_image():
    original_image = select_image()
    if original_image is not None:
        filtered_image = None
        option = option_var.get()
        if option == "Low Pass Filter":
            filtered_image = apply_low_pass_filter(original_image)
        elif option == "High Pass Filter":
            filtered_image = apply_high_pass_filter(original_image)
        
        if filtered_image is not None:
            display_images(original_image, filtered_image)

def display_images(original_image, filtered_image):
    # Tính toán tỷ lệ giữa chiều rộng và chiều cao của ảnh ban đầu
    original_height, original_width, _ = original_image.shape
    aspect_ratio = original_width / original_height

    # Resize original image
    original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
    original_image = cv2.resize(original_image, (int(IMAGE_HEIGHT * aspect_ratio), IMAGE_HEIGHT))
    original_image = Image.fromarray(original_image)
    original_image = ImageTk.PhotoImage(original_image)

    # Resize filtered image
    filtered_image = cv2.cvtColor(filtered_image, cv2.COLOR_BGR2RGB)
    filtered_image = cv2.resize(filtered_image, (int(IMAGE_HEIGHT * aspect_ratio), IMAGE_HEIGHT))
    filtered_image = Image.fromarray(filtered_image)
    filtered_image = ImageTk.PhotoImage(filtered_image)

    # Clear previous images
    original_label.config(image=None)
    filtered_label.config(image=None)

    # Update labels with resized images
    original_label.config(image=original_image)
    original_label.image = original_image
    filtered_label.config(image=filtered_image)
    filtered_label.image = filtered_image

# GUI
root = tk.Tk()
root.title("Image Filter")

option_var = tk.StringVar(root)
option_var.set("Low Pass Filter")

options = ["Low Pass Filter", "High Pass Filter"]

option_menu = tk.OptionMenu(root, option_var, *options)
option_menu.pack(pady=10)

process_button = tk.Button(root, text="Process Image", command=process_image)
process_button.pack(pady=5)

# Labels to display images
frame = tk.Frame(root)
frame.pack()

original_label = tk.Label(frame)
original_label.pack(side=tk.LEFT, padx=10, pady=5)

filtered_label = tk.Label(frame)
filtered_label.pack(side=tk.RIGHT, padx=10, pady=5)

root.mainloop()
