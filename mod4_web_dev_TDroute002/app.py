import os
from flask import Flask, request
from lib.database_connection import DatabaseConnection, get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist_repository import ArtistRepository
from lib.artist import Artist

app = Flask(__name__)

#db_connection = DatabaseConnection()
#db_connection.connect()
#db_connection.seed("seeds/music_library2.sql")

# ======== routes =============
#
@app.route('/albums', methods=['POST'])
def add_album():
    title = request.form['title']
    release_year = request.form['release_year']
    artist_id = request.form['artist_id']
    
    sub_connection = get_flask_database_connection(app)
    repo = AlbumRepository(sub_connection)
    #
    #
    repo.create(Album(1, title, release_year, artist_id))
    #
    albums = repo.all()
    response = ""
    for album in albums:
        response += f"{album}\n"
    return response
#
# ===============================
#
@app.route('/artists', methods=['GET'])
def get_artists():
    arg1 = request.args['all']
    sub_connection = get_flask_database_connection(app)
    artists_repo = ArtistRepository(sub_connection)
    artists = artists_repo.all()
    text_to_return = ""
    if arg1 == '1':
        for artist in artists:
            text_to_return += f"{artist}\n"
    elif arg1 == '2':
        text_to_return = ', '.join([artist.name for artist in artists])
    return text_to_return

@app.route('/artists', methods=['POST'])
def post_add_artist():
    arg1 = request.form['name']
    arg2 = request.form['genre']
    sub_connection = get_flask_database_connection(app)
    artists_repo = ArtistRepository(sub_connection)
    artists_repo.create(Artist(None, arg1, arg2))
    return ''
#
# ======== end rooutes ========

if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))