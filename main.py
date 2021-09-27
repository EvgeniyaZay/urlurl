from service import generate_short_link, is_url
from fastapi import FastAPI
from database.models import Item, write_data_db, get_links

app = FastAPI()

# hello world, метод GET, возврат строки
@app.get("/")
def hello():
    return "Hello World!"

@app.post("/short_link/")
def get_short_link(item: Item):
    """
    функция, которая получает длинную ссылку, возвращает короткую
    """
    short_url = is_url(item.url)
    if short_url :
        short_url = generate_short_link(item.url)
        write_data_db(item.url, short_url)
    url_short_url = f"{short_url}" 
    return {"url": url_short_url}
    
@app.post("/short_link/{short_url}")
def redirect(short_url: str):
    """
    функция, которая возвращает полную ссылку, получив короткую, редирект
    """
    long_url = get_links(code=short_url)
    return {"url": long_url[0]} 

# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=8000)    



        
         
