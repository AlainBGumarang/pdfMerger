# Alain B. Gumarang II
# PDF Merger Project
# Based on "3 PYTHON AUTOMATION PROJECTS FOR BEGINNERS" by Internet Made Coder
# https://youtu.be/vEQ8CXFWLZU?si=GSU_BR4ldmIDsWEj
# 
# Requirements:
#   - Install PyPDF2 using 'pip install PyPDF2'
#
# Syntax for code execution: python pdfmerge.py [newMergedFile]

import PyPDF2
from sys import argv
import os

mergeFile = PyPDF2.PdfMerger()
mergeFilename = argv[1] + ".pdf"
num = 0

# Merges the documents in order they appear in File Explorer.
for pdf in os.listdir(os.curdir):
    if pdf.endswith(".pdf"):
        mergeFile.append(pdf)
        num = num + 1

if num > 0:
    mergeFile.write(mergeFilename)
    print("\nDocuments merged.\n")
else:
    print("\nNo PDF Documents to merge\n")