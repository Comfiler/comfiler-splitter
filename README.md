# 📄 Certificate Splitter Web Tool

A fast and secure tool for splitting massive PDFs of **Certificates of Insurance (COIs)** into individual, named PDF files — now with an easy-to-use **Flask web interface**.

---

## 🚀 Features

- 🔍 Automatically detects and separates certificates from large PDFs
- 📂 Saves each certificate as an individual PDF named using the certificate holder
- ⚡ Handles massive files: ~13,000 pages / 2,000+ certs in under 7 minutes
- 🔐 Processing is in-memory only — nothing is stored permanently

---

## 🖥️ Usage

### 1. 📦 Clone the repo

```bash
git clone https://github.com/yourusername/certificate-splitter.git
cd certificate-splitter
```

### 2. 🐍 Set up Python environment
```bash
pip install -r requirements.txt
```
### Or use a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```
### 3. 🚦 Run the web app
```bash
flask run
```
Then visit: http://localhost:5000


### 🧾 Input
Upload a multi-page PDF containing many COIs. Each certificate should start with the standard:
### CERTIFICATE OF LIABILITY INSURANCE
### 📤 Output

One PDF per certificate, named using:

Certificate Holder

All certificates are zipped and returned as a download.



### 🔐 Privacy & Security
No certificate metadata is written to disk or stored

Everything runs locally and in-memory

Safe to deploy in secure internal environments

### 🛠️ Planned Features
- Folder organization by Named Insured or City
- Project number extraction from Description of Operations
- CSV metadata export
- OCR support for scanned/image-based COIs
- Docker container for deployment
- Email notifications & multi-user support

### 🧠 Built With
Flask

PyPDF

Standard Python modules: io, re, os, tempfile, zipfile

### 📬 Questions or Feature Ideas?
Open an issue or reach out to the maintainer.