from flask import *

app = Flask(__name__)
# -------------------- DATA --------------------

content = {
    "it-welcome-to-derry": {
        "title": "IT: Welcome to Derry",
        "type": "Serial",
        "seasons": {
            1: [
                {"episode": 1, "video": "series/WelcomeToDerry/WelcomeToDerryS1Ep1.mp4", "subtitles": "series/WelcomeToDerry/subtitles/WelcomeToDerryS1Ep1.vtt"},
                {"episode": 2, "video": "series/WelcomeToDerry/WelcomeToDerryS1Ep2.mp4", "subtitles": "series/WelcomeToDerry/subtitles/WelcomeToDerryS1Ep2.vtt"},
                {"episode": 3, "video": "series/WelcomeToDerry/WelcomeToDerryS1Ep3.mp4", "subtitles": "series/WelcomeToDerry/subtitles/WelcomeToDerryS1Ep3.vtt"},
                {"episode": 4, "video": "series/WelcomeToDerry/WelcomeToDerryS1Ep4.mp4", "subtitles": "series/WelcomeToDerry/subtitles/WelcomeToDerryS1Ep4.vtt"},
                {"episode": 5, "video": "series/WelcomeToDerry/WelcomeToDerryS1Ep5.mp4", "subtitles": "series/WelcomeToDerry/subtitles/WelcomeToDerryS1Ep5.vtt"},
                {"episode": 6, "video": "series/WelcomeToDerry/WelcomeToDerryS1Ep6.mp4", "subtitles": "series/WelcomeToDerry/subtitles/WelcomeToDerryS1Ep6.vtt"},
                {"episode": 7, "video": "series/WelcomeToDerry/WelcomeToDerryS1Ep7.mp4", "subtitles": "series/WelcomeToDerry/subtitles/WelcomeToDerryS1Ep7.vtt"},
                {"episode": 8, "video": "series/WelcomeToDerry/WelcomeToDerryS1Ep8.mp4", "subtitles": "series/WelcomeToDerry/subtitles/WelcomeToDerryS1Ep8.vtt"},
            ]
        },
        "cover": "images/WelcomToDerry.jpeg",
        "display": "images/PH3TeCuCqFZExX3Hqp5kCo.png",
        "genre": "Horror",
        "added_at": 1,
    },
    "caddo-lake": {
        "title": "Caddo Lake",
        "type": "Movie",
        "movie": {"video": "movies/CaddoLake/CaddoLake.mp4", "subtitles": "movies/CaddoLake/CaddoLake.vtt"},
        "cover": "images/CaddoLake.jpg",
        "display": "images/CaddoLakeBanner.avif",
        "genre": "Thriller, Mister",
        "added_at": 2,
    },
    "black-phone-2": {
        "title": "Black Phone 2",
        "type": "Movie",
        "movie": {"video": "movies/BlackPhone2/BlackPhone2.mp4", "subtitles": "movies/BlackPhone2/BlackPhone2.vtt"},
        "cover": "images/BlackPhone2.jpg",
        "display": "images/BlackPhone2Banner.jpg",
        "genre": "Horror",
        "added_at": 3,
    },
    "annihilation": {
        "title": "Annihilation",
        "type": "Movie",
        "movie": {"video": "movies/Annihilation/Annihilation.mp4", "subtitles": "movies/Annihilation/Annihilation.vtt"},
        "cover": "images/Annihilation.jpeg",
        "display": "images/AnnihilationBanner.webp",
        "genre": "Horror",
        "added_at": 4,
    },
    "howtotrainyourdragon": {
        "title": "How To Train Your Dragon",
        "type": "Movie",
        "movie": {"video": "movies/HowToTrainYourDragon/HowToTrainYourDragon.mp4", "subtitles": "movies/HowToTrainYourDragon/subs.vtt", "subtitlesSRT": "movies/HowToTrainYourDragon/subs.srt"},
        "cover": "movies/HowToTrainYourDragon/cover.jpg",
        "display": "movies/HowToTrainYourDragon/banner.jpg",
        "genre": "Family/Fantasy",
        "added_at": 5,
    },
    "howtotrainyourdragon2": {
        "title": "How To Train Your Dragon 2",
        "type": "Movie",
        "movie": {"video": "movies/HowToTrainYourDragon2/HowToTrainYourDragon2.mp4", "subtitles": "movies/HowToTrainYourDragon2/subs.vtt", "subtitlesSRT": "movies/HowToTrainYourDragon2/subs.srt"},
        "cover": "movies/HowToTrainYourDragon2/cover.jpg",
        "display": "movies/HowToTrainYourDragon2/banner.avif",
        "genre": "Family/Fantasy",
        "added_at": 6,
    },
    "howtotrainyourdragonthehiddenworld": {
        "title": "How To Train Your Dragon: The Hidden World",
        "type": "Movie",
        "movie": {"video": "movies/HowToTrainYourDragonTheHiddenWorld/HowToTrainYourDragonTheHiddenWorld.mp4", "subtitles": "movies/HowToTrainYourDragonTheHiddenWorld/subs.vtt", "subtitlesSRT": "movies/HowToTrainYourDragonTheHiddenWorld/subs.srt"},
        "cover": "movies/HowToTrainYourDragonTheHiddenWorld/cover.jpg",
        "display": "movies/HowToTrainYourDragonTheHiddenWorld/banner.jpg",
        "genre": "Family/Fantasy",
        "added_at": 7,
    },
    "nocountryforoldmen": {
        "title": "No Country For Old Men",
        "type": "Movie",
        "movie": {"video": "movies/NoCountryForOldMen/NoCountryForOldMen.mp4", "subtitles": "movies/NoCountryForOldMen/subs.vtt", "subtitlesSRT": "movies/NoCountryForOldMen/subs.srt"},
        "cover": "movies/NoCountryForOldMen/cover.jpg",
        "display": "movies/NoCountryForOldMen/banner.jpg",
        "genre": "Thriller, Mister",
        "added_at": 8,
    },
    "sinners": {
        "title": "Sinners",
        "type": "Movie",
        "movie": {"video": "movies/Sinners/Sinners.mp4", "subtitles": "movies/Sinners/subs.vtt", "subtitlesSRT": "movies/Sinners/subs.srt"},
        "cover": "movies/Sinners/cover.jpg",
        "display": "movies/Sinners/banner.avif",
        "genre": "Horror",
        "added_at": 9,
    },
    "returntosilenthill": {
        "title": "Return To Silent Hill",
        "type": "Movie",
        "movie": {"video": "movies/ReturnToSilentHill/ReturnToSilentHill.mp4", "subtitles": "", "subtitlesSRT": ""},
        "cover": "movies/ReturnToSilentHill/cover.jpg",
        "display": "movies/ReturnToSilentHill/banner.jpg",
        "genre": "Horror",
        "added_at": 10,
    },
    "hannibal": {
        "title": "Hannibal",
        "type": "Serial",
        "seasons": {
            1: [
                {"episode": 1, "epname": "Apéritif", "video": "series/Hannibal/Season1/Hannibal S01E01.mp4", "subtitles": "series/Hannibal/Season1/subtitles/Hannibal.S01E01.vtt", "subtitlesSRT": "series/Hannibal/Season1/subtitles/Hannibal.S01E01.srt"},
                {"episode": 2, "epname": "Amuse-Bouche", "video": "series/Hannibal/Season1/Hannibal S01E02.mp4", "subtitles": "series/Hannibal/Season1/subtitles/Hannibal.S01E02.vtt", "subtitlesSRT": "series/Hannibal/Season1/subtitles/Hannibal.S01E02.srt"},
                {"episode": 3, "epname": "Potage", "video": "series/Hannibal/Season1/Hannibal S01E03.mp4", "subtitles": "series/Hannibal/Season1/subtitles/Hannibal.S01E03.vtt", "subtitlesSRT": "series/Hannibal/Season1/subtitles/Hannibal.S01E03.srt"},
                {"episode": 4, "epname": "Oeuf", "video": "series/Hannibal/Season1/Hannibal S01E04.mp4", "subtitles": "series/Hannibal/Season1/subtitles/Hannibal.S01E04.vtt", "subtitlesSRT": "series/Hannibal/Season1/subtitles/Hannibal.S01E04.srt"},
                {"episode": 5, "epname": "Coquilles", "video": "series/Hannibal/Season1/Hannibal S01E05.mp4", "subtitles": "series/Hannibal/Season1/subtitles/Hannibal.S01E05.vtt", "subtitlesSRT": "series/Hannibal/Season1/subtitles/Hannibal.S01E05.srt"},
                {"episode": 6, "epname": "Entrée", "video": "series/Hannibal/Season1/Hannibal S01E06.mp4", "subtitles": "series/Hannibal/Season1/subtitles/Hannibal.S01E06.vtt", "subtitlesSRT": "series/Hannibal/Season1/subtitles/Hannibal.S01E06.srt"},
                {"episode": 7, "epname": "Sorbet", "video": "series/Hannibal/Season1/Hannibal S01E07.mp4", "subtitles": "series/Hannibal/Season1/subtitles/Hannibal.S01E07.vtt", "subtitlesSRT": "series/Hannibal/Season1/subtitles/Hannibal.S01E07.srt"},
                {"episode": 8, "epname": "Fromage", "video": "series/Hannibal/Season1/Hannibal S01E08.mp4", "subtitles": "series/Hannibal/Season1/subtitles/Hannibal.S01E08.vtt", "subtitlesSRT": "series/Hannibal/Season1/subtitles/Hannibal.S01E08.srt"},
                {"episode": 9, "epname": "Trou Normand", "video": "series/Hannibal/Season1/Hannibal S01E09.mp4", "subtitles": "series/Hannibal/Season1/subtitles/Hannibal.S01E09.vtt", "subtitlesSRT": "series/Hannibal/Season1/subtitles/Hannibal.S01E09.srt"},
                {"episode": 10, "epname": "Buffet Froid", "video": "series/Hannibal/Season1/Hannibal S01E10.mp4", "subtitles": "series/Hannibal/Season1/subtitles/Hannibal.S01E10.vtt", "subtitlesSRT": "series/Hannibal/Season1/subtitles/Hannibal.S01E10.srt"},
                {"episode": 11, "epname": "Rôti", "video": "series/Hannibal/Season1/Hannibal S01E11.mp4", "subtitles": "series/Hannibal/Season1/subtitles/Hannibal.S01E11.vtt", "subtitlesSRT": "series/Hannibal/Season1/subtitles/Hannibal.S01E11.srt"},
                {"episode": 12, "epname": "Relevés", "video": "series/Hannibal/Season1/Hannibal S01E12.mp4", "subtitles": "series/Hannibal/Season1/subtitles/Hannibal.S01E12.vtt", "subtitlesSRT": "series/Hannibal/Season1/subtitles/Hannibal.S01E12.srt"},
                {"episode": 13, "epname": "Savoureux", "video": "series/Hannibal/Season1/Hannibal S01E13.mp4", "subtitles": "series/Hannibal/Season1/subtitles/Hannibal.S01E13.vtt", "subtitlesSRT": "series/Hannibal/Season1/subtitles/Hannibal.S01E13.srt"},
            ],
            2: [
                {"episode": 1, "epname": "Kaiseki", "video": "series/Hannibal/Season2/Hannibal S02E01.mp4", "subtitles": "series/Hannibal/Season2/subtitles/Hannibal.S02E01.vtt", "subtitlesSRT": "series/Hannibal/Season2/subtitles/Hannibal.S02E01.srt"},
                {"episode": 2, "epname": "Sakizuke", "video": "series/Hannibal/Season2/Hannibal S02E02.mp4", "subtitles": "series/Hannibal/Season2/subtitles/Hannibal.S02E02.vtt", "subtitlesSRT": "series/Hannibal/Season2/subtitles/Hannibal.S02E02.srt"},
                {"episode": 3, "epname": "Hassun", "video": "series/Hannibal/Season2/Hannibal S02E03.mp4", "subtitles": "series/Hannibal/Season2/subtitles/Hannibal.S02E03.vtt", "subtitlesSRT": "series/Hannibal/Season2/subtitles/Hannibal.S02E03.srt"},
                {"episode": 4, "epname": "Takiawase", "video": "series/Hannibal/Season2/Hannibal S02E04.mp4", "subtitles": "series/Hannibal/Season2/subtitles/Hannibal.S02E04.vtt", "subtitlesSRT": "series/Hannibal/Season2/subtitles/Hannibal.S02E04.srt"},
                {"episode": 5, "epname": "Mukozuke", "video": "series/Hannibal/Season2/Hannibal S02E05.mp4", "subtitles": "series/Hannibal/Season2/subtitles/Hannibal.S02E05.vtt", "subtitlesSRT": "series/Hannibal/Season2/subtitles/Hannibal.S02E05.srt"},
                {"episode": 6, "epname": "Futamono", "video": "series/Hannibal/Season2/Hannibal S02E06.mp4", "subtitles": "series/Hannibal/Season2/subtitles/Hannibal.S02E06.vtt", "subtitlesSRT": "series/Hannibal/Season2/subtitles/Hannibal.S02E06.srt"},
                {"episode": 7, "epname": "Yakimono", "video": "series/Hannibal/Season2/Hannibal S02E07.mp4", "subtitles": "series/Hannibal/Season2/subtitles/Hannibal.S02E07.vtt", "subtitlesSRT": "series/Hannibal/Season2/subtitles/Hannibal.S02E07.srt"},
                {"episode": 8, "epname": "Su-zakana", "video": "series/Hannibal/Season2/Hannibal S02E08.mp4", "subtitles": "series/Hannibal/Season2/subtitles/Hannibal.S02E08.vtt", "subtitlesSRT": "series/Hannibal/Season2/subtitles/Hannibal.S02E08.srt"},
                {"episode": 9, "epname": "Shiizakana", "video": "series/Hannibal/Season2/Hannibal S02E09.mp4", "subtitles": "series/Hannibal/Season2/subtitles/Hannibal.S02E09.vtt", "subtitlesSRT": "series/Hannibal/Season2/subtitles/Hannibal.S02E09.srt"},
                {"episode": 10, "epname": "Naka-Choko", "video": "series/Hannibal/Season2/Hannibal S02E10.mp4", "subtitles": "series/Hannibal/Season2/subtitles/Hannibal.S02E10.vtt", "subtitlesSRT": "series/Hannibal/Season2/subtitles/Hannibal.S02E10.srt"},
                {"episode": 11, "epname": "Ko no Mono", "video": "series/Hannibal/Season2/Hannibal S02E11.mp4", "subtitles": "series/Hannibal/Season2/subtitles/Hannibal.S02E11.vtt", "subtitlesSRT": "series/Hannibal/Season2/subtitles/Hannibal.S02E11.srt"},
                {"episode": 12, "epname": "Tome-wan", "video": "series/Hannibal/Season2/Hannibal S02E12.mp4", "subtitles": "series/Hannibal/Season2/subtitles/Hannibal.S02E12.vtt", "subtitlesSRT": "series/Hannibal/Season2/subtitles/Hannibal.S02E12.srt"},
                {"episode": 13, "epname": "Mizumono", "video": "series/Hannibal/Season2/Hannibal S02E13.mp4", "subtitles": "series/Hannibal/Season2/subtitles/Hannibal.S02E13.vtt", "subtitlesSRT": "series/Hannibal/Season2/subtitles/Hannibal.S02E13.srt"},
            ],
            3: [
                {"episode": 1, "epname": "Antipasto", "video": "series/Hannibal/Season3/Hannibal S03E01.mp4", "subtitles": "series/Hannibal/Season3/subtitles/Hannibal.S03E01.vtt", "subtitlesSRT": "series/Hannibal/Season3/subtitles/Hannibal.S03E01.srt"},
                {"episode": 2, "epname": "Primavera", "video": "series/Hannibal/Season3/Hannibal S03E02.mp4", "subtitles": "series/Hannibal/Season3/subtitles/Hannibal.S03E02.vtt", "subtitlesSRT": "series/Hannibal/Season3/subtitles/Hannibal.S03E02.srt"},
                {"episode": 3, "epname": "Secondo", "video": "series/Hannibal/Season3/Hannibal S03E03.mp4", "subtitles": "series/Hannibal/Season3/subtitles/Hannibal.S03E03.vtt", "subtitlesSRT": "series/Hannibal/Season3/subtitles/Hannibal.S03E03.srt"},
                {"episode": 4, "epname": "Aperitivo", "video": "series/Hannibal/Season3/Hannibal S03E04.mp4", "subtitles": "series/Hannibal/Season3/subtitles/Hannibal.S03E04.vtt", "subtitlesSRT": "series/Hannibal/Season3/subtitles/Hannibal.S03E04.srt"},
                {"episode": 5, "epname": "Contorno", "video": "series/Hannibal/Season3/Hannibal S03E05.mp4", "subtitles": "series/Hannibal/Season3/subtitles/Hannibal.S03E05.vtt", "subtitlesSRT": "series/Hannibal/Season3/subtitles/Hannibal.S03E05.srt"},
                {"episode": 6, "epname": "Dolce", "video": "series/Hannibal/Season3/Hannibal S03E06.mp4", "subtitles": "series/Hannibal/Season3/subtitles/Hannibal.S03E06.vtt", "subtitlesSRT": "series/Hannibal/Season3/subtitles/Hannibal.S03E06.srt"},
                {"episode": 7, "epname": "Digestivo", "video": "series/Hannibal/Season3/Hannibal S03E07.mp4", "subtitles": "series/Hannibal/Season3/subtitles/Hannibal.S03E07.vtt", "subtitlesSRT": "series/Hannibal/Season3/subtitles/Hannibal.S03E07.srt"},
                {"episode": 8, "epname": "The Great Red Dragon", "video": "series/Hannibal/Season3/Hannibal S03E08.mp4", "subtitles": "series/Hannibal/Season3/subtitles/Hannibal.S03E08.vtt", "subtitlesSRT": "series/Hannibal/Season3/subtitles/Hannibal.S03E08.srt"},
                {"episode": 9, "epname": "...And the Woman Clothed with the Sun", "video": "series/Hannibal/Season3/Hannibal S03E09.mp4", "subtitles": "series/Hannibal/Season3/subtitles/Hannibal.S03E09.vtt", "subtitlesSRT": "series/Hannibal/Season3/subtitles/Hannibal.S03E09.srt"},
                {"episode": 10, "epname": "...And the Woman Clothed in Sun", "video": "series/Hannibal/Season3/Hannibal S03E10.mp4", "subtitles": "series/Hannibal/Season3/subtitles/Hannibal.S03E10.vtt", "subtitlesSRT": "series/Hannibal/Season3/subtitles/Hannibal.S03E10.srt"},
                {"episode": 11, "epname": "...And the Beast from the Sea", "video": "series/Hannibal/Season3/Hannibal S03E11.mp4", "subtitles": "series/Hannibal/Season3/subtitles/Hannibal.S03E11.vtt", "subtitlesSRT": "series/Hannibal/Season3/subtitles/Hannibal.S03E11.srt"},
                {"episode": 12, "epname": "The Number of the Beast Is 666", "video": "series/Hannibal/Season3/Hannibal S03E12.mp4", "subtitles": "series/Hannibal/Season3/subtitles/Hannibal.S03E12.vtt", "subtitlesSRT": "series/Hannibal/Season3/subtitles/Hannibal.S03E12.srt"},
                {"episode": 13, "epname": "The Wrath of the Lamb", "video": "series/Hannibal/Season3/Hannibal S03E13.mp4", "subtitles": "series/Hannibal/Season3/subtitles/Hannibal.S03E13.vtt", "subtitlesSRT": "series/Hannibal/Season3/subtitles/Hannibal.S03E13.srt"},
            ]
        },
        "cover": "series/Hannibal/cover.jpg",
        "display": "series/Hannibal/banner.jpg",
        "genre": "Horror",
        "added_at": 11,
    },
}

