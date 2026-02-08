import matplotlib.pyplot as plt


def hist(data):
    mean = data.mean()
    plt.hist(data, bins=20)
    plt.title(f"mean = {mean}")
    plt.grid(True)
    plt.show()

