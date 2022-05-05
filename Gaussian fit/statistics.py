import pandas
from scipy import stats
from matplotlib import pyplot as plt


def get_p_value(data):
    return stats.kstest(data, 'norm', (data.mean(), data.std()), N=len(data))[1]


def get_plot(data):
    data.plot.kde()
    plt.savefig('input_data.jpg')


data_df = pandas.read_csv("input_data.csv")
get_plot(data_df)
