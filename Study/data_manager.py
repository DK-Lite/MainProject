
# data set URL : https://grouplens.org/datasets/movielens/

ENCODING = "ISO-8859-1"

def load_movielens(path):
    movies = {}
    for line in open(path+'/movie.item', encoding = ENCODING):
        (id, title) = line.split('|')[0:2]
        movies[id] = title

    prefs = {}
    for line in open(path+'/movie.data', encoding = ENCODING):
        user, movie_id, rating, _ = line.split('\t')
        prefs.setdefault(user,{})
        prefs[user][movies[movie_id]] = float(rating)

    return prefs

prefs = load_movielens("data")
