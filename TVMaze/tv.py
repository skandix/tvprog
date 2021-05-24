import requests
import json

from time import sleep
from ics import Calendar, Event
from datetime import date
from loguru import logger as log

# TODO: Cleanup functions names
# TODO: Write docstrings for functions
# TODO: Cleanup the class variables
# TODO: Considering writing a parser to parse the data from the api and store in a json file as this will not cause the api to rate limit me when hoggin down lots of the same data i've downloaded 10-times from before.
# TODO: Cleanup the functions and 


class tvprog:
	def __init__(self):
		self.root_api = "http://api.tvmaze.com"
		self.calendar = "space.ics"
		self.t_year = int(date.today().strftime("%Y"))

	def get(self, route:str) -> dict:
		return requests.get(f"{self.root_api}{route}").json()

	def json_load(self):
		with open('./json/series.json') as file:
			return json.loads(file.read())

	def json_write(self, data:dict) -> dict:
		return json.dumps(data, indent=4)

	def get_shows(self, id:int) -> dict:
		return self.get(f'/shows/{id}')

	def get_single_search(self, show_name:str):
		return (self.get(f'/singlesearch/shows?q={show_name}'))
		
	def get_show_season(self, show_id:str):
		return self.get(f"/shows/{show_id}/seasons")

	def get_season_date(self, season_id:str):
		#URL: /seasons/:id/episodes
		return self.get(f"/seasons/{season_id}/episodes")

	def get_tv_episodes(self, tv_id:str):
		for season in (self.get_show_season(tv_id)):
			s_id = (season['id'])
			for episode in (self.get_season_date(s_id)):
				yield (episode)

	def diff_year(self, year_diff):
		return (int(year_diff.split('-')[0])>= self.t_year)

	def create_ics(self):
		# TODO: Cleanup messy function # HECK!!!

		c = Calendar()

		for show in self.json_load()['Shows']:
			#show = "The Simpsons"
			result = self.get_single_search(show)

			tv_id = (str(result['id']))
			tv_name = (str(result['name']))

			for ep_data in self.get_tv_episodes(tv_id):
				try:
					if ep_data['airtime'] != "":
						if (self.diff_year(ep_data['airdate'])): # if release is older than this year, we want to skip that.
							headline = f"{tv_name} - S{ep_data['season']}E{ep_data['number']}"
							e = Event()
							e.name = headline
							if str(ep_data['number']) == None:
								...

							e.begin = f"{ep_data['airstamp']}"
							e.duration = ({"minutes": ep_data['runtime']})
							e.description = ep_data['summary']
							c.events.add(e)
							log.info(f"Added Event {headline}")

							log.debug(f'Writing to {self.calendar}')
							with open(self.calendar, 'w', encoding='utf-8') as f:
								f.writelines(c)
							log.debug(f"Finished writing to {self.calendar}")

				except TypeError as Terror:
					log.error(f"Caugth Error {Terror} in {ep_data}")


if __name__ == '__main__':
	t = tvprog()
	#print (t.get_single_search("Legendary"))
	
	result = t.get_single_search("Legendary")

	tv_id = (str(result['id']))
	tv_name = (str(result['name']))

	for ep_data in t.get_tv_episodes(tv_id):
		print(ep_data)