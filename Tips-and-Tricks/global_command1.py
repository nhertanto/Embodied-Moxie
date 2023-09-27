# *************************************************************************************
# README:
# This python files creates the property data that gets passed to GlobalCommand.jinja
#    This allows the developer to create and manipulate the UI and the node
#    the user sees on the in-house tool.
# NOTE:
# To see the Global Command node utilized in the Tips and Tricks Activity, look at the
#    at the generated code in Generated-TipsAndTricks.top
# ( https://github.com/nhertanto/Embodied-Moxie/blob/main/Tips-and-Tricks/Generated-TipsAndTricks.top )
# *************************************************************************************

from ...flexible.flexible_node_data import FlexibleNodeData
from .flexible_interactions import FlexibleInteractions


class FlexibleGlobalCommand1(FlexibleInteractions):

	_AVAILABLE_GLOBAL_COMMANDS_PROPS = FlexibleNodeData.new_fixed_choice_properties(
		fixed_choice_jinja_name='chosen_global_command',
		fixed_choice_prop_name="chosen Global Command",
		displayed_name="Global Command",
		hint="The Global Command chosen to turn off",
		required=False,
		defaultValue="Sleep",
		possibleValues=["Sleep","SomethingElse", "ListenToMe", "Earmuffs", "HoldOn", "RepeatThat", "SpeakLouder", "SpeakSofter","Hello","WakeUp"]
	)

	_SUCCESS_TEXT = FlexibleNodeData.new_text_and_markup_properties(
		text_jinja_name="success_text",
		markup_jinja_name="success_markup",
		text_prop_name="successText",
		displayed_name="Said Global Command Perfectly Text",
		hint="Response for when the Mentor says the Global Command perfectly (ex. Moxie pls go to sleep)"
	)

	_SUCCESS_MOVE_ON = FlexibleNodeData.new_move_on_properties(
		move_on_name="Said Global Command Perfectly",
		jinja_name="success_move_on_topic",
		displayed_name="Said Global Command Perfectly Move On",
		hint="When the Mentor says the chosen Global Command perfectly",
		required=True,
		text_jinja_name="success_move_on_topic",
		pattern_jinja_name=""
	)

	_REMINDER_TEXT = FlexibleNodeData.new_text_and_markup_properties(
		text_jinja_name="reminder_text",
		markup_jinja_name="reminder_markup",
		text_prop_name="reminderText",
		displayed_name="Reminder of the Tip Text",
		hint="Response for when the Mentor almost gets the Command correctly (ex. Remember the tip is: Moxie pls go to sleep)"
	)	

	_DIDNT_SAY_MOXIE_TEXT = FlexibleNodeData.new_text_and_markup_properties(
		text_jinja_name="didnt_say_moxie_text",
		markup_jinja_name="didnt_say_moxie_markup",
		text_prop_name="didntSayMoxieText",
		displayed_name="Didn't say Moxie Text",
		hint="Response for when the Mentor forgets to say 'Moxie'"
	)

	_SCAFFOLD_PART01_TEXT = FlexibleNodeData.new_text_and_markup_properties(
		text_jinja_name="scaffold_part01_text",
		markup_jinja_name="scaffold_part01_markup",
		text_prop_name="scaffoldPart01Text",
		displayed_name="Scaffolded 1st part of Command",
		hint="1st part of the command (ex. You almost did it. Let's break it up, repeat after me, 'Moxie please')"
	)

	_SCAFFOLD_PART01_TEXT.extend(
	FlexibleNodeData.new_pattern_properties(
			displayed_name="Scaffolded 1st part of Command Pattern",
			hint="The pattern of the 1st part of the Global Command, if it was scaffolded",
			pattern_jinja_name="scaffold_part01_designer_patterns",
			required=True,
			name="scaffoldPart01DesignerPatterns",
		)
	)

	_SCAFFOLD_PART02_TEXT = FlexibleNodeData.new_text_and_markup_properties(
		text_jinja_name="scaffold_part02_text",
		markup_jinja_name="scaffold_part02_markup",
		text_prop_name="scaffoldPart02Text",
		displayed_name="Scaffolded 2nd part of Command",
		hint="2nd part of the command (ex. Great job! Now repeat after me, 'go to sleep')"
	)

	_SCAFFOLD_PART02_TEXT.extend(
	FlexibleNodeData.new_pattern_properties(
			displayed_name="Scaffolded 2nd part of Command Pattern",
			hint="The pattern of the 2nd part of the Global Command, if it was scaffolded",
			pattern_jinja_name="scaffold_part02_designer_patterns",
			required=False,
			name="scaffoldPart02DesignerPatterns",
		)
	)

	_SCAFFOLD_PART03_TEXT = FlexibleNodeData.new_text_and_markup_properties(
		text_jinja_name="scaffold_part03_text",
		markup_jinja_name="scaffold_part03_markup",
		text_prop_name="scaffoldPart03Text",
		displayed_name="Scaffolded 3rd part of Command",
		hint="prompt to say full command after scaffolding (ex. Great job! Now let's say the whole thing, 'Moxie pls go to sleep')"
	)

	_NO_UNDERSTAND_TEXT = FlexibleNodeData.new_text_and_markup_properties(
		text_jinja_name="no_understand_text",
		markup_jinja_name="no_understand_markup",
		text_prop_name="dontUnderstandText",
		displayed_name="Don't Understand Text",
		hint="Response when the Mentor doesn't understand what to do/say"
	)

	_NO_UNDERSTAND_TEXT.extend(
	FlexibleNodeData.new_pattern_properties(
			displayed_name="Don't Understand",
			hint="Any additional patterns that should be matched for 'don't understand",
			pattern_jinja_name="no_understand_designer_patterns",
			required=False,
			name="noUnderstandDesignerPatterns",
		)
	)

	_YES_UNDERSTAND_TEXT = FlexibleNodeData.new_text_and_markup_properties(
		text_jinja_name="yes_understand_text",
		markup_jinja_name="yes_understand_markup",
		text_prop_name="yesUnderstandText",
		displayed_name="Yes Text",
		hint="Response when the Mentor says 'yes' (Moxie doesn't move-on)"
	)	

	_NO_UNDERSTAND_MOVE_ON = FlexibleNodeData.new_move_on_properties(
		move_on_name="Don't Understand",
		jinja_name="no_understand_move_on_topic",
		displayed_name="Don't Understand Move On",
		hint="When the Mentor doesn't understand what to do/say",
		required=False,
		text_jinja_name="no_understand_move_on",
		pattern_jinja_name=""
	)

	_CANT_DO_IT_TEXT = FlexibleNodeData.new_text_and_markup_properties(
		text_jinja_name="cant_do_it_text",
		markup_jinja_name="cant_do_it_markup",
		text_prop_name="cantDoItText",
		displayed_name="Can't do it Text",
		hint="Response for when the Mentor cannot do the selected Global Command"
	)

	_CANT_DO_IT_TEXT.extend(
	FlexibleNodeData.new_pattern_properties(
			displayed_name="Can't Do It",
			hint="Any additional patterns that should be matched for 'Can't Do It",
			pattern_jinja_name="cant_do_it_designer_patterns",
			required=False,
			name="cantDoItDesignerPatterns",
		)
	)

	_CANT_DO_IT_MOVE_ON = FlexibleNodeData.new_move_on_properties(
		move_on_name="Cant Do It",
		jinja_name="cant_do_it_move_on_topic",
		displayed_name="Can't Do It Move On",
		hint="When the Mentor cannot do the selected Global Command",
		required=False,
		text_jinja_name="cant_do_it_move_on_topic",
		pattern_jinja_name=""
	)

	_TIMED_OUT_MOVE_ON = FlexibleNodeData.new_move_on_properties(
		move_on_name="Timed Out",
		jinja_name="timed_out_move_on_topic",
		displayed_name="Timed Out Move On",
		hint="When the Mentor doesn't say/do anything for an extended amount of time",
		required=False,
		text_jinja_name="timed_out_move_on_topic",
		pattern_jinja_name=""
	)

	_FAILED_ATTEMPTS_MOVE_ON = FlexibleNodeData.new_move_on_properties(
		move_on_name="Failed to say Global Command perfectly",
		jinja_name="failed_all_attempts_move_on_topic",
		displayed_name="Failed to say Global Command perfectly Move On",
		hint="When the Mentor incorrectly says the Global Command 3+ times",
		required=False,
		text_jinja_name="failed_all_attempts_move_on_topic",
		pattern_jinja_name=""
	)	


	def __init__(self):
		super().__init__()
		self.name = "global_command_v1"
		self.displayedName = "Module Specific/Global Command"
		self.templateName = "GlobalCommand.jinja"
		self.outgoingConnectionIDs = []
		self.propertyDefinitions.extend(self._AVAILABLE_GLOBAL_COMMANDS_PROPS)
		self.propertyDefinitions.extend(self._SUCCESS_TEXT)
		self.propertyDefinitions.extend(self._SUCCESS_MOVE_ON)
		self.propertyDefinitions.extend(self._REMINDER_TEXT)
		self.propertyDefinitions.extend(self._DIDNT_SAY_MOXIE_TEXT)
		self.propertyDefinitions.extend(self._SCAFFOLD_PART01_TEXT)
		self.propertyDefinitions.extend(self._SCAFFOLD_PART02_TEXT)
		self.propertyDefinitions.extend(self._SCAFFOLD_PART03_TEXT)
		self.propertyDefinitions.extend(self._NO_UNDERSTAND_TEXT)
		self.propertyDefinitions.extend(self._NO_UNDERSTAND_MOVE_ON)
		self.propertyDefinitions.extend(self._YES_UNDERSTAND_TEXT)
		self.propertyDefinitions.extend(self._CANT_DO_IT_TEXT)
		self.propertyDefinitions.extend(self._CANT_DO_IT_MOVE_ON)
		self.propertyDefinitions.extend(self._TIMED_OUT_MOVE_ON)
		self.propertyDefinitions.extend(self._FAILED_ATTEMPTS_MOVE_ON)	

		if type(self) == FlexibleGlobalCommand1:
			self.hideFromEditor = True

	@staticmethod
	def get_description() -> str:
		return """
		The Global Command node 'turns off' the chosen Global Command in the scroll-down menu.
        This listens for if the Mentor:
        - says the Global Command perfectly
        - almost correctly say the Global Command
        - didn't understand what to do
        - can't do selected Global Command
        - timing out
        - simply says "yes"

        NOTE: This node shouldn't be used without all Leads permission!!!
              As such, this node is hidden from the Editor.
		"""
