##### authors: Simon B., Valerio P - @Makers_accademy
# {{ ADD NAME }} Route Design Recipe
```
# Request:
GET /names?add=Eddie

# This route should return a list of pre-defined names, plus the name given.

# Expected response (2OO OK):
Julia, Alice, Karim, Eddie
```
## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# Home route
GET /add_name

# Naming route
GET /add_name?add=<string>

# Submit message route
GET /add_name
  name: string
  list of names: list of strings
```

## 2. Create Examples as Tests
_Include the status code and the response body._

```python
# EXAMPLE

# GET /add_name?add=Eddie
#  Expected response (200 OK):
"""
given a name
 -returns code = 200
 -returns Julia, Alice, Karim, Eddie
"""

```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
"""
GET /add_name
  Expected response (200 OK):
  "Julia, Alice, Karim, Eddie"
"""
def test_add_name(web_client):
    response = web_client.get('/add_name')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Julia, Alice, Karim, Eddie'



