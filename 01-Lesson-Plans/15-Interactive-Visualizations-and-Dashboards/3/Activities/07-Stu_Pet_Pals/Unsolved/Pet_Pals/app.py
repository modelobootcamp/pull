# import necessary libraries
from sqlalchemy import func

from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)

from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///db/pets.sqlite"
app.config['ENV'] = 'development'
app.config['DEBUG'] = True
app.config['TESTING'] = True


db = SQLAlchemy(app)


class Pet(db.Model):
    __tablename__ = 'pets'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64))
    type = db.Column(db.String)
    age = db.Column(db.Integer)

    def __repr__(self):
        return '<Pet %r>' %(self.name)



@app.before_first_request
def setup():
    db.drop_all()
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

    # app.logger("errors")
# @TODO: Create a route "/send" that handles both GET and POST requests
# If the request method is POST, save the form data to the database
# Otherwise, return "form.html"

@app.route("/send", methods = ["POST", "GET"])
def send():
    if request.method == "POST":
        petName = request.form["petName"]
        petType = request.form["petType"]
        petAge = request.form["petAge"]
   

        some_var = Pet(name=petName, age=petAge , type = petType)
        db.session.add(some_var)
        db.session.commit()



        return redirect( "/" ,code = 302)

    return render_template("form.html")
 






# @TODO: Create an API route "/api/pals" to return data to plot
@app.route("/api/pals")
def pals():
    # results = db.session.query(Pet.type, func.count(Pet.type)) \
    #     .group_by(Pet.type) \
    #     .all()
    results = db.session.query(Pet.type, func.count(Pet.type)) \
                .group_by(Pet.type) \
                .all()

    pet_type = [result[0] for result in results]
    age = [result[1] for result in results]

    trace = {
        "x": pet_type
        "y": age,
        "type": "bar"
    }

    return jsonify(trace)



if __name__ == "__main__":
    app.run()
