class Employee:   
    employee_dict = {}
    def __init__(self, name_, age_, dOfJ, sal, jobOcc, country_, email_, phoneNo):
        self.dateOfJoining = dOfJ
        self.salary = sal
        self.jobOccupation = jobOcc
        self.name = name_
        self.age = age_
        self.country = country_
        self.email = email_
        self.phoneNumber = phoneNo
        Employee.employee_dict[self.name] = self

    def show_details(self, employeeID, l = employee_dict):
        try:
            print("\nName: " + l[employeeID].name + "\n" + "Age: " + str(l[employeeID].age) + "\n" + "Date of Joining: " + l[employeeID].dateOfJoining + "\n" + "Salary: " + str(l[employeeID].salary) + "\n" + "Job Occupation: " + l[employeeID].jobOccupation + "\n" + "Country: " + l[employeeID].country + "\n" + "Email: " + l[employeeID].email + "\n" + "Phone Number: " + l[employeeID].phoneNumber + "\n")
        except:
            print("There is no person named " + l[employeeID].name + " in the company. \n Check for any spelling errors and make sure to add full name.")


def get_info(): 
    global employee
    inputname = input("Enter your name (first middle last): ")
    inputage = int(input("Enter your age: "))
    inputdOfJ = input("Enter your date of joining: ")
    inputsal = float(input("Enter your salary: "))
    inputjobOcc = input("Enter your job occupation: ")
    inputcountry = input("Enter your country: ")
    inputemail = input("Enter your email: ")
    inputphoneno = input("Enter your phone number: ")

    employee = Employee(inputname, inputage, inputdOfJ, inputsal, inputjobOcc, inputcountry, inputemail, inputphoneno)
    # Employee.employee_dict[inputname] = employee

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
        employeeID = input("Enter Employee Name: ")
        print(employee.show_details(employeeID))
    elif choice == 4:
        break
    else:
        print("Wrong Choice.")

    # print(employee.show_details(emplo))