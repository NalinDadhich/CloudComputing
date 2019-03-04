from locust import HttpLocust, TaskSet

def index(l):
    l.client.get("/")

class UserBehavior(TaskSet):
    
    def on_start(self):
        index(self)

    def on_stop(self):
        index(self)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 0
    max_wait = 0