import tkinter as tk
from tkinter import filedialog, messagebox
import cv2
from image_processing import apply_high_pass_filter, apply_low_pass_filter
from PIL import Image, ImageTk

class ImageFilterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Filter Application")

        self.original_image = None
        self.filtered_image = None

        # Create GUI elements
        self.upload_button = tk.Button(root, text="Upload Image", command=self.upload_image)
        self.upload_button.pack(pady=10)

        self.high_pass_button = tk.Button(root, text="Apply High Pass Filter", command=self.apply_high_pass_filter)
        self.high_pass_button.pack(pady=5)

        self.low_pass_button = tk.Button(root, text="Apply Low Pass Filter", command=self.apply_low_pass_filter)
        self.low_pass_button.pack(pady=5)

        self.canvas = tk.Canvas(root, width=400, height=400)
        self.canvas.pack()

    def upload_image(self):
        filename = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.png;*.jpeg")])
        if filename:
            self.original_image = cv2.imread(filename)
            if self.original_image is not None:
                self.original_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2RGB)
                self.display_image(self.original_image)
            else:
                messagebox.showerror("Error", "Failed to load image.")

    def display_image(self, image):
        if image is not None:
            image = cv2.resize(image, (400, 400))
            img = Image.fromarray(image)
            self.canvas.image = ImageTk.PhotoImage(img)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=self.canvas.image)

    def apply_high_pass_filter(self):
        if self.original_image is None:
            messagebox.showerror("Error", "No image uploaded.")
            return

        self.filtered_image = apply_high_pass_filter(self.original_image)
        self.display_image(self.filtered_image)

    def apply_low_pass_filter(self):
        if self.original_image is None:
            messagebox.showerror("Error", "No image uploaded.")
            return

        self.filtered_image = apply_low_pass_filter(self.original_image)
        self.display_image(self.filtered_image)
