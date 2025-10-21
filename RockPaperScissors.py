print('press 1 for rock')
print('press 2 dor paper')
print('press 3 for scissors')
choice = input('please enter your choice:  ')
a = int(choice)
if a == 1:
    print('i select paper')
elif a == 2:
    print('i select scissors')
elif a == 3:
    print('i select rock')
else:
    print('invalid input')