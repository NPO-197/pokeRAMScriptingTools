import Savefileedit as SaveEdit

with open("Data/emerald.sav","br") as f:
    bindata = bytearray(f.read())

sectors = []
sector = 0xff
numSaves=0

for i in range(32):
    sectors.append(SaveEdit.SaveSector(bindata[i*0x1000:(i+1)*0x1000]))
    if SaveEdit.IDtoString(sectors[i].getID()) in ["Slot2_SaveBlock1_END","Slot1_SaveBlock1_END"]:
        if numSaves < sectors[i].getSaveCounter():
            numsaves = sectors[i].getSaveCounter()
            sector = i

assert sector!=0xff,"Couldn't find save sector"

#Ram script binay to alter NPC interaction
with open("RAMScript/RAMScript-EN.bin",'br') as f:
    RAMScript = bytes(f.read())

for i,u8 in enumerate(RAMScript):
    sectors[sector].data[0x08a8+i] = u8

# Update checksums for save sectors that are signed, and combine all sectors into a new sav file
newSave = []
for sect in sectors:
    if sect.checkIsSigned():
        sect.updateChecksum()
    newSave.extend(sect.data)

with open("Out/EmeraldRamScript.sav","bw") as f:
    f.write(bytearray(newSave))
