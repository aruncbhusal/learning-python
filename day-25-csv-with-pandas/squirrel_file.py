# The challenge this time is to use a csv from a 2018 central park squirrel census
# Which has a fairly large amount of data, and create another csv from it.
# The csv contains details about how many squirrels there are in the park with a
# particular fur color. We need to make a list of all colors and their counts
    # import pandas

    # squirrel_data = pandas.read_csv("day-25-csv-with-pandas\central-park-squirrel-census-data.csv")
    # # We need data from the primary fur color attribute only so let's separate that
    #             # fur_color = squirrel_data["Primary Fur Color"]
    #             # color_list = fur_color.to_list()
    # # Rather, we can just get the list of all rows with the fur colors as given by just using
    # # the row extraction statement inside the for loop
    # fur_data = {}
    # fur_list = ["Gray", "Cinnamon", "Black"]
    # color_list = []
    # for _ in fur_list :
    #     color_list.append(squirrel_data[squirrel_data["Primary Fur Color"] == _ ])
    #     count = len(color_list[-1])
    #     # Since the rows returned act as iterables, we can just count their numbers
    #     fur_data[fur_list.index(_)] =[ _ , count]

    # fur_dataframe = pandas.DataFrame(fur_data)
    # fur_dataframe.to_csv("day-25-csv-with-pandas/fur_data.csv")

# Instead of doing this incomprehensible pile of nothing, the method in the course looks neater
import pandas

squirrel_data = pandas.read_csv("day-25-csv-with-pandas\central-park-squirrel-census-data.csv")
gray_squirrels = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])
black_squirrels = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [gray_squirrels, cinnamon_squirrels, black_squirrels]
}
data = pandas.DataFrame(data_dict)
data.to_csv("day-25-csv-with-pandas/fur_color_clean.csv")