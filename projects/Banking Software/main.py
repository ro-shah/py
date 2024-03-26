# imports 
import profile
import time
from tkinter import *
import json
from tkinter import ttk
from datetime import datetime
import smtplib
import base64
import ssl
from email.message import EmailMessage
import random
from tkinter import messagebox
from CP_OTP import send_otp


# color scheme
color1 = "#6e7f80"
color2 = "#536872"
color3 = '#708090'
color4 = '#536878'
color5 = '#36454f'

root = Tk()
canvas = Canvas(root, width = 1000, height = 1000, bg = 'black').pack()
border = Frame(canvas, bg = color2)
border.place(rely = 0.02, relx = 0.02, relheight = 0.96, relwidth = 0.96)
title = Label(border,  text = 'RonilBanksCo', font = ('ink free', 96), fg = 'black', bg = color2).pack()
basic_text = ('ink free', 22)
title_text = ("Times New Roman", 50)
sender = "ronil.theamazing@gmail.com"
sender_password = "gfapdputusthxjsa"

# Setup
def login_screen():
    global border, password, username
    log_in_frame = Frame(border, bg = color2, bd = 5)
    log_in_frame.place(rely = 0.3, relx = 0.1, relheight = 0.4, relwidth = 0.8)

    username = Entry(log_in_frame, font = ('Times New Roman', 22), bd = 4, bg = color1)
    username.place(relwidth = 0.7, relheight = 0.15, relx = 0.3)
    usertext = Label(log_in_frame, bg = color2, text = 'Username: ', font = basic_text, fg = 'black')
    usertext.place(relx = 0, rely = 0, relheight = 0.15, relwidth = 0.3)

    password = Entry(log_in_frame, font = ('Times New Roman', 22), bd = 4, bg = color1, show = '*')
    password.place(relwidth = 0.7, relheight = 0.15, relx = 0.3, rely = 0.2)
    passtext = Label(log_in_frame, bg = color2, text = 'Password: ', font = basic_text, fg = 'black')
    passtext.place(relx = 0, rely = 0.2, relheight = 0.15, relwidth = 0.3)

    sign_in = Button(log_in_frame, bg = color1, command = login, text = 'Sign In', font = basic_text)
    sign_in.place(relx = 0.3, rely = 0.6, relheight = 0.15, relwidth = 0.4)

    sign_up_txt = Label(log_in_frame, text = "Don't have an account? Click Here.", font = ('ink free', 22), fg = 'blue', bg = color2, cursor = 'Hand2')
    sign_up_txt.place(relx = 0.15, rely = 0.85, relheight = 0.15, relwidth = 0.7)
    sign_up_txt.bind("<Button-1>", sign_up)

def give_account_data():
    handle_r = open("C:\Python\VScode Programs\Python Class\Banking Software\AccDatabase.json", "r")
    data = json.load(handle_r)
    handle_r.close()
    return data

def write_account_data(data):
    handle_w = open("C:\Python\VScode Programs\Python Class\Banking Software\AccDatabase.json", "w")
    json.dump(data, handle_w, indent = 4)
    handle_w.close()


def login():
    global username, password, username_nt
    data = give_account_data()
    username_nt = username.get()
    password_nt = password.get()
    if username_nt in data:
        if data[username_nt]["password"] == password_nt:
            messagebox.showinfo("showinfo", "Login Successfull!")
            home_screen()
        else:
            messagebox.showerror("showerror", "Incorrect Password!")
    else:
        messagebox.showerror("showerror", "Incorrect Username!")

