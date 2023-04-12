# age-calculator
age calculator using tkinter in Python

This code is an implementation of a simple age calculator GUI using the Tkinter library in Python. The program allows the user to enter their name and birthdate, and then calculates their age when the "Calculate Age" button is clicked.
The program starts by importing necessary modules - tkinter and datetime, and PIL (Python Imaging Library) for image processing.
Next, a new window is created using the Tk() method, and its size and title are set. Then, the labels for the name, year, month, and date fields are created and placed on the grid using the grid() method. The corresponding entry fields are also created using the Entry() method and placed on the grid using the same method.
A function called "get()" is defined, which retrieves the user inputs and calculates the age using the Person class. It then displays the result using the Text() method and the insert() method.
Finally, a Button widget is created with the text "Calculate Age" and the command set to the "get()" function. The button is placed on the grid using the grid() method.
The Person class is defined with two attributes - name and birthdate, and a method called "age()" which calculates the age based on the birthdate provided.
The program then enters the main loop using the mainloop() method, which displays the window and waits for user input.
Overall, this code is a simple implementation of a GUI-based age calculator using the Tkinter library in Python.
