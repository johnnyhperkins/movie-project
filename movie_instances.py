import movie
import fresh_tomatoes
import tmdbsimple as tmdb
tmdb.API_KEY = "2e19bd4dddd47138cd8060d63194bc98"

## Get movie data from the API. Movie IDs can be found through the following search method:
## search = tmdb.Search()
## response = search.movie(query="shawshank")
## for s in search.results:
##    print(s['id'], s['title'])

cog_info = tmdb.Movies(598)
response = cog_info.info()

coadm_info = tmdb.Movies(4912)
coadm_response = coadm_info.info()

kkbb_info = tmdb.Movies(5236)
kkbb_response = kkbb_info.info()

nr_info = tmdb.Movies(18079)
nr_response = nr_info.info()

borat_info = tmdb.Movies(496)
borat_response = borat_info.info()

shawshank_info = tmdb.Movies(278)
shawshank_response = shawshank_info.info()

## Create instances
city_of_god = movie.Movie(cog_info.title, cog_info.tagline,"http://image.tmdb.org/t/p/w342"+cog_info.poster_path,"https://www.youtube.com/watch?v=ioUE_5wpg_E", cog_info.overview.encode('utf-8'))
confessions_of_a_dangerous_mind = movie.Movie(coadm_info.title, coadm_info.tagline,"http://image.tmdb.org/t/p/w342"+coadm_info.poster_path,"https://www.youtube.com/watch?v=xha4hZeXFtQ",coadm_info.overview.encode('utf-8'))
kiss_kiss_bang_bang = movie.Movie(kkbb_info.title, kkbb_info.tagline,"http://image.tmdb.org/t/p/w342"+kkbb_info.poster_path,"https://www.youtube.com/watch?v=K1xsTRG-O04",kkbb_info.overview.encode('utf-8'))
nueve_reinas = movie.Movie(nr_info.title, nr_info.tagline,"http://image.tmdb.org/t/p/w342"+nr_info.poster_path,"https://www.youtube.com/watch?v=Awu9WonTVB0",nr_info.overview.encode('utf-8'))
borat = movie.Movie(borat_info.title, borat_info.tagline,"http://image.tmdb.org/t/p/w342"+borat_info.poster_path,"https://www.youtube.com/watch?v=4_I3tIjztj8",borat_info.overview.encode('utf-8'))
shawshank = movie.Movie(shawshank_info.title, shawshank_info.tagline,"http://image.tmdb.org/t/p/w342"+shawshank_info.poster_path,"https://www.youtube.com/watch?v=6hB3S9bIaco", shawshank_info.overview.encode('utf-8'))

movies = [city_of_god, confessions_of_a_dangerous_mind, kiss_kiss_bang_bang, nueve_reinas, borat, shawshank]

## Run the open_movies function by passing the list of movie instances
fresh_tomatoes.open_movies_page(movies)