def sign_up(smartie):
    global password_s, conf_password, username_s
    signup_frame = Frame(border, bg = color2, bd = 5)
    signup_frame.place(rely = 0.3, relx = 0.1, relheight = 0.4, relwidth = 0.8)
    username_s = Entry(signup_frame, font = ('Times New Roman', 22), bd = 4, bg = color2)
    username_s.place(relwidth = 0.7, relheight = 0.15, relx = 0.3)
    usertext_s = Label(signup_frame, bg = color2, text = 'New Username: ', font = basic_text, fg = 'black')
    usertext_s.place(relx = 0, rely = 0, relheight = 0.15, relwidth = 0.3)

    password_s = Entry(signup_frame, font = ('Times New Roman', 22), bd = 4, bg = color2)
    password_s.place(relwidth = 0.7, relheight = 0.15, relx = 0.3, rely = 0.2)
    passtext_s = Label(signup_frame, bg = color2, text = 'New Password: ', font = basic_text, fg = 'black')
    passtext_s.place(relx = 0, rely = 0.2, relheight = 0.15, relwidth = 0.3)

    conf_password = Entry(signup_frame, font = ('Times New Roman', 22), bd = 4, bg = color2)
    conf_password.place(relwidth = 0.7, relheight = 0.15, relx = 0.3, rely = 0.4)
    conf_passtext = Label(signup_frame, bg = color2, text = 'Confirm Password: ', font = basic_text, fg = 'black')
    conf_passtext.place(relx = 0, rely = 0.4, relheight = 0.15, relwidth = 0.3)

    create_account = Button(signup_frame, bg = color2, command = validate, text = 'Create Account', font = basic_text)
    create_account.place(relx = 0.25, rely = 0.6, relheight = 0.15, relwidth = 0.5)


def validate():
    global password_s, conf_password, root, username_s, username_t
    password_t = password_s.get()
    conf_password_t = conf_password.get()
    username_t = username_s.get()
    if password_t == conf_password_t and password_validate(password_t):
        confirmation = Toplevel(root, height = 300, width = 900, bg = 'black')
        Label(confirmation, text = 'Sucess! Account has been created.', font = basic_text, bg = 'black', fg = color2).pack()
        # time.sleep(10)
        # confirmation.quit()
        personal_data()
        print(password, conf_password) 
    else:
        sign_up('smartie')
        incorrect = Toplevel(root, height = 300, width = 900, bg = 'black')
        Label(incorrect, text = 'Account passwords are not the same, or it \ndoes not fit the requirments of the password \n(One capital, lowercase, number, special character [#, @, $, _],\n and it must be above 7 characters.', font = basic_text, bg = 'black', fg = color2).pack()    

def password_validate(password_t):
    one_upper = lambda x: any(i.isupper() for i in x)
    one_lower =  lambda x: any(i.islower() for i in x)
    one_number = lambda x: any(i.isnumeric() for i in x)
    one_special = lambda x: any(i in ['#', '@', '$', '_'] for i in x)
    if len(password_t) > 7 and password and one_upper(password_t) and one_lower(password_t) and one_number(password_t) and one_special(password_t):  
        data = give_account_data()
        data[username_t] = {"password": password_t}
        handle_w = open("C:\Python\VScode Programs\Python Class\Banking Software\AccDatabase.json", "w")
        json.dump(data, handle_w, indent = 4)
        handle_w.close()
        return True
    else:
        return False 

