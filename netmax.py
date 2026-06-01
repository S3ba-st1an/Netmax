import os
from flask import Flask, flash, render_template, request, redirect, url_for, abort
from werkzeug.utils import secure_filename
import sqlite3

UPLOAD_MOVIES = os.path.join('static', 'content', 'filme')
UPLOAD_SERIES = os.path.join('static', 'content', 'seriale')

def init_db():
    return sqlite3.connect('movie_list.db')

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

                    save_path = os.path.join(upload_folder, *safe_parts)

                    os.makedirs(os.path.dirname(save_path), exist_ok=True)

                    file.save(save_path)

                    print(file.filename)

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
    return render_template ("index.html", moviess=moviess, latest_movie=latest_movie)

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

app.run (port=5001, host="0.0.0.0", debug=True)