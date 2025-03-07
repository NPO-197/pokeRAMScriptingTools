	@Original file from https://github.com/pret/pokeemerald
	
	.macro inc x:req
	.set \x, \x + 1
	.endm

	.macro enum_start x=0
	.set __enum__, \x
	.endm

	.macro enum constant:req
	.equiv \constant, __enum__
	inc __enum__
	.endm

