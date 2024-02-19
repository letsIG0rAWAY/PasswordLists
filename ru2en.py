import sys
russianFilename = sys.argv[1]
englishFilename = "english.txt"
keyboardDict= {
	"ё":"`",
	"й":"q",
	"ц":"w",
	"у":"e",
	"к":"r",
	"е":"t",
	"н":"y",
	"г":"u",
	"ш":"i",
	"щ":"o",
	"з":"p",
	"х":"[",
	"ъ":"]",
	"ф":"a",
	"ы":"s",
	"в":"d",
	"а":"f",
	"п":"g",
	"р":"h",
	"о":"j",
	"л":"k",
	"д":"l",
	"ж":";",
	"э":"'",
	"/":"<",
	"я":"z",
	"ч":"x",
	"с":"c",
	"м":"v",
	"и":"b",
	"т":"n",
	"ь":"m",
	"б":",",
	"ю":".",
	".":"/",
	"Ё":"~",
	"Й":"Q",
	"Ц":"W",
	"У":"E",
	"К":"R",
	"Е":"T",
	"Н":"Y",
	"Г":"U",
	"Ш":"I",
	"Щ":"O",
	"З":"P",
	"Х":"{",
	"Ъ":"}",
	"Ф":"A",
	"Ы":"S",
	"В":"D",
	"А":"F",
	"П":"G",
	"Р":"H",
	"О":"J",
	"Л":"K",
	"Д":"L",
	"Ж":":",
	"Э":'"',
	"/":"|",
	"|":">",
	"Я":"Z",
	"Ч":"X",
	"С":"C",
	"М":"V",
	"И":"B",
	"Т":"N",
	"Ь":"M",
	"Б":"<",
	"Ю":">",
	",":"?"
}
with open(russianFilename, encoding="utf-8") as rf:
	with open(englishFilename, "w") as ef:
		for russianStr in rf:
			englishStr = ""
			for russianChar in russianStr.rstrip():
				if russianChar in keyboardDict.keys():
					englishStr += keyboardDict[russianChar]
				else:
					englishStr += russianChar
			ef.write(englishStr + "\n") 
	
