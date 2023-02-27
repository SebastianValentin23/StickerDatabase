# Done in array instead of dictionaries to portray the differences between dictionaries and arrays
# Database tuples are normally received in an array
productList = [['1', "Bad Bunny Album", 'Solid', 'desc here', 'Yes', 'Small', 'White', 'bad_corazon_sticker.jpg', '15', 'active', '89', '89'],
               ['2', 'Naruto Shippuden', 'Glossy', 'desc', 'Yes', 'Large', 'Red', 'naruto_sticker.png', '3', 'active', '270', '290']]


def getProductsModel():
    return productList


# Find the specific product given the ID, found in element 0 of the sub-arrays
def getsingleproductmodel(prodID):
    for product in productList:
        if product[0] == prodID:
            return product
