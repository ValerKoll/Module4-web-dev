
# Single Table Design Recipe Template

## 1. Extract nouns from the user stories or specification

```
User: "I want insert a new entry in the table albums"
```

```
>>> Nouns:
>>>  album, title, release year
```

## 2. Set Table Name and Columns

Database: music_library <br>
status:   exist

| table `albums`        | Properties              |
| --------------------- | ----------------------- |
|                       | `title`                 |
|                       | `release year`          |
|                       | `artist_id`             |


## 3. column types

[Here's a full documentation of PostgreSQL data types](https://www.postgresql.org/docs/current/datatype.html).

```
id: SERIAL
title: VARCHAR(255)
release_year: INTEGER
artist_id:  (FK) INTEGER
```

## 4. SQL

n/a
```sql
CREATE TABLE albums (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255),
  release_year INTEGER
  artist_id INTEGER
);
```

## 5. table (if needs)

```bash
psql -h 127.0.0.1 database_name < albums_table.sql
```
## 6. seed the table (if needs) 
n/a