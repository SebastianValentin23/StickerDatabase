
# This is our simulation of the database
# We have two products here.
# The students must create their own productList when working on their eCommerce site
# Product images are loaded into static/images/product-images/
# Done in array instead of dictionaries to portray the differences    
                        #Old order                         
# ID 0,Name 1,Material 2,Description 3,
#WaterProof 4,
# Size 5,Color 6,Imagelink 7,stock 8,
#IDk 9,Price 10,Cost 11                      
productList = [['1', "Bad Bunny Album", 'Solid', 'The iconic heart from Bad Bunnys album art.', 'Yes', 'Small', 'White', 'bad_corazon_sticker.jpg', '5', 'active', '5', '5'],
               ['2', 'Naruto Shippuden', 'Glossy', 'The side view of the most famous ninja in anime, Naruto.', 'No', 'Large', 'Red', 'naruto_sticker.png', '3', 'active', '9', '9'],
               ['3', 'Chopper One Piece', 'Glossy', 'The "wanted" poster of the famous character from the One Piece series, Chopper.', 'No', 'Medium', 'Red', 'choppersticker.png', '3', 'active', '7', '7'],
               ['4', 'Bugatti Logo', 'Metallic', 'The logo of the luxury car brand Bugatti.', 'Yes', 'Small', 'Red', 'bugattisticker.png', '3', 'active', '5', '5'],
               ['5', 'Beach Sunset', 'Glossy', 'The beautiful view of a relaxing landscape on the beach.', 'No', 'Large', 'Red', 'BeachSunsetSticker.png', '3', 'active', '9', '9']]
#====================================New Code testing===================================================================================================================================================================================                        
                        #New order
                              # Make sure ImageLink is ID+Name.png (DeleteSpaces,lowercase)
# ID 0, Name 1, ImageLink 2, Stock 3, 
# Size 4
# WaterProof 5, Price 6, Cost 7,
# Material 8, 
# Color 9, Brand 10, Description 11
newproductList = [['1','Bad Bunny Icon','1badbunnyicon.png','13','Custom','Yes','15','6.5','Solid','Red','Bad Bunny','The iconic heart from Bad Bunnys album art.'],
                  ['2','Bugatti Logo','2bugattilogo.png','7','Oval','Yes','9','5','Solid','Red','Bad Bunny','The iconic heart from Bad Bunnys album art.']]
#=========================================================================================================================================================================================================================================
                                #Old model
def getProductsModel():
    return productList

def sort_productlistAscending(awa):
    awa = sorted(productList, key=lambda product: product[10])
    return awa

def sort_productlistDescending(ewe):
   ewe = sorted(productList, key=lambda product: product[10],reverse = True)        
   return ewe

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
#=========================================================================================================================================================================================================================================
                                #new Model     
def getNewProductsModel():
    return newproductList

def sort_newproductlistAscending(awa):
    awa = sorted(newproductList, key=lambda product: product[6])
    return awa

def sort_newproductlistDescending(ewe):
   ewe = sorted(newproductList, key=lambda product: product[6],reverse = True)        
   return ewe

def getSizeModel():
    size = ["Square 5x5", "Square 3x3","Circle","Bumper","Oval","Custom"]
    return size

def getWaterProofModel():
    waterproof = ['Yes', 'No']
    return waterproof

def getMaterialModel():
    material = ["Solid","Glossy","Metallic"]
    return material

def getPrimaryColorModel():
    primarycolor = ["Rainbow","Monocrome","Red","Blue","Yellow","Orange","Green","Purple","Pink","Brown"]
    return primarycolor
