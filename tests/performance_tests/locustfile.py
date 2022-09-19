from locust import HttpUser, task


valid_email = "admin@irontemple.com"
club = "Simply Lift"
competition = "Spring Festival"
places_bought = 2
occurences = 1


class ProjectPerfTest(HttpUser):

    @task(occurences)
    def index(self):
        self.client.get("/")

    @task(occurences)
    def showSummary(self):
        self.client.post('showSummary', data={'email': [valid_email]})

    @task(occurences)
    def logout(self):
        self.client.get("logout")

    @task(occurences)
    def clubsTable(self):
        self.client.get("clubs")

    @task(occurences)
    def purchasePlace(self):
        self.client.post('purchasePlaces',
                         data=dict(club=club,
                                   competition=competition,
                                   places=places_bought))
