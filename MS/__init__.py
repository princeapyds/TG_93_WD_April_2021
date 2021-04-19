x = int(input('enter the number'))
if x>0:
    print('positive number')

    if x%2==0:
        print('even number')
    else:
        print('odd')

elif x <0:
    print('negative')

else:
    print('zero')