# -------------------- ROUTES --------------------

@app.route("/")
def main():
    latest_show = max(
        content.values(),
        key=lambda show: show["added_at"]
    )
    return render_template("index.html", content=content, latest_show=latest_show)


@app.route("/show/<slug>/")
def episode_detail(slug):
    show = content.get(slug)
    if not show:
        abort(404)

    if show["type"] == "Movie":
        return redirect(url_for("movie", slug=slug))

    # Pass all seasons to the template
    return render_template("content.html", show=show, content=content)


@app.route("/show/<slug>/season/<int:season>/episode/<int:episode>")
def episode(slug, season, episode):
    show = content.get(slug)
    if not show or show["type"] != "Serial":
        abort(404)

    # Get the season data
    episodes = show["seasons"].get(season)
    if not episodes:
        abort(404)
    
    ep = next((e for e in episodes if e["episode"] == episode), None)
    if not ep:
        abort(404)

    # Find the specific episode
    ep = next((e for e in episodes if e["episode"] == episode), None)
    if not ep:
        abort(404)

    return render_template("movie.html", show=show, video=ep["video"], 
                         subtitles=ep.get("subtitles"), season=season, episode=episode, epname=ep["epname"])


@app.route("/movie/<slug>/")
def movie(slug):
    show = content.get(slug)
    if not show or show["type"] != "Movie":
        abort(404)

    return render_template("movie.html", show=show, video=show["movie"]["video"], 
                         subtitles=show["movie"].get("subtitles"))
    
# -------------------- RUN --------------------

#if __name__ == "__main__":
    #app.run(debug=True, host="0.0.0.0", port=5001)