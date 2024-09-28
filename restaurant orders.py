# a=['a \n b\n  c']
# print('a \n b\n  c')
# if we want want to show something line by line we need to code it this way
# in this project i am trying to creat a manu system and people can order from here
# in this project i used basically dictionary and conditions and format strings
manu={'pizza':300,
      'pasta':180,
      'choclete shake':100,
                 'water':20

}
#we need to greet customers
print('welcome to my restaurant!!')
print("Pizza 10inch:300tk\n Pasta(regular):180tk \n choclete shake :100tk\n water 500ml:20tk")

ordertotal=0
# eikhane items er daam add hobe

item1=input('select your dish  '  ).lower()
if item1 in manu:
    ordertotal+=manu[item1]
    print(f'your {item1} has been added !')

else:
    print(f'{item1} is not available!!\n please order from given manu' )
print('do you want to order more?')
ans=input('please type yes or no ')
if ans =='yes':
    print('here we go for second item')
else:
    print(f'pay only {ordertotal}')
item2=input('choclete shake or water ?' ).lower()
if item2 in manu:
    ordertotal+=manu[item2]
    print(f'{item2} has been added to your order ')

else:
    print(f'{item2} is not available!!\n payable amount{ordertotal}')

print(f'total payable amount {ordertotal}')

print('thank you for ordering')




