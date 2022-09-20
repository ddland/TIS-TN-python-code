#!/usr/bin/env python3

if __name__ == "__main__":
    import matplotlib.pyplot as plt
    from TN_code.hardware import lees_data_numpy

    # data van 1 kanaal weergeven
    fn = "filename.txt"
    data = lees_data_numpy.readArray(fn)
    time = data[:, 0]
    print("Samplerate: ", len(time) / (time[-1] - time[0]))
    plt.plot(time, data[:, 1])
    plt.show()
