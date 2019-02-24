import cc_dat_utils
import cc_data
import json

#Part 3
#Load your custom JSON file
#Convert JSON data to cc_data
#Save converted data to DAT file

def make_CC_data_from_JSON(json_data):

    CCData = cc_data.CCDataFile()

    for game_level in json_data:

        # Make a new CCLevel
        level = cc_data.CCLevel()

        # Get data from current level
        level.level_number = game_level["level_number"]
        level.time = game_level["time"]
        level.num_chips = game_level["num_chips"]
        level.upper_layer = game_level["upper_layer"]

        # Retrieve data from optional fields
        optional_fields = game_level["optional_fields"]
        for field in optional_fields:
            if field["type_val"] == 3:
                init_field = cc_data.CCMapTitleField(field["title"])
            elif field["type_val"] == 4:
                coordinates = []
                for val in field["traps"]:
                    init_coord = cc_data.CCTrapControl(val[0], val[1], val[2], val[3])
                    coordinates.append(init_coord)
                init_field = cc_data.CCTrapControlsField(coordinates)
            elif field["type_val"] == 5:
                coordinates = []
                for val in field["clones"]:
                    init_coord = cc_data.CCCloningMachineControl(val[0], val[1], val[2], val[3])
                    coordinates.append(init_coord)
                init_field = cc_data.CCCloningMachineControlsField(coordinates)
            elif field["type_val"] == 6:
                init_field = cc_data.CCEncodedPasswordField(field["pass"])
            elif field["type_val"] == 7:
                init_field = cc_data.CCMapHintField(field["hint"])
            elif field["type_val"] == 10:
                coordinates = []
                for val in field["monsters"]:
                    init_coord = cc_data.CCCoordinate(val[0], val[1])
                    coordinates.append(init_coord)
                init_field = cc_data.CCMonsterMovementField(coordinates)
            level.add_field(init_field)
        CCData.add_level(level)
    print (CCData)
    return CCData

with open("data/joannele_cc1.json", "r") as reader:
    format_json = json.load(reader)

CCData = make_CC_data_from_JSON(format_json)
dat_file = "data/joannele_cc1.dat"
cc_dat_utils.write_cc_data_to_dat(CCData, dat_file)