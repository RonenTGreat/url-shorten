import pyshorteners
from tkinter import *

long_url = input("Enter the URL to shorten: ")
print(long_url)

type_tiny = pyshorteners.Shortener()
short_url = type_tiny.tinyurl.short(long_url)
print("The Shortened URL is: " + short_url)

