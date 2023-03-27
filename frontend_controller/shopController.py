from frontend_model.shopModel import *


def getProducts():
    products = getProductsModel()
    return products

def getProductAscending():
    products = sort_productlistAscending(getProductsModel())
    return products

def getProductDescending():
    products = sort_productlistDescending(getProductsModel())
    return products

def getBrands():
    return getBrandsModel()


def getColors():
    return getColorsModel()


def getVideoRes():
    return getVideoResModel()


def getWifi():
    return getWifiModel()
#=========================================================================================================================================================================================================================================
#new controller
def getNewProducts():
    newproducts = getNewProductsModel()
    return newproducts

def getSize():
    return getSizeModel()

def getWaterProof():
    return getWaterProofModel()

def getMaterial():
    return getMaterialModel()

def getPrimaryColor():
    return getPrimaryColorModel()
