# Dictionary uniter
def MagerDicts(dict1, dict2):
    if isinstance(dict1, list) and isinstance(dict2, list):
        return dict1 + dict2
    elif isinstance(dict1, dict) and isinstance(dict2, dict):
        return dict(list(dict1.items()) + list(dict2.items()))
    return False


# Simulated database of orders and their products
# order1 contains productsOrder1...
order1 = {"tracking_num": "71287249",
    "order_date": "01/17/23",
    "arrival_date": "01/20/23",
    "address_line_1": "Villa Linda Ave Palo Blanco",
    "address_line_2": "Ave Interamericana #343",
    "total": 15.00,
    "amount": 3,
    "payment_method": "Visa",
    "status": 'shipped'}

order2 = {"tracking_num": "71287249",
    "order_date": "01/17/23",
    "arrival_date": "01/20/23",
    "address_line_1": "Villa Linda Ave Palo Blanco",
    "address_line_2": "Ave Interamericana #343",
    "total": 15.00,
    "amount": 3,
    "payment_method": "Mastercard",
    "status": 'delivered'}

productDict1 = {"1": {
    "image": 'naruto_sticker.png',
    "name": 'Naruto',
    "brand": 'Naruto',
    "price": 5.00,
    "quantity": 1,
    "total_price": 5.00
}}

productDict2 = {"2": {
    "image": 'bad_corazon_sticker.jpg',
    "name": 'Un verano sin ti',
    "brand": 'Bad Bunny',
    "price": 5.00,
    "quantity": 2,
    "total_price": 10.00
}}

productsOrder1 = productDict1
productsOrder1 = MagerDicts(productsOrder1, productDict2)

productDict3 = {"3": {
    "image": 'choppersticker.png',
    "name": 'Chopper Wanted',
    "brand": 'One Piece',
    "price": 5.00,
    "quantity": 2,
    "total_price": 10.00
}}

productDict4 = {"4": {
    "image": 'BeachSunsetSticker.png',
    "name": 'Beach sticker',
    "brand": 'Fauna',
    "price": 5.00,
    "quantity": 1,
    "total_price": 5.00
}}

productsOrder2 = productDict3
productsOrder2 = MagerDicts(productsOrder2, productDict4)


def getorder1M():
    return order1


def getorder2M():
    return order2


def getorder1prodM():
    return productsOrder1


def getorder2prodM():
    return productsOrder2




