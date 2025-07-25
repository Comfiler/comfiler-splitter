# 📄 Certificate Splitter Web Tool

A fast and secure tool for splitting massive PDFs of **Certificates of Insurance (COIs)** into individual, named PDF files — now with an easy-to-use **Flask web interface**.

---

## 🚀 Features

- 🔍 Automatically detects and separates certificates from large PDFs
- 📁 Optionally organizes certs into folders by **Named Insured** and **City**
- 🧠 Extracts **project numbers** from the Description of Operations
- ⚡ Handles massive files: ~13,000 pages / 2,000+ certs in under 7 minutes
- 🔐 No metadata is stored — processing is in-memory only

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

### 🛠️ Coming Soon
Additional ways to split certificates i.e. Named insured, Project Numbers

CSV metadata export (optional)

OCR support for scanned (image-based) COIs

Docker container for deployment

Email notifications + multi-user support

### 🧠 Built With
Flask

PyPDF

Standard Python modules: io, re, os, tempfile, zipfile

### 📬 Questions or Feature Ideas?
Open an issue or reach out to the maintainer.