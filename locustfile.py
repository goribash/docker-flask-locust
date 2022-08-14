from locust import HttpUser, Task, between

def index(l):
    l.client.get("/")

class UserBehavior(Task):
    tasks = {index: 1}

class WebsiteUser(HttpUser):
    task = UserBehavior
    wait_time = between(5.0, 9.0)