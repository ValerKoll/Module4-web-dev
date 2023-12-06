# Tests for your routes go here

# === Example Code Below ===
"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"
# === End Example Code ===

"""
When I send a request GET /wave?name=Dana
  I expect the return value to be 200OK
"""
def test_get_wave_name_dana(web_client):
    response = web_client.get("/wave?name=dana")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "I am waving at dana"
    
"""
When I send a request GET /count_vowels?name=Dana
  I expect the return value to be 200 and #4
"""
def test_post_count_vowels(web_client):
    response = web_client.post('/count_vowels', data={'text':'eeao'})
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "The number is 4"
    #assert response.data.decode("utf-8") == ""

"""
When I send a request GET /count_vowels?name=Dana
  I expect the return value to be 200 and #5
"""
def test_post_count_vowels2(web_client):
    response = web_client.post('/count_vowels', data={'text':'eeuhfjfvao'})
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "The number is 5"
    #assert response.data.decode("utf-8") == ""
    
"""
post - sort-names
"""
def test_post_sort_names(web_client):
    response = web_client.post('/sort-names', data = {'names': 'Joe,Alice,Zoe,Julia,Kieran'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice,Joe,Julia,Kieran,Zoe'