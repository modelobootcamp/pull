# 1. import Flask
from flask import Flask, jsonify

# 2. Create an app, being sure to pass __name__
app = Flask(__name__)


# 3. Define what to do when a user hits the index route
@app.route("/")
def home():
    print("Server received request for 'Home' page... NO seriously!  This is us!")
    return "Hello"



# 4. Define what to do when a user hits the /about route
@app.route("/about")
def about():
    location = "San Diego"
    print("Server received request for 'About' page...")
    return f"Joon in  {location}!"

@app.route("/contact")
def contact():
    print("Server received request for 'contact' page...")
    return jsonify({'email': 'joonyoo@gmail.com'})


if __name__ == "__main__":
    app.run(debug=True)