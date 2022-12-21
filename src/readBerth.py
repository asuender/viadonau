import requests
import ssl
import json
from types import SimpleNamespace

url = 'https://www.eurisportal.eu/visuris/api/Berths_v2/GetCompactBerths'

class TLSAdapter(requests.adapters.HTTPAdapter):

    def init_poolmanager(self, *args, **kwargs):
        ctx = ssl.create_default_context()
        ctx.set_ciphers('DEFAULT@SECLEVEL=1')
        kwargs['ssl_context'] = ctx
        return super(TLSAdapter, self).init_poolmanager(*args, **kwargs)

session = requests.session()
session.mount('https://', TLSAdapter())

res = session.get(url)
data = res.json()
d = json.dumps(data)
x = json.loads(d, object_hook=lambda d: SimpleNamespace(**d))
array=x.items
print(array)

