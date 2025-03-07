.include "../asm.inc"
.include "../event.inc"

	@.set offset,0x02000047 @For use with vadderess, not sure if needed
RamScript:
	.word 0 @ checksum placeholder
DataStart:
	.byte 0x33 @magic ram script number
	.byte 0,9 @  LittleRoot
	.byte 2   @ "Power of Sience" guy
ScriptStart:

	setvaddress ScriptStart
	vmessage CustomText
	waitmessage 
	waitbuttonpress
	release
	end 

CustomText:
Text_EN "The power of science is amazing! :D@"

DataEnd:

