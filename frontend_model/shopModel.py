
# This is our simulation of the database
# We have two products here.
# The students must create their own productList when working on their eCommerce site
# Product images are loaded into static/images/product-images/
# Done in array instead of dictionaries to portray the differences
productList = [['1', "Bad Bunny Album", 'Solid', 'desc here', 'Yes', 'Small', 'White', 'bad_corazon_sticker.jpg', '5', 'active', '89', '89'],
               ['2', 'Naruto Shippuden', 'Glossy', 'desc', 'No', 'Large', 'Red', 'naruto_sticker.png', '3', 'active', '15', '290'],
               ['3', 'Chopper One Piece', 'Glossy', 'desc', 'No', 'Medium', 'Red', 'choppersticker.png', '3', 'active', '10', '290'],
               ['4', 'Bugatti Logo', 'Metallic', 'desc', 'Yes', 'Small', 'Red', 'bugattisticker.png', '3', 'active', '5', '290'],
               ['5', 'Beach Sunset', 'Glossy', 'desc', 'No', 'Large', 'Red', 'BeachSunsetSticker.png', '3', 'active', '15', '290']]


def getProductsModel():
    return productList


def getBrandsModel():
    # Simulating grabbing these filters via SQL from the database
    brands = ["Solid", "Glossy", "Metallic"]
    return brands

def getColorsModel():
    colors = ["White", "Gray", "Red"]
    return colors


def getVideoResModel():
    videores = ["Small", "Medium", "Large"]
    return videores


def getWifiModel():
    wifi = ['Yes', 'No']
    return wifi
