import json
## Open the JSON file of movie data
movies = open("./movies.json", encoding="utf8")
## create variable "data" that represents the enitre movie list
data = json.load(movies)

# file 1 
""" for movies in data:
    print(movies['title']) """

#file 2
""" gah = int(input('year? :')) 
for tah in data:
    if gah < tah['year']:
        print(tah['title'], tah['year']") """

""" #file 3
low = int(input('lb?:'))
uppa = int(input('ub?:'))
for tree in data:
    if (tree['year'] > low) and (tree['year']  < uppa):
        print(tree['title'], tree['year']) """

#file4 
""" ball = int(input('when?:'))
for smth in data:
    if ball == smth['year']:
        print(smth['title'], smth['year'])  """

#file5
""" ti = input('write :') 
def find(x):
    for g in data:
        if x.lower() in g['title'].lower():
            print(g['title'])
find(ti) """

#file6 genre
billy = input('genre? :')
def gen(x):
    for la in data:
        for things in la['genres']:
            if things in la['genres']:
                print(la['title'])
gen(billy) 