def personal_data():
    global personal_data_frame, name, last_name, phone_number, email, address
    personal_info = Toplevel(root, height = 1000, width = 1000)
    personal_data_frame = Frame(personal_info, bg = color2, bd = 5)
    personal_data_frame.place(rely = 0.1, relx = 0.1, relheight = 0.8, relwidth = 0.8)

    name = Entry(personal_data_frame, font = ('Times New Roman', 22), bd = 4, bg = color2)
    name.place(relwidth = 0.7, relheight = 0.1, relx = 0.3)
    nametext = Label(personal_data_frame, bg = color2, text = 'First Name: ', font = basic_text, fg = 'black')
    nametext.place(relx = 0, relheight = 0.1, relwidth = 0.3)

    last_name = Entry(personal_data_frame, font = ('Times New Roman', 22), bd = 4, bg = color2)
    last_name.place(relwidth = 0.7, relheight = 0.1, relx = 0.3, rely = 0.1)
    last_name_text = Label(personal_data_frame, bg = color2, text = 'Last Name: ', font = basic_text, fg = 'black')
    last_name_text.place(relx = 0, rely = 0.1, relheight = 0.1, relwidth = 0.3)

    phone_number = Entry(personal_data_frame, font = ('Times New Roman', 22), bd = 4, bg = color2)
    phone_number.place(relwidth = 0.7, relheight = 0.1, relx = 0.3, rely = 0.2)
    phone_number_text = Label(personal_data_frame, bg = color2, text = 'Phone #: ', font = basic_text, fg = 'black')
    phone_number_text.place(relx = 0, rely = 0.2, relheight = 0.1, relwidth = 0.3)

    email = Entry(personal_data_frame, font = ('Times New Roman', 22), bd = 4, bg = color2)
    email.place(relwidth = 0.7, relheight = 0.1, relx = 0.3, rely = 0.3)
    email_text = Label(personal_data_frame, bg = color2, text = 'Email Address: ', font = basic_text, fg = 'black')
    email_text.place(relx = 0, rely = 0.3, relheight = 0.15, relwidth = 0.3)

    address = Entry(personal_data_frame, font = ('Times New Roman', 22), bd = 4, bg = color2)
    address.place(relwidth = 0.7, relheight = 0.1, relx = 0.3, rely = 0.4)
    address_text = Label(personal_data_frame, bg = color2, text = 'Address: ', font = basic_text, fg = 'black')
    address_text.place(relx = 0, rely = 0.4, relheight = 0.1, relwidth = 0.3)

    submit_details = Button(personal_data_frame, bg = color2, command = enter_details, text = 'Submit Details', font = basic_text)
    submit_details.place(relx = 0.3, rely = 0.6, relheight = 0.1, relwidth = 0.4)

def enter_details():
    name_t = name.get()
    last_name_t = last_name.get()
    phone_number_t = phone_number.get()
    email_t = email.get()
    address_t = address.get()
    acc_data = give_account_data()
    
    for k, v in [("name", name_t), ("last name", last_name_t), ("phone #", phone_number_t), ("email", email_t), ("address", address_t), ("balance", 0), ("transactions", []), ("file path", "None")]:
        acc_data[username_t][k] = v

    write_account_data(acc_data)
    login_screen()

def update_balances():
    global wbal_label, balance, dbal_label
    wbal_label.configure(text = 'Current Balance:\n' + '$' + str(bal))
    dbal_label.configure(text = 'Current Balance:\n' + '$' + str(bal))
    balance.configure(text = '$' + str(bal))
 
def email_statement():
    global reciever
    global username_nt
    file = "C:\\Python\\VScode Programs\\Python Class\\Banking Software\\Bank Statements\\" + username_nt + '.txt'
    fo = open(file, "r")
    filecontent = fo.read()
    data = give_account_data()
    reciever = data[username_nt]["email"]
    msg = EmailMessage()
    msg["From"] = sender
    msg["Subject"] = "Subject"
    msg["To"] = reciever
    msg.set_content("This is the message body")
    msg.add_attachment(filecontent)

    # data[username_nt]["file path"] = file
    # print(filecontent)
    # encodedcontent = base64.b64encode(filecontent)  # base64
    # print(encodedcontent)

    # marker = "AUNIQUEMARKER"

    body ="""
    Below is your recent transactions for your RonilBanksCo account. If you have not signed up for RonilBanksCo, report this message as spam.
    """
    # # Define the main headers.
    # part1 = """From: <%s>
    # To: <%s>
    # Subject: RonilBanksCo Email Statement
    # MIME-Version: 1.0
    # Content-Type: multipart/mixed; boundary=%s
    # --%s
    # """ % (sender, reciever, marker, marker)

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


    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender, sender_password)
        server.sendmail(sender, reciever, msg)
        
    write_account_data(data)
    print("Sent")

