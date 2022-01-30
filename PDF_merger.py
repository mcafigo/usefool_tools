#! python3
# combinePdfs.py - Combines all the PDFs in the current working directory intoa single PDF.

import PyPDF2, os

pdfFiles = []


for filename in os.listdir('.'):
  if filename.endswith('.pdf'):
    pdfFiles.append(filename)
pdfFiles.sort(key = str.lower)
    
pdfWriter = PyPDF2.PdfFileWriter()

# TODO: Loop through all the PDF files.
for filename in pdfFiles:
  pdfFileObj = open(filename, 'rb')
  pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
  
# TODO: Loop through all the pages (except the first) and add them.
  for pageNum in range(0, pdfReader.numPages):
        pageObj = pdfReader.getPage(pageNum)
        pdfWriter.addPage(pageObj)
  
# TODO: Save the resulting PDF to a file.
pdfOutput = open('allDrawings.pdf', 'wb')
pdfWriter.write(pdfOutput)
pdfOutput.close()
