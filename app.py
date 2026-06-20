from flask import Flask, render_template, request, redirect

app = Flask(__name__)

movies = [
    {"id": 1, "title": "Saalar"},
    {"id": 2, "title": "ANIMAL"},
    {"id": 3, "title": "Hi Nanna"},
    {"id": 4, "title": "Kanguva"},
]

@app.route("/")
def index():
    return render_template("index.html", movies=movies)

@app.route("/book/<int:movie_id>")
def book(movie_id):
    movie = next((m for m in movies if m["id"] == movie_id),movie_id)
    if movie:
        return render_template("book.html", movie=movie)
    else:
        return "Movie not found"

@app.route("/confirm_booking", methods=["POST"])
def confirm_booking():
    movie_id = request.form.get("movie.title")
    name = request.form.get("name")
    tickets = int(request.form.get("tickets"))

    # Here, you can implement further processing like storing the booking details in a database.

    return render_template("confirmation.html",name=name, tickets=tickets)

if __name__ == "__main__":
    app.run(debug=True)
    