from PyPDF2 import PdfFileMerger

pdfs = ['1.pdf', '2.pdf']

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(open(pdf, 'rb'))

with open('1othmerge.pdf', 'wb') as fout:
    merger.write(fout)
