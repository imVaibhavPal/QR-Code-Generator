import os
import qrcode
from tkinter import Tk, filedialog

print("=" * 50)
print("        QR Code Generator")
print("=" * 50)

try:
    # User input
    data = input("Enter URL or Text: ").strip()

    if not data:
        raise ValueError("Input cannot be empty!")

    filename = input("Enter file name (without extension): ").strip()

    if filename == "":
        filename = "qrcode"

    image_format = input("Choose format (png/jpg): ").strip().lower()

    if image_format not in ["png", "jpg"]:
        print("Invalid format. Using PNG.")
        image_format = "png"

    qr_color = input("QR Color (default: black): ").strip().lower()

    if qr_color == "":
        qr_color = "black"

    background_color = input("Background Color (default: white): ").strip().lower()

    if background_color == "":
        background_color = "white"

    # Create output folder
    # Hide the Tkinter root window
    root = Tk()
    root.withdraw()

    file_path = filedialog.asksaveasfilename(
    title="Save QR Code",
    defaultextension=f".{image_format}",
    initialfile=filename,
    filetypes=[
        ("PNG Image", "*.png"),
        ("JPEG Image", "*.jpg")
        ]
    )

    if not file_path:
         raise Exception("Save operation cancelled.")
   

    # Generate QR
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )

    qr.add_data(data)
    qr.make(fit=True)

    qr_image = qr.make_image(
        fill_color=qr_color,
        back_color=background_color
    )

    # JPG conversion
    if image_format == "jpg":
        qr_image = qr_image.convert("RGB")

    # Save
    qr_image.save(file_path)

    print("\nQR Code Generated Successfully!")
    print(f"Saved to: {file_path}")

    qr_image.show()
except Exception as error:
    print("\nSomething went wrong.")
    print(error)