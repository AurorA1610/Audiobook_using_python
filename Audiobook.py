# importing necessary libraries
import pyttsx3
import PyPDF2

# creating a book reader
book = open('python_tutorial.pdf', 'rb')
reader = PyPDF2.PdfReader(book)
no_of_pages = len(reader.pages)
print("number of pages in pdf is", no_of_pages)

# initiating reader that can read out loud
loud_reader = pyttsx3.init()

# reader will from page 19 (the previous pages are index, we don't want to read that) to the last page
for num in range(19, no_of_pages):
    page = reader.pages[num]
    text = page.extract_text()
    loud_reader.say(text)
    loud_reader.runAndWait()