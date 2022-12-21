import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

url = "http://10.2.24.50:18086"
token = "98d6ecce53492f2051067df3ce7198b3fef208500deeabc0f91c6f90fd5f1f80"
org = "org"
bucket = "doris"

client = influxdb_client.InfluxDBClient(
   url=url,
   token=token,
   org=org
)


