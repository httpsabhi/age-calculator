import tkinter as tk
import datetime
from PIL import Image, ImageTk

window = tk.Tk()
window.geometry("520x680")
window.title("Age Calculator")

name = tk.Label(text = "Name")
name.grid(column=0, row=1)
year = tk.Label(text = "Year")
year.grid(column=0, row=2)
month = tk.Label(text = "Month")
month.grid(column=0, row=3)
date = tk.Label(text = "Day")
date.grid(column=0, row=4)

nameInput = tk.Entry()
nameInput.grid(column=1, row=1)
yearInput = tk.Entry()
yearInput.grid(column=1, row=2)
monthInput = tk.Entry()
monthInput.grid(column=1, row=3)
dateInput = tk.Entry()
dateInput.grid(column=1, row=4)

def get():
    name = nameInput.get()
    nam = Person(name, datetime.date(int(yearInput.get()),
                                     int(monthInput.get()),
                                     int(dateInput.get())))
    textArea = tk.Text(master=window, height=5, width=25)
    textArea.grid(column=1, row=6)
    answer = "Hi {nam}!. You are {age} years old !!".format(nam=name,age=nam.age())
    textArea.insert(tk.END, answer)
    
button = tk.Button(window, text="Calculate Age", command=get, bg="pink")
button.grid(column=1, row=5)

class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self.birthdate = birthdate
    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year
        return age
    
window.mainloop()