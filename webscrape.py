
import urllib3
import bs4


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
        
    def parse_bs4(self):
        soup = bs4.BeautifulSoup(self.html, features="html.parser")
        div_main = soup.find_all('div', attrs={"id":"main"})[0]
        self.data = div_main.find_all('pre')[0]
        
    def extract_data(self):
        self.data = self.data.text

    def parse_html(self):
        # parse bs4
        self.parse_bs4()
        # extraure dades html
        self.extract_data()


    def get_data(self):
        # descarregar web
        self.get_web()
        # llegir html
        self.parse_html()
        # retornar dades
        pass


if __name__=="__main__":
    client = WebScrape()
    dades = client.get_data()
    print(dades)