import os
import sys
import qrcode
from tkinter import Tk, filedialog

# Valid colors
VALID_QR_COLORS = ["black", "blue", "red", "green", "purple"]
VALID_BG_COLORS = ["white", "yellow", "pink", "cyan"]


def get_user_input():
    """Collect and validate user input."""

    print("=" * 50)
    print("            QR Code Generator")
    print("=" * 50)

    data = input("Enter URL or Text: ").strip()
    if not data:
        raise ValueError("Input cannot be empty!")

    filename = input("Enter file name (without extension): ").strip()
    if not filename:
        filename = "qrcode"

    image_format = input("Choose image format (png/jpg): ").strip().lower()

    if image_format not in ["png", "jpg"]:
        print("Invalid format! Using PNG.")
        image_format = "png"

    print("\nAvailable QR Colors:")
    print(", ".join(VALID_QR_COLORS))

    qr_color = input("QR Color (default: black): ").strip().lower()

    if qr_color not in VALID_QR_COLORS:
        print("Invalid QR color! Using black.")
        qr_color = "black"

    print("\nAvailable Background Colors:")
    print(", ".join(VALID_BG_COLORS))

    background_color = input("Background Color (default: white): ").strip().lower()

    if background_color not in VALID_BG_COLORS:
        print("Invalid background color! Using white.")
        background_color = "white"

    return (
        data,
        filename,
        image_format,
        qr_color,
        background_color
    )


def choose_save_location(filename, image_format):
    """Open save dialog."""

    root = Tk()
    root.withdraw()
    root.attributes("-topmost", True)

    try:
        file_path = filedialog.asksaveasfilename(
            title="Save QR Code",
            initialfile=filename,
            defaultextension=f".{image_format}",
            filetypes=[
                ("PNG Image", "*.png"),
                ("JPEG Image", "*.jpg")
            ]
        )
    finally:
        root.destroy()

    if not file_path:
        print("Save cancelled.")
        sys.exit()

    return file_path


def generate_qr(data, qr_color, background_color):
    """Generate QR Code."""

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4
    )

    qr.add_data(data)
    qr.make(fit=True)

    return qr.make_image(
        fill_color=qr_color,
        back_color=background_color
    )


def main():

    try:
        (
            data,
            filename,
            image_format,
            qr_color,
            background_color
        ) = get_user_input()

        file_path = choose_save_location(
            filename,
            image_format
        )

        qr_image = generate_qr(
            data,
            qr_color,
            background_color
        )

        # Convert to RGB if saving as JPG
        extension = os.path.splitext(file_path)[1].lower()

        if extension == ".jpg":
            qr_image = qr_image.convert("RGB")

        qr_image.save(file_path)

        print("\n" + "=" * 50)
        print("✅ QR Code Generated Successfully!")
        print("=" * 50)
        print(f"📁 Saved At      : {file_path}")
        print(f"📄 File Name     : {os.path.basename(file_path)}")
        print(f"🎨 QR Color      : {qr_color}")
        print(f"🖼 Background     : {background_color}")

        try:
            qr_image.show()
        except Exception:
            print("Unable to preview image.")

    except Exception as error:
        print("\n Error:", error)


if __name__ == "__main__":
    main()