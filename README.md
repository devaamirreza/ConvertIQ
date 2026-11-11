<div align="center">

# ConvertIQ

### Your everyday unit converter.

A clean, responsive unit-conversion app built with Python and Streamlit — with four conversion categories and a Light/Dark theme.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](YOUR_STREAMLIT_APP_URL)
[![Python](https://img.shields.io/badge/Python-3.13+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

</div>

---

## ✨ Overview

ConvertIQ makes everyday unit conversions simple. Choose a category, select the source and target units, enter a value, and get the converted result.

The interface includes a unified workspace, a category-specific visual panel, and a theme toggle for comfortable use in both light and dark environments.

## 🚀 Live Demo

**[Launch ConvertIQ](https://convertiq-devaamirreza.streamlit.app/)**

> Replace `YOUR_STREAMLIT_APP_URL` with the public URL of your deployed Streamlit app.

## 🧰 Features

- **Length:** Kilometres ↔ Metres
- **Weight:** Kilograms ↔ Grams
- **Temperature:** Celsius, Fahrenheit and Kelvin
- **Volume:** Litres ↔ Millilitres
- **Light and Dark themes**
- **Persistent conversion result** when switching themes
- **Responsive Streamlit interface**
- Separate conversion logic for easier maintenance

## 🖥️ Preview

<!-- Add a screenshot of the running app to the repository, then update the path below. -->
<!-- Suggested path: assets/convertiq-preview.png -->

![ConvertIQ application preview](assets/convertiq-preview.png)

## 🛠️ Built With

- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/)
- CSS for custom styling
- Git and GitHub for version control

## 📁 Project Structure

```text
ConvertIQ/
├── app.py              # Streamlit user interface
├── conversions.py      # Unit conversion functions and router
├── requirements.txt    # Python dependencies
├── README.md           # Project documentation
└── assets/             # Optional project images and screenshots
```

## ⚙️ Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/devaamirreza/ConvertIQ.git
cd ConvertIQ
```

### 2. Create and activate a virtual environment

**Windows:**

```bash
python -m venv .venv
.venv\Scripts\activate
```

**macOS / Linux:**

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the app

```bash
streamlit run app.py
```

The app will open in your browser, usually at `http://localhost:8501`.

## 🧠 Project Structure & Design

The project separates the interface from the conversion logic:

- `app.py` handles the Streamlit interface, category selection, theme state and result display.
- `conversions.py` contains reusable conversion functions and the `convert_units()` router.

This separation keeps the code easier to test, understand and extend.

## 🗺️ Roadmap

Potential future improvements:

- [ ] Add more length, weight and volume units
- [ ] Add area and speed conversions
- [ ] Add conversion history
- [ ] Add automated tests
- [ ] Improve mobile layout and accessibility

## 🤝 Contributions

Suggestions and improvements are welcome. Feel free to open an issue or submit a pull request.

## 📄 License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

<div align="center">

**Built with Python, Streamlit and curiosity.**

</div>
