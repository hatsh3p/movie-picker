import csv
import random

def organize_movie_file(filename):
    list = []
    with open(filename, newline='') as csvfile:
        moviereader = csv.DictReader(csvfile)
        for row in moviereader:
            list.append(row['Title']) 
    return list 
        
# Can add other categories later - Version 2!
# 'Year: ', row['Year'], 'Other notes: ', row['Other notes:'])

movielist = organize_movie_file('sm_movie_list.csv')

def pick_three_movies(list):
    return(random.sample(list, 3))

#print(movielist)
#print(pick_three_movies(movielist))
