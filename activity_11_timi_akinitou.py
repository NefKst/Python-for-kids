#λειπει ο σχολιασμος

ektasi = float(input("Πόσα τ.μ. είναι το ακίνητο;"))
perioxi = str(input("Σε ποια περιοχή βρίσκεται το ακίνητο;"))
if perioxi == "ΚΕΝΤΡΟ" or perioxi =="Κέντρο" or perioxi =="κέντρο":
    proForou = ektasi * 700
    foros = (proForou * 24) / 100
    metaForou = proForou + foros
    print ("Η τιμή του ακινήτου με τον φόρο είναι €" + str(metaForou))

elif perioxi == "ΑΓΙΑ ΣΟΦΙΑ" or perioxi =="Αγία Σοφία" or perioxi =="αγία σοφία":
    proForou = ektasi * 600
    foros = (proForou * 24) / 100
    metaForou = proForou + foros
    print ("Η τιμή του ακινήτου με τον φόρο είναι €" + str(metaForou))

elif perioxi == "ΡΙΟ" or perioxi =="Ρίο" or perioxi =="ρίο":
    proForou = ektasi * 800
    foros = (proForou * 24) / 100
    metaForou = proForou + foros
    print ("Η τιμή του ακινήτου με τον φόρο είναι €" + str(metaForou))

else:
    print("Η περιοχή δε βρέθηκε! \n Δοκιμάστε: ΚΕΝΤΡΟ, ΑΓΙΑ ΣΟΦΙΑ, ΡΙΟ")
