import qrcode
from tkinter import Tk, filedialog

print("=" * 50)
print("         QR Code Generator")
print("=" * 50)

try:
    # -----------------------------
    # Get user input
    # -----------------------------
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
    print("black, blue, red, green, purple")

    qr_color = input("QR Color (default: black): ").strip().lower()
    if not qr_color:
        qr_color = "black"

    print("\nAvailable Background Colors:")
    print("white, yellow, pink, cyan")

    background_color = input("Background Color (default: white): ").strip().lower()
    if not background_color:
        background_color = "white"

    # -----------------------------
    # Choose Save Location
    # -----------------------------
    root = Tk()
    root.withdraw()
    root.attributes("-topmost", True)

    file_path = filedialog.asksaveasfilename(
        title="Save QR Code",
        initialfile=filename,
        defaultextension=f".{image_format}",
        filetypes=[
            ("PNG Image", "*.png"),
            ("JPEG Image", "*.jpg")
        ]
    )

    root.destroy()

    if not file_path:
        print("Save cancelled.")
        exit()

    # -----------------------------
    # Create QR Code
    # -----------------------------
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

    # Convert to RGB only for JPG
    if image_format == "jpg":
        qr_image = qr_image.convert("RGB")

    # -----------------------------
    # Save QR Code
    # -----------------------------
    qr_image.save(file_path)

    print("\n" + "=" * 50)
    print("✅ QR Code Generated Successfully!")
    print("=" * 50)
    print("📁 Location :", file_path)
    print("📄 File Name:", filename)
    print("🎨 QR Color :", qr_color)
    print("🖼 Background:", background_color)

    # Open the generated image
    qr_image.show()

except Exception as error:
    print("\n❌ Error:", error)