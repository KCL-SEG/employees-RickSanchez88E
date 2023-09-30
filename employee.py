class Employee:
    def __init__(self, name):
        self.name = name

    def get_pay(self):
        pass

    def __str__(self):
        return self.name


class MonthlySalaryEmployee(Employee):
    def __init__(self, name, monthly_salary):
        super().__init__(name)
        self.monthly_salary = monthly_salary

    def get_pay(self):
        return self.monthly_salary


class ContractEmployee(Employee):
    def __init__(self, name, hours_worked, hourly_rate):
        super().__init__(name)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate

    def get_pay(self):
        return self.hours_worked * self.hourly_rate


class CommissionEmployee(Employee):
    def __init__(self, name, monthly_salary, commission_rate, num_contracts, commission_per_contract):
        super().__init__(name)
        self.monthly_salary = monthly_salary
        self.commission_rate = commission_rate
        self.num_contracts = num_contracts
        self.commission_per_contract = commission_per_contract

    def get_pay(self):
        base_pay = self.monthly_salary
        commission = self.num_contracts * self.commission_per_contract
        return base_pay + commission


class BonusCommissionEmployee(Employee):
    def __init__(self, name, monthly_salary, bonus_commission):
        super().__init__(name)
        self.monthly_salary = monthly_salary
        self.bonus_commission = bonus_commission

    def get_pay(self):
        return self.monthly_salary + self.bonus_commission


# Billie works on a monthly salary of 4000. Their total pay is 4000.
billie = MonthlySalaryEmployee('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour. Their total pay is 2500.
charlie = ContractEmployee('Charlie', 100, 25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract. Their total pay is 3800.
renee = CommissionEmployee('Renee', 3000, 0, 4, 200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract. Their total pay is 4410.
jan = CommissionEmployee('Jan', 0, 0.25, 3, 220)
jan.hours_worked = 150
jan.hourly_rate = 25

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500. Their total pay is 3500.
robbie = BonusCommissionEmployee('Robbie', 2000, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600. Their total pay is 4200.
ariel = ContractEmployee('Ariel', 120, 30)
ariel.bonus_commission = 600

# Calculate and print the pay for each employee
employees = [billie, charlie, renee, jan, robbie, ariel]
for employee in employees:
    print(f"{employee}: {employee.get_pay()}")
