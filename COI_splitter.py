import os
import re
from pypdf import PdfReader, PdfWriter

CERTIFICATE_IDENTIFIER = 'CERTIFICATE OF LIABILITY INSURANCE'
HOLDER_RUNOFF = 'THE    EXPIRATION    DATE    THEREOF,    NOTICE   WILL   BE   DELIVERED   IN'

def extract_certificate_holder_name(text):
    for line in text.splitlines():
        if HOLDER_RUNOFF in line:
            holder = line.replace(HOLDER_RUNOFF, '').strip()
            holder = re.sub(r'[^a-zA-Z0-9,\s]', ' ', holder)  # Replace symbols with spaces
            holder = re.sub(r'\s{2,}', ' ', holder)  # Collapse multiple spaces
            return holder[:80].strip()
    return 'Unknown Holder'

def extract_text(page):
    try:
        return page.extract_text(extraction_mode="layout") or ""
    except Exception:
        return ""


def is_certificate_page(text):
    """
    Determine whether a page is the start of a new certificate.
    This logic should be updated to match how certificates are separated.
    """
    lines = text.splitlines()
    return len(lines) >= 3 and CERTIFICATE_IDENTIFIER in lines[2]


def sanitize_filename(name):
    # Keep letters, digits, spaces, hyphens, and commas
    return "".join(c if c.isalnum() or c in (' ', '-', ',') else "" for c in name).strip()


def save_certificate(pages, counter, output_dir, holder_name="Unknown_Holder"):
    writer = PdfWriter()
    for page in pages:
        writer.add_page(page)

    os.makedirs(output_dir, exist_ok=True)

    filename = f"{holder_name}_{counter:04d}.pdf"
    filepath = os.path.join(output_dir, filename)

    with open(filepath, "wb") as f:
        writer.write(f)


def split_certificates(input_pdf_path, output_dir):
    """
    Reads a bulk PDF of COIs and splits it into separate PDFs based on detection logic.
    Saves results into one flat folder (no nested folders by named insured or city).
    """
    reader = PdfReader(input_pdf_path)
    num_pages = len(reader.pages)

    certificate_pages = []
    certificate_counter = 1

    for i in range(num_pages):
        page = reader.pages[i]
        text = extract_text(page)

        is_start = is_certificate_page(text)
        is_last_page = (i == num_pages - 1)

        if is_start and certificate_pages:
            # Use the first page of the certificate to get the holder name
            holder_name = extract_certificate_holder_name(extract_text(certificate_pages[0]))
            holder_name = sanitize_filename(holder_name)
            save_certificate(certificate_pages, certificate_counter, output_dir, holder_name)
            certificate_pages = []
            certificate_counter += 1

        certificate_pages.append(page)

        if is_last_page:
            holder_name = extract_certificate_holder_name(extract_text(certificate_pages[0]))
            holder_name = sanitize_filename(holder_name)
            save_certificate(certificate_pages, certificate_counter, output_dir, holder_name)

