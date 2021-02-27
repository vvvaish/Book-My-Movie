import mod1
class Main:
    def fun1(self):
        obj1.show()
    def fun2(self):
        obj1.buy_ticket()
    def fun3(self):
        obj1.statistics()
    def fun4(self):
        obj1.show_BookedTicketUser_info()



obj = Main()
print('Enter Number Of Rows: ')
x = int(input())
print('Enter Number Of Seats In Each Row: ')
y = int(input())
obj1 = mod1.operations(x,y)
inp = 'h'
print('-------------- Book My Show -----------------')
while inp != 0:
    print('1. Show The Seats')
    print('2. Buy A Ticket')
    print('3. Statistics')
    print('4. Show Booked Tickets User Info')
    print('0. Exit')
    print('---------------------------------')

    inp = int(input())
    if inp == 1:
        obj.fun1()
    elif inp == 2:
        obj.fun2()
    elif inp == 3:
        obj.fun3()
    elif inp == 4:
        obj.fun4()
    elif inp != 0:
        print('\n')
        print('Invalid Choice!!!')
        print('\n')


