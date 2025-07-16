from PyPDF2 import PdfMerger
import os
merger=PdfMerger()
files=os.listdir("PDF FOLDER")   # You can also write "." instead of "PDF FOLDER" which means the current directory.
for file in files:
    if file.endswith(".pdf"):
        merger.append(f"PDF FOLDER/{file}")
merger.write("PDF FOLDER/MERGED FILES.pdf")   # This will create "MERGED FILES" File inside "PDF FOLDER".
merger.close()