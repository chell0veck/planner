import datetime
import matplotlib.pyplot as plt

def feb_plain_model():
    dates = [datetime.date(2019, 2, 1) + datetime.timedelta(i) for i in range(30)]
    parts = [dates[:i] for i in range(1, len(dates))]
    hols = [len([a for a in v if a.weekday() in (5, 6)]) for v in parts]
    work = [len([a for a in v if a.weekday() not in (5, 6)]) for v in parts]
    days = [len(part) for part in parts]
    div = [round(a/b, 2)for a, b in zip(hols, days)]
    div_zoom = [a * 30 for a in div]

    fig = plt.figure(figsize=(12, 8), dpi = 100)
    ax = fig.add_subplot(111)
    plt.plot(days, div_zoom, 'g-', label='x30 zoomed plain efficiency', linewidth=3)
    plt.plot(days, div, 'g-', label='plain efficiency', linewidth=1)
    plt.plot(days, hols, 'b-', label='holidays', linewidth=1)
    plt.plot(days, work, 'r-', label='working days', linewidth=1)

    ax.set_yticks(list(range(0, 30, 1)))
    ax.set_xticks(list(range(0, 30, 1)))


    ax.grid(which='major', alpha=1)

    ax.set_xlabel('days')
    ax.set_ylabel('days')


    plt.legend(loc='upper left')

    plt.show()


feb_plain_model()