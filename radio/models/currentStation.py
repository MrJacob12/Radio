
class CurrentStation:
    def __init__(self, name, url, logo):
        self.name = name
        self.url = url
        self.logo = logo
    def set(self, name, url, logo):
        self.name = name
        self.url = url
        self.logo = logo
    def get(self):
        return self.name, self.url, self.logo
