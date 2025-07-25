# app.py

from flask import Flask, request, render_template, send_file
import tempfile
import os
import io
import zipfile

from COI_splitter import split_certificates

app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 200 * 1024 * 1024  # 200MB limit


def compress_folder(input_folder, output_zip_path):
    """Compresses the entire folder into a ZIP with compression."""
    with zipfile.ZipFile(output_zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, _, files in os.walk(input_folder):
            for file in files:
                full_path = os.path.join(root, file)
                # Store files with relative paths (flat in your case)
                arcname = os.path.relpath(full_path, input_folder)
                zipf.write(full_path, arcname)


@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        uploaded_file = request.files.get('pdf_file')

        if not uploaded_file or not uploaded_file.filename.endswith('.pdf'):
            return "Please upload a valid PDF file."

        with tempfile.TemporaryDirectory() as tmp_dir:
            input_path = os.path.join(tmp_dir, 'input.pdf')
            uploaded_file.save(input_path)

            output_dir = os.path.join(tmp_dir, 'output')
            split_certificates(input_path, output_dir)

            zip_path = os.path.join(tmp_dir, 'certificates.zip')
            compress_folder(output_dir, zip_path)

            # Read zip into memory so we can serve it before temp folder cleanup
            with open(zip_path, 'rb') as f:
                zip_bytes = f.read()

            zip_stream = io.BytesIO(zip_bytes)
            zip_stream.seek(0)

            return send_file(
                zip_stream,
                as_attachment=True,
                download_name='certificates.zip',
                mimetype='application/zip'
            )

    return render_template('upload.html')