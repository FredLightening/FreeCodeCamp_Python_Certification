class Category:
    def __init__(self,name):
        self.name=name
        self.ledger=[]
        self.withdrawal=[]

    def deposit(self,amount,description=''):
        self.ledger.append({'amount':amount, 'description':description})

    def withdraw(self,amount,description=''):
        negative_amount=amount*(-1)
        self.ledger.append({'amount':negative_amount,'description':description})
        self.withdrawal.append({'amount':negative_amount,'description':description})
        # if True:
        #     return True
        # else:
        #     return False
        if self.check_funds(amount):
            return True
        else:
            return False

    def get_withdrawal(self):
        sum=0
        for input in self.withdrawal:
            sum+=input['amount']
        return sum*(-1)
    
    def get_balance(self):
        sum=0
        for input in self.ledger:
            sum+=input['amount']
        return sum

    def transfer(self,amount,category):
        self.withdraw(amount,f'Transfer to {category.name}')
        category.deposit(amount,f'Transfer from {self.name}')
        # if True:
        #     return True
        # else:
        #     return False
        if self.check_funds(amount):
            return True
        else:
            return False

    def check_funds(self,amount):
        if amount<=self.get_balance():
            return True
        else:
            return False

    def __str__(self):
        top=(self.name.center(30,'*'))
        lines=[top]
        for object in self.ledger:
            lines.append(f"{object['description'][:23]:<23}{object['amount']:>7.2f}")
        lines.append(f'Total: {self.get_balance()}')
        return "\n".join(lines)
def create_spend_chart(categories):
    output=[]
    output.append('Percentage spent by category')
    percent=[]
    percent_list=[]
    summ=0
    
    names=[]
    # total=0
    # for category in categories:
    #     total+=category.get_balance()
    for category in categories:
        percent_break=category.get_withdrawal()//10
        percentage=percent_break*10
        percent.append(percentage)

    for num in percent:
        summ+=num
    for num in percent:
        percent_list.append((num/summ)*100)
    for category in categories:
        names.append(category.name)

    max_length= max(len(name) for name in names)
    for i in range(100,-1,-10):
        yaxis=f'{i:>3}| '
        for num in percent_list:
            if num>=i:
                char='o  '
            else:
                char='   '
            yaxis+=char
        output.append(yaxis) 
    output.append(f"    {'---'*len(categories)}-")
    for num in range(max_length):
        line='     '
        for name in names:
            if num<len(name):
                line+=f'{name[num]}  '
            else:
                line+='   '
        output.append(line)    
    return '\n'.join(output)
# ha=76//10
# print(ha*10)
# ack=Category('Test')
# ack.deposit(2000)
# ack
# for i in ack.ledger:
#     print(i)
food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')

clothing = Category('Clothing')
food.transfer(50, clothing)
clothing.deposit(2000)

# Cloth = Category('clothing')
clothing.deposit(1000, 'initial deposit')
clothing.withdraw(200, 't-shirt')
clothing.withdraw(300, 'restaurant and more food for dessert')

auto=Category('Auto')
auto.deposit(3000)
auto.withdraw(555.9)
auto.withdraw(600)

cat_list=[clothing,auto,food]
print(create_spend_chart(cat_list))
