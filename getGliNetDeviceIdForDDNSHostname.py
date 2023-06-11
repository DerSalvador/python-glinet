import sys, time, datetime
from pyglinet import GlInet
glinet = GlInet()
glinet._keep_alive=False
glinet._keep_alive_intervall=0
glinet._password="Ades121204"
# glinet._url=
# glinet._username=
glinet._verify_ssl_certificate=False
glinet.login()
# glinet._url=
# glinet._username=
glinet._verify_ssl_certificate=False
glinet.login()
# Get current timestamp
current_timestamp = datetime.datetime.now()
# Convert timestamp to a string
timestamp_str = str(current_timestamp)

api= glinet.get_api_client()
print ("device_id=" + api.ddns.get_config().device_id)
