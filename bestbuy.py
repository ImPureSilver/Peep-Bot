class BestBuy:

    def __init__(self, sku_list, driver):
        self.sku_list = sku_list
        self.driver = driver

    def check_stock(self):
        api_link = "https://api.bestbuy.com/click/-/%s/pdp"

        temp = ""
        for sku in self.sku_list:
            # format the link with the sku
            temp = f"https://api.bestbuy.com/click/-/{sku}/pdp"
            # pass in the link to the webdriver to open

            # look for the add to cart
            # if it's there, add it to cart and follow checkout procedure
            # else, check on the next sku
            pass

    def find_add_to_cart(self, page_source="") -> bool:

        if page_source.find("buttonState\":\"ADD_TO_CART\\\\") < 0:
            return False
        else:
            return True
