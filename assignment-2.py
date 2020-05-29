#asssgnment-2 
#Kim Nikolas Fiedler - 431303
#Sarmad Rezayat- 515784

#######Task-3######### 
from functools import reduce
#a

def evenListMaker(n):
    return [a for a in list(range(n+1)) if (lambda a: a % 2 == 0)(a)]
print("Task 3 part a: \n",evenListMaker(10), "\n")

################################
##########alternative###########

def evenNumber(n):
    return list(filter(lambda a: a%2==0, range(n+1)))

print("Task 3 part a(the alternative): \n", evenNumber(10), "\n")

#b

inchToCm = lambda n: round(n * 2.45, 3)
l = [4, 4.5, 5, 5.5, 6, 7]
lengthList = list(map(inchToCm, l))
print("Task 13 part b: \n", lengthList, "\n")

#c

filterList = list(filter(lambda n: n >= 4 and n <=6, l))
print("Task 3 part c: \n", filterList, "\n")

#d

reducedList = reduce(lambda x, y: x+y, l)
print("Task 3 part d: \n", reducedList, " \n")

#######Task-4#########
import pandas as pd
import matplotlib.pyplot as plt


#a

movies = pd.read_csv('moviedata.csv')
print("Task 4 part a.1: \n", movies.shape, movies.columns, movies.info, "\n")
movies.describe()
print("Task 4 part a.2: \n", movies.head(5), movies.tail(5), "\n")

#b 

firstFiveColumn = movies[['duration', 'movie_title', 'num_voted_users']].head(5)
firstFiveColumn.describe()
print("Task 4 part b: \n", firstFiveColumn, "\n")

#c

moviesGenres = movies.filter(['movie_title', 'genres'])

actionsMovie = moviesGenres[moviesGenres['genres'].str.contains('Action')]
print("Task 4 part c: \n", actionsMovie.head(5), "\n")

#d

ratedMovies = movies.sort_values(by=['imdb_score'], ascending=False)
print("Task 4 part d: \n", ratedMovies[['movie_title', 'imdb_score']].head(10), "\n")

#e

pd.options.display.float_format = '{:,.1f}'.format
noNan = movies[movies.gross.notnull()]
directors = noNan.groupby(['director_name']).mean()
bestSeller = directors.sort_values(by = ['gross'], ascending=False )
print("Task 4 part e: \n", bestSeller[['gross']].head(10), "\n")

#f

na = movies.dropna()
na.shape
na.hist(['gross'], color = 'g')
plt.suptitle('Gross')
pd.plotting.scatter_matrix(na[['gross','duration','num_critic_for_reviews','imdb_score']], color = 'g')
plt.suptitle('Scatter matrix',alpha = 0.5)
plt.show()