from flask import Flask, request, redirect, render_template, url_for

# scraper for getting data
# from bs4 import BeautifulSoup as bs
# import requests

############################################################
# SETUP
############################################################

app = Flask(__name__)

############################################################
# Test Data
############################################################

# get data from redbuble
# r = requests.get("https://www.redbubble.com/shop/ap/59785340")
# soup = bs(r.content)
# items = soup.find_all("a", attrs={"class": "styles__link--2sYi3"})

# for item in items:
#     print(item.find("img", attrs={"class": "styles__image--2CwxX styles__rounded--1lyoH styles__fluid--3dxe-"}))

art_products = [
    {
        "src": "https://ih1.redbubble.net/image.1751903044.6537/fp,840x830,black,off_white,box20,s,f8f8f8-pad,1000x1000,f8f8f8.jpg",
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

    return render_template('home.html')

@app.route('/about')
def about():
    """Display the about page."""

    return render_template('about.html')

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
        "products": art_products
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
        "products": [
            {
                "src": "https://ih1.redbubble.net/image.1751903044.6537/fp,840x830,black,off_white,box20,s,f8f8f8-pad,1000x1000,f8f8f8.jpg",
                "alt": "#",
                "title": "Example Product"
            },
            {
                "src": "https://ih1.redbubble.net/image.1751903044.6537/fp,840x830,black,off_white,box20,s,f8f8f8-pad,1000x1000,f8f8f8.jpg",
                "alt": "#",
                "title": "Example Product"
            },
            {
                "src": "https://ih1.redbubble.net/image.1751903044.6537/fp,840x830,black,off_white,box20,s,f8f8f8-pad,1000x1000,f8f8f8.jpg",
                "alt": "#",
                "title": "Example Product"
            },
            {
                "src": "https://ih1.redbubble.net/image.1751903044.6537/fp,840x830,black,off_white,box20,s,f8f8f8-pad,1000x1000,f8f8f8.jpg",
                "alt": "#",
                "title": "Example Product"
            },
            {
                "src": "https://ih1.redbubble.net/image.1751903044.6537/fp,840x830,black,off_white,box20,s,f8f8f8-pad,1000x1000,f8f8f8.jpg",
                "alt": "#",
                "title": "Example Product"
            },
            {
                "src": "https://ih1.redbubble.net/image.1751903044.6537/fp,840x830,black,off_white,box20,s,f8f8f8-pad,1000x1000,f8f8f8.jpg",
                "alt": "#",
                "title": "Example Product"
            },
            {
                "src": "https://ih1.redbubble.net/image.1751903044.6537/fp,840x830,black,off_white,box20,s,f8f8f8-pad,1000x1000,f8f8f8.jpg",
                "alt": "#",
                "title": "Example Product"
            },
            {
                "src": "https://ih1.redbubble.net/image.1751903044.6537/fp,840x830,black,off_white,box20,s,f8f8f8-pad,1000x1000,f8f8f8.jpg",
                "alt": "#",
                "title": "Example Product"
            },
            {
                "src": "https://ih1.redbubble.net/image.1751903044.6537/fp,840x830,black,off_white,box20,s,f8f8f8-pad,1000x1000,f8f8f8.jpg",
                "alt": "#",
                "title": "Example Product"
            },
            {
                "src": "https://ih1.redbubble.net/image.1751903044.6537/fp,840x830,black,off_white,box20,s,f8f8f8-pad,1000x1000,f8f8f8.jpg",
                "alt": "#",
                "title": "Example Product"
            },
            {
                "src": "https://ih1.redbubble.net/image.1751903044.6537/fp,840x830,black,off_white,box20,s,f8f8f8-pad,1000x1000,f8f8f8.jpg",
                "alt": "#",
                "title": "Example Product"
            },
            {
                "src": "https://ih1.redbubble.net/image.1751903044.6537/fp,840x830,black,off_white,box20,s,f8f8f8-pad,1000x1000,f8f8f8.jpg",
                "alt": "#",
                "title": "Example Product"
            },
            {
                "src": "https://ih1.redbubble.net/image.1751903044.6537/fp,840x830,black,off_white,box20,s,f8f8f8-pad,1000x1000,f8f8f8.jpg",
                "alt": "#",
                "title": "Example Product"
            },
            {
                "src": "https://ih1.redbubble.net/image.1751903044.6537/fp,840x830,black,off_white,box20,s,f8f8f8-pad,1000x1000,f8f8f8.jpg",
                "alt": "#",
                "title": "Example Product"
            },
        ]
    }

    return render_template('products.html', **context)

@app.route('/item/<item_id>')
def item(item_id):
    """Display the item page."""

    context = {
        "src": "https://ih1.redbubble.net/image.1751903044.6537/fp,840x830,black,off_white,box20,s,f8f8f8-pad,1000x1000,f8f8f8.jpg",
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
        "art_products": art_products
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
        "art_products": art_products
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