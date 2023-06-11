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
print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))
# Get current timestamp
current_timestamp = datetime.datetime.now()

# Convert timestamp to a string
timestamp_str = str(current_timestamp)

localip=sys.argv[1]
gatewayip=sys.argv[2]
api= glinet.get_api_client({'url':'http://' + gatewayip,'username':'admin','password':'Ades121204','keep_alive':'False'})
fw = api.firewall
print ("localip=" + localip)
for item in api.firewall.get_port_forward_list().res: print (item.name); api.firewall.remove_port_forward({'all': True});
api.ddns.set_config({'enable_ddns': True, 'enable_ssh_access': True, 'enable_http_access': True, 'enable_https_access': True})
fw.add_port_forward({'name': 'mac-' + timestamp_str, 'proto': 'tcp udp', 'src': 'wan', 'src_dport': 8081, 'dest': 'lan', 'dest_ip': localip, 'dest_port': 8081})
