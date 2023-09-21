class Category:
    
    def __init__(self, name):
        self.name = name
        self.ledger = []
        self.balance = 0.0
        
    def __repr__(self):
        header = self.name.center(30, '*') + '\n'
        body = str()
        for item in self.ledger:
            left = item['description'][:23].ljust(23)
            amount = "%.2f" % item['amount']
            right = amount.rjust(7)
            body += left + right + '\n'
        total = 'Total: ' + '%.2f' % self.balance
        ledger = header + body + total
        return ledger
    
    def deposit(self, amount, description=''):
        self.ledger.append({'amount': amount, 'description': description})
        self.balance += amount
        
    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            self.balance -= amount
            return True
        else:
            return False
    
    def get_balance(self):
        return self.balance
    
    def transfer(self, amount, category):
        if self.withdraw(amount, 'Transfer to {}'.format(category.name)):
            category.deposit(amount, 'Transfer from {}'.format(self.name))
            return True
        else:
            return False
        
    def check_funds(self, amount):
        if amount > self.balance:
            return False
        else:
            return True

def create_spend_chart(categories):
    n = len(categories)
    if n > 4:
        return False
    
    # Get total expended and how much was expended in each category
    total_expended = 0.0
    expenses_per_cat = [None] * n
    for i in range(n):
        expenses = 0.0
        for amount in categories[i].ledger:
            if amount['amount'] < 0:
                expenses += (amount['amount'] * -1)
        expenses_per_cat[i] = expenses
        total_expended += expenses
    
    # Percentage rounded down for category
    percentages = [None] * n
    for i in range(n):
        percent = (expenses_per_cat[i] / total_expended) * 100
        percent = int(percent / 10) * 10
        percentages[i] = percent

    
    # Answer string with header
    ans = 'Percentage spent by category\n'
    
    # Draw graphic
    i = 100
    while i >= 0:
        if i == 100:
            ans += str(i)
        elif i > 0:
            ans += ' ' + str(i)
        else:
            ans += '  ' + str(i)
        ans += '| '
        for j in range(n):
            if percentages[j] >= i:
                ans += 'o  '
            else:
                ans += '   '
        ans += '\n'
        i -= 10
    
    ans += ' ' * 4 + '-' * 3 * n + '-\n'
    
    # Draw categories
    ## Find max length of a word to iterate
    names = [i.name.capitalize() for i in categories]
    lengths = [len(word) for word in names]
    
    for i in range(max(lengths)):
        ans += '     '
        for j in range(len(names)):
            try:
                ans += names[j][i] + '  '
            except:
                ans += '   '
        if i != (max(lengths) - 1):
            ans += '\n'
    return ans