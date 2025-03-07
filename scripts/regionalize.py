# -*- coding: utf-8 -*-

# Original file from https://github.com/Artrios/pokecarde

import sys
from gen3text import utf8ToRSText
from asmquote import asmQuote

data_region = sys.argv[3] # determines region code
text_region = sys.argv[4] # determines string translation

out = open(sys.argv[2], 'w')

with open(sys.argv[1], 'r') as f:
	for asm in f:
		asms = asm.split('"')
		command = asms[0].strip()
		if (command == "Text_" + text_region) or (command == "Text"):
			asms[1] = utf8ToRSText(asms[1], text_region)
			try:
				length = asms[2].split(';')[0] # strip trailing comment
				padding = int(length) - len(asms[1])
				if padding > 0:
					asms[1] += '\xFF'
				for i in range(padding - 1):
					asms[1] += "\x00"
			except ValueError:
				pass
			outstr = '.byte '
			for b in asms[1]:
				outstr+=("0x%02x,"%b)
			outstr = outstr[:-1]+'\n'
			out.write(outstr)
		elif len(command) < 5 or command[0:5] != "Text_":
			out.write(asm)
			if "macros.asm" in asm:
				# can’t do this until after REGION_EN, etc. are loaded
				out.write("DEF REGION EQU REGION_" + data_region + "\n")
		# else this is foreign text, delete it
f.closed