from flask import Flask, request, redirect, render_template, url_for

# scraper for getting data
from bs4 import BeautifulSoup as bs
import requests
import time

############################################################
# SETUP
############################################################

app = Flask(__name__)

############################################################
# Test Data
############################################################

# products = []
# art_work = [
#     "59786537-Lady-in-the-Wallpaper",
# 	"59785340-Dancing-Ladies",
# 	"44242884-Lights-&-Dust",
# 	"44241848-Paint-Mix",
# 	"44239383-Cave-Flowers",
# 	"44239763-Green-Splash",
# 	"44241267-Pink-Spray",
# 	"44240623-Lover's-Self-Portrait",
# 	"44208376-Blue-Ocean",
# 	"44211284-Painted-Acrylic-Color-Flow",
# 	"44227432-Colorful-Yellow-Painted-Twist",
# ]
# get data from redbuble
# for art in art_work:
#     r = requests.get(f"https://www.redbubble.com/people/PaintedArtLover/works/{art}")
#     soup = bs(r.content)
#     items = soup.find_all("li", attrs={"class": "carousel_item"})

#     for item in items:
#         href = item.find("a")['href']
#         href_len = len(href)
#         products.append({
#             "href": href,
#             "title": item.find("a")['title'],
#             "src": item.find("img")['src'],
#             "alt": item.find("img")['alt'],
#             "_id": href[href_len-14:href_len]
#         })

# print(products)

products = [
    {
        "src": "data:image/gif;base64,R0lGODdhFQAXAPAAANba3wAAACwAAAAAFQAXAAACFISPqcvtD6OctNqLs968+w+GolUAADs=",
        "alt": "#",
        "title": "Example Product",
        "_id": 123456789
    },
    {
        "src": "https://ih1.redbubble.net/image.1751903044.6537/fp,840x830,black,off_white,box20,s,f8f8f8-pad,1000x1000,f8f8f8.jpg",
        "alt": "#",
        "title": "Example Product",
        "_id": 7653413
    },
    {
        "src": "https://ih1.redbubble.net/image.1751903044.6537/fp,840x830,black,off_white,box20,s,f8f8f8-pad,1000x1000,f8f8f8.jpg",
        "alt": "#",
        "title": "Example Product",
        "_id": 9786416736078
    },
    {
        "src": "https://ih1.redbubble.net/image.1751903044.6537/fp,840x830,black,off_white,box20,s,f8f8f8-pad,1000x1000,f8f8f8.jpg",
        "alt": "#",
        "title": "Example Product",
        "_id": 7645262356989
    },
    {
        "src": "https://ih1.redbubble.net/image.1751903044.6537/fp,840x830,black,off_white,box20,s,f8f8f8-pad,1000x1000,f8f8f8.jpg",
        "alt": "#",
        "title": "Example Product",
        "_id": 76533412359567874336745
    },
    {
        "src": "https://ih1.redbubble.net/image.1751903044.6537/fp,840x830,black,off_white,box20,s,f8f8f8-pad,1000x1000,f8f8f8.jpg",
        "alt": "#",
        "title": "Example Product",
        "_id": 87641797868
    },
    {
        "src": "https://ih1.redbubble.net/image.1751903044.6537/fp,840x830,black,off_white,box20,s,f8f8f8-pad,1000x1000,f8f8f8.jpg",
        "alt": "#",
        "title": "Example Product",
        "_id": 8965452124547867800679546
    },
    {
        "src": "https://ih1.redbubble.net/image.1751903044.6537/fp,840x830,black,off_white,box20,s,f8f8f8-pad,1000x1000,f8f8f8.jpg",
        "alt": "#",
        "title": "Example Product",
        "_id": 8728758734
    },
    {
        "src": "https://ih1.redbubble.net/image.1751903044.6537/fp,840x830,black,off_white,box20,s,f8f8f8-pad,1000x1000,f8f8f8.jpg",
        "alt": "#",
        "title": "Example Product",
        "_id": 384765760239567
    },
    {
        "src": "https://ih1.redbubble.net/image.1751903044.6537/fp,840x830,black,off_white,box20,s,f8f8f8-pad,1000x1000,f8f8f8.jpg",
        "alt": "#",
        "title": "Example Product",
        "_id": 2398562309785623890564
    },
    {
        "src": "https://ih1.redbubble.net/image.1751903044.6537/fp,840x830,black,off_white,box20,s,f8f8f8-pad,1000x1000,f8f8f8.jpg",
        "alt": "#",
        "title": "Example Product",
        "_id": 897234789345908
    },
    {
        "src": "https://ih1.redbubble.net/image.1751903044.6537/fp,840x830,black,off_white,box20,s,f8f8f8-pad,1000x1000,f8f8f8.jpg",
        "alt": "#",
        "title": "Example Product",
        "_id": 6542345678345
    },
    {
        "src": "https://ih1.redbubble.net/image.1751903044.6537/fp,840x830,black,off_white,box20,s,f8f8f8-pad,1000x1000,f8f8f8.jpg",
        "alt": "#",
        "title": "Example Product",
        "_id": 76435287667
    },
    {
        "src": "https://ih1.redbubble.net/image.1751903044.6537/fp,840x830,black,off_white,box20,s,f8f8f8-pad,1000x1000,f8f8f8.jpg",
        "alt": "#",
        "title": "Example Product",
        "_id": 764524756
    },
]

