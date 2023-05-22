from locust import HttpUser, task, between

class BasicUser(HttpUser):
    wait_time = between(1, 5)
    
    @task
    def index(self):
        self.client.get("/")
        

    @task
    def sum(self):
        self.client.post("/sum", name="sum", json={'num1': 1, 'num2': 2})
    