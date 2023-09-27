# *************************************************************************************
# README:
# This python files creates the property data that gets passed to Reading.jinja
#    This allows the developer to create and manipulate the UI and the node
#    the user sees on the in-house tool.
# NOTE:
# To see the Reading node utilized in the Reading Activity, look at the
#    at the generated code in Generated-Reading-ReadingNode.top
# ( https://github.com/nhertanto/Embodied-Moxie/blob/main/Reading-Activity/Generated-Reading-ReadingNode.top )
# *************************************************************************************

import csv
import os

from ....... import CHATSCRIPT_ROOT
from .....logs import log
from ...flexible.flexible_node_data import FlexibleNodeData
from .active_listening1 import FlexibleActiveListening1

class FlexibleReading1(FlexibleActiveListening1):

    _NO_MOXIE_END_PATTERN = FlexibleNodeData.new_pattern_properties(
        displayed_name="End Pattern without Moxie",
        hint="Patterns that would end the reading experience, but without Moxie's name",
        pattern_jinja_name="no_moxie_end_pattern",
        required=True,
        name="noMoxieEndPatterns",
    )

    _BOOKS_SFX_SHEET = FlexibleNodeData.new_csv_properties(
        displayed_name="CSV File Path",
        hint="the csv file path containing the sheet with the sfx desired to play"
    )


    def __init__(self):
        super().__init__()
        self.name = "reading_node_v1"
        self.displayedName = "Module Specific/Reading"
        self.templateName = "Reading.jinja"
        self.outgoingConnectionIDs = [
        "End",
        "Exit"
        ]
        self.propertyDefinitions.extend(self._NO_MOXIE_END_PATTERN)
        self.propertyDefinitions.extend(self._BOOKS_SFX_SHEET)
        self.new_fallback_context_properties(defaultValue="SILENT", possibleValues=["SILENT"], noContext=True)

    def update_prop_dict(self, prop_dict, **kwargs) -> dict:

        for prop_def in self.propertyDefinitions:
            if prop_def.type == FlexibleNodeData.Property.PropertyType.CSV_RELATIVE_PATH:

                # If we don't have a csv file, throw an error
                if not prop_def.jinjaName in prop_dict:
                    raise Exception(f"The Reading node gently urges you to place a sheet in it -- {log.context(self.parent_element)}")

                else:
                    # Go through the csv file + needs the full filepath . . .
                    csv_full_path = os.path.join(CHATSCRIPT_ROOT, "chatscript", prop_dict[prop_def.jinjaName])
                    with open(csv_full_path, "r") as f:
                        csv_tags = f.readline()
                        csv_column_names = f.readline().strip().lower().split(",")

                    # . . . and ensure that the csv file have the following column names
                    hasKeyword = False
                    hasMarkup = False
                    hasKeywordType = False

                    for col in csv_column_names:
                        if col == "keywords":
                            hasKeyword = True
                        elif col == "markup":
                            hasMarkup = True
                        elif col == "type":
                            hasKeywordType = True

                    if not hasKeyword or not hasMarkup or not hasKeywordType:
                        errorMessage = "The csv file inside the Reading Node pleads with you to have these column(s) titled: "
                        if not hasKeyword:
                            errorMessage += "\n - 'Keywords' which has the patterns"
                        if not hasMarkup:
                            errorMessage += "\n - 'Markup' which has the markup"
                        if not hasKeywordType:
                            errorMessage += "\n - 'Type' which has the type of markup (ie. sfx, stinger, etc...)"
                        raise Exception(f" {errorMessage} -- {log.context(self.parent_element)}")

        return prop_dict

    @staticmethod
    def get_description():
        return f"""
        This Reading node was made specifically for the Reading module. This node features:
        - Turning on/off STT Partials
        - Users can input a sheet, and Moxie is able to detect the keywords/patterns from the sheet, and output markup
        - Allows for cooldown time in between keywords
        - Each keyword can only be said once.
        - Global commands are accessible
        - Mentor shouldn't be able to trigger politeness rules
        - Moxie should not fall asleep during this node.
        The file requires:
        - A column titled 'Keywords' which contains the patterns we are looking for
        - A column titled 'Markup' for each Keyword's markup
        - A column titled 'Type' that indicates what kind of markup it is (sfx, stinger, comment, etc)
        - NOTE: Type 'comment' are currently deprecated
        """
