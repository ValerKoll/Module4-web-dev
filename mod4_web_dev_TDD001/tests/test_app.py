"""
get - wave
"""
def test_get_name(web_client):
    response = web_client.get('/wave?name=pippo')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "hello I am pippo"

"""
post - wave
"""
def test_post_name(web_client):
    response = web_client.post('/wave', data = {'name': 'pippo', 'meet': 'mickey'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == "hi pippo nice to meet you, I am mickey"
    
"""
post - sort-names
"""
def test_post_sort_names(web_client):
    response = web_client.post('/sort-names', data = {'names': 'Joe,Alice,Zoe,Julia,Kieran'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice,Joe,Julia,Kieran,Zoe'
    

# ===== CHALLENGE GOES HERE ======
#
def test_add_name(web_client):
    response = web_client.get('/add_name?add=Eddie')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Julia, Alice, Karim, Eddie'
    #assert response.data.decode('utf-8') == ['Julia', 'Alice', 'Karim', 'Eddie']
#
# ===== CHALLENGE end ============z