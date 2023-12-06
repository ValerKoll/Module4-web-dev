"""
given: all=1 or 2
 action: 1.read all the artists' entries
 returns: 200 (OK)
          a list of artists
"""
def test_get_a_list_of_artists(web_client, db_connection):
    db_connection.seed('seeds/music_library2.sql')
    response = web_client.get('/artists?all=1')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Artist(1, Pixies, Rock)\nArtist(2, ABBA, Pop)\nArtist(3, Taylor Swift, Pop)\nArtist(4, Nina Simone, Jazz)\n"
    response = web_client.get('/artists?all=2')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Pixies, ABBA, Taylor Swift, Nina Simone"

"""
given: name=Wild nothing & genre=Indie
  action: 1.add 1 entry to the artists table
          2.read all the artists' entries using GET
 returns: 200 (OK)
          a list of artists
"""

def test_post_add_one_artis(web_client, db_connection):
    db_connection.seed('seeds/music_library2.sql')
    response = web_client.post('/artists', data={
        'name':'Wild nothing', 'genre':'Indie'
        })
    assert response.status_code == 200
    assert response.data.decode('utf-8') == ''
    
    response = web_client.get('/artists?all=2')
    
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "Pixies, ABBA, Taylor Swift, Nina Simone, Wild nothing"