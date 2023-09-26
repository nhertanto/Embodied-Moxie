# *************************************************************************************
# README:
# This python files creates the property data that gets passed to ShowFace.jinja
#    This allows the developer to create and manipulate the UI and the node
#    the user sees on the in-house tool.
# *************************************************************************************

import logging
from .....logs import log
from ...flexible.flexible_node_data import FlexibleNodeData
from .polar1 import FlexiblePolar1

class FlexibleShowFace1(FlexiblePolar1):

    _SHOW_MOVE_ON = FlexibleNodeData.new_move_on_properties(
        move_on_name="showFace",
        jinja_name="show_face_move_on_topic",
        displayed_name="Show Face Move On Topic Name",
        hint="When user Shows Their Face, we will move to the specified node.",
        required=False,
        text_jinja_name="show_face_text",
        pattern_jinja_name=""
    )

    _TIMED_OUT = FlexibleNodeData.new_move_on_properties(
        move_on_name="timedOut",
        jinja_name="timed_out_move_on_topic",
        displayed_name="Timed Out Move On Topic Name",
        hint="When Moxie can't see user's face or hear anything, move along here.",
        required=False,
        text_jinja_name="timed_out_text",
        pattern_jinja_name=""
    )

    _SHOW_FACE_TIMER_PROPS = FlexibleNodeData.new_fixed_choice_properties(
        fixed_choice_jinja_name='show_face_timer',
        fixed_choice_prop_name="showFaceTimer",
        displayed_name="Show Face Timer",
        hint="How long we show wait (in seconds) before acknowledging we found face",
        required=False,
        defaultValue="medium(3.0s)",
        possibleValues=["monologue(0.25s)","short(1.0s)","medium(3.0s)","long(5.0s)","reprompt(10.0s)"]
    )

    _SHOW_FACE_TEXT = [
    FlexibleNodeData.Property(
        displayed_name="Show Face Text (macro by default)",
        hint="When Moxie recognizes the user's face, Moxie will say this",
        jinja_name="show_face_text",
        name="showFaceText",
        required=False,
        prop_type=FlexibleNodeData.Property.PropertyType.BIG_TEXT
        ),
    FlexibleNodeData.Property(
        displayed_name="Marked Up Show Face Text",
        hint="Marked up version of showFaceText",
        jinja_name="marked_up_show_face_text",
        mark_for_prop_name="markedUpShowYesText",
        name="markedUpShowFaceText",
        required=False,
        canvas_shown=False,
        prop_type=FlexibleNodeData.Property.PropertyType.MARKUP
        )
    ]

    def __init__(self):
        super().__init__()
        self.name = "show_face_v1"
        self.displayedName = "Show/Show Face"
        self.templateName = "ShowFace.jinja"
        self.outgoingConnectionIDs = []
        self.propertyDefinitions.extend(self._SHOW_MOVE_ON)
        self.propertyDefinitions.extend(self._TIMED_OUT)
        self.propertyDefinitions.extend(self._SHOW_FACE_TIMER_PROPS)
        self.propertyDefinitions.extend(self._SHOW_FACE_TEXT)

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
        This node allows Moxie to detect the user's face,

        uses the standard node leading into this one as the prompt and the mentor is able to respond with:

        yes, no, idk, here's my face or user showing their face to Moxie.
        """