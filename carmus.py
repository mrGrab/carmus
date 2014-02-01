#!/usr/bin/python2.7

import sys, mutagen, codecs
from mutagen.mp3 import MP3, EasyMP3
from mutagen.id3 import ID3

'''def getTags(path):
    """"""
    id3r = id3reader.Reader(path)
 
    print "Artist: %s" % id3r.getValue('performer')
    print "Album: %s" % id3r.getValue('album')
    print "Track: %s" % id3r.getValue('title')
    print "Release Year: %s" % id3r.getValue('year')'''
    
def main ():
	i = 1
	while  i < len(sys.argv):
		print ("{0:-^100}".format(sys.argv[i]))
		file = ID3(sys.argv[i])
#		for key, value in file.items():
#			print (key)
#			print (value.encoding)
#		print ("{0:-^100}".format(sys.argv[i]))
		print (file.pprint())
#		tit = str(file.getall("TIT2"))
#		print (tit)
#		print (tit.decode('utf8'))
#		print (mp3.get("TPE1"))
#		audio = TIT2(sys.argv[i])
#		print (mutagen.easyid3.pprint (sys.argv[i]))
#		name_of_song = audio.getall("TIT2")
#		name_of_artist = audio.getall("TPE1")
#		file = audio.pprint()
#		print ("name_of_song- " + str(name_of_song),"name_of_artist - " + str(name_of_artist))
#		print (file)
#		print (audio)
		i += 1
	
main()