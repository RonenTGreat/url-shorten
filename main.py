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

# Long URL Input
long_url_label = Label(text="URL: ")
long_url_label.grid(column=0, row=1)
long_url_input = Entry(width=25)
long_url_input.grid(column=1, row=1)

# Short URL input
short_url_label = Label(text="Shortened URL: ")
short_url_label.grid(column=0, row=3)
shorted_url = Entry(width=25)
shorted_url.grid(column=1, row=3)

window.mainloop()

long_url = input("Enter the URL to shorten: ")
print(long_url)

type_tiny = pyshorteners.Shortener()
short_url = type_tiny.tinyurl.short(long_url)
print("The Shortened URL is: " + short_url)

