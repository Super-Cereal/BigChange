import base64
from requests import get


geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
static_map_api_server = "http://static-maps.yandex.ru/1.x/"
geocoder_apikey = "40d1649f-0493-4b70-98ba-98533de7710b"


def get_ll(town):
    geo_params = {
        'geocode': town,
        'apikey': geocoder_apikey,
        'format': 'json'
    }
    geo_response = get(geocoder_api_server, params=geo_params)
    try:
        ll = geo_response.json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['Point']['pos']
    except Exception:
        return 0
    return ','.join(ll.split())


def get_map(ll):
    map_params = {
        'll': ll,
        'pt': f'{ll},pm2rdm',
        'l': 'sat',
        'z': 16,
        'size': '450,450'
    }
    map_response = get(static_map_api_server, params=map_params)
    return recode_image(map_response.content)


def recode_image(byte_image):
    image = base64.b64encode(byte_image)
    return image.decode('utf-8')
