#Create a dictionary of your favorite movies and their release years. Add a new movie to the 
#dictionary, update the release year of one of the movies, and remove a movie.

#creating dictionary of favorite movie list 
fav_movie = {'Avatar':2009, 'Harry Potter':2000, 'Jhola':2013}
#Now adding one move favorite movie in that list 
fav_movie['Kalki'] = 2024
#removing one movie from the list 
fav_movie.pop('Jhola')
#updating one moive release date
fav_movie['Harry Potter']=2001

#display 
for movie,year in fav_movie.items():
    print(f"{movie}:{year}")

