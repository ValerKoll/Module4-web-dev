"""
given: Voyage & 2022 & 2
 action: 1.add new entry to albums
         2.read all the albums' entries
 returns: 200 (OK)
          updated list of albums
"""
def test_add_album(web_client, db_connection):
    db_connection.seed("seeds/music_library2.sql")
    response = web_client.post('/albums', data={'title': 'Voyage', 'release_year': 2022, 'artist_id': 2})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "" \
        "Album(1, Doolittle, 1989, 1)\n" \
        "Album(2, Surfer Rosa, 1988, 1)\n" \
        "Album(3, Waterloo, 1974, 2)\n" \
        "Album(4, Super Trouper, 1980, 2)\n" \
        "Album(5, Voyage, 2022, 2)\n"

"""
given: Voyage & 2022 & null
 action: 1.DON'T add new entry to albums
         2.read all the albums' entries
 returns: 400 (BAD_REQUEST)
          A NOT updated list of albums
"""
def test_add_wrong_submit(web_client):
    response = web_client.post('/albums', data={'title': 'Voyage', 'release_year': 2022})
    assert response.status_code == 400
   