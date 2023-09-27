# *************************************************************************************
# README:
# This python files creates the property data that gets passed to bookRecognizer.jinja
#    This allows the developer to create and manipulate the UI adn the node
#    the user sees on the in-house tool.
# NOTE:
# To see the Book Recognizer node utilized in the Reading Activity, look at the
#    at the generated code in Generated-Reading-BookRecognizer.top
# ( https://github.com/nhertanto/Embodied-Moxie/blob/main/Reading-Activity/Generated-Reading-BookRecognizerNode.top )
# *************************************************************************************

from ...flexible.flexible_node_data import FlexibleNodeData
from . module.select_content_id import FlexibleSelectContentID1

class FlexibleBookRecognizer1(FlexibleSelectContentID1):

	_TIMED_OUT_MOVE_ON = FlexibleNodeData.new_move_on_properties(
		move_on_name="timed out",
		jinja_name="timed_out_move_on_topic",
		displayed_name="Timed Out On Showing Book move-on topic",
		hint="If the Mentor doesn't say or show a book cover after some time, we will time out and move-on.",
		required=True,
		text_jinja_name="timed_out_text",
		pattern_jinja_name="timed_out_pattern",
		pattern=""
	)

	_RECOGNIZED_BOOK_BY_COVER = FlexibleNodeData.new_move_on_properties(
		move_on_name="Book not in index",
		jinja_name="Not_in_the_index_move_on",
		displayed_name="Book isn't in the Index move-on topic",
		hint="Moxie recognized the book cover, but it's not in the index.",
		text_jinja_name="",
		pattern_jinja_name=""
	)


	def __init__(self):
		super().__init__()
		self.name = "book_recognizer_v1"
		self.displayedName = "Module Specific/Book Recognizer"
		self.templateName = "BookRecognizer.jinja"
		self.outgoingConnectionIDs = []

		self.propertyDefinitions.extend(self._TIMED_OUT_MOVE_ON)
		self.propertyDefinitions.extend(self._RECOGNIZED_BOOK_BY_COVER)

       

	@staticmethod
	def get_description() -> str:
		return """ 
		The Book Recognizer node is essentially a show node, while being a Select Content ID node.
		This node allows Moxie to recognize a book by its cover, while connecting that book to the Index.csv.
		This move-on is called ID Selected.
		Even if the book isn't in the Index, but has been scanned, Moxie can recognize it as well,
		and it will have it's own move-on, called Recognize Book by Cover.
		This node allows Moxie to differentiate items that she sees from the Index, and not!
		Lastly, this node allows Moxie to time out if the Mentor doesn't say/show anything.
		After the 2nd timed out, Moxie will move-on, called Timed Out.
		"""
