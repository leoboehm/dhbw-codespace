import random
import datetime

def listExperiments():
    oldList = []

    for i in range(20):
        oldList.append(random.randint(0, 15))

    print("Complete list: ", oldList)
    print("List length: ", len(oldList))

    newList = list(set(oldList))

    print("List without duplicates: ", newList)
    print("List length: ", len(newList))
    print("List maximum: ", max(newList))
    print("List minimum: ", min(newList))

listExperiments()

def dictExperiments():
    transactions = []
    types = ["Purchase", "Sale"]
    dates = []
    
    today = datetime.date.today()
    for i in range(4):
        dates.append(str(datetime.date(today.year, today.month, today.day-i)))
        i-=1
    
    for i in range(10):
        transactions.append({"type": random.choice(types), "amount": random.randint(1, 100), "date": random.choice(dates)})
    
    print("All transactions:", transactions)

    yesterdaysTransactions = getValuesByKeyValuePair(transactions, "date", str(datetime.date(today.year, today.month, today.day-1)))
    print("Yesterday's transactions:", yesterdaysTransactions)
    print("Amount:", len(yesterdaysTransactions))

    print("Total expenses:", sumTransactionsByType(transactions, "Purchase"))
    print("Total income:", sumTransactionsByType(transactions, "Sale"))

    total = sumTransactionsByType(transactions)
    print("Total money:", total)
    if total > 0:
        print("You made money!")
    else:
        print("You lost money!")

def getValuesByKeyValuePair(list, key, value):
    filteredList = []
    for item in list:
        if item[key] == value:
            filteredList.append(item)
    return filteredList

def sumTransactionsByType(list, type=None):
    sum = 0
    for item in list:
        if type == None or item["type"] == type:
            sum += item["amount"]
    return sum

dictExperiments()