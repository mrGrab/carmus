#!/usr/bin/python3.3
#coding: UTF-8
import sys, codecs, os, shutil,optparse, string

from mutagenx.mp3 import MP3
from mutagenx.id3  import ID3, TIT2, TPE1

alph = {u'юй': u'yuy', u'ей': u'yay', u'Юй': u'Yuy', u'Ей': u'Yay',
    u'а': u'a',  u'б': u'b',  u'в': u'v',  u'г': u'g', u'д': u'd', u'е': u'e',
    u'ё': u'yo', u'ж': u'zh', u'з': u'z',  u'и': u'i', u'й': u'y', u'к': u'k',
    u'л': u'l',  u'м': u'm',  u'н': u'n',  u'о': u'o', u'п': u'p', u'р': u'r',
    u'с': u's',  u'т': u't',  u'у': u'u',  u'ф': u'f', u'х': u'h', u'ц': u'c',
    u'ч': u'ch', u'ш': u'sh', u'щ': u'sh', u'ъ': u'',  u'ы': u'y', u'ь': u'',
    u'э': u'e',  u'ю': u'yu', u'я': u'ya',
    u'А': u'A',  u'Б': u'B',  u'В': u'V',  u'Г': u'G', u'Д': u'D', u'Е': u'E',
    u'Ё': u'Yo', u'Ж': u'Zh', u'З': u'Z',  u'И': u'I', u'Й': u'Y', u'К': u'K',
    u'Л': u'L',  u'М': u'M',  u'Н': u'N',  u'О': u'O', u'П': u'P', u'Р': u'R',
    u'С': u'S',  u'Т': u'T',  u'У': u'U',  u'Ф': u'F', u'Х': u'H', u'Ц': u'C',
    u'Ч': u'Ch', u'Ш': u'Sh', u'Щ': u'Sh', u'Ъ': u'',  u'Ы': u'Y', u'Ь': u'',
    u'Э': u'E',  u'Ю': u'Yu', u'Я': u'Ya',
    u'Є': u'Ye', u'І': u'I', u'Ї': u'Yi', u'Ґ': u'G', u'є': u'ye', u'і': u'i', u'ї': u'yi', u'ґ': u'g'}

#Check if symbol is readable in eng or cyr.
def is_valid(sym):
	cyr_alph =[u'А', u'Б', u'В', u'Г', u'Д', u'Е', u'Ё', u'Ж', u'З', u'И', u'Й', u'К', u'Л', u'М', u'Н', u'О', u'П', u'Р', u'С', u'Т', u'У', 
			u'Ф', u'Х', u'Ц', u'Ч', u'Ш', u'Щ', u'Ъ', u'Ы', u'Ь', u'Э', u'Ю', u'Я', u'а', u'б', u'в', u'г', u'д', u'е', u'ё', u'ж', u'з', 
			u'и', u'й', u'к', u'л', u'м', u'н', u'о', u'п', u'р', u'с', u'т', u'у', u'ф', u'х', u'ц', u'ч', u'ш', u'щ', u'ъ', u'ы', u'ь', 
			u'э', u'ю', u'я', u'і', u'І', u'ї', u'Ї', u'є', u'Є']
	if sym in cyr_alph or sym in string.ascii_letters:
		return (True)
	else:
		return (False)
		
#Getting something from user
def get_response(message, default=None, min_len=0, max_len=100, number=False):
	message += ": " if default is None else " [{0}]: ".format(default)
	class RangeError(Exception): pass
	while True:
		try:
			line = input (message)
			if not line:
				if default is not None:
					return default
				if min_len == 0:
					return ""
				else:
					raise RangeError("{0} may not be empty".format(name))
			if number is True:
				if int(line):
					line = int(line)
			else:
				if not (min_len <= len(line) <= max_len):
					print ("Must be at least {0} and at most {1} characters".format(min_len, max_len))
			return line
		except RangeError as err:
			print ("ERROR:", err)
		except ValueError as err:
			print ("{0} must be integer".format(name))

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
	test = 0

	for sym in text:
		if sym not in string.punctuation or sym not in string.digits:
			break
	else:
#		print ("nothing for convert: ", text)
		return (text)
	
	for i in c_type:
		if enc(sym, i, "e"):
			for k in c_type:
				if enc(sym.encode(i), k, "d") and is_valid(sym.encode(i).decode(k)):
					test = 1
					break
			if test == 1:
				break
	return text.encode(i).decode(k) if test == 1 else None
	
#Updating ID3 tags
def update_tag (file, tags):
#	print (file, tags)
	audio = MP3(file)

	t = ID3(file)['TIT2'].text[0] if MP3(file).tags and ID3(file).getall('TIT2') else None
	a = ID3(file)['TPE1'].text[0] if MP3(file).tags and ID3(file).getall('TPE1') else None
	print ("was ---> title:",t, " art:",a)
	print ("new title -->:",tags['title'],"new art -->:", tags['art'])
#	audio["TIT2"] = TIT2(encoding=3, text=tags['title']) 
#	audio["TPE1"] = TPE1(encoding=3, text=tags['art'])
#	audio.save()

