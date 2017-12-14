
from string import ascii_lowercase as al

translate = [
'@', '8', '(', '|)', '3', '#', '6', '[-]', '|', '_|', '|<', '1', '[]\\/[]', 
'[]\\[]', '0', '|D', '(,)', '|Z', '$', "']['",'|_|', '\\/', '\\/\\/', '}{', '`/', '2'
]

translate = dict(zip(al,translate))

print ''.join(map( lambda c: translate.get(c,c) , 
	raw_input().lower()))

