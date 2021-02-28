class operations:
    def __init__(self,row,col):
        self.row = row
        self.col = col
        self.cinema = []
        for i in range(self.row + 1):
            x = []
            for j in range(self.col + 1):
                if i == 0:
                    if j == 0 and j == 0:
                        x.append(' ')
                    else:
                        x.append(j)
                elif j == 0:
                    x.append(i)
                else:
                    x.append('S')
            self.cinema.append(x)

        if self.row*self.col > 60:
            self.price_list = []
            y1 = self.row // 2
            for i in range(self.row):
                x1 = []
                for j in range(self.col):
                    if i + 1 <= y1:
                        x1.append(10)
                    else:
                        x1.append(8)
                self.price_list.append(x1)


        self.dict = {}
        self.ticket = 0
        self.curr_income = 0


    def show(self):
        for i in range(self.row + 1):
            for j in range(self.col + 1):
                print(self.cinema[i][j],end = ' ')
            print('')

        print('\n')

    def buy_ticket(self):
        x = int(input('Row Number    :'))
        y = int(input('column Number :'))
        if self.cinema[x][y] == 'B':
            print('\n')
            print('Already Booked!!!')
            print('\n')
            return
        if (self.row*self.col<= 60):
            print('PRICE: ',10)
            price = 10
        else:
            print('PRICE: ',self.price_list[x-1][y-1])
            price = self.price_list[x-1][y-1]
        i1 = input('Do You Want To Buy It? (yes/no) ?')

        if i1 == 'yes':
            l = {}
            print('\n')
            print('Kindly Fill Details\n')
            a = input('Enter Name: ')
            b = input('Enter Gender: ')
            c = input('Enter Age: ')
            print('Ticket Price: ',str(price))
            e = input('Enter Contact no: ')
            l['name'+str(len(self.dict)+1)] = a
            l['gen' + str(len(self.dict) + 1)] = b
            l['age' + str(len(self.dict) + 1)] = c
            l['price' + str(len(self.dict) + 1)] = price
            l['no' + str(len(self.dict) + 1)] = e
            self.dict[str(x)+str(y)] = l
            self.cinema[x][y] = 'B'
            self.ticket += 1
            if self.row * self.col >60:
                self.curr_income += self.price_list[x - 1][y - 1]
            print('\n')
            print('Ticket Booked Successfully')
            print('\n')
        else:
            print('\n')
            print("ohh!!!! You Missed Such A Nice Movie")
            print('\n')

    def statistics(self):
        if self.row * self.col <= 60:
            ans = ((self.ticket*10) / (self.row * self.col * 10))*100
            print('Number Of Purchased Tickets: ',self.ticket)
            print('Percentage: ',str(round(ans,2))+'%')
            print('Current Income: ','$'+str(self.ticket*10))
            print('Total Income: ','$'+str(self.row*self.col*10))
            print('\n')
        else:
            x = 0
            for i in self.price_list:
                x = x + sum(i)

            ans = (self.curr_income/x)*100
            print('Number Of Purchased Tickets: ',self.ticket)
            print('Percentage: ', str(round(ans, 2)) + '%')
            print('Current Income: ', '$' + str(self.curr_income))
            print('Total Income: ', '$' + str(x))
            print('\n')



    def show_BookedTicketUser_info(self):
        a = int(input('Enter Row Number: '))
        b = int(input('Enter Column Number: '))
        print('\n')
        l = ['Name:','Gender:','Age:','Ticket Price:','Phone Number:']
        if str(a)+str(b) not in self.dict:
            print("This Sit Not Booked Yet!!!")
        for i in self.dict:
            count = 0
            if i == str(a)+str(b):
                for j in self.dict[str(a)+str(b)]:
                    print(l[count], self.dict[str(a)+str(b)][j])
                    count += 1
        print('\n')



