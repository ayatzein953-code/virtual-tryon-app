# 👕 AI Virtual Try-On Application

An interactive web-based Virtual Try-On application built with Python, Streamlit, and IDM-VTON AI Model via Hugging Face API.

## 📌 Features
- Garment Transfer: Fits target clothing onto a person's photo accurately while preserving face features and background.
- Interactive UI: Simple drag-and-drop web dashboard created using Streamlit.
- Lightweight Integration: Connects seamlessly with open-source AI models without needing local heavy GPU requirements.

## 🚀 How to Run Locally

1. Clone the repository:
   `bash
   git clone [https://github.com/YOUR_USERNAME/virtual-tryon-app.git](https://github.com/ayatzein953-code/virtual-tryon-app.git)
   cd virtual-tryon-app
2. Create a virtual environment & install dependencies
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   pip install -r requirements.txt
3. Run the Streamlit app
   streamlit run app.py
