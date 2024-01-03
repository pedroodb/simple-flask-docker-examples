from locust import HttpUser, task, between

class BasicUser(HttpUser):
    wait_time = between(1, 5)

    @task(1)
    def index(self):
        self.client.get("/")

    @task(3)
    def sum(self):
        self.client.post("/api/sum", json={'num1': 1, 'num2': 2})
