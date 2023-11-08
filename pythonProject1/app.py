from flask import Flask, render_template

from models.database import db, Book, Genre

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
db.init_app(app)


with app.app_context():
    db.drop_all()
    db.create_all()

    fantasy = Genre(name="фентези")
    db.session.add(fantasy)

    Harry_potter = Book(
            id=1,
            name="Гарри Поттер",
            author="Дж. К. Роулинг",
            genre=fantasy,
        )
    db.session.add(Harry_potter)
    db.session.add(
        Book(
            id=2,
            name="Властелин колец",
            author="Дж. Р. Р. Толкина",
            genre=fantasy
        )
    )

    db.session.commit()


@app.route("/")
def all_books():
    books = db.session.execute(db.select(Book).order_by(Book.id)).scalars()
    return render_template("Books.html", books=books)


@app.route("/genre/<int:genre_id>")
def books_by_genre(genre_id):
    genre = Genre.query.get_or_404(genre_id)
    return render_template(
        "books_by_genre.html",
        genre_name=genre.name,
        books=genre.books,
    )


if __name__ == "__main__":
    app.run(debug=True)