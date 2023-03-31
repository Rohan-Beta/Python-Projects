# merge pdf

# to perform any task in pdf we use this library
import PyPDF2 # this library is used to merge pdf

pdfFiles = ["sample.pdf" , "file-sample.pdf"] # store two pdf files

merger = PyPDF2.PdfMerger() # meged two pdf

for file in pdfFiles : # access all the files in pdf
    pdfFiles2 = open(file , "rb") # open pdf
    
    pdfReader = PyPDF2.PdfReader(pdfFiles2) # read the pdf files
    merger.append(pdfReader) # append and merged
    
pdfFiles2.close() # close the pdf
merger.write("merged.pdf") #create new file to store merged pdf
