# Radio Mehfil

Retro Indian music web radio built with Python + Flask.

## Run locally

```bash
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000`.

## Music

Put MP3 files you are authorized/licensed to stream in `static/music/` and keep the filenames used in `app.py`.

Do not upload commercial recordings unless you have the necessary rights or licence.

## GitHub Pages note

GitHub Pages serves static files and does not run a Flask server. This repository is therefore set up as a Flask project for local/server deployment; for a live GitHub-hosted static version, the player can be converted to HTML/CSS/JavaScript without Flask.
