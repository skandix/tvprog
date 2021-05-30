# Shows

## Show main information
### URL: /shows/:id
### Example: http://api.tvmaze.com/shows/1
### Example: http://api.tvmaze.com/shows/1?embed=cast

## Show episode list
### URL: /shows/:id/episodes
### (optional) specials: do include both significant and insignificant specials in the list
### Example: http://api.tvmaze.com/shows/1/episodes
### Example: http://api.tvmaze.com/shows/1/episodes?specials=1

## Show alternate lists
### URL: /shows/:id/alternatelists
### Example: http://api.tvmaze.com/shows/180/alternatelists

### URL: /alternatelists/:id
### Example: http://api.tvmaze.com/alternatelists/1
### Example: http://api.tvmaze.com/alternatelists/1?embed=alternateepisodes

### URL: /alternatelists/:id/alternateepisodes
### Example: http://api.tvmaze.com/alternatelists/1/alternateepisodes
### Example: http://api.tvmaze.com/alternatelists/1/alternateepisodes?embed=episodes
