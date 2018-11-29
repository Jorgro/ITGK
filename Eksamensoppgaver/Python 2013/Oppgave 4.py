#4a)
def payment(price, count):
    if count > 3: 
        return price*count*0.9
    else:
        return price*count

#4b)
def get_price(concert):

    with open('prices.txt', 'r') as file:
        for line in file: 
            line = line.split(';')
            if line[0] == concert and len(line) == 2:
                line[1] = float(line[1].rstrip('\n'))
                return line[1]
    return -1

print(get_price('The aller beste'))

#4c) 
def ticket(name, concert, tickets):
    price_concert = get_price(concert)
    price = payment(price_concert, tickets)

    print('*'*47)
    print('UKA 2015')
    print('*'*47)

    print('Navn:'.rjust(17) + name.rjust(30))
    print('Konsert:'.rjust(17) + concert.rjust(30))
    print('Antall billetter:'.rjust(17) + str(tickets).rjust(30))
    print('Total pris:'.rjust(17) + str(price).rjust(30))

ticket('Nils Nilsen', 'The Rectorats', 8)

#4d)
def write_to_file(buyer_name, concert, tickets, file_name):
    price = get_price(concert)
    total_price = int(payment(price, tickets))
    to_be_added = concert + ';' + str(tickets) + ';' + str(total_price) + ';' + buyer_name + '\n'
    with open(file_name, 'a') as file:
        file.write(to_be_added)


#write_to_file('Me', 'The Rectorats', 8, 'concerts.txt')

#4e)
def main():
    menu = 'Press 1 for tickets sold for a given concert\nPress 2 for a concerts revenue\nPress 3 for total revenue\nPress 4 to quit the program'
    
    dict_concert = {}
    with open('concerts.txt', 'r') as file:
        for line in file:
            line = line.split(';')
            try: 
                updated = dict_concert.get(line[0])
                updated[0] += line[1]
                updated[1] += line[2]
            except:
                dict_concert[line[0]] = line[1:3]
    print(dict_concert)
    print(menu)
    switch = True
    while switch: 
        user = input('What do you want to do? ')

        if user == '1':
            concert = input('What concert? ')
            sold = dict_concert.get(concert)
            print(f'Tickets sold for {concert}: {sold[0]}')

        elif user == '2': 
            concert = input('What concert? ')
            earnings = dict_concert.get(concert)[1]
            
            print(f'Earnings from {concert}: {earnings}')
        
        elif user == '3':
            total_earnings = 0
            for key, value in dict_concert.items():
                try:
                    total_earnings += int(value[1])
                except:
                    continue
            print(f'Total earnings: {total_earnings}')
        
        else: 
            break
            switch = False
main()
