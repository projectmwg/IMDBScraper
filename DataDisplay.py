import pandas as pd
import matplotlib.pyplot as plt

def plot_scores():

    fig, axes = plt.subplots(nrows = 1, ncols = 3, figsize = (16, 4))
    ax1, ax2, ax3 = fig.axes

    movie_ratings = pd.read_csv('movie_ratings.csv')

    ax1.hist(movie_ratings['imdb'], bins = 10, range = (0, 10))
    ax1.set_title('IMDB Rating')

    ax2.hist(movie_ratings['metascore'], bins = 10, range = (0, 100))
    ax2.set_title('Metascore')

    ax3.hist(movie_ratings['n_imdb'], bins = 10, range = (0, 100), histtype = 'step')
    ax3.hist(movie_ratings['metascore'], bins = 10, range = (0, 100), histtype = 'step')
    ax3.legend(loc = 'upper left')
    ax3.set_title('The Two Normalized Distributions')

    for ax in fig.axes:
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

    plt.show()
