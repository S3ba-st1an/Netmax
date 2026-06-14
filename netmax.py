import os
import random
import cv2
from flask import Flask, flash, render_template, request, redirect, url_for, abort
from werkzeug.utils import secure_filename
import sqlite3

UPLOAD_MOVIES = os.path.join('static', 'content', 'filme')
UPLOAD_SERIES = os.path.join('static', 'content', 'seriale')

def get_series_structure():
    base = app.config['UPLOAD_SERIES']
    data = {}

    for series in os.listdir(base):
        series_path = os.path.join(base, series)
        if not os.path.isdir(series_path):
            continue

        seasons_data = {}

        for season in os.listdir(series_path):
            season_path = os.path.join(series_path, season)

            thumbnails_path = os.path.join(season_path, "thumbnails")

            if not os.path.isdir(season_path) or season == "thumbnails":
                continue

            images = []

            if os.path.exists(thumbnails_path):
                for img in os.listdir(thumbnails_path):
                    if img.lower().endswith(('.jpg', '.png', '.jpeg', '.webp')):
                        images.append(img)

            seasons_data[season] = images

        data[series] = seasons_data

    return data

def init_db():
    return sqlite3.connect('movie_list.db')

def save_random_scene(video_path, output_image):
    cap = cv2.VideoCapture(video_path)

    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    if fps <= 0 or frame_count <= 0:
        cap.release()
        return False

    duration = frame_count / fps

    # Pick a random point between 20% and 80% of the video
    random_second = random.uniform(duration * 0.2, duration * 0.8)

    # Jump to that timestamp
    cap.set(cv2.CAP_PROP_POS_MSEC, random_second * 1000)

    success, frame = cap.read()

    if success:
        cv2.imwrite(output_image, frame)

    cap.release()
    return success


app = Flask(__name__)
app.config['UPLOAD_MOVIES'] = UPLOAD_MOVIES
app.config['UPLOAD_SERIES'] = UPLOAD_SERIES

@app.route('/dashboard', methods =["GET", "POST"])
def uploadfile():
    if request.method == "POST":
        inpName = request.form.get('name')
        inpGenre = request.form.get('genre')
        inpReleaseDate = request.form.get('release_date')
        inpDescription = request.form.get('description')
        inpType = request.form.get('type')

        if inpType == 'film':
            with init_db() as con:
                cursor = con.cursor()
                cursor.execute("CREATE TABLE IF NOT EXISTS movies("
                            "id INTEGER PRIMARY KEY, name TEXT, type TEXT, genre TEXT, year INTEGER, description TEXT)"
                            )
                cursor.execute("INSERT INTO movies (name, type, genre, year, description) VALUES(?, ?, ?, ?, ?)",
                                (inpName, inpType, inpGenre, inpReleaseDate, inpDescription))
                con.commit()

                files = request.files.getlist('file')

                if not files:
                    flash('No selected folder')
                    return redirect(request.url)

                folder_name = secure_filename(inpName)

                upload_folder = os.path.join(
                    app.config['UPLOAD_MOVIES'],
                    folder_name
                )

                os.makedirs(upload_folder, exist_ok=True)

                for file in files:

                    if file.filename == '':
                        continue

                    relative_path = file.filename

                    path_parts = relative_path.replace('\\', '/').split('/')

                    safe_parts = [secure_filename(part) for part in path_parts]

                    safe_relative_path = os.path.join(*safe_parts)

                    save_path = os.path.join(
                        upload_folder,
                        safe_relative_path
                    )

                    os.makedirs(os.path.dirname(save_path), exist_ok=True)

                    file.save(save_path)

                    print(file.filename)   
        elif inpType == 'serial':
            with init_db() as con:
                cursor = con.cursor()
                cursor.execute("CREATE TABLE IF NOT EXISTS series("
                            "id INTEGER PRIMARY KEY, name TEXT, type TEXT, genre TEXT, year INTEGER, description TEXT)"
                            )
                cursor.execute("INSERT INTO series (name, type, genre, year, description) VALUES(?, ?, ?, ?, ?)",
                                (inpName, inpType, inpGenre, inpReleaseDate, inpDescription))
                con.commit()

                files = request.files.getlist('file')

                if not files:
                    flash('No selected folder')
                    return redirect(request.url)

                folder_name = secure_filename(inpName)
                upload_folder = os.path.join(
                    app.config['UPLOAD_SERIES'],
                    folder_name
                )
                os.makedirs(upload_folder, exist_ok=True)
                for file in files:
                    if file.filename == '':
                        continue

                    relative_path = file.filename.replace('\\', '/')
                    path_parts = relative_path.split('/')

                    if len(path_parts) > 1:
                        path_parts = path_parts[1:]

                    safe_parts = [secure_filename(part) for part in path_parts]

                    # ✅ 1. CREATE SAVE PATH FIRST
                    save_path = os.path.join(upload_folder, *safe_parts)

                    os.makedirs(os.path.dirname(save_path), exist_ok=True)

                    # ✅ 2. SAVE FILE
                    file.save(save_path)

                    ext = os.path.splitext(save_path)[1].lower()

                    if ext in ['.mp4', '.mkv', '.avi', '.mov']:

                        # ✅ 3. NOW YOU CAN USE save_path SAFELY
                        season_folder = os.path.dirname(save_path)
                        season = os.path.basename(season_folder)

                        screenshots_folder = os.path.join(season_folder, "thumbnails")
                        os.makedirs(screenshots_folder, exist_ok=True)

                        episode_name = os.path.splitext(os.path.basename(save_path))[0]

                        screenshot_path = os.path.join(
                            screenshots_folder,
                            f"{episode_name}.jpg"
                        )

                        save_random_scene(save_path, screenshot_path)

    with init_db() as con:
        cursor = con.cursor()
        cursor.execute("SELECT name, type, genre FROM movies")
        test = cursor.fetchall()
    
    with init_db() as con:
        cursor = con.cursor()
        cursor.execute("SELECT name, type, genre FROM series")
        seriesData = cursor.fetchall()
    return render_template ("upload.html", test=test, seriesData=seriesData)

