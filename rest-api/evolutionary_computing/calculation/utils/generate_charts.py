import statistics

from matplotlib import pyplot as plt


def make_chart(calculation_result):
    epoch = []
    value = []
    for i in calculation_result:
        epoch.append(i[0])
        value.append(i[3])

    plt.figure(figsize=(7, 4), dpi=200)
    plt.title("Wartosc funkcji od kolejnej iteracji")
    plt.xlabel('Ilosc epok')
    plt.ylabel('Wartosc funkcji')
    plt.plot(epoch, value, label='f(x,y)', color='red', linewidth=2)
    plt.legend()
    plt.savefig('wartosc_funkcji', dpi=250)
    plt.show()
    return epoch, value


def save_charts(values):
    plt.figure(figsize=(7, 4), dpi=200)
    plt.title("Srednia wartosc funkcji oraz odchylenie standardowe")
    plt.ylabel('Ilosc epok')
    plt.xlabel('Wartosc funkcji')

    plt.hist(values, bins=50, color='c', edgecolor='k')
    m = statistics.mean(values)
    sd = statistics.stdev(values)

    plt.axvline(m, color='k', linestyle='dashed')
    plt.axvline(m + sd, color='y', linestyle='dashed')
    plt.axvline(m - sd, color='y', linestyle='dashed')
    plt.savefig('srednia_wartosc_odchylenie_standardowe', dpi=250)
    plt.show()
