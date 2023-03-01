# Done in array instead of dictionaries to portray the differences between dictionaries and arrays
# Database tuples are normally received in an array
productList = [['1', "Bad Bunny Album", 'Solid', 'desc here', 'Yes', 'Small', 'White', 'bad_corazon_sticker.jpg', '5', 'active', '5', '5'],
               ['2', 'Naruto Shippuden', 'Glossy', 'desc', 'No', 'Large', 'Red', 'naruto_sticker.png', '3', 'active', '15', '15'],
               ['3', 'Chopper One Piece', 'Glossy', 'desc', 'No', 'Medium', 'Red', 'choppersticker.png', '3', 'active', '10', '10'],
               ['4', 'Bugatti Logo', 'Metallic', 'desc', 'Yes', 'Small', 'Red', 'bugattisticker.png', '3', 'active', '5', '5'],
               ['5', 'Beach Sunset', 'Glossy', 'desc', 'No', 'Large', 'Red', 'BeachSunsetSticker.png', '3', 'active', '15', '15']]

def getProductsModel():
    return productList


# Find the specific product given the ID, found in element 0 of the sub-arrays
def getsingleproductmodel(prodID):
    for product in productList:
        if product[0] == prodID:
            return product
