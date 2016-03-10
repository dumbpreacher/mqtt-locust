
## Load test for AWS IoT applications using Locust.io and Paho MQTT client

This repo is based on code found originally <a href="https://github.com/ajm188/mqtt-locust" target="new">here</a>


### Dependencies

* Highly recommended to use virtualenv when installing and running this test.
* Python 2.7.9 or later. The code in this repo requires support for TLSv1.2, which is available starting in Python 2.7.9
* The code in this repo does NOT work with Python 3 due to Locust not supporting Python 3.
* GCC (GNU Compiler Collection), required by Locust: ```sudo yum install gcc```
* Locust: ```pip install locustio```
* OpenSSL v1.0.1 or greater (also due to TLSv1.2)
* Paho MQTT client: ```pip install paho-mqtt```


### mqtt_locust.py

This file contains logic to create an MQTT client, initiate a connection, publish messages
to a topic and subscribe to a topic. It also reports failure or success results to Locust.

At the time, it only supports QoS=0, which is what is needed for connecting to the AWS IoT
service.

Another important feature is the support for TLSv1.2, which is required by AWS IoT in order 
to establish a secure connection. You must create certificate files for AWS IoT, attach an 
IAM policy to them in AWS and your locust tests must indicate the location of the certificate
files in your system.

### aws-iot-publish.py

This file creates a basic locust test that publishes messages to an AWS IoT topic. The payload
is a random value between 0 and 10, which represents a temperature reading. 

### Certificates
Follow the instructions in the <a href="http://docs.aws.amazon.com/iot/latest/developerguide/secure-communication.html" target="new">AWS IoT documentation</a> in order 
to create certificate files. Follow the instructions <a href="http://docs.aws.amazon.com/iot/latest/developerguide/verify-pub-sub.html" target="new">here</a> to create a CA certificate. 
Set environment variables CA_CERT, IOT_CERT and IOT_PRIVATE_KEY with the full location of your .pem files

### Topics
Set the environment variable ```MQTT_TOPIC``` with the topic you want to publish messages to.


### Running the test

First you need to get the endpoint AWS IoT has assigned to your account, using the AWS CLI:
```aws iot describe-endpoint```

then run the locust command from your environment:

```locust --host=<my AWSIoT endpoint> -f aws-iot-publish.py```









 
