
import urllib.request
import xmltodict
import pprint

class ArxivClient(object):
    def __init__(self) -> None:
        self.url = "http://export.arxiv.org/api/query?start=0&max_results=10&search_query=all:"
        pass

    def query_arxiv(self, query):
        url_query = urllib.request.urlopen(self.url+query)
        xml_data = url_query.read().decode("utf-8")
        return xml_data
    
    def convert_xml(self, results):
        dades = xmltodict.parse(results)
        return dades

    def extract_data(self, data):
        results = []
        for e in data["feed"]["entry"]:
            title = e["title"]
            if len(e["author"]) > 1:
                authors = [a["name"] for a in e["author"]]
                authors = ",".join(authors)
            else:
                authors = e['author']["name"]
            results.append((title,authors))
        return results

    def get_data(self, query):
        # consultar API arxiv
        result_arxiv = self.query_arxiv(query)
        # convertir xml -> dades
        dades = self.convert_xml(result_arxiv)
        # reduir dades
        resultats = self.extract_data(dades)
        # return dades
        return resultats


if __name__=="__main__":
    client = ArxivClient()
    dades = client.get_data("transformers")
    pprint.pprint(dades)