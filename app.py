from flask import Flask, render_template

app = Flask(__name__)

SONGS = [
    {"title": "Aaja Piya Tohe Pyar Doon", "artist": "Lata Mangeshkar", "year": "1970s", "file": "/static/music/01.mp3"},
    {"title": "Rimjhim Gire Saawan", "artist": "Kishore Kumar", "year": "1970s", "file": "/static/music/02.mp3"},
    {"title": "Kahin Door Jab Din Dhal Jaye", "artist": "Mukesh", "year": "1970s", "file": "/static/music/03.mp3"},
    {"title": "Chura Liya Hai Tumne", "artist": "Asha Bhosle / Mohammed Rafi", "year": "1970s", "file": "/static/music/04.mp3"},
    {"title": "Lag Ja Gale", "artist": "Lata Mangeshkar", "year": "1960s", "file": "/static/music/05.mp3"},
]

@app.route("/")
def home():
    return render_template("index.html", songs=SONGS)

if __name__ == "__main__":
    app.run(debug=True)
