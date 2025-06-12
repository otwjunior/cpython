# This program says hello and ask for my name.

print('Hello, world!')
print('What is your name?') #ask for their name
myname = input()
print('it is good too meet you, ' + myname)
print('The length of your name is:')
print(len(myname))
print('What is your age?') # ask for their age
myage = input()
print('You will be ' + str(int(myage) +1) + ' in an year')