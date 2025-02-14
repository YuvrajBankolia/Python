class employee:
    companyName = "Apple"            # class se associated h
    def __init__(self , name):
        self.name = name
        self.raise_amount  = 0.23023
    def showDetails(self):
            print(f"the name of the employee is {self.name} and the raise amount in {self.companyName} is {self.raise_amount}")

emp1 =employee("UV")
emp1 .raise_amount =0.4 
emp1.companyName = "apple india"      # ye instance se associated h 
emp1.showDetails()

emp2 = employee("Nestle")
emp2 =employee("Rohan")
emp2.showDetails()
# employee.showDetails(emp1)