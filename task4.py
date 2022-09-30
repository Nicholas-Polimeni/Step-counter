import parser_data
from plot_data import plot_data


def segment_climbing_walking(data):
    '''
    While collecting data on stairs there were times when you were also walking rather than climbing
    It is important to remove the parts from the data where you were walking in between the flight of stairs
    Write your own algorithm to find segments in data which corresponds to climbing only

    This functions returns
    List of tuples (x,y,z) which corresponds to climbing only.
    i.e. remove data points from the original data which corresponds to walking
    '''

    print ('segment_climbing_walking')
    plot_data(data)
    data = data[501:4398]
    mov_avg = moving_average(data, window_size = 40)
    
    # identify peaks
    bar = 1.5*sum(mov_avg)/len(mov_avg)
    peaks, _ = scipy.signal.find_peaks(mov_avg, height=bar)
    mov_avg = numpy.array(mov_avg)
    
    # find index interval that represents walking period
    cutoff = []
    for cluster in clusters:
        front, end = cluster[0], cluster[1]
        for i in range(1, len(mov_avg)):
            mid_i = end+i
            if mid_i == len(mov_avg) - 1 or (mov_avg[mid_i] < mov_avg[mid_i-1] and mov_avg[mid_i] < mov_avg[mid_i+1]):
                t = mid_i
                break

        for i in range(1, len(mov_avg)):
            mid_i = front-i
            if mov_avg[mid_i] < mov_avg[mid_i-1] and mov_avg[mid_i] < mov_avg[mid_i+1]:
                s = mid_i
                break
        cutoff.append((s, t))
        
    # cut walking period from data
    climb_data = []
    slice_i = 0
    for i in range(len(cutoff)+1):
        if i < len(cutoff):
            slice_j = cutoff[i][0]
        else:
            slice_j = len(cutoff) - 1
        climb_data += list(data[slice_i:slice_j])

        if i < len(cutoff):
            slice_i = cutoff[i][1]
            
    data = numpy.array(climb_data)

    return data


def count_steps(data):
    print ('count_steps')
    num_steps = 0
    '''
    This function counts the number of steps in data and returns the number of steps
    '''
    data = moving_average(data, window_size = 40)
    plt.plot(data)
    
    avg_a = sum(data)/len(data)
    peaks, _ = scipy.signal.find_peaks(data, height=avg_a)
    num_steps = len(peaks)
    
    data = numpy.array(data)
    plt.plot(data)
    plt.plot(peaks, data[peaks], "x")
    plt.show()
    
    return num_steps


def main():
    # Get data
    file_name = "climbing_steps.csv"  # Change this to your data file name
    data = parser_data.get_data(file_name)
    segmented_data = segment_climbing_walking(data)
    number_of_steps = count_steps(segmented_data)
    print ("Number of steps counted are :{0:d}".format(number_of_steps))


if __name__== "__main__":
    main()
