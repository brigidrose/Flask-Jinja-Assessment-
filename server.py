"""Some general notes:
    I thought I understood the concept of sessions but was unable to implement 
    conditional statements that checked to see if a name had or hadn't already
    been given. I think it might have something with how I am evaluating to none,
    but I was confused by my session print statment not returning anything at all.

    As noted on base.html, I used the melon shoping cart excercise as a
    reference for jinja inheritance. I feel as thought I understand the 
    concept of this but I am confused by some of the implementation I have seen.

    I struggled most with understanding how to unpack/refer to the information
    in the dictionary of dictionaries. I would love more examples of/ practice
    time with this specific kind of nested dataset. 
"""

from flask import Flask, redirect, request, render_template, session, flash
from flask_debugtoolbar import DebugToolbarExtension
from jinja2 import StrictUndefined
from random import choice


app = Flask(__name__)
app.jinja_env.undefined = StrictUndefined
app.jinja_env.auto_reload = True

# Required to use Flask sessions and the debug toolbar
app.secret_key = "ABC"

# Getting our list of MOST LOVED MELONS
MOST_LOVED_MELONS = {
    'cren': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimRegular/crenshaw.jpg',
        'name': 'Crenshaw',
        'num_loves': 584,
    },
    'jubi': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimThumbnail/Jubilee-Watermelon-web.jpg',
        'name': 'Jubilee Watermelon',
        'num_loves': 601,
    },
    'sugb': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimThumbnail/Sugar-Baby-Watermelon-web.jpg',
        'name': 'Sugar Baby Watermelon',
        'num_loves': 587,
    },
    'texb': {
        'img': 'http://www.rareseeds.com/assets/1/14/DimThumbnail/Texas-Golden-2-Watermelon-web.jpg',
        'name': 'Texas Golden Watermelon',
        'num_loves': 598,
    },
}

# YOUR ROUTES GO HERE

@app.route("/")
def index():
    """Return homepage."""

    #If name already entered redirect to top-melons
    print sessions.get("user_name")
    if sessions.get("user_name") != None:  #not properly implemented  :(
        print HELLLLLLLLOOOOOOOOO
        return redirect('/top-melons')

    return render_template("homepage.html")


@app.route("/top-melons")
def show_top_melons():

    #if no name, redirect to home page. 
    print sessions.get("user_name")
    if sessions.get("user_name") == None: #not properly implemented :(
        print HELLLLLLLLOOOOOOOOO
        return render_template("homepage.html")


    melon_info = MOST_LOVED_MELONS
    melon_key = choice(melon_info.keys())
    print melon_key
    melon_value = melon_info.get(melon_key)
    print melon_value
    return render_template("top-melons.html",
                            melons=melon_value)

@app.route("/get_name")
def get_first_name():

    name = request.args.get("user_name")
  
   

    session["user_name"] = name
    print session
    
      #username = request.form['user_name']
    #flash("Yay! Welcome to Melon Love!") #I was trying to be extra fancy
    return redirect('/top-melons')             #with this. I don't know why it
                                            #prints twice?
    
   

@app.route("/thank-you")
def show_thank_you():
    """Return homepage."""

    return render_template("thank-you.html")


if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the
    # point that we invoke the DebugToolbarExtension
    app.debug = False    #this causes an issue with redirct if set to true so..
                        #I set it to false to no longer be annoying.

    # Use the DebugToolbar
    DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
