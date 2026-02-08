import matplotlib.pyplot as plt


def plot(data):
    mean = data.mean()
    plt.plot(data)
    plt.title(f"mean = {mean}")
    plt.grid(True)
    plt.show()

