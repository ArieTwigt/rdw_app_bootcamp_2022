# import the required modules
from flask import Flask, render_template
from custom_modules.import_functions import *

# create a flask instance
app = Flask(__name__)


# route for the home page
@app.route("/")
def index():
    return render_template("index.html")


# route for getting the cars
@app.route("/return_cars/<kenteken>")
def return_cars(kenteken):
    data = get_car(kenteken)
    return render_template("return_cars.html",
                            data=data)

# run the application
if __name__ == '__main__':
    app.run()