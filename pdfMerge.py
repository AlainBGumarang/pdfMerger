# Alain B. Gumarang II
# PDF Merger Project 
# (based on "3 PYTHON AUTOMATION PROJECTS FOR BEGINNERS" by Internet Made Coder)
# https://youtu.be/vEQ8CXFWLZU?si=GSU_BR4ldmIDsWEj

import PyPDF2
from sys import argv
import os

mergeFile = PyPDF2.PdfMerger()
mergeFilename = argv[1]

# Merges the documents in order they appear in File Explorer.
for pdf in os.listdir(os.curdir):
    if pdf.endswith(".pdf"):
        mergeFile.append(pdf)

mergeFile.write(mergeFilename)