def home_screen():
    global bal, balance
    home_base = Toplevel(root, height = 600, width = 900, bg = color2)

    button_frame = LabelFrame(home_base, bg = color2, highlightbackground = 'black', highlightthickness = 4, text = "Options", fg = 'black', font = basic_text, labelanchor = 'n')
    button_frame.place(relx = 0.05, rely = 0.05, relheight = 0.9, relwidth = 0.3)

    acc_balance_frame = Frame(home_base, bg = color2, highlightthickness = 4, highlightbackground = 'black')
    acc_balance_frame.place(relx = 0.4, rely = 0.05, relheight = 0.9, relwidth = 0.55)

    button_height = 0.1875
    button_spacing = 0.05
    banking_button = Button(button_frame,bg=color2,fg='black',font = basic_text, text='Banking', command = banking)
    banking_button.place(relx = 0.1, rely = button_spacing, relheight = 0.1875, relwidth = 0.8)

    emailStatement_button = Button(button_frame, bg = color2, fg = 'black', font = basic_text, text = 'Email Statement', command = email_statement)
    emailStatement_button.place(relx = 0.1, rely = button_spacing * 2 + button_height, relheight = 0.1875, relwidth = 0.8)

    profile_button = Button(button_frame, bg = color2, fg = 'black',font = basic_text, text ='Profile')
    profile_button.place(relx = 0.1, rely = button_spacing * 3 + button_height * 2, relheight = 0.1875, relwidth = 0.8)

    changePassword_button = Button(button_frame,bg=color2,fg='black',font=basic_text, text = 'Change Password', command = changePasswordUI)
    changePassword_button.place(relx = 0.1, rely = button_spacing * 4 + button_height * 3, relheight = 0.1875, relwidth = 0.8)

    json_file_info = give_account_data()
    bal = json_file_info[username_nt]["balance"]
    info = Label(acc_balance_frame, font = basic_text, bg = color2, text = "Your balance is: ", fg = 'black')
    info.place(rely = 0.1, relx = 0.1)

    balance = Label(acc_balance_frame, font = ("ink free", 40), bg = color2, text = '$' + str(bal), fg = 'black')
    balance.place(rely = 0.2, relx = 0.1)

