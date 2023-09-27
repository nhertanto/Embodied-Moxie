# *************************************************************************************
# README:
# This python files creates the property data that gets passed to ShowDrawing.jinja
#    This allows the developer to create and manipulate the UI and the node
#    the user sees on the in-house tool.
# NOTE:
# To see the Show Drawing node utilized in the Making Friends mission, look at the
#    at the generated code in Generated-MakingFriendsMission-drawing.top
# ( https://github.com/nhertanto/Embodied-Moxie/blob/main/Daily-Missions/Generated-MakingFriendsMission-drawing.top )
# *************************************************************************************

import logging
from .....logs import log
from ...flexible.flexible_node_data import FlexibleNodeData
from .polar1 import FlexiblePolar1

class FlexibleShowDrawing1(FlexiblePolar1):
    def __init__(self):
        super().__init__()

        _SHOW_MOVE_ON = FlexibleNodeData.new_move_on_properties(
            move_on_name="showDrawing",
            jinja_name="show_drawing_move_on_topic",
            displayed_name="Show Drawing Move On Topic Name",
            hint="When user Shows their Drawing we will move to the specified node.",
            required=False,
            text_jinja_name="show_drawing_text",
            pattern_jinja_name="show_drawing_pattern",
            pattern="(^globalPattern_lookAtBot()) ([ here look there] *~3 {~botname} >) ([I we he she they] *~3 [draw did ~complete made] ) ([here this be it Hughes] *~3 [(it be) letter poem write list story paper picture ~draw art work]) ([I we she he they] *~4 hold) (front *~4 [you ~botname]) (do *~1 [you ~botname] *~4 [~watch ~like think ]) (right [here there] {~botname} >)"
            )

        _TIMED_OUT = FlexibleNodeData.new_move_on_properties(
            move_on_name="timedOut",
            jinja_name="timed_out_move_on_topic",
            displayed_name="Timed OUt Move On Topic Name",
            hint="If Moxie doesn't see the drawing or here a certain pattern, and times out.",
            required=False,
            text_jinja_name="timed_out_move_on_topic",
            pattern_jinja_name=""
            )

        _SHOW_DRAWING_TEXT = [
        FlexibleNodeData.Property(
            displayed_name="Show Drawing Text (macro by default)",
            hint="When Moxie sees the drawing or hears 'here it is' Moxie will say this text",
            jinja_name="show_drawing_text",
            name="showFaceText",
            required=False,
            prop_type=FlexibleNodeData.Property.PropertyType.BIG_TEXT
            ),
    
        FlexibleNodeData.Property(
            displayed_name="Marked Up Show Drawing Text",
            hint="Marked up version of showDrawingText",
            jinja_name="marked_up_show_drawing_text",
            mark_for_prop_name="markedUpShowDrawingText",
            name="markedUpShowDrawingText",
            required=False,
            canvas_shown=False,
            prop_type=FlexibleNodeData.Property.PropertyType.MARKUP
            )
        ]

        self.name = "show_drawing_v1"
        self.displayedName = "Show/Show Drawing"
        self.templateName = "ShowDrawing.jinja"
        self.outgoingConnectionIDs = []

        self.propertyDefinitions.extend(_SHOW_MOVE_ON)
        self.propertyDefinitions.extend(_TIMED_OUT)
        self.propertyDefinitions.extend(_SHOW_DRAWING_TEXT)


    def update_prop_dict(self, prop_dict, **kwargs) -> dict:
    
        # Ensure the timedOut move-on is utilized, otherwise throw an exception
        for prop_def in self.propertyDefinitions:
            if prop_def.name == "timedOutMoveOnTopicName":
                if prop_def.jinjaName not in prop_dict:
                    raise Exception(f"An '{prop_def.name}' located in the filepath of the last 'Converting file' line above is empty. "
                                    f"Please provide a move on connection for the timed out move-on {log.context(self.parent_element)}.")
        return prop_dict
    
    
    @staticmethod
    def get_description() -> str:
        return """
        This node allows Moxie to detect GRL drawing paper (paper with aruco codes) during a short conversation about the user's art,

        uses the standard node leading into this one as the prompt and the mentor is able to respond with:

        yes, no, idk, here's my art or showing the aruco code to Moxie.
        """
