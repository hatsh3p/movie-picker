import csv
import random

def organize_movie_file(filename):
    with open(filename, newline='') as csvfile:
        moviereader = csv.DictReader(csvfile)
        movielist = []
        for row in moviereader:
            row = (row['Title'], ' | ',row['Category'], ' | ',row['Year'],' | ',row['Other Notes'])
            item = ''.join(row)
            movielist.append(item)
        return movielist

#print(organize_movie_file('sm_movie_list.csv'))

organizedmovielist = organize_movie_file('sm_movie_list.csv')

def pick_three_movies(list):
    return(random.sample(list, 3))

#print(movielist)

print(pick_three_movies(organizedmovielist))