@app.route('/')
def main():
    with init_db() as con:
        cursor = con.cursor()
        cursor.execute("SELECT name FROM movies")
        moviess = cursor.fetchall()

        cursor.execute("SELECT * FROM movies ORDER BY id DESC LIMIT 1")
        latest_movie = cursor.fetchone()

    with init_db() as con:
        cursor = con.cursor()
        cursor.execute("SELECT name FROM series")
        series = cursor.fetchall()

    return render_template ("index.html", moviess=moviess, latest_movie=latest_movie, series=series)

@app.route('/movie/<moviePlaceholder>/')
def movie(moviePlaceholder):
    moviePlaceholder = moviePlaceholder.replace('-', ' ')
    with init_db() as con:
        cursor = con.cursor()
        cursor.execute('SELECT * FROM movies WHERE name = ?', (moviePlaceholder,))

        movie = cursor.fetchone()
    
    with init_db() as con:
        cursor = con.cursor()
        cursor.execute('SELECT * FROM movies WHERE genre = "Horror"')


        movieGenre = cursor.fetchall()

    if movie is None:
        abort(404)

    return render_template ('movie-page.html', movie=movie, movieGenre=movieGenre)

@app.route('/movie/watch/<moviePlaceholder>')
def watch(moviePlaceholder):
    moviePlaceholder = moviePlaceholder.replace('-', ' ')
    with init_db() as con:
        cursor = con.cursor()
        cursor.execute('SELECT * FROM movies WHERE name = ?', (moviePlaceholder,))

        movieName = cursor.fetchone()
    return render_template ('movie-watch.html', movieName=movieName)

@app.route('/series/<seriesPlaceholder>/')
def series(seriesPlaceholder):
    seriesPlaceholder = seriesPlaceholder.replace('-', ' ')
    with init_db() as con:
        cursor = con.cursor()
        cursor.execute('SELECT * FROM series WHERE name = ?', (seriesPlaceholder,))

        series = cursor.fetchone()
    
    with init_db() as con:
        cursor = con.cursor()
        cursor.execute('SELECT * FROM series WHERE genre = "Horror"')

        seriesGenre = cursor.fetchall()

    if series is None:
        abort(404)
    series_structure = get_series_structure()
    return render_template ('series-page.html', series=series, seriesGenre=seriesGenre, series_structure=series_structure)

@app.route('/series/watch/<seriesPlaceholder>/')
def seriesWhatch(seriesPlaceholder):
    seriesPlaceholder = seriesPlaceholder.replace('-', ' ')

app.run (port=5001, host="0.0.0.0", debug=True)