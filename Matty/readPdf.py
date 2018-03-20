#hello world
#import PyPDF2
import sys
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.layout import LAParams
import io

def pdfparser(data):

    fp = open(data, 'rb')
    rsrcmgr = PDFResourceManager()
    retstr = io.StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    # Create a PDF interpreter object.
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    # Process each page contained in the document.

    for page in PDFPage.get_pages(fp):
        interpreter.process_page(page)
        data =  retstr.getvalue()

    print(data)

if __name__ == '__main__':
    #pdfparser(sys.argv[1])
    pdfparser('meh.pdf')
'''file=open("meh.pdf","rb")
fileReader = PyPDF2.PdfFileReader(file)

# print the number of pages in pdf file
#print(fileReader.numPages)
#print(fileReader.getPage(1))
read_pdf = PyPDF2.PdfFileReader(file)
page = read_pdf.getPage(0)
page_content = page.extractText()
print page_content
#print (page.getContents())
'''
