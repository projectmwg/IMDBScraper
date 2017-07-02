from requests import get
from bs4 import BeautifulSoup
import pandas as pd
from time import time
from time import sleep
from random import randint
from IPython.core.display import clear_output
from warnings import warn

def make_request():

    pages = [str(i) for i in range(1, 5)]
    years_url = [str(i) for i in range(2000, 2018)]

    names = []
    years = []
    imdb_ratings = []
    metascores = []
    votes = []

    start_time = time()
    requests = 0

    for year_url in years_url:

        for page in pages:

            response = get('http://www.imdb.com/search/title?release_date=' + year_url + '&sort=num_votes,desc&page=' + page)

            sleep(randint(8, 15))

            requests += 1
            elapsed_time = time() - start_time
            print('Request: {}; Frequency: {} requests/s'.format(requests, requests / elapsed_time))
            clear_output(wait = True)

            if response.status_code != 200:
                warn('Request: {}; Status Code: {}'.format(requests, response.status_code))

            if requests > 72:
                warn('Number of requests was greater than expected.')
                break

            page_html = BeautifulSoup(response.text, 'html.parser')

            movie_containers = page_html.find_all('div', class_ = 'lister-item mode-advanced')

            for container in movie_containers:
                if container.find('div', class_ = 'ratings-metascore') is not None:
                    name = container.h3.a.text
                    names.append(name)

                    year = container.h3.find('span', class_ = 'lister-item-year').text
                    years.append(year)

                    imdb_rating = float(container.strong.text)
                    imdb_ratings.append(imdb_rating)

                    metascore = int(container.find('span', class_ = 'metascore').text)
                    metascores.append(metascore)

                    vote = int(container.find('span', attrs = {'name':'nv'})['data-value'])
                    votes.append(vote)

    movie_ratings = pd.DataFrame({'movie': names,
                            'year': years,
                            'imdb': imdb_ratings,
                            'metascore': metascores,
                            'votes': votes})
    movie_ratings = movie_ratings[['movie', 'year', 'imdb', 'metascore', 'votes']]
    movie_ratings.loc[:, 'year'] = movie_ratings['year'].str[-5:-1].astype(int)
    movie_ratings['n_imdb'] = movie_ratings['imdb'] * 10
    movie_ratings.to_csv('movie_ratings.csv')
