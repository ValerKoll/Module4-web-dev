# Route Design Recipe
## 1. Design the Route Signature

```
# albums route
POST /albums
    `title:` string
    `release_year:` int
    `artist_id:` int 
```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python
"""
given: Voyage & 2022 & 2
 action: 1.add new entry to albums
         2.read all the albums' entries
 returns: 200 (OK)
          updated list of albums
"""
POST /albums
    title=Voyage
    release_year=2022
    artist_id=2
  Expected response: 200 (OK)
  Expected response: "Voyage, 2022, 2"

"""
given: Voyage & 2022 & null
 action: 1.DON'T add new entry to albums
         2.read all the albums' entries
 returns: 400 (BAD_REQUEST)
          A NOT updated list of albums
"""

```

## 3. Test-drive the Route

see tes_albums
