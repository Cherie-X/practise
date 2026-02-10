info=" Agent:007_Bond; Coords:(40,74); Items:gun,money,gun;Mission:2025-RESCUE-X "
info_new=info.replace(" ","")
items=["gun","money","gun"]
items_new=set(items)
mission="2025-RESCUE-X"
mission_new=mission[5::1]
parts=info_new.split(";")
Agent=parts[0]
Agent_new=Agent[6::]
Coords=(40,74)
dict={"Agent":Agent_new,"Coords":Coords,"items":items_new,"mission":mission_new}
print(dict)
