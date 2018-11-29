#2a)

def file_to_list(filename):
    try:
        with open(filename, 'r') as file:
            file_list = file.readlines()
    except:
        print('lmao')
        return

    return_list = []
    for i in file_list:
        temp = i.split('\t')
        temp[-1] = float(temp[-1])
        return_list.append(temp)

    return return_list

# print(file_to_list('price.txt'))

data = [['Rema', 'Milk', 14.5], ['Rema', 'Pepsi Max', 20.0], ['Extra', 'Milk', 14.2],
['Kiwi', 'Pepsi Max', 20.5], ['Extra', 'Pepsi Max', 19.5], ['Rema', 'Banana',
12.5], ['Kiwi', 'Milk', 13.0], ['Rema', 'Juice', 29.3], ['Extra', 'Juice', 23.0],
['Rema', 'Chocolate', 14.0], ['Extra', 'Chocolate', 13.3], ['Kiwi', 'Chocolate',
13.0], ['Kiwi', 'Banana', 10.5], ['Extra', 'Banana', 11.0], ['Kiwi', 'Juice',
27.5], ['Bunnpris', 'Milk', 13.0], ['Bunnpris', 'Pepsi Max', 21.5], ['Bunnpris',
'Banana', 15.9], ['Bunnpris', 'Juice', 26.0], ['Bunnpris', 'Chocolate', 12.5]]
#2b)
def list_stores(dataList):
    stores = []
    for i in dataList:
        if i[0] not in stores:
            stores.append(i[0])
    return stores
dsa

data2 = list_stores(data)
print(data2)
#2c)
def sum_prices_stores(dataList, storeList):
    store_sum = [0 for i in range(len(storeList))]

    for i in range(len(dataList)):
        for j in storeList:
            if dataList[i][0] == j:
                store_sum[storeList.index(j)] += dataList[i][-1]
    return store_sum
print(sum_prices_stores(data, data2))


#2d)
def rank_stores(storeList, sumStores):
    dict = {}

    for i in range(len(sumStores)):
        dict[sumStores[i]] = storeList[i]

    sumStores.sort()
    ranked = []

    for i in sumStores:
        ranked.append(dict.get(i))

    return ranked
print(rank_stores(data2, sum_prices_stores(data, data2)))

#2e)
def store_analysis(filename):
    data = file_to_list(filename)
    data2 = list_stores(data)
    data3 = sum_prices_stores(data, data2)
    print("The total price for shopping per store is:")
    for i in range(len(data2)):
        print(f'{data2[i]} : {data3[i]} kr')

    data4 = rank_stores(data2, data3)

    print("The ranking of stores according to prices is:")
    for i in range(1, len(data2)+1):
        print(f'{i} {data4[i-1]}')
#store_analysis(data)
