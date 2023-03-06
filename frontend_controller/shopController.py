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