############################################################
# ROUTES
############################################################

@app.route('/')
def home():
    """Display the home page."""

    context = {
        "linked_pg": [
            {
                "src": "https://ih1.redbubble.net/image.1751903044.6537/fp,840x830,black,off_white,box20,s,f8f8f8-pad,1000x1000,f8f8f8.jpg",
                "alt": "#",
                "href": "/art",
                "title": "Original Painting"
            },
            {
                "src": "https://ih1.redbubble.net/image.1751866563.5340/ur,apron_realistic_flatlay,square,1000x1000.jpg",
                "alt": "#",
                "href": "/art",
                "title": "Artsy Products"
            },
            {
                "src": "https://s.alicdn.com/@sc01/kf/HTB1nUS4m1uSBuNjSsplq6ze8pXaS.jpg_300x300.jpg",
                "alt": "#",
                "href": "/art_supplies",
                "title": "Art Supplies"
            },
            {
                "src": "https://ih1.redbubble.net/image.1751903044.6537/fp,840x830,black,off_white,box20,s,f8f8f8-pad,1000x1000,f8f8f8.jpg",
                "alt": "#",
                "href": "/art",
                "title": "Prints"
            }
        ],
        "spotlight": [
            {
                "src": "https://ih1.redbubble.net/image.1751903044.6537/fp,840x830,black,off_white,box20,s,f8f8f8-pad,1000x1000,f8f8f8.jpg",
                "alt": "#",
                "title": "Example Product",
                "_id": 764524756,
                "info": "Ex info, the item info goes here.",
                "href": "/item/764524756"
            },
            {
                "src": "https://ih1.redbubble.net/image.1751903044.6537/fp,840x830,black,off_white,box20,s,f8f8f8-pad,1000x1000,f8f8f8.jpg",
                "alt": "#",
                "title": "Example Product",
                "_id": 764524756,
                "info": "Ex info, the item info goes here.",
                "href": "/item/764524756"
            },
            {
                "src": "https://ih1.redbubble.net/image.1751903044.6537/fp,840x830,black,off_white,box20,s,f8f8f8-pad,1000x1000,f8f8f8.jpg",
                "alt": "#",
                "title": "Example Product",
                "_id": 764524756,
                "info": "Ex info, the item info goes here.",
                "href": "/item/764524756"
            },
        ]
    }

    return render_template('home.html', **context)

@app.route('/about')
def about():
    """Display the about page."""

    return render_template('about.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/art')
def art():
    """Display the art page."""
    

    context = {
        "page": {
            "name": "Art"
        },
        "other_pages": [
            {
                "name": "Original Pantings",
                "src": "https://i.etsystatic.com/21906914/r/il/c63418/2575610432/il_1588xN.2575610432_ltfh.jpg",
                "alt": "#"
            },
            {
                "name": "Prints",
                "src": "https://ih1.redbubble.net/image.1751903044.6537/fp,840x830,black,off_white,box20,s,f8f8f8-pad,1000x1000,f8f8f8.jpg",
                "alt": "#"
            },
            {
                "name": "Artsy Products",
                "src": "https://ih1.redbubble.net/image.1751866563.5340/ur,apron_realistic_flatlay,square,1000x1000.jpg",
                "alt": "#"
            }
        ],
        "products": products
    }

    return render_template('products.html', **context)

