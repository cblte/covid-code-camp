def prices_list(name, price):
    liste = []
    for i in range(1,11):
        s = str(i) + " x " + name + ": " + str(price * i)
        liste.append(s)
    return liste #return object to caller

prices = prices_list("Wunderkerkeks", 0.79)
print(prices)

