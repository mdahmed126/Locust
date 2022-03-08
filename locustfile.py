from locust import HttpUser, constant, task


class HelloWorld(HttpUser):

    wait_time = constant(1)
    #host = "https://petstore.octoperf.com"
    host = "https://britannia-admin-portal.dev.actyv.com/"

    @task
    def test(self):
        self.client.get("/")

