from flask import Flask, render_template

from models.database import db, Book

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)


with app.app_context():
    db.drop_all()
    db.create_all()


@app.route("/")
def all_books():
    books = Book.query.all()
    return render_template("Books.html", books=books)


if __name__ == "__main__":
    app.run(debug=True)