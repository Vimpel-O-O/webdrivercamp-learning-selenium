ebay_watches_url = 'https://www.ebay.com/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw=watch&_sacat=0'

# Rolex xpath
rolex_checkbox = "//span[contains(text(), 'Rolex')]"
rolex_item_1 = "(//div[@class='s-item__title']/span[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'rolex')])[1]"
rolex_item_2 = "(//div[@class='s-item__title']/span[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'rolex')])[2]"
rolex_item_1_price = "(//div[@class='s-item__title']/span[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'rolex')])[1]/ancestor::div/div[@class='s-item__details clearfix']//span[@class='s-item__price']"
rolex_item_2_price = "(//div[@class='s-item__title']/span[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'rolex')])[2]/ancestor::div/div[@class='s-item__details clearfix']//span[@class='s-item__price']"

# Casio xpath
casio_checkbox = "//span[contains(text(), 'Casio')]"
casio_item_1 = "(//div[@class='s-item__title']/span[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'casio')])[1]"
casio_item_2 = "(//div[@class='s-item__title']/span[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'casio')])[2]"
casio_item_1_price = "(//div[@class='s-item__title']/span[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'casio')])[1]/ancestor::div/div[@class='s-item__details clearfix']//span[@class='s-item__price']"
casio_item_2_price = "(//div[@class='s-item__title']/span[contains(translate(text(), 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', 'abcdefghijklmnopqrstuvwxyz'), 'casio')])[2]/ancestor::div/div[@class='s-item__details clearfix']//span[@class='s-item__price']"

# New tab xpath
newTab_title = "//h1[@class = 'x-item-title__mainTitle']"
newTab_price = "//div[@class = 'x-price-primary']/span"
