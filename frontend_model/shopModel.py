
# This is our simulation of the database
# We have two products here.
# The students must create their own productList when working on their eCommerce site
# Product images are loaded into static/images/product-images/
# Done in array instead of dictionaries to portray the differences
productList = [['1', "Bad Bunny Album", 'Solid', 'desc here', 'Yes', 'Small', 'White', 'dji_tello.jpg', '15', 'active', '89', '89'],
               ['2', 'Naruto Shippuden', 'Glossy', 'desc', 'Yes', 'Large', 'Red', 'parrot_bebop_2.jpg', '3', 'active', '270', '290']]


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
