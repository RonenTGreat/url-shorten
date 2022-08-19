import pyshorteners
from tkinter import *

# Window Setup
window = Tk()
window.title("URL Shortener")
window.config(padx=30, pady=30)

# Canvas Setup
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="cut.png")
canvas.create_image(100, 90, image=logo_img)
canvas.grid(column=1, row=0)

# URL Input
url_label = Label(text="URL: ")
url_label.grid(column=0, row=1)
url_input = Entry(width=25)
url_input.grid(column=1, row=1)

window.mainloop()

long_url = input("Enter the URL to shorten: ")
print(long_url)

type_tiny = pyshorteners.Shortener()
short_url = type_tiny.tinyurl.short(long_url)
print("The Shortened URL is: " + short_url)

