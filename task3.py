from plot_data import plot_data
import parser_data

def count_steps(data):
    print("Accelerometer data graph")
    plot_data(data)
    num_steps = 0
    '''
    ADD YOUR CODE HERE. This function counts the number of steps in data and returns the number of steps
    '''
    data = moving_average(data, 50)
    avg_a = sum(data)/len(data)

    max_height = max(data)
    min_height = min(data)
    top_quarter = ((max_height - min_height) / 6) + avg_a
    peaks, _ = scipy.signal.find_peaks(data, height=top_quarter)
    num_steps = len(peaks)
    
    data = numpy.array(data)
    plt.plot(data)
    plt.plot(peaks, data[peaks], "x")
    plt.show()
    
    return num_steps


def main():
    # Get data   
    for i in [1,2]:
        file_name = f"walking_steps_{i}_clean.csv" 
        data = parser_data.get_data(file_name)
        number_of_steps = count_steps(data)
        print("Number of steps counted are : {0:d}".format(number_of_steps))


if __name__== "__main__":
    main()

