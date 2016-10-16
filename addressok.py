import urllib.parse
import urllib.request
import urllib
import json

# URL для запроса адреса
addressok_url = 'http://localhost:14000/'

def flaskImmutableMultiDictToDict(request_form):
    """Преобразует ImmutableMultiDict в обычный Python-словарь.
    Используется в микрофреймворке Flask."""
    res = {}
    for key in request_form.keys():
        res[key] = request_form[key]
    return res

def getAddress(addr_request):
    data = urllib.parse.urlencode(addr_request)
    data = data.encode('ascii')
    req = urllib.request.Request(addressok_url, data)
    response = urllib.request.urlopen(req)
    result = json.loads(response.read().decode('utf-8'))

    return result
