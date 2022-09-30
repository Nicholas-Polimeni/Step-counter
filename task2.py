import parser_data
from plot_data import plot_data



def clean_data(data):
    print ("Write code to remove garbage data")


    print ("Create new file without garbage data and save it in data folder")
    file_name_clean = "walking_steps_clean.csv"
    if num is not None:
        file_name_clean = f"data/walking_steps_{num}_clean.csv" 
        with open(file_name_clean, "w") as f:
            f.write("time,X,Y,Z\n")
            # write your cleaned data to the file    
            start_index, end_index = -1, -1
            for i in range(len(data)):
                if data[i][0] > start_time and start_index == -1:
                    start_index = i
                if data[i][0] > end_time and end_index == -1:
                    end_index = i
#                 print(data[i])
            new_data = data[start_index:end_index]
            csv_writer = csv.writer(f)
            for each in new_data:
                csv_writer.writerow(each)




def main():
    # Get data    
    time_stamps = [(5.5, 73), (12.5, 81)]
    for i in [1,2]:
        file_name = f"walking_steps_{i}.csv" # Change to your file name 
        data = parser_data.get_data(file_name) #data -- time,X,Y,Z 
        clean_data(data, time_stamps[i-1][0], time_stamps[i-1][1], i)
        newdata = parser_data.get_data(f"walking_steps_{i}_clean.csv")
        
        # Plot original and clean data
        plot_data(data)
        plot_data(newdata)        


if __name__== "__main__":
    main()

