# 📱 QR Code Generator

A simple and customizable **QR Code Generator** built with **Python**.  
This application allows users to generate QR codes from URLs or text with customizable colors, multiple image formats, and a user-selected save location.

---

## ✨ Features

- 🔗 Generate QR codes from URLs or plain text
- 🎨 Customize QR code color
- 🖼️ Customize background color
- 📄 Save as **PNG** or **JPG**
- 💾 Choose where to save the QR code
- 👀 Automatic preview after generation
- ⚠️ Basic error handling for invalid inputs

---

## 🛠️ Tech Stack

- **Python 3**
- **qrcode**
- **Pillow**
- **Tkinter**

---

## 📂 Project Structure

```text
QR-Code-Generator/
│
├── qr_generator.py
├── README.md
├── requirements.txt
├── .gitignore
└── screenshots/
    ├── terminal.png
    └── generated_qr.png
```

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/imVaibhavPal/QR-Code-Generator.git
```

### 2. Navigate to the Project Folder

```bash
cd QR-Code-Generator
```

### 3. Install Required Libraries

```bash
pip install -r requirements.txt
```

### 4. Run the Program

```bash
python qr_generator.py
```

---

## 💻 How It Works

1. Enter a URL or text.
2. Enter a filename.
3. Choose PNG or JPG format.
4. Select QR color.
5. Select background color.
6. Choose a location to save the QR code.
7. The QR code is generated and opened automatically.

---

## 📸 Screenshots

### Terminal

> Add a screenshot named `terminal.png` inside the `screenshots` folder.

![Terminal Screenshot](screenshots/terminal.png)

---

### Generated QR Code

> Add a screenshot named `generated_qr.png` inside the `screenshots` folder.

![Generated QR Code](screenshots/generated_qr.png)

---

## 📌 Example

### Input

```text
URL:
https://github.com

Filename:
github

Format:
png

QR Color:
blue

Background:
white
```

### Output

```text
QR Code Generated Successfully!
```

A QR code image is generated and saved to the selected location.

---

## 📈 Future Improvements

- Add logo support in the center of the QR code
- Build a GUI using Tkinter
- Create a Streamlit web version
- Batch QR code generation
- QR code scanner
- QR history using SQLite
- More customization options

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch

```bash
git checkout -b feature-name
```

3. Commit your changes

```bash
git commit -m "Add new feature"
```

4. Push the branch

```bash
git push origin feature-name
```

5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Vaibhav Kumar Pal**

- 🎓 B.Tech CSE (AI & ML), VIT Bhopal University
- 💻 Python Developer | AI & ML Enthusiast

### Connect with Me

- GitHub: https://github.com/imVaibhavPal
- LinkedIn: https://www.linkedin.com/in/vaibhav-kumar-pal-955aa6293/

