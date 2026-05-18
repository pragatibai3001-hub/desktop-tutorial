#ATM menu program

balance = 5000

while True:
    print ('1.balance')
    print ('2.deposit')
    print ('3.withdraw')
    print ('4.exit')

    choice = int (input('Enter you choice: '))

    if choice == 1:
        print ('Balance: ', balance)
    elif choice == 2:
        amount = int (input('Enter the amount to deposit: '))
        print ('updated balance: ', balance+amount)
    elif choice == 3:
        amount = int(input('Enter the amount to withdraw'))
        if amount <= balance:
            print ('updated balance: ', balance-amount)
        else:
            print('Insufficient balance')
    elif choice == 4:
        print ('Thank you')
        break
    else:
        print ('Invalid choice')
    
        

    
