import csv
import random

# FUNCTION 1: ORGANIZES CSV FILE INTO A LIST OF DICTIONARIES
def organize_csv_file(filename):
    with open(filename, newline='') as csvfile:
        csv_reader = csv.DictReader(csvfile)
        csv_list = [] # This is a list of dictionaries, each row is a dictionary
        for row in csv_reader:
            csv_list.append(row)
    return csv_list


# FUNCTION 2: FILTERS THE CSV FILE TO CREATE A NEW LIST OF DICTIONARIES THAT
# ONLY INCLUDES UNWATCHED MOVIES
def create_list_of_unwatched_movies(list):
    unwatched_movie_list = []
    for movie in list:
        movie_dict = movie
        for key in movie_dict:
            if key == 'Watched' and movie_dict[key] == 'No':
                unwatched_movie_list.append(movie_dict)
    return unwatched_movie_list



# FUNCTION 3: TAKES THE UNWATCHED MOVIE LIST AND MAKES IT PRETTY
def create_pretty_list(list):
    pretty_list = []
    for row in list:
        row = (row['Title'], ' | ',row['Category'], ' | ',row['Year'],' | ',row['Other Notes'])
        item = ''.join(row)
        pretty_list.append(item)
    return pretty_list


# FUNCTION 4: PICKS 3 RANDOMLY
def pick_three(list):
    return(random.sample(list, 3))


# FUNCTION 5: CALLS FUNCTIONS 1-4 
def pick_three_unwatched_movies():
    # movie_list is a list of dictionaries
    # Each item in the list is a dictionary 
    # The dictionary is organized as follows
    # {'Title' : 'some movie title', 'Category' : 'some movie category', 
    # 'Year' : 'XXXX', 'Other Notes': 'notes', 'Watched' : 'yesorno'}
    movie_list = []
    movie_list = organize_csv_file('sm_movie_list.csv')
    updated_movie_list = create_list_of_unwatched_movies(movie_list)
    pretty_list = create_pretty_list(updated_movie_list)
    three_movies = pick_three(pretty_list)
    for movie in three_movies:
        print(movie)

pick_three_unwatched_movies()
