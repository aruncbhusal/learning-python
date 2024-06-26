# In today's lesson, we will be learning how to work with csv files
# CSV (Comma Separated Values) is a way to store data in rows, each data
# in a row being separated by a comma. That way multiple data can be represented

# We have a file called weather-data.csv, which we will first open like what
# we learned in the last lesson and get all the data into a list since they are
# separated by a newline character anyway

            # with open("day-25-csv-with-pandas\weather-data.csv") as weather:
            #     data_list = weather.readlines()
# We could do that, but we still have comma separated string after we extract this
# But there's a more convenient way to make use of this data: Using csv

# csv is a built in library in Python that can let us handle data files
        # import csv

        # with open("day-25-csv-with-pandas\weather-data.csv") as data_file:
        #     data = csv.reader(data_file)
        #     # This creates a csv reader object which can be looped through to see all items
        #     # A challenge is to get all temperature values from this file into a list
        #     temp = []
        #     for row in data:
        #         if row[1] != 'temp':
        #             temp.append(int(row[1]))
        #     print(temp)
    # Okay looks like my code was identical to the course
# Just to extract one single column of data, we had to go through such troubles,
# even with the inbuilt csv library.

# So instead, we use Pandas, a very powerful library used for data analysis in Python
# It is not built in so we need to install first. Docs at https://pandas.pytdata.org
import pandas

data= pandas.read_csv("day-25-csv-with-pandas\weather-data.csv")
# print(data) will print the csv in a beautiful tabular format
print(data["temp"])
# Just 3 lines above are enough and look better than all that we did with csv library
# If we use type(data) we can see the data type is "DataFrame"
# In pandas, a whole table is called a dataframe, and a single column (1-Dimensional)
# is called a series. if we checked type of data["temp"] it would return as "series"

# In the Pandas docs https://pandas.pydata.org/docs/reference/index.html for DataFrame
# We can see that we can convert a dataframe to any format like excel, csv or even dictionary
data_dict = data.to_dict()
print(data_dict)
# Similarly, in the Series docs, we can convert it into a list as well:
temp_list = data["temp"].to_list()
print(temp_list)

# The next challenge was to calculate the average temperature. Since we already have a list
average_temp = sum(temp_list)/len(temp_list)
# Instead, we could simply use mean() from the pandas series docs:
average_temp = data["temp"].mean() 
print(f"Average temperature: {round(average_temp,2)}")
# The next challenge was to get the max value in this series, using a series method
max_temp = data["temp"].max()
print(f"Max temp: {max_temp}")

# Rather than using the dictionary notation to get the data like in 'data["temp"]'
# we can instead use the name of the first row element as an attribute for the object
print(data.condition)
# This returns the series "conditions" as seen in the csv. It could also be written as
# print(data["conditions"]), this is neater. Both are case sensitive though

# In order to get a row from the data, we must check for a condition
print(data[data.day == "Tuesday"])
# It selects the column "day" and returns data from where the day is "Tuesday"

# Next challenge is to print the data for the day where temperature is maximum
print(data[data.temp == data.temp.max()])
# We are basially filtering the table this way
# While using rows, a neat thing is that we can use it as a shortened DataFrame
monday = data[data.day == "Monday"]
# A challenge was to convert Monday's temperature to fahrenheit
print(f"Temperature on Monday in Fahrenheit: {monday.temp[0]*9/5 +32}")
# The [0] will let us take a single value from a series

# We can instead create our own DataFrame from scratch rather than getting from a csv
# Say we have a random dictionary we want to convert into a csv
fruit_price = {
    "fruit" : ['Nepal', 'USA', 'India'],
    "apple" : [360, 450, 280],
    "mango" : [120, 180, 80],
    "grapes" : [180, 250, 160],
    "guava" : [60, 140, 40]
}
price_data = pandas.DataFrame(fruit_price)
price_data.to_csv("day-25-csv-with-pandas/fruit-price.csv")
# This just takes an argument of the location to save the converted csv file