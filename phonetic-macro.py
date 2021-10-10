#!/usr/bin/python3

#import socket  # only needed on win32-OOo3.0.0
from com.sun.star.awt import MessageBoxButtons as MSG_BUTTONS
import uno
import requests
from bs4 import BeautifulSoup
# from WordReference_API import translations as tr

class WordNotFoundError(Exception):
	pass

class NetworkError(Exception):
	pass

def getPhonetic(word, language, variant="UK") :
	"""
	Search a word's phonetic in 'WordReference'.
	You can use 'English' language and two variants are available : 'US' and 'UK'
	It will return you a string containing the phonetic transcription of the word pronunciation
	"""

	langFrom = ""
	langTo = ""

	if language == "English":
		langFrom = "en"
		langTo = "fr"

	try:
		page = requests.get(f"https://www.wordreference.com/{langFrom}{langTo}/{word}")
	except:
		return NetworkError

	soup = BeautifulSoup(page.content, 'html.parser')
	pronuncation_widget = soup.find("div", {"id":"pronunciation_widget"})

	if pronuncation_widget != None:
		pronuncation = pronuncation_widget.text
	else :
		return WordNotFoundError # Le mot cherché n'est pas disponible sur WordReference

	try:
		if variant == "US" and "US" in pronuncation.split('/')[2]:
			return pronuncation.split('/')[3]
		else :
			return pronuncation.split('/')[1]
	except:
		return WordNotFoundError

class Document():
	def __init__(self) :
		"""
		# get the uno component context from the PyUNO runtime
		localContext = uno.getComponentContext()
		# create the UnoUrlResolver
		resolver = localContext.ServiceManager.createInstanceWithContext(
						"com.sun.star.bridge.UnoUrlResolver", localContext )
		# connect to the running office
		ctx = resolver.resolve( "uno:socket,host=localhost,port=2002;urp;StarOffice.ComponentContext" )
		smgr = ctx.ServiceManager
		# get the central desktop object
		desktop = smgr.createInstanceWithContext( "com.sun.star.frame.Desktop",ctx)
		self.model = desktop.getCurrentComponent()
		"""
		self.model = XSCRIPTCONTEXT.getDocument()
		# access the current writer document
		

		
	def get_selection(self):
		# create a cursor
		self.cursor = self.model.getCurrentController().getViewCursor()
		# insert the text into the document
		return self.model.getCurrentSelection().getByIndex(0).getString()

	def insert_text(self, text):
		self.cursor.gotoEndOfLine(True)
		self.model.Text.insertString( self.cursor, text, 0)

	def get_phonetic(self, word):
		response = getPhonetic(word.lower(), "English")
		if response == NetworkError :
			msgbox("You are not connected to the Internet, or wordreference.com is not reachable")
			return NetworkError
		elif response == WordNotFoundError:
			msgbox(f"Can't find phonetic for \"{word}\" ")
			return ""
		else :
			return (f" [{response}] ")




def create_instance(name, with_context=False):
	CTX = XSCRIPTCONTEXT.getComponentContext()
	SM = CTX.getServiceManager()
	if with_context:
		instance = SM.createInstanceWithContext(name, CTX)
	else:
		instance = SM.createInstance(name)
	return instance

def msgbox(message, title='LibreOffice', buttons=MSG_BUTTONS.BUTTONS_OK, type_msg='infobox'):
	""" Create message box
		type_msg: infobox, warningbox, errorbox, querybox, messbox
		https://api.libreoffice.org/docs/idl/ref/interfacecom_1_1sun_1_1star_1_1awt_1_1XMessageBoxFactory.html
	"""
	toolkit = create_instance('com.sun.star.awt.Toolkit')
	parent = toolkit.getDesktopWindow()
	mb = toolkit.createMessageBox(parent, type_msg, buttons, title, str(message))
	return mb.execute()


def insert_phonetic():
	doc = Document()
	selection = doc.get_selection()
	selection = selection.replace('\n', ' ')
	selection_ = selection.split(' ')
	new_selection = [selection]
	if '' in selection_ or len(selection_) > 1:
		new_selection = []
		for i in selection_ :
			if i != '' :
				new_selection.append(i)

	for i in new_selection :
		text = doc.get_phonetic(i)
		if text == NetworkError: 
			break
		doc.insert_text(text)

#subprocess.call(["nohup", "soffice", "--writer", "--accept=\"socket,host=localhost,port=2002;urp;StarOffice.ServiceManager\""])