def banking():
    global with_entry, wbal_label, dep_entry, dbal_label, show_trans, trans_button
    banking_frame = Toplevel(root, height = 600, width = 300, bg = color2)
    
    notebook = ttk.Notebook(banking_frame)
    notebook.pack(pady=10, expand=True)

    # create frames
    withdraw = ttk.Frame(notebook, width=800, height=560)
    deposit = ttk.Frame(notebook, width=800, height=560)
    show_trans = ttk.Frame(notebook, width = 800, height = 560)

    withdraw.pack(fill='both', expand=True)
    deposit.pack(fill='both', expand=True)
    show_trans.pack(fill = 'both', expand = True)

    # add frames to notebook
    notebook.add(withdraw, text='Withdraw')
    notebook.add(deposit, text='Deposit')
    notebook.add(show_trans, text='Show Transactions')

    withdraw_frame = Frame(withdraw, bg = color2, highlightbackground = 'black', highlightthickness = 3)
    withdraw_frame.place(rely = 0.1, relx = 0.1, relwidth = 0.8, relheight = 0.3)

    with_label = Label(withdraw_frame, fg = 'black', bg = color2, font = basic_text, text = 'Enter withdrawl amount:')
    with_label.place(rely = 0, relx = 0, relwidth = 1, relheight = 0.5)
    with_entry = Entry(withdraw_frame, bg = color2, font = basic_text)
    with_entry.place(rely = 0.5, relx = 0, relwidth = 0.7, relheight = 0.5)
    withdraw_money = Button(withdraw_frame, fg = 'black', bg = 'dark gray', font = basic_text, text = 'GO', command = withdrawal)
    withdraw_money.place(rely = 0.5, relx = 0.7, relwidth = 0.3, relheight = 0.5)

    wbal_label = Label(withdraw, fg = 'black', bg = color2, font = basic_text, text = 'Current Balance:\n' + '$' + str(bal), highlightbackground = 'black', highlightthickness = 3)
    wbal_label.place(rely = 0.5, relx = 0.1, relwidth = 0.8, relheight = 0.25)

    # notenook ui for deposit
    deposit_frame = Frame(deposit, bg = color2, highlightbackground = 'black', highlightthickness = 3)
    deposit_frame.place(rely = 0.1, relx = 0.1, relwidth = 0.8, relheight = 0.3)

    dep_label = Label(deposit_frame, fg = 'black', bg = color2, font = basic_text, text = 'Enter deposit amount:')
    dep_label.place(rely = 0, relx = 0, relwidth = 1, relheight = 0.5)
    dep_entry = Entry(deposit_frame, bg = color2, font = basic_text)
    dep_entry.place(rely = 0.5, relx = 0, relwidth = 0.7, relheight = 0.5)
    deposit_money = Button(deposit_frame, fg = 'black', bg = 'dark gray', font = basic_text, text = 'GO', command = deposit_func)
    deposit_money.place(rely = 0.5, relx = 0.7, relwidth = 0.3, relheight = 0.5)

    dbal_label = Label(deposit, fg = 'black', bg = color2, font = basic_text, text = 'Current Balance:\n' + '$' + str(bal), highlightbackground = 'black', highlightthickness = 3)
    dbal_label.place(rely = 0.5, relx = 0.1, relwidth = 0.8, relheight = 0.25)

    # show transactions button to load recent transactions
    trans_button = Button(show_trans, bg = 'dark gray', fg = 'black', text = "Show transactions", command = transactions)
    trans_button.place(rely = 0.1, relx = 0.1, relwidth = 0.8, relheight = 0.8)

def withdrawal():
    global bal, wbal_label
    with_amnt = with_entry.get()
    with_entry.delete(0, END)
    bal = bal - float(with_amnt)
    json_file_info = give_account_data()
    json_file_info[username_nt]["balance"] = bal

    text_entry = "Withdrawal".ljust(15) + str(with_amnt).ljust(10) + str(bal).ljust(10)
    json_file_info[username_nt]["transactions"].append(text_entry)

    write_account_data(json_file_info)

    # this is to update the label that shows the balance after withdrawal
    update_balances()

def deposit_func():
    global bal, dbal_label, text_entry
    dep_amnt = dep_entry.get()
    dep_entry.delete(0, END)
    bal = bal + float(dep_amnt)
    json_file_info = give_account_data()
    json_file_info[username_nt]["balance"] = bal

    date = datetime.now()
    current_date = str(date).split()
    print(current_date[0])

    text_entry = str(current_date[0]).ljust(15) + "Deposit".ljust(10) + str(dep_amnt).ljust(10) + str(bal).ljust(10)
    json_file_info[username_nt]["transactions"].append(text_entry)

    write_account_data(json_file_info)

    # this is to update the label that shows the balance after withdrawal
    update_balances()

def transactions():
    global text_entry, trans_button
    trans_button.destroy()
    acc_data = give_account_data()
    transaction = acc_data[username_nt]["transactions"]
    if len(transaction) > 5:
        transaction = transaction[-5:]

    trans = Label(show_trans, bg = color2, fg = 'black', font = basic_text, text = "Date".ljust(15) + "Type of Trans.".ljust(15) + 'Amount'.ljust(10) + "Curr. Bal.".ljust(15))    
    trans.place(rely = 0, relx = 0, relwidth = 1, relheight = 0.15)

    rely = 0.15
    for i in range(len(transaction)):
        trans = Label(show_trans, bg = color2, fg = 'black', font = basic_text, text = transaction[i])
        trans.place(rely = rely, relx = 0, relwidth = 1, relheight = 0.17)
        rely += 0.17

