#!/usr/bin/python
#coding: UTF-8
import sys, codecs, os

from mutagen.mp3 import MP3
from mutagen.id3  import ID3

#Check if symbol is readable in eng or cyr.
def is_valid(sym):
	en_alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
			'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
	cyr_alph =[u'А', u'Б', u'В', u'Г', u'Д', u'Е', u'Ё', u'Ж', u'З', u'И', u'Й', u'К', u'Л', u'М', u'Н', u'О', u'П', u'Р', u'С', u'Т', u'У', 
			u'Ф', u'Х', u'Ц', u'Ч', u'Ш', u'Щ', u'Ъ', u'Ы', u'Ь', u'Э', u'Ю', u'Я', u'а', u'б', u'в', u'г', u'д', u'е', u'ё', u'ж', u'з', 
			u'и', u'й', u'к', u'л', u'м', u'н', u'о', u'п', u'р', u'с', u'т', u'у', u'ф', u'х', u'ц', u'ч', u'ш', u'щ', u'ъ', u'ы', u'ь', 
			u'э', u'ю', u'я', u'і', u'І', u'ї', u'Ї', u'є', u'Є']
	
	if sym in en_alph or sym in cyr_alph:
			return (True)
	else:
		return (False)

#Check if encoder and decoder are good
def enc(sym, coder, type):
	try:
		if type == "e":
			sym.encode(coder)
			return True
		elif type == "d":
			sym.decode(coder)
			return True
	except:
		return False

#Convert unicode text to readable format
def converter (text):
	c_type = ["CP1251", "CP1252", "ISO-8859-1","UTF-8","UTF-16","UTF-16BE", "KOI8-R"]
	start = ["1","2","3","4","5","6","7","8","9","0",u' ',u'_']
	test = 0
	
	sym = text[-1] if text[0] in start else text[0]
	for i in c_type:
		if enc(sym, i, "e"):
			for k in c_type:
				if enc(sym.encode(i), k, "d") and is_valid(sym.encode(i).decode(k)):
					test = 1
					break
			if test == 1:
				break
	return unicode(text).encode(i).decode(k) if test == 1 else None
	
#Updating ID3 tags
def update_tag (file, tags):
	print tags['art']

	
#Getting id3 tags  from file
def get_id3_tags (file):
	tags = {'art':None, 'title':None}
	title = ID3(file)['TIT2'].text[0] if ID3(file).getall('TIT2') else None
	art = ID3(file)['TPE1'].text[0] if ID3(file).getall('TPE1') else None
	
	for key, text  in zip(tags.keys(), (art, title)):
		if text is None or is_valid(text[0]):
			pass
		else:
			text = converter(text)
		tags[key] = text
	print "art - ", tags['art']
	print "titile - ", tags['title']
	return (tags)

def main ():
	for i in range(1, len(sys.argv)):
		print ("{0:-^100}".format(sys.argv[i]))
		if MP3(sys.argv[i]).tags is None:
			print ('No tags')
		else:
#			print ID3(sys.argv[i]).pprint()
			update_tag (sys.argv[i], get_id3_tags (sys.argv[i]))
			
		
main()
