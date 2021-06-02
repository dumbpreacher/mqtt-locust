import json
import random
import resource
import ssl
import time
import os

from locust import task, User
from locust.user.task import TaskSet

from mqtt_locust import MQTTLocust

#this value is the number of seconds to be used before retrying operations (valid for QoS >1)
RETRY = 5

#ms
PUBLISH_TIMEOUT = 10000
SUBSCRIBE_TIMEOUT = 10000


class ThingBehavior(TaskSet):
    @task
    def pubqos0(self):
        topic = 'test-topic'
        # if topic == '':
        #   raise ValueError("Please set environment variable MQTT_TOPIC")
        self.client.publish(topic, payload=self.payload(), qos=0, name='publish:qos0:'+topic, timeout=PUBLISH_TIMEOUT)

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
# class MyThing(MQTTLocust):
#     # ca_cert = os.getenv('CA_CERT','')
#     # iot_cert = os.getenv('IOT_CERT','')
#     # iot_private_key = os.getenv('IOT_PRIVATE_KEY','')
#     # if ca_cert == '' or iot_cert == '' or iot_private_key == '':
#     #   raise ValueError("Make sure the following environment variables are set: CA_CERT, IOT_CERT, IOT_PRIVATE_KEY")
#     tasks = [ThingBehavior]
#     min_wait = 1000
#     max_wait = 1500
    