import pyshorteners
from tkinter import *
import pyperclip



def shorten():
    type_tiny = pyshorteners.Shortener()
    short_url = type_tiny.tinyurl.short(long_url_input.get())
    shorted_url.insert(0, short_url)
    print("The Shortened URL is: " + short_url)

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

# Shorted Button
shorten_button = Button(text="Shorten", width=20, command=shorten)
shorten_button.grid(column=1, row=4, columnspan=2)

# copy_button = Button(text="Copy", width=20, command=copy)
# copy_button.grid(column=1, row=5, columnspan=2)



window.mainloop()

