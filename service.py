from urllib.parse import urlparse
import uuid

def is_url(url: str):
    """
    валидация ссылки
    """
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False

def generate_short_link(url: str):
    """
    функция, которая генерирует короткую ссылку
    """
    url = uuid.uuid4().hex
    return url[:10]
        
