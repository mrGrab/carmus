<h3 align=center>CarMus</h3>
<p aling=center>My first try in Python and script for managing MP3 files. He automaticaly try to find correct encoding for ID3 tags.
<br>Also takes data for tags from file name if tags is empty or not even exist.
And convert cyrillic text in file name and ID3 tags to translit.</p>
<br>So, 
<br>Usage: carmus.py [options] file_name
<p>
<br>Options:
  <br>--version      show program's version number and exit
  <br>-h, --help     show this help message and exit
  <br>-b, --backup   do not remove original file
  <br>-u, --update   update ID3 tags
  <br>-c, --convert  convert all cyrillic text to translit
  <br>-r, --rename   rename file in translit
  <br>-y, --yes      automaticaly put "yes" in all dialogs
