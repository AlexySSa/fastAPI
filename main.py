from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = "mi aplicacion con fastapi"
app.version = "0.0.1"

movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': 2009,
        'rating': 7.8,
        'category': 'Acción'
    },
    {
        'id': 2,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': 2008,
        'rating': 7.8,
        'category': 'Terror'
    }
]
#HTML en fastAPI
@app.get('/', tags=["home"])
def mensaje():
    return HTMLResponse('<h1>hello world</h1>')

@app.get('/movies', tags=['movies'])
def get_movies():
    return movies

@app.get('/movies/{id}', tags=['movies'])
def get_movie(id: int):
    for item in movies:
        if item['id'] == id:
            return item

    return []
#filtrado de peliculas segun year y categorias
@app.get('/movies/', tags=['movies'])
def get_movies_by_category(category: str, year: int):
    for item in movies:
        if item["category"] == category:
            return item
    return []

@app.post('/movies', tags=['movies'])
def create_movies(id: int = Body(), title: str = Body(), overview: str = Body(), year: int = Body(), rating: float = Body(), category: str = Body()):
    movies.append({
        "id": id, 
        "title": title,
        "overview":overview,
        "year": year,
        "rating": rating,
        "category":category
    })
    return movies