

class ArxivClient(object):
    def __init__(self) -> None:
        self.url = "http://export.arxiv.org/api/query?start=0&max_results=1&search_query=all:"
        pass

    def get_data(self):
        # consultar API arxiv
        # convertir xml -> dades
        # reduir dades
        # return dades
        pass


if __name__=="__main__":
    client = ArxivClient()
    dades = client.get_data("transformers")
    print(dades)