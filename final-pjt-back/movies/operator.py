from apscheduler.schedulers.background import BackgroundScheduler
from django.conf import settings
import requests
import sys
# import io
from .models import Movie, Genre, Production, Actor

api_key = settings.SECRET_KEY


def fixedDataSave():
    # sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')
    # sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding = 'utf-8')


    Genre_URL = "https://api.themoviedb.org/3/genre/movie/list"

    # Genre 저장
    para = {
        "api_key" : api_key,
    }

    res = requests.get(Genre_URL, params=para)

    d = res.json()["genres"]

    for y in d:
        genre = Genre(id = y.get('id'), name = y.get('name'))
        genre.save()



def GetTrailerUrl(id):
    prms = {
        "api_key" : api_key,
    }
    movieTrailerUrl = f"https://api.themoviedb.org/3/movie/{id}/videos"

    res = requests.get(movieTrailerUrl, params=prms)
    key = res.json()['results']
    trailer_key = key[0].get('key')
    trailerUrl = f"https://www.youtube.com/embed/{trailer_key}?autoplay=1&mute=1&loop=1&playlist={trailer_key}"
    return trailerUrl


def GetMovieDetail(id):
    prms = {
        "api_key" : api_key,
        "language" : "ko-KR",
    }
    movieDetailUrl = f"https://api.themoviedb.org/3/movie/{id}"

    res = requests.get(movieDetailUrl, params=prms)
    key = res.json()

    return key


def saveDb():

    fixedDataSave()
                        
    MovieList_URL = "https://api.themoviedb.org/3/discover/movie"

    # MovieList json으로 저장하기

    for i in range(1, 11):
        params = {
            "api_key" : api_key,
            "language" : "ko-KR",
            "page": i,
        }

        r = requests.get(MovieList_URL, params=params)
        data = r.json()['results']

        for x in data:
            try:
                id = x.get('id')
                
                key = GetMovieDetail(id)

                for data in key['production_companies']:
                    try:
                        if (data.get('logo_path')):
                            logo_path = f"https://image.tmdb.org/t/p/original/{data.get('logo_path')}"
                        else:
                            logo_path = 'https://cdn.pixabay.com/photo/2017/04/06/09/39/nothing-2207785_960_720.jpg'

                        production = Production(id=data.get('id'), name=data.get('name'), logo_path=logo_path, original_country=data.get('original_country'))
                        production.validate_unique()
                        production.save()
                    except:
                        continue
                
                movieCreditURL = f"https://api.themoviedb.org/3/movie/{id}/credits"
                
                parameter = {
                    "api_key" : api_key,
                    "language" : "ko-KR",
                }
                
                actor_data = requests.get(movieCreditURL, params=parameter).json()['cast']
                
                for act in actor_data:
                    if (act.get('known_for_department') == "Acting"):
                        try:
                            actor_id = act.get('id')
                            prm = {
                            "api_key" : api_key,
                            "language" : "ko-KR",                
                            }
                            PersonDetailURL = f"https://api.themoviedb.org/3/person/{actor_id}"
                            res = requests.get(PersonDetailURL, params=prm)

                            dt = res.json()
                            
                            if (dt.get('gender') == 1) :
                                gender = 'Female'
                            else:
                                gender = 'Male'
                            
                            if (dt.get('profile_path')):
                                profile_path = f"https://image.tmdb.org/t/p/original/{dt.get('profile_path')}"
                            else:
                                profile_path = "https://icons.veryicon.com/png/o/internet--web/55-common-web-icons/person-4.png"
                                
                            actor = Actor(name=dt.get('name'), biography=dt.get('biography'), birthday=dt.get('birthday'),
                                        deathday=dt.get('deathday'), gender=gender, id=actor_id, place_of_birth=dt.get('place_of_birth'),
                                        popularity=dt.get('popularity'), profile_path=profile_path)
                            
                            actor.validate_unique()
                            actor.save()
                            
                        except:
                            continue
                

                trailerUrl = GetTrailerUrl(id)

                poster_path_original = f"https://image.tmdb.org/t/p/original/{key.get('poster_path')}"
                backdrop_path_original = f"https://image.tmdb.org/t/p/original/{key.get('backdrop_path')}"

                if key.get('release_date'):
                    movie = Movie(id = id, title = key.get('title'), release_date = key.get('release_date'), 
                        popularity = key.get('popularity'), vote_count = key.get('vote_count'), 
                        vote_average = key.get('vote_average'), overview = key.get('overview'),
                        poster_path_original = poster_path_original, backdrop_path_original = backdrop_path_original,
                        trailerUrl = trailerUrl, budget = key.get('budget'), revenue = key.get('revenue'),
                        runtime = key.get('runtime'), homepage = key.get('homepage'))
                    
                else:
                    movie = Movie(id = id, title = key.get('title'), release_date = '1999-12-31', 
                        popularity = key.get('popularity'), vote_count = key.get('vote_count'), 
                        vote_average = key.get('vote_average'), overview = key.get('overview'),
                        poster_path_original = poster_path_original, backdrop_path_original = backdrop_path_original,
                        trailerUrl = trailerUrl, budget = key.get('budget'), revenue = key.get('revenue'),
                        runtime = key.get('runtime'), homepage = key.get('homepage'))
                
                    
                movie.validate_unique()
                movie.save()

                for g in key.get('genres'):
                    movie.genres.add(g.get('id'))

                for company in key.get('production_companies'):
                    movie.production_companies.add(company.get('id'))
                    
                for aid in actor_data:
                    if aid.get('known_for_department') == "Acting":
                        movie.actor.add(aid.get('id'))

            except:
                continue
            
            

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(saveDb, 'cron', hour=1, minute=51, second=10, id="saveDataBase")
    # scheduler.add_job(saveDb, 'interval', seconds=30, id="saveDataBase")
    scheduler.start()