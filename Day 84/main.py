# Import statements:
import os
from tkinter import *
from tkinter import filedialog

from PIL import Image, ImageTk


# Function to apply watermark and save image:
def apply_watermark(img_path, wm_path):
    img = Image.open(img_path)
    wm = Image.open(wm_path)
    img.alpha_composite(wm)
    new_file = os.path.join("images", "wmrk_" + os.path.basename(img_path))
    img.save(new_file)

# GUI class:


class WatermarkApp:
    def __init__(self, master):
        self.master = master
        self.master.configure(background='#353B45')
        self.master.title("RHC-IV Watermark App")
        self.master.geometry('800x600')

        # Add logo to GUI:
        self.logo = ImageTk.PhotoImage(Image.open("images/logo.png"))
        self.logo_label = Label(
            image=self.logo,
            background='#353B45'
        )
        self.logo_label.pack()

        # Add browse button:
        self.browse_button = Button(
            text="Browse",
            foreground='#D19A66',
            font=(
                'SF Pro Display',
                18,
                'bold',
            ),
            command=self.browse
        )
        self.browse_button.pack()

        # Add cancel button:
        self.cancel_button = Button(
            text="Cancel",
            foreground='#D19A66',
            font=(
                'SF Pro Display',
                18,
                'bold',
            ),
            command=self.cancel
        )
        self.cancel_button.pack()

        # Add close button:
        self.close_button = Button(
            text="Close",
            foreground='#D19A66',
            font=(
                'SF Pro Display',
                18,
                'bold',
            ),
            command=self.master.quit
        )
        self.close_button.pack()

    # Browse for images:
    def browse(self):
        options = {
            'initialdir': 'Users/rhc.iv/Pictures',
            'title': 'Select Image',
            'filetypes': (("PNG files", "*.png"), ("all files", "*.*"))
        }
        img_path = filedialog.askopenfilename(**options)
        if img_path:
            apply_watermark(img_path, "images/wm_rhc.png")
            self.browse_button.config(
                text="Watermarked!",
                state=DISABLED
            )

    # Cancel browsing:
    def cancel(self):
        self.browse_button.config(
            text="Browse",
            state=NORMAL
        )

# Main function to run the app:


if __name__ == "__main__":
    root = Tk()
    app = WatermarkApp(root)
    root.mainloop()
