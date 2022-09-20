import numpy as np


def saveArray(data, filename):
    """
    slaat de data in een comma gescheiden bestand op.

    argumenten:
        data: 2d numpy array met data
        filename: string met de filenaam
    """

    np.savetxt(filename, np.column_stack(data), delimiter=",")
