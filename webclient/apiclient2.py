import requests
import json
import pprint

class ArxivClient(object):
    def __init__(self) -> None:
        self.url1 = "https://api.ipify.org/?format=json"
        self.url2 = "https://ipinfo.io/"
        self.url2_suffix = "/geo"
        

    def query_json(self, url):
        resultat = requests.get(url)
        dades = json.loads(resultat.text)
        return dades
    
    def query_myip(self):
        dades = self.query_json(self.url1)
        return dades["ip"]

    def query_ipinfo(self, ip):
        dades = self.query_json(self.url2+ip+self.url2_suffix)
        return dades

    def get_data(self, query):
        # consultar meva IP
        myip = self.query_myip()
        # consultar info IP
        dades = self.query_ipinfo(myip)
        # extract dades
        # resultats = self.extract_data(dades)
        # return dades
        return dades


if __name__=="__main__":
    client = ArxivClient()
    dades = client.get_data("transformers")
    pprint.pprint(dades)