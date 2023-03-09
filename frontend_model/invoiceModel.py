
def MagerDicts(dict1, dict2):
    if isinstance(dict1, list) and isinstance(dict2, list):
        return dict1 + dict2
    elif isinstance(dict1, dict) and isinstance(dict2, dict):
        return dict(list(dict1.items()) + list(dict2.items()))
    return False

orderDict = {
    "tracking_num": "71287249",
    "order_date": "01/17/23",
    "arrival_date": "01/20/23",
    "address_line_1": "Vista Azulin Calle 11 L13",
    "address_line_2": "Arecibor Puerto Ricor, 00614",
    "total": 1197.00,
    "payment_method": "Mastercard"
}

productDict1 = {"1":{
    "image": 'naruto_sticker.png',
    "name": 'Naruto Shippuden',
    "brand": 'Naruto',
    "price": 5.99,
    "quantity": 2,
    "total_price": 11.98
}}

productDict2 = {"2":{
    "image": 'bad_corazon_sticker.jpg',
    "name": 'Un Verano Sin Ti',
    "brand": 'bad_bunny',
    "price": 25.80,
    "quantity": 1,
    "total_price": 25.80
}}

products = productDict1
products = MagerDicts(products, productDict2)


def getOrderModel():
    return orderDict


def getProductsModel():
    return products
