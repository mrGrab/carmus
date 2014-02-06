------------------------------------  CarMus  ----------------------------
My first try in Python and script for managing MP3 files.
He automaticaly try to find correct encoding for ID3 tags.
Also takes data for tags from file name if tags is empty or not even exist.
And convert cyrillic text in file name and ID3 tags to translit.
So, 
Usage: carmus.py [options] file_name

Options:
  --version      show program's version number and exit
  -h, --help     show this help message and exit
  -b, --backup   do not remove original file
  -u, --update   update ID3 tags
  -c, --convert  convert all cyrillic text to translit
  -r, --rename   rename file in translit
  -y, --yes      automaticaly put "yes" in all dialogs
