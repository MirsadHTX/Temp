import random
HojestTal= int(input("Hvilket tal skal være højest    "))
AntalForsog= int(input("Hvor mange forsøg vil du have    "))

ComputerFinderRandomTal = random.randint(1,HojestTal)

for BrugteForsog in range(0, AntalForsog):
    MitIndtastedeTal= int(input("Gæt et fucking tal     "))
    if (ComputerFinderRandomTal == MitIndtastedeTal):
        print("KÆFT EN EINSTEN HUUUUUUUUU!!!!!")
        break
    if (ComputerFinderRandomTal > MitIndtastedeTal):
        print("større!")
    if (ComputerFinderRandomTal < MitIndtastedeTal):
        print("mindre!")
    print("Du har haft " + str(BrugteForsog + 1) + " forsøg")


print("tak for spillet")
print ("Made by Manse Højlund Kadribasic")
print ("og en lille smulle tata og mimmergøj")