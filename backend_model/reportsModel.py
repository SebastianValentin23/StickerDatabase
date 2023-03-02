# Orders simulation for the reports that specify date
dictProd1 = {1: {'name': 'Bad Bunny Album', 'brand': 'White', 'date': '2023-01-01', 'price': '5.00', 'quantity': 2, 'total_price': 10.00}}
dictProd2 = {2: {'name': 'Naruto Shippuden', 'brand': 'Orange', 'date': '2023-01-04', 'price': '15.00', 'quantity': 1, 'total_price': 15.00}}
dictProd3 = {3: {'name': 'Chopper One Piece', 'brand': 'Red', 'date': '2023-12-5', 'price': '10.00', 'quantity': 3, 'total_price': 30.00}}
dictProd4 = {4: {'name': 'Bugatti Logo', 'brand': 'Red', 'date': '2023-04-12', 'price': '5.00', 'quantity': 1, 'total_price': 5.00}}
dictProd5 = {5: {'name': 'Beach Sunset', 'brand': 'Red', 'date': '2023-01-01', 'price': '15.00', 'quantity': 2, 'total_price': 30.00}}


# Orders simulation for the inventory/stock report
product1 = {1: {'name': "Bad Bunny Album", 'brand': 'White', 'quantity': 15}}
product2 = {2: {'name': "Naruto Shippuden", 'brand': 'Orange', 'quantity': 4}}
product3 = {3: {'name': "Chopper One Piece", 'brand': 'Red', 'quantity': 13}}
product4 = {4: {'name': "Bugatti Logo", 'brand': 'Red', 'quantity': 25}}
product5 = {5: {'name': "Beach Sunset", 'brand': 'Red', 'quantity': 2}}
product6 = {6: {'name': "Bad Bunny Album", 'brand': 'White', 'quantity': 65}}


def MagerDicts(dict1, dict2):
    if isinstance(dict1, list) and isinstance(dict2, list):
        return dict1 + dict2
    elif isinstance(dict1, dict) and isinstance(dict2, dict):
        return dict(list(dict1.items()) + list(dict2.items()))
    return False


ordersList = dictProd1
ordersList = MagerDicts(ordersList, dictProd2)
ordersList = MagerDicts(ordersList, dictProd3)
ordersList = MagerDicts(ordersList, dictProd4)
ordersList = MagerDicts(ordersList, dictProd5)


productsList = product1
productsList = MagerDicts(productsList, product2)
productsList = MagerDicts(productsList, product3)
productsList = MagerDicts(productsList, product4)
productsList = MagerDicts(productsList, product5)
productsList = MagerDicts(productsList, product6)


def getDatedReportModel():
    return ordersList


def getStockReportModel():
    return productsList
