class Parser ():
	'''
	This class holds all tools for parsing our markdown language

	Creates a tree that contains the description of the GUI
	'''

	def __init__(self):
		'''
		create the parser
		'''
		pass

	def parse(self, markdown_file):
		'''
		parses the markdown file that we pass this
		'''
		def parse_container():
			'''
			parses a tag that contains
			other objects, could be 
			'''

			pass

		def parse_physical():
			'''
			parses physical object. 
			Could be text or an image or something else
			'''

		def parse_tag():
			'''
			check what the next tag is, add it to the tree
			and creates the 