from flask import Flask
from pick_three_movies_v2 import organize_movie_file 
from pick_three_movies_v2 import pick_three_movies


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)

@app.route('/')
def display_three_movies():
    """Return a friendly HTTP greeting."""
    movielist = organize_movie_file('sm_movie_list.csv')
    threemovies = pick_three_movies(movielist)
    return '<ol>' + ''.join(map(lambda m: '<li>' + m + '</li>', threemovies)) + '</ol>'


@app.route('/boop')
def boop():
    return 'Snoot!'

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. This
    # can be configured by adding an `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)
