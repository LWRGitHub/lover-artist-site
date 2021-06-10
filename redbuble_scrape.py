from bs4 import BeautifulSoup as bs
import requests
import time
import json

products = []
art_work = [
  "59786537-Lady-in-the-Wallpaper",
	"59785340-Dancing-Ladies",
	"44242884-Lights-&-Dust",
	"44241848-Paint-Mix",
	"44239383-Cave-Flowers",
	"44239763-Green-Splash",
	"44241267-Pink-Spray",
	"44240623-Lover's-Self-Portrait",
	"44208376-Blue-Ocean",
	"44211284-Painted-Acrylic-Color-Flow",
	"44227432-Colorful-Yellow-Painted-Twist",
]

# get data from redbuble
for art in art_work:
    r = requests.get(f"https://www.redbubble.com/people/PaintedArtLover/works/{art}")
    soup = bs(r.content, 'lxml')
    items = soup.find_all("li", attrs={"class": "carousel_item"})

    for item in items:
        href = item.find("a")['href']
        src = item.find("img")['src']

        # --Go into the webpage that is specific to the product and grab data on product--
        r_item = requests.get(href)
        soup_item = bs(r_item.content, 'lxml')
        imgs = soup_item.find_all("img", attrs={"class": "GalleryImage__img--12Vov"})
        srcs = []
        for img in imgs:
            srcs.append(img['src'])
        # price = soup.find("span", attrs={"class": "styles__box--2Ufmy styles__text--23E5U styles__display2--3HydH styles__display-block--3kWC4 styles__marginBottom-m--2W0L-"}).contents[0]

        src_main = srcs
        src_li = srcs
        src_len = len(srcs)
        if src_len == 0:
          src_main = [src]
        elif src_len < 3:
            if src_len < 2:
                src_main = srcs[0]
                src_li.remove(srcs[0])
            else:
                src_main = srcs[1]
        else:
            src_main = srcs[2]
            src_li.remove(srcs[2])
        # --/Go into the webpage that is specific to the product and grab data on product--

        #  add product info to products
        href_len = len(href)
        products.append({
            "href": href,
            "title": item.find("a")['title'],
            "src": src,
            "alt": item.find("img")['alt'],
            "_id": href[href_len-14:href_len],
            "src_main": src_main,
            "src_li": src_li,
        })

print(products)
# data = json.dumps(products)
# f = open("data.txt", "a")
# f.write(data)
# f.close()

#open and read the file after the appending:
# f = open("data.txt", "r")
# print(f.read())

# items data

# href = href_from_id(item_id)

# r = requests.get(href)
# soup = bs(r.content)
# imgs = soup.find_all("img", attrs={"class": "GalleryImage__img--12Vov"})
# srcs = []
# for img in imgs:
#     srcs.append(img['src'])
# price = soup.find("span", attrs={"class": "styles__box--2Ufmy styles__text--23E5U styles__display2--3HydH styles__display-block--3kWC4 styles__marginBottom-m--2W0L-"}).contents[0]


# src_main = srcs
# src_li = srcs
# src_len = len(srcs)
# if src_len < 3:
#     if src_len < 2:
#         src_main = srcs[0]
#         src_li.remove(srcs[0])
#     else:
#         src_main = srcs[1]
# else:
#     src_main = srcs[2]
#     src_li.remove(srcs[2])
    


# context = {
#     "src_main": src_main,
#     "src_li": src_li,
#     "alt": "#",
#     "title": "Example Product",
#     "_id": item_id,
#     "description": "Example info of the product. This will description the product.",
#     "price": 499.49,
#     "sale": True,
#     "discount": 211.27,
#     "specifications": [
#         {
#             "header": "Expl Header",
#             "info": "Expl info"
#         },
#         {
#             "header": "Expl Header",
#             "info": "Expl info"
#         },
#         {
#             "header": "Expl Header",
#             "info": "Expl info"
#         }
#     ],
#     "products": products
# }