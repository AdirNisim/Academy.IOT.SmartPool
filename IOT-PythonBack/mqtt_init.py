import socket
from firebase_admin import credentials

nb=1 # 0- HIT-"139.162.222.115", 1 - open HiveMQ - broker.hivemq.com
brokers=[str(socket.gethostbyname('vmm1.saaintertrade.com')), str(socket.gethostbyname('broker.hivemq.com'))]
ports=['80','1883']
usernames = ['MATZI',''] # should be modified for HIT
passwords = ['MATZI',''] # should be modified for HIT
broker_ip=brokers[nb]
port=ports[nb]
username = usernames[nb]
password = passwords[nb]
conn_time = 0 # 0 stands for endless
mzs=['matzi/','']
sub_topics =[mzs[nb]+'#','#']
pub_topics = [mzs[nb]+'test','test']

broker_ip=brokers[nb]
broker_port=ports[nb]
username = usernames[nb]
password = passwords[nb]
sub_topic = sub_topics[nb]
pub_topic = pub_topics[nb]



#Common
conn_time=0
comm_topic='hitpool/pool/all'
manag_time=10

# Limits
air_condition_limit = 30
water_tempature_limit = 16

#rates
update_rate = 5000 # in msec

#Db
cred = credentials.Certificate("HITPOOL.json") # Firebase cloud config (inisilized in manager)
