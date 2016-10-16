# coding: utf-8
import urllib, urllib2
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
    data = urllib.urlencode(addr_request)
    req = urllib2.Request(addressok_url, data)
    response = urllib2.urlopen(req)
    result = json.loads(response.read().decode('utf-8'))

    return result
