import test_data
import json

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json(json_data):
    #Initialize a new GameLibrary
    game_library = test_data.GameLibrary()

    #Loop through the json_data
        #Create a new Game object from the json_data by reading
        #  title
        #  year
        #  platform (which requires reading name and launch_year)
        #Add that Game object to the game_library

    for game_name in json_data:
        game_data = json_data[game_name]

        # Make a new game
        game = test_data.Game()

        # Get data from current game
        game.title = game_data["title"]
        game.year = game_data["year"]

        platform = game_data["platform"]
        launch_year = platform["launch year"]
        name = platform["name"]

        new_platform = test_data.Platform(launch_year,name)

        game.platform = new_platform
        game_library.add_game(game)


    return game_library


#Part 2
input_json_file = "data/test_data.json"

with open("data/test_data.json", "r") as reader:
    test_json = json.load(reader)

game_data = make_game_library_from_json(test_json)
### Begin Add Code Here ###
#Open the file specified by input_json_file
#Use the json module to load the data from the file
#Use make_game_library_from_json(json_data) to convert the data to GameLibrary data
#Print out the resulting GameLibrary data using print()
### End Add Code Here ###
print (game_data)
