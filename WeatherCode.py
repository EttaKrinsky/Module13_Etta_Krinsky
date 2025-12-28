import matplotlib.pyplot as plt

def read_weather_data(filename):
    #Lists are created to store data.
    months = []
    avg_highs = []
    avg_lows = []
    rainfall = []

    #Open and read file, skip the header
    with open("weather_data_flatbush.csv","r") as file:
        header = file.readline()

        #Loop through the file
        for line in file:
            line = line.strip()
            data = line.split(",")

            month = data[0]
            high = float(data[1])
            low = float(data[2])
            rain = float(data[3])

            #append the data to relevant lists
            months.append(month)
            avg_highs.append(high)
            avg_lows.append(low)
            rainfall.append(rain)
    #Return the lists
    return months, avg_highs, avg_lows, rainfall
#Similar code but for the other file
def read_extremes_data(filename):
    record_highs = []
    record_lows = []
    snowfall = []

    with open(filename, "r") as file:
        header = file.readline()

        for line in file:
            data = line.strip().split(",")

            record_highs.append(float(data[1]))
            record_lows.append(float(data[2]))
            snowfall.append(float(data[3]))

    return record_highs, record_lows, snowfall

def plot_avg_temps(months, avg_highs, avg_lows, colors):
    #Plot average high and low temperatures with markers
    plt.plot(months, avg_highs, 'o',linestyle = "-", label = "Average Highs")
    plt.plot(months, avg_lows, 'o', linestyle = "-", label = "Average Lows")

    #Title and Labels
    plt.title("Average Monthly Temperatures in Flatbush")
    plt.xlabel("Month")
    plt.ylabel("Temperature (°F)")
    plt.xticks(rotation = 45)
    plt.grid(True)
    #legend shows the line labels:
    plt.legend()

    plt.show()

def plot_snowfall(months, snowfall, colors):
    #Create a list of colors for each bar
    bar_colors =[]
    for i in range(len(months)):
        bar_colors.append(colors[i % len(colors)])

    plt.bar(months, snowfall, color = bar_colors)
    #Title and Axis Labels
    plt.title("Average Monthly Snowfall in Flatbush")
    plt.xlabel("Month")
    plt.ylabel("Snowfall (inches)")
    plt.xticks(rotation = 45)

    plt.show()


def calculate_temp_ranges(record_highs, record_lows):
    ranges = []
    #Calculates the temperature range (high-low) for each month
    for i in range(len(record_highs)):
        ranges.append(record_highs[i] - record_lows[i])

    return ranges

def print_insights(months, values, label):
    #Prints the month with the highest, lowest, and average values
    max_value = max(values)
    min_value = min(values)

    max_month = months[values.index(max_value)]
    min_month = months[values.index(min_value)]

    average = sum(values) / len(values)

    print(f"{label}")
    print(f"Highest Value Month: {max_month}")
    print(f"Lowest Value Month: {min_month}")
    print(f"Average Value: {round(average, 2)}")
    print()

def main():
    colors = ("#264653","#2a9d8f","#e9c46a","#f4a261","#e76f51")

    #Read the data
    months, avg_highs, avg_lows, rainfall = read_weather_data("weather_data_flatbush.csv")
    record_highs, record_lows, snowfall = read_extremes_data("flatbush_extremes.csv")

    #Plot Graphs
    plot_avg_temps(months, avg_highs, avg_lows, colors)
    plot_snowfall(months, snowfall, colors)

    #Calculate Temperature Ranges
    temp_ranges = calculate_temp_ranges(record_highs, record_lows)
    max_range = max(temp_ranges)
    max_range_month = months[temp_ranges.index(max_range)]

    #Print Insights
    print_insights(months, avg_highs, "Average High Temperatures")
    print_insights(months, snowfall, "Snowfall")

    print("Month with largest temperature range: ", max_range_month)

if __name__ == "__main__" :
    main()