def changePassword():
    global otp
    database_password = give_account_data()[username_nt]["password"]
    if database_password == entries[0].get():
        if True:
        # if password_validate(entries[1].get(), username_nt):
            if entries[1].get() == entries[2].get():
                if entries[3].get() == otp:
                    data = give_account_data()
                    data[username_nt]["password"] = entries[1].get()
                    write_account_data(data)
                    messagebox.showinfo("showinfo", "Password Succefully Changed!")
                    profile_screen.destroy()
                else:
                    messagebox.showerror("showerror", "Incorrect OTP!")
            else:
                messagebox.showerror("showerror", "New password and confirmation password are different!")
        else:
            messagebox.showerror("showerror", " Password does not fit the requirments of the password \n(One capital, lowercase, number, special character [#, @, $, _],\n and it must be above 7 characters.")
    else:
        messagebox.showerror("showerror", "Incorrect current password!")



def changePasswordUI():
    global entries, reciever, otp, data, profile_screen
    profile_screen = Toplevel(root, height = 1000, width = 1000, bg = color2)

    data = give_account_data()
    reciever = data[username_nt]["email"]
    otp = send_otp(reciever)

    # title
    title_cp = Label(profile_screen, bg = color2, fg = 'black', font = title_text, text = 'Change Password')
    title_cp.place(relx = 0.05, rely = 0.05, relwidth = 0.8, relheight = 0.2)
    
    # beginning profile screen
    cp_frame = Frame(profile_screen, bg = color2, bd = 5)
    cp_frame.place(rely = 0.3, relx = 0.1, relheight = 0.4, relwidth = 0.8)

    oldpassword_cp = Entry(cp_frame, font = ('Times New Roman', 22), bd = 4, bg = color2)
    oldpassword_cp.place(relwidth = 0.7, relheight = 0.15, relx = 0.3)
    Label(cp_frame, bg = color2, text = 'Old Password: ', font = basic_text, fg = 'black', anchor = 'w').place(relx = 0, rely = 0, relheight = 0.15, relwidth = 0.3)

    new_password_cp = Entry(cp_frame, font = ('Times New Roman', 22), bd = 4, bg = color2)
    new_password_cp.place(relwidth = 0.7, relheight = 0.15, relx = 0.3, rely = 0.2)
    Label(cp_frame, bg = color2, text = 'New Password: ', font = basic_text, fg = 'black', anchor = 'w').place(relx = 0, rely = 0.2, relheight = 0.15, relwidth = 0.3)

    conf_password_cp = Entry(cp_frame, font = ('Times New Roman', 22), bd = 4, bg = color2)
    conf_password_cp.place(relwidth = 0.7, relheight = 0.15, relx = 0.3, rely = 0.4)
    Label(cp_frame, bg = color2, text = 'Confirm Password: ', font = basic_text, fg = 'black', anchor = 'w').place(relx = 0, rely = 0.4, relheight = 0.15, relwidth = 0.3)

    otp_cp = Entry(cp_frame, font = ('Times New Roman', 22), bd = 4, bg = color2)
    otp_cp.place(relwidth = 0.7, relheight = 0.15, relx = 0.3, rely = 0.6)
    Label(cp_frame, bg = color2, text = 'Enter OTP: ', font = basic_text, fg = 'black', anchor = 'w').place(relx = 0, rely = 0.6, relheight = 0.15, relwidth = 0.3)

    entries = [oldpassword_cp, new_password_cp, conf_password_cp, otp_cp]

    create_account = Button(cp_frame, bg = color2, text = 'Change Password', font = basic_text, command = changePassword)
    create_account.place(relx = 0.25, rely = 0.8, relheight = 0.15, relwidth = 0.5)

login_screen()
root.mainloop()