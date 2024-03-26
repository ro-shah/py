# from datetime import datetime

# date = datetime.now()
# current_date = str(date).split()
# print(current_date[0])

# lis = [i for i in range(1, 11)]
# print(lis)
# lis = lis[-5:]
# print(lis)

# username = "hello"
# file_path = r'C:\Python\VScode Programs\Banking Software\Bank Statements' + "\\" + username+ ".txt"

# print(file_path)

# import smtplib

# username = 'ronilbanksco@gmail.com'
# password = 'RonilBanks_007'
# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.starttls()
# server.login(username, password)
# message = ('''<h1>Heading 1</h1>
#         <h2>Heading 2</h2>
#         <h3>Heading 3</h3>
#         <h4>Heading 4</h4>
#         <h5>Heading 5</h5>
#         <h6>Heading 6</h6>''')
# server.sendmail(username, "ronil.theamazing@gmail.com", message)
# print("sent")

# import smtplib
# import base64

# file = r'C:\Python\VScode Programs\Banking Software\Bank Statements\ronil.txt'
# fo = open(file, "rb")
# filecontent = fo.read()
# encodedcontent = base64.b64encode(filecontent)  # base64

# marker = "AUNIQUEMARKER"

# body ="""
# This is a text afile of your bank account ad we can also rob you.
# """
# # Define the main headers.
# part1 = """From: From Person <ronilbanksco@gmail.com>
# To: To Person <amrood.admin@gmail.com>
# Subject: Sending Attachement
# MIME-Version: 1.0
# Content-Type: multipart/mixed; boundary=%s
# --%s
# """ % (marker, marker)

# # Define the message action
# part2 = """Content-Type: text/plain
# Content-Transfer-Encoding:8bit

# %s
# --%s
# """ % (body,marker)

# # Define the attachment section
# part3 = """Content-Type: multipart/mixed; name=\"%s\"
# Content-Transfer-Encoding:base64
# Content-Disposition: attachment; filename=%s

# %s
# --%s--
# """ %(file, file, encodedcontent, marker)
# message = part1 + part2 + part3


# server = smtplib.SMTP_SSL('smtp.googlemail.com', 465)
# server.starttls()
# server.login('ronilbanksco@gmail.com','RonilBanks_007')
# server.sendmail('ronilbanksco@gmail.com','ronil.theamazing@gmail.com',message)
# print('sent')

# import turtle

# hello = turtle.Turtle()
# print(hello.direction)

# turtle.done()

# class Home:
#     def __init__(self, numberofstories, color, squarefeet):
#         self.nos = numberofstories
#         self.colour = color
#         self.sqft = squarefeet

#     def show_details(self):
#         print("Number of Stories is " + str(self.nos) + ", Color is " + self.colour + ", Square Feet is " + str(self.sqft))

# townhome = Home(2, "Beige", 1000)
# apartment = Home(1, "White", 600)
# hut = Home(1, "Brown", 100)

# print(townhome.nos)
# print(apartment.nos, apartment.colour, apartment.sqft)
# print(hut.show_details())
# a = "ronil"
# print(type(a))

# class AnythingThatYouWant:
#     Temp = 300

# obj1 = AnythingThatYouWant()
# obj1.temp = 100
# obj2 = AnythingThatYouWant()
# obj2.temp = 200
# print(obj1.temp, obj2.temp, obj1.Temp)

# from tkinter import *
# from tkinter import font

# root = Tk()
# root.title('Font Families')
# fonts=list(font.families())
# fonts.sort()

# def populate(frame):
#     '''Put in the fonts'''
#     listnumber = 1
#     for item in fonts:
#         label = "listlabel" + str(listnumber)
#         label = Label(frame,text=item,font=(item, 16)).pack()
#         listnumber += 1

# def onFrameConfigure(canvas):
#     '''Reset the scroll region to encompass the inner frame'''
#     canvas.configure(scrollregion=canvas.bbox("all"))

# canvas = Canvas(root, borderwidth=0, background="#ffffff")
# frame = Frame(canvas, background="#ffffff")
# vsb = Scrollbar(root, orient="vertical", command=canvas.yview)
# canvas.configure(yscrollcommand=vsb.set)

# vsb.pack(side="right", fill="y")
# canvas.pack(side="left", fill="both", expand=True)
# canvas.create_window((4,4), window=frame, anchor="nw")

# frame.bind("<Configure>", lambda event, canvas=canvas: onFrameConfigure(canvas))

# populate(frame)

# root.mainloop()

# from tkinter import *

# root = Tk()
# root.title("Calculator")
# root.mainloop()

# expression = '[3, 4 5]'
# expression = eval(expression)
# expression.append(12)
# print(expression)

# button_name_list = [[0 for i in range(4)] for j in range(5)]
# print(button_name_list)

# button_name_list = [[0] * 4] * 5
# print(button_name_list)

# import math

# number = 9
# print(eval('9 sin'))

# i = 1873
# print(i[1:2])

# new_matrix = [[0] * 4 for _ in range(4)]
# print(new_matrix)

matrix = [
[2, 0, 0, 0], 
[2, 0, 4, 0], 
[2, 0, 0, 0], 
[2, 0, 0, 0]]

def stack():
    global matrix
    new_matrix = [
    [0, 0, 0, 0], 
    [0, 0, 0, 0], 
    [0, 0, 0, 0], 
    [0, 0, 0, 0]]

    for i in range(4):
        fill_position = 0
        for j in range(4):
            if matrix[i][j] != 0:
                new_matrix[i][fill_position] = matrix[i][j]
                fill_position += 1
            
    matrix = new_matrix.copy()

def combine():
    global matrix
    for i in range(4):
        for j in range(3):
            if matrix[i][j] != 0 and matrix[i][j+1] == matrix[i][j]:
                matrix[i][j] = matrix[i][j] + matrix[i][j+1]
                matrix[i][j+1] = 0

def reverse():
    global matrix
    new_matrix = [
    [0, 0, 0, 0], 
    [0, 0, 0, 0], 
    [0, 0, 0, 0], 
    [0, 0, 0, 0]]
    for i in range(4):
        for j in range(4):
            new_matrix[i][j] = matrix[i][3 - j]

    matrix = new_matrix

def transpose():
    global matrix
    new_matrix = [[0] * 4 for i in range(4)]
    for i in range(4):
        for j in range(4):
            new_matrix[i][j] = matrix[j][i]
    
    matrix = new_matrix

transpose()
reverse()
stack()
combine()
stack()
reverse()
transpose()

print(*matrix, sep='\n')

                