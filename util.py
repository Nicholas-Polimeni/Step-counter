from scipy.signal import butter, lfilter
import numpy

def vector_magnitude(data):
    """ function to calculate the magnitude of a vector

    Calculate the magnitude of the vector superposition of data (for
    example, acceleration) on x, y, and z axis

    Arguments:
        data: array of (x, y, z) tuples for a vector

    Returns:
        array of the magnitude of a vector

    """
    norms = []
    for each in data:
        norm = numpy.linalg.norm(each[1:], ord=2)
        norms.append(norm)
        
    return norms


def moving_average(data, window_size):
    """ moving average filter

    Implement a simple moving average filter to use as a low pass
    filter

    Arguments:
        data: data be filtered
        window_size: window_size chosen for the data

    Returns:
        The filtered data.

    TODO:
        Finish this function. Think about how you want to handle
        the size difference between your input array and output array.
        You can write it yourself or consider using numpy.convole for
        it:
        https://docs.scipy.org/doc/numpy/reference/generated/numpy.convolve.html

    """
    moving_averages = []
    magnitude = vector_magnitude(data)
    for i in range(len(magnitude) - window_size):
        avg = 0
        for y in range(window_size):
            avg += magnitude[i + y]
        avg = avg / window_size
        moving_averages.append(avg)
        
    return moving_averages
