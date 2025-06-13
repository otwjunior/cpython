import pyinputplus as pyip
breadprice =10
cheeseprice =2
vegprice= 3
total= 0
print('Welcome to the new kfc sandwich corner')
breadtype= pyip.inputMenu(['white','wheat', 'sourdough'], prompt= 'pick bread type: \n', numbered = True,)
if breadtype:
    total += 10
cheeseoption = pyip.inputYesNo('ddo you want cheese?')
if  cheeseoption == 'yes':
    cheesetype= pyip.inputMenu(['cheddar', 'swiss','mozzarella'], prompt='pick your taste', numbered= True)
    total+=2
vegtype = pyip.inputYesNo('do you want mayo,mustard,lettuce or tomato: ')
if vegtype == 'yes':
    total+= 3
quantity = pyip.inputInt('how many such sandwitch: ')
Bill =total * quantity
print(Bill)