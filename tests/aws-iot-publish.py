import json
import random
import resource
import ssl
import time

from locust import TaskSet, task

from mqtt_locust import MQTTLocust

#this value is the number of seconds to be used to retry operations (valid for QoS >1)
RETRY = 5

#ms
PUBLISH_TIMEOUT = 10000
SUBSCRIBE_TIMEOUT = 10000

# _/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/
# Config section
CA_CERTS = "../certs/VeriSign-Class%203-Public-Primary-Certification-Authority-G5.pem"
CERTFILE = "../certs/thing-cert.pem"
KEYFILE = "../certs/thing-private-key.pem"
TOPIC = 'locust/thing/temperature'
# _/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/_/


class ThingBehavior(TaskSet):
    @task
    def pubqos0(self):
        self.client.publish(topic=TOPIC, payload=self.payload(), qos=0, name='publish:qos0:'+TOPIC, timeout=PUBLISH_TIMEOUT)

    def on_start(self):
        #allow for the connection to be established before doing anything (publishing or subscribing) to the MQTT topic
        time.sleep(5)


    def payload(self):
        payload = {
           'temperature': random.randrange(0,10,1) #set temperature between 0 and 10
           } 
        return json.dumps(payload)


"""
   Locust hatches several instances of this class, according to the number of simulated users
   that we define in the GUI. Each instance of MyThing represents a device that will connect to AWS IoT.
"""
class MyThing(MQTTLocust):
    ca_certs = CA_CERTS
    certfile = CERTFILE
    keyfile = KEYFILE
    task_set = ThingBehavior
    min_wait = 1000
    max_wait = 1500
    