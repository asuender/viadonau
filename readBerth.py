import requests
import ssl
import json
from types import SimpleNamespace
import psycopg2

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

conn = psycopg2.connect("dbname='viadonau' user='viadonau' host='localhost' password='viadonau'")
cur = conn.cursor()	
#get current timestamp
cur.execute("SELECT NOW()")
timestamp = cur.fetchone() 
cur.execute("INSERT INTO berthMessage (timestamp) VALUES (%s)", (timestamp))
conn.commit()
for i in array:
    cur.execute("SELECT MAX(messageId) FROM berthmessage")
    messageId = cur.fetchone()
    cur.execute("INSERT INTO berth(messageId, locode) VALUES ({0},'{1}')".format(messageId[0],i.locode))
    
conn.commit()
cur.close()
conn.close()