@app.route('/art_supplies')
def art_supplies():
    """Display the art_supplies page."""

    context = {
        "page": {
            "name": "Art Supplies"
        },
        "other_pages": [
            {
                "name": "Paint",
                "src": "https://s.alicdn.com/@sc01/kf/HTB1nUS4m1uSBuNjSsplq6ze8pXaS.jpg_300x300.jpg",
                "alt": "#"
            },
            {
                "name": "Brushes & More",
                "src": "https://s.alicdn.com/@sc01/kf/Ha4164887b5074d098c682be35f164f1cU.jpg_300x300.jpg",
                "alt": "#"
            },
            {
                "name": "Art Canvases",
                "src": "https://s.alicdn.com/@sc01/kf/HTB1TuS.XLjM8KJjSZFyq6xdzVXar.jpg_300x300.jpg",
                "alt": "#"
            }
        ],
        "products": products
    }

    return render_template('products.html', **context)

def href_from_id(item_id):
    for i in products:
        if i["_id"] == item_id:
            return i['href']

@app.route('/item/<item_id>')
def item(item_id):
    """Display the item page."""
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
        
    src_main = "https://ih1.redbubble.net/image.1751903044.6537/fp,840x830,black,off_white,box20,s,f8f8f8-pad,1000x1000,f8f8f8.jpg"
    src_li = ["https://ih1.redbubble.net/image.1751903044.6537/fp,840x830,black,off_white,box20,s,f8f8f8-pad,1000x1000,f8f8f8.jpg","https://ih1.redbubble.net/image.1751903044.6537/fp,840x830,black,off_white,box20,s,f8f8f8-pad,1000x1000,f8f8f8.jpg","https://ih1.redbubble.net/image.1751903044.6537/fp,840x830,black,off_white,box20,s,f8f8f8-pad,1000x1000,f8f8f8.jpg"]

    context = {
        "src_main": src_main,
        "src_li": src_li,
        "alt": "#",
        "title": "Example Product",
        "_id": item_id,
        "description": "Example info of the product. This will description the product.",
        "price": 499.49,
        "sale": True,
        "discount": 211.27,
        "specifications": [
            {
                "header": "Expl Header",
                "info": "Expl info"
            },
            {
                "header": "Expl Header",
                "info": "Expl info"
            },
            {
                "header": "Expl Header",
                "info": "Expl info"
            }
        ],
        "products": products
    }

    if context["sale"]:
        context["sale_price"] = context["price"] - context["discount"]

    # for item in art_products:
    #     if item["_id"] == item_id:
    #         context["title"] = item["title"]
    #         context["_id"] = item_id
    #         context["alt"] = item["alt"]
    #         context["src"] = item["src"]

    return render_template('item.html', **context)

@app.route('/cart')
def cart():
    """Display the cart page."""

    context ={
        "cart": [
            {
                "src": "https://ih1.redbubble.net/image.1751903044.6537/fp,840x830,black,off_white,box20,s,f8f8f8-pad,1000x1000,f8f8f8.jpg",
                "alt": "#",
                "title": "Ex Title",
                "description": "Ex description goes here.",
                "price": 499.49,
                "sale": True,
                "discount": 211.27,
            },
            {
                "src": "https://ih1.redbubble.net/image.1751903044.6537/fp,840x830,black,off_white,box20,s,f8f8f8-pad,1000x1000,f8f8f8.jpg",
                "alt": "#",
                "title": "Ex Title",
                "description": "Ex description goes here.",
                "price": 499.49,
                "sale": True,
                "discount": 211.27,
            },
        ],
        "products": products
    }

    for item in context["cart"]:
        if item["sale"]:
            item["sale_price"] = item["price"] - item["discount"]

    return render_template('cart.html', **context)

@app.route('/help')
def help():
    """Display the help page."""

    return render_template('help.html')

@app.route('/jobs')
def jobs():
    """Display the jobs page."""

    return render_template('jobs.html')

if __name__ == '__main__':
    app.run(debug=True)