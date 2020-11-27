from flask import Flask, request, redirect, render_template, url_for

############################################################
# SETUP
############################################################

app = Flask(__name__)

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

    return render_template('art.html')

@app.route('/art_supplies')
def art_supplies():
    """Display the art_supplies page."""

    return render_template('art_supplies.html')

@app.route('/item')
def item():
    """Display the item page."""

    return render_template('item.html')

@app.route('/cart')
def cart():
    """Display the cart page."""

    return render_template('cart.html')

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