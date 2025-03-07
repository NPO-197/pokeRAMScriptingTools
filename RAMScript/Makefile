
all: RAMScript-EN.bin
PREFIX := arm-none-eabi-
AS := $(PREFIX)as
LD := $(PREFIX)ld
OBJCOPY := $(PREFIX)objcopy
ASFLAGS := -mcpu=arm7tdmi --defsym MODERN=$(MODERN)

RAMScript-%.tx: RAMScript.asm
	python ../scripts/regionalize.py $< $@ $* $*
RAMScript-%.o: RAMScript-%.tx
	$(AS) -o $@ $<
RAMScriptNocrc-%.bin: RAMScript-%.o
	$(OBJCOPY) -O binary $< $@
RAMScript-%.bin: RAMScriptNocrc-%.bin
	python ../scripts/crc_calc.py $< $@

clean:
	rm -f *.tx *.o *.gbc *.z80 *.bin *.mev *.vpk *.raw