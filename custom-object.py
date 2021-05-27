#custom-object.py
"""Creates an object representing a purchase made for a given amount."""

class Purchase(object):
    def __init__(self, amount):
        self.amount=amount
    
    def calculateTax(self, taxPercent):
        return self.amount*taxPercent/100.0

    def calculateTip(self, tipPercent):
        return self.amount*tipPercent/100.0
    
    def calculateTotal(self, taxPercent, tipPercent):
        return self.amount*(1+taxPercent/100.0+tipPercent/100.0)

#prompts the user for purchase, tax %, and tip %
x=float(input('What is the purchase amount? '))
y=float(input('What is the tax percentage? '))
z=float(input('What is the tip percentage? '))

#sets purchase amount as an object given inputted value
purchase=Purchase(x)

#sets tax and tip percentages as objects given inputted values
taxPercent=y
tipPercent=z

#calculates tax, tip, and total dollar amounts from the given purchase amount
tax=purchase.calculateTax(taxPercent)
tip=purchase.calculateTip(tipPercent)
my_total=purchase.calculateTotal(taxPercent, tipPercent)

#values printed as readable dollar amounts with 2 decimal places
print(f'Tax is: ${tax:.2f}')
print(f'Tip is: ${tip:.2f}')
print(f'Total amount is: ${my_total:.2f}')
