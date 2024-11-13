from time import sleep
inventory = []
name = input("Hej, vad heter du? ")
greeting = "Välkommen till min värld [name]. Du vaknar upp efter en lång natts sömn..."
greeting = greeting.replace("[name]", name)
print(greeting)
print("Mystiskt nog finner du dig i en hamsters kropp, där du löper över ängarna i jakt på en gyllene maskros.")
print("Du rycker till och fryser i din tanke, tittar du på [maskrosen], eller din mystiska [hamster]-kropp")
choice = input("Vad väljer du? ").lower()
if "hamster" in choice:
    print("I drömlik slowmotion beundrar du den fantastiska fluffigheten, dina sinnen förnimmer havre och damm.")
    print("Du tänker [Boromir]? Vad är det som händer, det luktar [rostad macka], vad är detta?")
    choice = input("Vad väljer du? ").lower()
    if choice in "boromir":
        print("Känner du till Boromir? Du kanske vill [lära dig mer]?(https://sv.wikipedia.org/wiki/Boromir)")
    else:
        print("Så deprimerande, har du ingen kärlek till litteratur och fantastik?")
    sleep(0.6)
    print("Oj, jag ber om ursäkt, var var vi nu...")
elif "maskros" in choice:
    print("Du skriker inombords som den maskrosallergiker du är, prosit, du stoppar maskrose i din hamsterpåse")
    inventory.append("maskros")
else:
    print("Stavning är inte din starka gren, du fortsätter...")
print("Men se där...")
# testa ditt inventory
# for item in inventory:
#   print(item)

