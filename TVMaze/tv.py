import requests
import json


class tvMaze:
    def __init__(self):
        self.root_api = "http://api.tvmaze.com"
        self.get = lambda route: requests.get(f"{self.root_api}{route}").json()
        self.shows = ['Young Sheldon, ']

    def json_load(self):
        with open('./json/series.json') as file:
            return json.loads(file.read())

    def json_write(self, data, file_name="metadata") -> dict:
        return json.dumps(data, indent=4)

    def pp_json(self, data: dict) -> dict:
        return json.dumps(data, indent=4)

    # TVMaze LOGIC

    def get_shows(self, id:int) -> dict:
        return (self.get(f'/shows/{id}'))

    def get_single_search(self, show_name):
        return (self.get(f'/singlesearch/shows?q={show_name}'))
    
    def get_lookup(self,shows)


#print (tvprog().search("Young Sheldon"))

"""
for j in tvMaze().json_load()['Shows']['Norwegian']:
    print (tvMaze().search(j))
    print ("\n")
"""