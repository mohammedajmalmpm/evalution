"""
componey:
parent class : employee
management, development, 
annual hike
devops hike
management team -> controlled 
"""

class Employee:
    def __init__(self,name,email_id,salary):
        """[Create Employee]

        Args:
            name ([str]): [name of employee]
            email_id ([str]): [email of employee]
            salary ([int]): [current salary of employee]
        """
        self.name = name
        self.email_id = email_id
        self.salary = salary

    def details(self):
        """Details of employee
        """
        print(f'Employee Details')
        print(f'Name: {self.name} \n email_id: {self.email_id} \n salary: {self.salary}')

    def hike_amount(self,amount):
        """salary hike

        Args:
            amount ([int]): [hike amount of employee]
        """
        self.amount = amount
        print(f'Annual hike amount {self.salary + self.amount}')
        return self.salary + self.amount

class Development(Employee):
    description = "Development"
    def __init__(self,name,email_id,salary):
        """Development Team

        Args:
            name ([str]): [name of employee]
            email_id ([str]): [email id of employee]
            salary ([int]): [salary of employee]
        """
        super().__init__(name,email_id,salary)

    def employee_details(self):
        """details
        """
        print(f'Name : {self.name}\n Email_id : {self.email_id}\n Annual_Hike : {self.amount}\n Current_salary : {self.salary}')

class Devops(Employee):
    description =  "Devops"
    def __init__(self,name,email_id,salary):
        """Devops Team

        Args:
            name ([str]): [name of employee]
            email_id ([str]): [email id of employee]
            salary ([int]): [salary of employee]
        """
        super().__init__(name,email_id,salary)

    def extra_hike(self,hike_amount):
        """extra hike amount details

        Args:
            hike_amount ([int]): [hike amount]
        """
        self.hike_amount = hike_amount
        salary = self.salary + self.amount + self.hike_amount

        print(f'{self.__class__.__name__} team extra hike_amount is {salary}')
    
    def devops_details(self):
        """Devops details
        """
        # print(f'{self.name}\n{self.email_id}\n{self.amount}\n\n{self.salary}')
        print(f'Name : {self.name}\n Email_id : {self.email_id}\n Extra_hike : {super().hike_amount(self.amount)}\n Annual_Hike : {self.amount}\n Current_salary : {self.salary}')

class Management(Devops,Development):
    description = "Management"
    def __init__(self,name,email_id,salary):
        """Management Team

        Args:
            name ([str]): [name of employee]
            email_id ([str]): [email id of employee]
            salary ([int]): [salary of employee]
        """
        super().__init__(name,email_id,salary)

    def dev_details(self):
        print("Devops details")
        super().devops_details()
        print("Development details")
        super().development_details()



emp1 = Devops("kittu","kittu@gmail.com",15000)
print(emp1.description)
emp1.details()
emp1.hike_amount(5000)
emp1.extra_hike(2000)
print(f'\n\n')
emp2 = Development("Abhijith","abhijith@gmail.com",15000)
print(emp2.description)
emp2.details()
emp2.hike_amount(2000)
print(f'\n\n')
emp3 = Management("ebin","ebin@gmail.com",15000)
print(emp3.description)
emp3.details()
emp3.hike_amount(2000)
print(f'\n\n')
emp1.devops_details()
emp2.employee_details()
emp3.employee_details()



    