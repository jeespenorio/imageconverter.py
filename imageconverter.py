# Importing the libraries
import tkinter as tk
from tkinter import filedialog
from PIL import Image
import os

# Define the ImageConverterApp class
class ImageConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Converter ni Hot Papi")

        # Section 1: Input
        self.label_input = tk.Label(root, text="Select a PNG image:")
        self.label_input.pack()
        self.input_button = tk.Button(root, text="Browse", command=self.load_image)
        self.input_button.pack()

        # Section 2: Output
        self.label_output = tk.Label(root, text="Output directory:")
        self.label_output.pack()
        self.output_button = tk.Button(root, text="Browse", command=self.choose_output_directory)
        self.output_button.pack()

        # Section 3: Convert button
        self.convert_button = tk.Button(root, text="Convert to JPG", command=self.convert_to_jpg)
        self.convert_button.pack()

        # Initialize variables
        self.input_file = ""
        self.output_dir = ""

    # Function for loading the input image
    def load_image(self):
        self.input_file = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
        self.label_input.config(text=f"Selected image: {self.input_file}")

    # Function for choosing the output directory
    def choose_output_directory(self):
        self.output_dir = filedialog.askdirectory()
        self.label_output.config(text=f"Output directory: {self.output_dir}")

    # Function for converting the input image to JPG
    def convert_to_jpg(self):
        if self.input_file and self.output_dir:
            try:
                img = Image.open(self.input_file)
                img = img.convert('RGB')

                output_file = f"{self.output_dir}/{self.get_file_name()}.jpg"
                img.save(output_file, "JPEG")
                tk.messagebox.showinfo("Success", "Image converted and saved as JPG.")
            except Exception as e:
                tk.messagebox.showerror("Error", f"An error occurred: {str(e)}")
        else:
            tk.messagebox.showerror("Error", "Please select an input image and an output directory.")

    # Function to get the file name from the input file path
    def get_file_name(self):
        return os.path.splitext(os.path.basename(self.input_file))[0]

# Main program
if __name__ == "__main__":
    root = tk.Tk()
    app = ImageConverterApp(root)
    root.mainloop()
