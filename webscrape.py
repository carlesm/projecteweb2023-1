
import urllib3


class WebScrape(object):

    def __init__(self) -> None:
        self.url = "https://www.99-bottles-of-beer.net/language-python-808.html"
        pass

    def get_web(self):
        # connectar http
        httppool = urllib3.PoolManager()
        # enviar peticio
        resposta = httppool.request("GET", self.url)
        # guardar html resposta
        self.html = resposta.data.decode("utf-8")
        

    def get_data(self):
        # descarregar web
        self.get_web()
        # llegir html
        # retornar dades
        pass


if __name__=="__main__":
    client = WebScrape()
    dades = client.get_data()
    print(dades)