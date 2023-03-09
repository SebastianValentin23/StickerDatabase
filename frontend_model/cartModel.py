from flask import session

# Dictionary uniter
def MagerDicts(dict1, dict2):
    if isinstance(dict1, list) and isinstance(dict2, list):
        return dict1 + dict2
    elif isinstance(dict1, dict) and isinstance(dict2, dict):
        return dict(list(dict1.items()) + list(dict2.items()))
    return False


# Cart items simulated
dictitems1 = {'1': {'name': "Naruto Shippuden", 'price': 3.99, 'quantity': 2, 'total_price': 7.98,
                  'stock': 15, 'brand': "DJI", 'wifi': "Yes", 'videores': "480p", 'desc': "Naruto Sticker Descripcion",
                  'image': "naruto_sticker.png", 'cost': 89.00}}
dictitems2 = {'2': {'name': "Album Bad Bunny", 'price': 5.99, 'quantity': 1, 'total_price': 5.99,
                  'stock': 10, 'brand': "Ruko", 'wifi': "Yes", 'videores': "4k", 'desc': "Un Verano sin ti Descripcion",
                  'image': "bad_corazon_sticker.jpg", 'cost': 350.00}}

def getCartModel():
    # Checking if cart is in session or not and adding the dictionaries to it
    # Create an array with the products able to add
    #session['cartitems'] = MagerDicts(dictitems1, dictitems2)

    return


def addCartModel(ID):
    # make changes to cart here
    # not in use at the moment
    
    #Add ID element from array to session['cart']    
    session['cart'] = dictitems1
    
#    if 'cart' in session:
#        session['cart'] = MagerDicts(session['cart'], session['cartitems'][ID])
#    else:
#        session['cart'] = session['cartitems'][ID]
    
    return


def deleteCartItemModel(ID):
    # delete item from cart
    # not in use at the moment
    del session['cart']
    
    
    return



