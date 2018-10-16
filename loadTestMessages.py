import pika
import json
##import datetime
##import pypyodbc
##import sys

def getRbmqParam():
    with open('settingsProd.json') as fi:
        settings = json.load(fi)        
        username, password, hostname, port, vhost, rbmqqueue = settings.get('username'), settings.get('password'), settings.get('hostname'), settings.get('port'), settings.get('vhost'), settings.get('rbmqqueue')
        connectRBMQ(username, password, hostname, port, vhost, rbmqqueue)

def connectRBMQ(username, password, hostname, port, vhost, rbmqqueue):
    credentials = pika.PlainCredentials(username, password)
    parameters = pika.ConnectionParameters(hostname,
                                           port,
                                           vhost,
                                           credentials)    
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    with open('publishMessage.json') as fi1:
        queueNames = json.load(fi1)
        for queueName in queueNames:
                channel.basic_publish(exchange='',
                          routing_key= queueName,
                          body=
                          """
                            <command>
                            <type>Type</type>
                            <property>Property</property>
                            <value>"z_testing"</value>
                            </command>""")
                print("Message Sent for " + queueName)
    connection.close()

def main():
    getRbmqParam()

main()


##currentDate = datetime.datetime.now() - datetime.timedelta(days=1)
##eodDate = currentDate.strftime("%Y%m%d")
##print(eodDate)

##if len(sys.argv) == 2:
##    eodDate = sys.argv[1]

# channel.queue_declare creates the queues for you
# channel.queue_declare(queue = "z_test_message", durable = True)
# channel.queue_declare(queue = "z_test_message1", durable = True)
# channel.queue_declare(queue = "z_test_message2", durable = True)
# channel.queue_declare(queue = "queue4", durable = True)
# channel.queue_declare(queue = "queue5", durable = True)
# channel.queue_declare(queue = "queue6", durable = True)

# channel.basic_publish(exchange='',
#                       routing_key= "z_test_message1",
#                       body=
#                       """
#                         <command>
#                         <type>Type</type>
#                         <property>Property</property>
#                         <value>"cheesers!!!"</value>
#                         </command>""")
#     print("Message Sent2")

#     channel.basic_publish(exchange='',
#                           routing_key= "z_test_message2",
#                           body=
#                           """
#                             <command>
#                             <type>Type</type>
#                             <property>Property</property>
#                             <value>"cheeseys!!!"</value>
#                             </command>""")
#     print("Message Sent3")
#     channel.close()