#	print ("Now ---> title:",ID3(file)['TIT2'].text[0], " art:", ID3(file)['TPE1'].text[0])

	
#Getting id3 tags  from file
def get_id3_tags (file, translate=False, yes=False):
	tags = {'art':None, 'title':None}

	title = ID3(file)['TIT2'].text[0] if MP3(file).tags and ID3(file).getall('TIT2') else None
	art = ID3(file)['TPE1'].text[0] if MP3(file).tags and ID3(file).getall('TPE1') else None

	for key, text  in zip(('art','title'), (art, title)):
#		print ("text: ", text, ", type: ", type(text),  is_valid(text[0]))
		if text != None and is_valid(text[0]) is False:
#			print ("for convert", text)
			text = converter(text)
		if text == None:
			text = tags_from_name (file, key, True, yes)  
		tags[key] = translator(text, gaps=True) if translate else text
#	print ("art ---> ", tags['art'],": title --> ", tags['title'])
	return (tags)

def tags_from_name (file, tag, convert=False, yes=True):
	file_name = get_file(file)
	confirm = "Yes" if yes else []
	while confirm  not in ("Y", "y", "yes", "YES" "Yes", "N", "n", "no", "No", "NO"):
		if  tag =="art":
			new_tag = file_name[1].partition("-")[0].strip().rstrip("_") if '-' in file_name[1] else file_name[1][:-4]
		elif  tag =='title':
			new_tag = file_name[1].partition("-")[2][:-4].strip().lstrip("_") if '-' in file_name[1] else file_name[1][:-4]
		message = "No "+tag+". Takes data from file-name:\""+new_tag+"\""
		confirm = "Yes" if yes else get_response(message, default="Yes", min_len=1, max_len=3)
		if confirm in ("Y", "y", "yes", "Yes", "YES"):
			return (new_tag)
		elif confirm in ("N", "n", "no", "No", "NO"):
			return ("-")

#for converting cyr to translit
def translator (text, gaps=True):
	new_text = []
#	print (text)
	line = ''.join(text)
	for i in line:
		if i not in alph:
			new_text.append(i.replace("_"," ")) if gaps else new_text.append(i.replace(" ","_")) 
		else:
			new_text.append(alph.get(i.replace("_"," "))) if gaps else new_text.append(alph.get(i.replace(" ","_")))
	return(''.join(new_text))

def get_file (path):
	link = path if path.startswith("/") else os.getcwd()+"/"+path
	if os.path.exists(link):
		return (os.path.split(link))
	else:
		print ("error: no such file or directory")

def rename_file (old_name, new_name, path, backup=False, yes=False):
	ask = []
	while ask not in ("Y", "y", "yes", "Yes", "YES", "N", "n", "No", "NO"):
		print ("Going to rename {0} to {1}...".format(old_name, new_name))
		ask = "Yes" if yes else get_response(" [Y]es [N]o", default="Y", min_len=0, max_len=3)
		if ask in ("Y", "y", "yes", "Yes", "YES"):
			if os.access(path, os.W_OK):
				if backup:
					shutil.copyfile((path+"/"+old_name),(path+"/"+new_name))
					return (True)
				else:
					os.rename ((path+"/"+old_name),(path+"/"+new_name))
					return (True)
			else:
				print ('error: no access to file')
		elif ask in ( "N", "n", "No", "NO"):
			break
			return (False)
	else:
		return (False)

def main ():
	parser = optparse.OptionParser(version="0.1", usage='%prog [options] file_name', description='Program for edit ID3 tags and converting cyrillic to translit')
	parser.add_option("-b", "--backup", action='store_true', dest='backup', default=False,
		help="do not remove original file")
	parser.add_option("-u", "--update", action='store_true', dest='update', default=False,
		help="update ID3 tags")
	parser.add_option("-c", "--convert", action='store_true', dest='convert', default=False,
		help='convert all cyrillic text to translit')
	parser.add_option("-r", "--rename", action='store_true', dest='rename', default=False,
		help='rename file in translit')	
	parser.add_option ("-y", "--yes",  action='store_true', dest='yes', default=False,
		help='automaticaly put "yes" in all dialogs')
	opts, args=parser.parse_args()
	
	if len(args) > 0:
		for arg in args:
			file = get_file(arg)
			print (" {0:-^100} ".format(file[1]))
			if opts.convert and opts.update is False:
				print ("Error flag \"-c, --convert\" should be used with \"-u, --update\" ")
				break
			if opts.update:
#				print (MP3(arg).pprint())
				tags = get_id3_tags(arg, opts.convert, opts.yes)
				for k in tags.keys():
					if tags[k].find("Track") != -1:
						print ("Fount Track")
						tags[k] = tags_from_name (file[1],k, convert=opts.convert, yes=opts.yes)
					elif tags[k].find("(zaycev.net)") != -1:
						print ("Found zaycev.net")
						tags[k] = tags[k].replace("(zaycev.net)", "")
#				print (tags)
				update_tag (arg, tags)
			if opts.rename:
				new_file = translator(file[1], False)
#				print (file[1], new_file)
				if new_file == file[1]:
					print ('files are the same, nothing to do...{0}'.format(file[1]))
				else:
					print ("Will do")
					rename_file (file[1], new_file, file[0], backup=opts.backup, yes=opts.yes)
	else:
		parser.error("Wrong number of arguments. Use -h or --help for more info. ")
	
main()
