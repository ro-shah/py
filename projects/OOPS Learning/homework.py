import json



class Employee:   
    employee_list = []
    def __init__(self, name_, age_, dOfJ, sal, jobOcc, country_, email_, phoneNo):
        self.dateOfJoining = dOfJ
        self.salary = sal
        self.jobOccupation = jobOcc
        self.name = name_
        self.age = age_
        self.country = country_
        self.email = email_
        self.phoneNumber = phoneNo

    def show_details(self, ind, l = employee_list):
        print("Name: " + l[ind].name + "\n" + "Age: " + str(l[ind].age) + "\n" + "Date of Joining: " + l[ind].dateOfJoining + "\n" + "Salary: " + str(l[ind].salary) + "\n" + "Job Occupation: " + l[ind].jobOccupation + "\n" + "Country: " + l[ind].country + "\n" + "Email: " + l[ind].email + "\n" + "Phone Number: " + l[ind].phoneNumber)


def get_info(): 
    global employee
    inputname = input("Enter your name: ")
    inputage = int(input("Enter your age: "))
    inputdOfJ = input("Enter your date of joining: ")
    inputsal = float(input("Enter your salary: "))
    inputjobOcc = input("Enter your job occupation: ")
    inputcountry = input("Enter your country: ")
    inputemail = input("Enter your email: ")
    inputphoneno = input("Enter your phone number: ")

    employee = Employee(inputname, inputage, inputdOfJ, inputsal, inputjobOcc, inputcountry, inputemail, inputphoneno)
    Employee.employee_list.append(employee)

# def data_into_database():
#     fhandle = open("C:\Python\VScode Programs\OOPS Learning\employees.json", "w")
#     json.dump(fhandle)

while True:
    choice = int(input('''1. Add Employee
2. Remove Employee
3. See Employee Details
4. Quit
Type Here: '''))
    if choice == 1:
        get_info()
    elif choice == 2:
        pass
    elif choice == 3:
        employeeID = int(input("Enter Employee ID: "))
        print(employee.show_details(employeeID))
    elif choice == 4:
        break
    else:
        print("Wrong Choice.")

    # print(employee.show_details(emplo))

    