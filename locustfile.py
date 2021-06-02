from locust import HttpUser, TaskSet

def index(l):
    l.client.get("/")

class UserBehavior(TaskSet):
    tasks = {index:1}

def on_start(self):
    index(self)

# class WebsiteUser(HttpUser):
#     task_set = UserBehavior
#     min_wait=1000
#     max_wait=2000
