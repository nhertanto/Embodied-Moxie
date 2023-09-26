# *************************************************************************************
# README:
# This python files creates the property data that gets passed to RepeatMentorSpeech.jinja
#    This allows the developer to create and manipulate the UI and the node
#    the user sees on the in-house tool.
# *************************************************************************************

from ...flexible.flexible_node_data import FlexibleNodeData


class FlexibleRepeatMentorSpeech1(FlexibleNodeData):

	_MOXIE_PREPEND_REPLY_TEXT = FlexibleNodeData.new_text_and_markup_properties(
		text_jinja_name="Moxie_prepend_reply_text",
		markup_jinja_name="Moxie_prepend_reply_markup",
		text_prop_name="moxiePrependReplyText",
		displayed_name="Prepended Moxie's reply",
		required=False,
		hint="Prepend Moxie's reply to Mentor's speech"
	)

	_MENTOR_REPLY = FlexibleNodeData.new_move_on_properties(
		move_on_name="Mentor's Reply",
		jinja_name="mentor_reply_move_on_topic",
		displayed_name="Mentor's Reply",
		hint="Once Mentor replies with a global fallback.",
		required=True,
		text_jinja_name="mentor_reply_text",
		pattern_jinja_name="mentor_reply_pattern",
		pattern=""	
	)

	def __init__(self):
		super().__init__()
		self.name = "repeat_mentor_speech_v1"
		self.displayedName = "Interactions/Repeat Mentor Speech"
		self.templateName = "RepeatMentorSpeech.jinja"
		self.outgoingConnectionIDs = []

		self.propertyDefinitions.extend(self._MOXIE_PREPEND_REPLY_TEXT)
		self.propertyDefinitions.extend(self._MENTOR_REPLY)

		# This hides the node from the editor...for now! Possibly remove this later!
		if type(self) == FlexibleRepeatMentorSpeech1:
			self.hideFromEditor = True

	@staticmethod
	def get_description() -> str:
		return """ 
		NOTE: This node repeats the Mentor's speech, and parrots it back to the user!

		"""