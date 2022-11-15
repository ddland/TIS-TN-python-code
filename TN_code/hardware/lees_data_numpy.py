import numpy as np


def readArray(filename):
    """
    lees een door saveArray opgeslagen array weer uit

    arugmenten:
        filename: filenaam waar de data staat
    """
    data = np.loadtxt(filename, unpack=False, delimiter=",")
    return data


if __name__ == "__main__":
    # module wordt uitgevoerd
    import matplotlib.pyplot as plt

    # data van 1 kanaal weergeven
    fn = "meting_test1_1603898691.txt"
    data = readArray(fn)
    time = data[:, 0]
    plt.plot(time, data[:, 1])
    plt.show()
