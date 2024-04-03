#calculator
def addition(num1, num2):
    return num1 + num2
def subtract(num1, num2):
    return num1 - num2
def multiply(num1, num2):
    return num1 * num2
def division(num1, num2):
    return num1 / num2
print('Welcome to my calculator')


while True:
    try:

       userinput = input('Enter the expression (or q to quit): ')

       if userinput.find('+') != -1:
           split = userinput.split('+')
           if split[0].find('.') != -1 or split[1].find('.') != -1:
               num1 = float(split[0])
               num2 = float(split[1])
               print(num1, '+', num2, '=', "{:,.2f}".format(addition(num1, num2)))
           else:
               num1 = int(split[0])
               num2 = int(split[1])
               print(num1, '+', num2, '=', addition(num1, num2))

       elif userinput.find('-') != -1:
           split = userinput.split('-')
           if split[0].find('.') != -1 or split[1].find('.') != -1:
               num1 = float(split[0])
               num2 = float(split[1])
               print(num1, '+', num2, '=', "{:,.2f}".format(subtract(num1, num2)))
           else:
                num1 = int(split[0])
                num2 = int(split[1])
                print(num1, '-', num2, '=', subtract(num1, num2))

       elif userinput.find('*') !=  -1:
           split = userinput.split('*')
           if split[0].find('.') != -1 or split[1].find('.') != -1:
               num1 = float(split[0])
               num2 = float(split[1])
               print(num1, '+', num2, '=', "{:,.2f}".format(multiply(num1, num2)))
           else:
               num1 = int(split[0])
               num2 = int(split[1])
               print(num1, '*', num2, '=', multiply(num1, num2))
       elif userinput.find('/') != -1:
           split = userinput.split('/')
           if split[0].find('.') != -1 or split[1].find('.') != -1:
               result1 = division(float(split[0]), float(split[1]))
               if split[1] == '0':
                   print('Cannot divide by zero')
               else:
                   print(split[0] , '/', split[1] , ' = ' , "{:,.2f}".format(result1))
           elif split[0].find('.') == -1 or split[1].find('.') == -1:
               result2 = division(float(split[0]), float(split[1]))
               if split[1] == 0:
                   print('Cannot divide by zero')
               else:
                   print(split[0], '/', split[1], ' = ', "{:,.2f}".format(result2))
       if userinput == 'q' or userinput == 'Q':
           print('Goodbye!')
           break
    except ValueError:
        print('Error in expression')



