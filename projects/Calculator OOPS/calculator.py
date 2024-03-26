from ast import operator
from tkinter import *

class Calcuator:
    def __init__(self, height, width):
        self.Height = height
        self.Width = width
        self.root = Tk()
        self.root.title("Calculator")
        self.input_text = ''
        self.button_list = [['C', '**', "Del", 'ScNot'], ['1', '2', '3', '/'], ['4', '5', '6', '*'], ['7', '8', '9', '-'], ['.', '0', '=', '+']]
        self.number_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        self.operator_list = ['+', '-', '*', '/', '**', '.']
        self.delete = 'Del'
        self.equalsTo = '='
        self.clear = 'C'
        self.scientific_notation = 'ScNot'
        self.operator_flag = False
        self.setup()
    
    def setup(self):
        self.canvas = Canvas(self.root, bg = "white", height = self.Height, width = self.Width)
        self.canvas.pack()

        border_frame = Frame(self.canvas, bg = "black")
        border_frame.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.15)

        input_frame = Frame(border_frame, bg = 'white')
        input_frame.place(relx = 0.02, rely = 0.05, relheight = 0.9, relwidth = 0.96)
        self.equation = StringVar()
        self.number_entry = Entry(input_frame, bg = 'light gray', text = self.equation, font = ("Times New Roman", 30))
        self.number_entry.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

        self.button_frame = Frame(self.canvas, bg = "light gray", bd = 3)
        self.button_frame.place(relx = 0.1, rely = 0.25, relwidth = 0.8, relheight = 0.6)

        self.placeButtons()
    
    def placeButtons(self):
        for i in range(5):
            relx = 0
            for j in range(4):
                text = self.button_list[i][j]
                button = Button(self.button_frame, bg = 'black', text = text, fg = 'white', font = ('Times New Roman', 30), command = lambda r = i, c = j: self.markup(r, c))
                button.place(relx = j / 4, rely = i / 5, relheight = 0.2, relwidth = 0.25)

    def markup(self, r, c):
        self.text = self.button_list[r][c]
        if self.text in self.number_list or self.text in self.operator_list:
            self.numberAndOperatorEntry(r, c)
        elif self.text == self.delete:
            self.deleteFunc()
        elif self.text == self.clear:
            self.clearFunc()
        elif self.text == self.equalsTo:
            self.evaluate()

    def numberAndOperatorEntry(self, r, c):
        if self.operator_flag:
            self.input_text += self.text
            self.equation.set(self.input_text)
            if self.text in self.operator_list:
                self.operator_flag = False
        else:
            if self.text in self.number_list:
                self.input_text += self.text
                self.equation.set(self.input_text)   
                self.operator_flag = True         
        
    def deleteFunc(self):
        self.input_text = self.input_text[0:-2] if self.input_text[-2:] == '**' else self.input_text[0:-1]
        self.equation.set(self.input_text)

    def clearFunc(self):
        self.input_text = ''
        self.equation.set(self.input_text)

    def evaluate(self):
        self.input_text = eval(self.input_text)
        self.input_text = str(self.input_text)
        self.equation.set(self.input_text)

    def mainloop(self):
        self.root.mainloop()

GUI = Calcuator(1200, 800)
GUI.mainloop()