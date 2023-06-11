import sys
from pyglinet import GlInet
glinet = GlInet()
glinet.login()
api= glinet.get_api_client({'url':'http://192.168.8.1','username':'admin','password':'Ades121204','keep_alive':'False'})
fw = api.firewall
print ('Number of arguments:', len(sys.argv), 'arguments.')
print ('Argument List:', str(sys.argv))
localip=sys.argv[1]
print ("localip=" + localip)
for item in api.firewall.get_port_forward_list().res: print (item.name); api.firewall.remove_port_forward({'all': True});
fw.add_port_forward({'name': 'mac1', 'proto': 'tcp udp', 'src': 'wan', 'src_dport': 8081, 'dest': 'lan', 'dest_ip': '192.168.8.106', 'dest_port': 8081})
