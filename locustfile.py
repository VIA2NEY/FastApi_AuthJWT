from locust import HttpUser, task, between

class FastAPIUser(HttpUser):
    wait_time = between(1, 5)

    def on_start(self):
        # Connexion et obtention du token
        response = self.client.post("/auth/token", data={"username": "johndoe", "password": "secret"})
        self.token = response.json()["access_token"]
        self.headers = {"Authorization": f"Bearer {self.token}"}

    @task
    def get_dishes(self):
        self.client.get("/api/plat")

    @task
    def get_dish(self):
        self.client.get("/api/plats/Salad")

    @task
    def create_dish(self):
        payload = {
            "name": "Pasta",
            "description": "Delicious pasta with tomato sauce",
            "price": 9.99
        }
        self.client.post("/api/new_plat", json=payload, headers=self.headers)

    @task
    def update_dish(self):
        payload = {
            "description": "Updated description",
            "price": 11.99
        }
        self.client.put("/api/update_plat/Pasta", json=payload, headers=self.headers)

    @task
    def delete_dish(self):
        self.client.delete("/api/delete_plat/Pasta", headers=self.headers)
