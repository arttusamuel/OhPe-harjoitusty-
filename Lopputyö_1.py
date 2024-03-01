
import pprint
import time

print("\n\njärjestelmä käynnistyy...\n")

#KIRJOITTAMINEN JA LUKEMINEN TIEDOSTOON JA :STA
# paivat sanakirja sisältää päivät salit näytösajat: joiden sisällä elokuva ja katsojat(list)

# Tekee tiedoston varauskalenterille ja tallentaa pohjarakenteen tekstimuodossa

#tuplet varauskalenterin viittauksia varten
p_tuple = ("Maanantai", "Tiistai", "Keskiviikko", "Torstai", "Perjantai", "Lauantai")
s_tuple = ("Sali1", "Sali2", "Sali3")
n_tuple = ("15:00", "18:00", "21:00")
e_k_tuple = ("Elokuva", "Katsojat")

#varausjärjestelmän kalenterirakenne
paivat_aloitus = {
"Maanantai": 
            {
            "Sali1": {"15:00": {"Elokuva": "", "Katsojat": []},"18:00": {"Elokuva": "", "Katsojat": []},"21:00": {"Elokuva": "", "Katsojat": []}},
            "Sali2": {"15:00": {"Elokuva": "", "Katsojat": []},"18:00": {"Elokuva": "", "Katsojat": []},"21:00": {"Elokuva": "", "Katsojat": []}},
            "Sali3": {"15:00": {"Elokuva": "", "Katsojat": []},"18:00": {"Elokuva": "", "Katsojat": []},"21:00": {"Elokuva": "", "Katsojat": []}}
            } ,
"Tiistai": 
            {
            "Sali1": {"15:00": {"Elokuva": "", "Katsojat": []},"18:00": {"Elokuva": "", "Katsojat": []},"21:00": {"Elokuva": "", "Katsojat": []}},
            "Sali2": {"15:00": {"Elokuva": "", "Katsojat": []},"18:00": {"Elokuva": "", "Katsojat": []},"21:00": {"Elokuva": "", "Katsojat": []}},
            "Sali3": {"15:00": {"Elokuva": "", "Katsojat": []},"18:00": {"Elokuva": "", "Katsojat": []},"21:00": {"Elokuva": "", "Katsojat": []}}
            } ,
"Keskiviikko": 
            {
            "Sali1": {"15:00": {"Elokuva": "", "Katsojat": []},"18:00": {"Elokuva": "", "Katsojat": []},"21:00": {"Elokuva": "", "Katsojat": []}},
            "Sali2": {"15:00": {"Elokuva": "", "Katsojat": []},"18:00": {"Elokuva": "", "Katsojat": []},"21:00": {"Elokuva": "", "Katsojat": []}},
            "Sali3": {"15:00": {"Elokuva": "", "Katsojat": []},"18:00": {"Elokuva": "", "Katsojat": []},"21:00": {"Elokuva": "", "Katsojat": []}}
            } ,
"Torstai": 
            {
            "Sali1": {"15:00": {"Elokuva": "", "Katsojat": []},"18:00": {"Elokuva": "", "Katsojat": []},"21:00": {"Elokuva": "", "Katsojat": []}},
            "Sali2": {"15:00": {"Elokuva": "", "Katsojat": []},"18:00": {"Elokuva": "", "Katsojat": []},"21:00": {"Elokuva": "", "Katsojat": []}},
            "Sali3": {"15:00": {"Elokuva": "", "Katsojat": []},"18:00": {"Elokuva": "", "Katsojat": []},"21:00": {"Elokuva": "", "Katsojat": []}}
            } ,
"Perjantai": 
            {
            "Sali1": {"15:00": {"Elokuva": "", "Katsojat": []},"18:00": {"Elokuva": "", "Katsojat": []},"21:00": {"Elokuva": "", "Katsojat": []}},
            "Sali2": {"15:00": {"Elokuva": "", "Katsojat": []},"18:00": {"Elokuva": "", "Katsojat": []},"21:00": {"Elokuva": "", "Katsojat": []}},
            "Sali3": {"15:00": {"Elokuva": "", "Katsojat": []},"18:00": {"Elokuva": "", "Katsojat": []},"21:00": {"Elokuva": "", "Katsojat": []}}
            } ,
"Lauantai": 
            {
            "Sali1": {"15:00": {"Elokuva": "", "Katsojat": []},"18:00": {"Elokuva": "", "Katsojat": []},"21:00": {"Elokuva": "", "Katsojat": []}},
            "Sali2": {"15:00": {"Elokuva": "", "Katsojat": []},"18:00": {"Elokuva": "", "Katsojat": []},"21:00": {"Elokuva": "", "Katsojat": []}},
            "Sali3": {"15:00": {"Elokuva": "", "Katsojat": []},"18:00": {"Elokuva": "", "Katsojat": []},"21:00": {"Elokuva": "", "Katsojat": []}}
            }
}
#Elokuvakirjasto: Tallennetaan erillistiedostoon!!! Lisää elokuvatiedoston lataus lisää_elokuva funktioon!
elokuvat = {}






#### # #   PÄÄOHJELMA # # ####

#Ohjelman aloitus funktio
def aloitus():
        
    print("\nTervetuloa AreCinemaan!\n")
    print(f"Avataan valikko...:\n, {valikko()}") 
    time.sleep(1)   

#Funktiolla Valitaan asiakas tai ylläpitäjä
def valikko():

    print("\n1. Avaa asiakasnäkymä\n2. Avaa ylläpitäjänäkymä\n")


    try:
        valinta = int(input("Valitse toiminto 1 | 2 : "))
    except ValueError:
        print("Käytitkö kirjaimia? Tarkista syöte!\n")
        time.sleep(1)
        valikko()


    if valinta == 1:
        time.sleep(1)
        print("\nAvataan asiakassivut...\n\n")
        time.sleep(1)
        asiakas()



    #Pyytää salasanan 1234, jos väärin -> palaa valikkoon
    elif valinta == 2:
        sala = input("Anna salasana: ")
        if sala == "1234":
            time.sleep(1)
            print("\nAvataan AreCinema ylläpitosivut...\n")
            yllapito()
        else:
            print("Salasana on väärin...\n")
            time.sleep(1)
            valikko()
    else:
        print("Tarkista syöttämäsi arvo!\n")
        time.sleep(2)
        valikko()



#### Asiakkaan funtkiot:

#Asiakassivun aloitus #### VIRHEKORJATTU
def asiakas():
    print(f"AreCinema esittää: \n")
    #Listaa näytillä olevat elokuvat jossa avain järjestysnumerona, ladattu tiedostosta 
    with open("elokuvalista.txt", "r") as t:
        sisalto = eval(t.read())
    for avain in sisalto:
        print(sisalto[avain])

    #Asiakas valitsee
    print("\n1. Varaa elokuvaliput\n2. Palaa etusivulle.")
    try:
        valinta = int(input("\nValitse toiminto 1 | 2 : "))
    except ValueError:
        print("Käytitkö kirjaimia? Tarkista syöte!\n")
        time.sleep(1)
        asiakas()

    if valinta == 1:
        lisaa_varaus()
    
    elif valinta == 2:
        print("Takaisin etusivulle...\n")
        time.sleep(1)
        valikko()
    else:
        print("Tarkista syöte!\n")
        time.sleep(1)
        valikko()

#Varauksen lisääminen elokuvasaliin #### VIRHEKORJATTU
def lisaa_varaus():
    seuraava = input("\nUusi varaus? kyllä/ei: ")
    while seuraava != "ei":

        #valitaan päivä ja talennetaan se tuplen avulla oikeaan muotoon jotta voi viitata kalenteriin

        try:
            p = int(input("Valitse päivä: \n1. Maanantai\n2. Tiistai\n3. Keskiviikko\n4. Torstai\n5. Perjantai\n6. Lauantai\nValinta: "))
        except ValueError:
            print("Kirjoititko kirjaimen? Tarkista syöte.\n")
            time.sleep(1)
            asiakas()
        except UnboundLocalError:
            print("Jotain meni pieleen, palataan valikkoon.\n")
            time.sleep(1)
            asiakas()
        if p > 6 or p < 1:

            print("Tarkista syöte!\n")
            time.sleep(1)
            asiakas()
        
        p -= 1
        p = p_tuple[p]
        print("\n")
        #valitse sali.. ja muuttujaan
        
        try:
            s = int(input("Valitse sali: \n1. Sali 1 (max 5 paikkaa)\n2. Sali 2 (max 10 paikkaa)\n3. Sali 3 (max 15 paikkaa)\nValinta: "))
        except ValueError:
            print("Kirjoititko kirjaimen? Tarkista syöte.\n")
            time.sleep(1)
            asiakas()
        except UnboundLocalError:
            print("Jotain meni pieleen, palataan valikkoon.\n")
            time.sleep(1)
            asiakas()

        if s > 3 or s < 1:

            print("Tarkista syöte!\n")
            time.sleep(1)
            asiakas()                 
        s -= 1
        #Asettaa valitulle salille maximi tilan
        if s == 0:
            s_max = 5
        elif s == 1:
            s_max = 10
        elif s == 2:
            s_max = 15

        s = s_tuple[s]
        print("\n")


        #valise näytösaika.. ja muuttujaan
        try:
            n = int(input("Valitse näytösaika: \n1. 15:00\n2. 18:00\n3. 21:00\nValinta: "))
        except ValueError:
            print("Kirjoititko kirjaimen? Tarkista syöte.\n")
            time.sleep(1)
            asiakas()
        except UnboundLocalError:
            print("Jotain meni pieleen, palataan valikkoon.\n")
            time.sleep(1)
            asiakas()

        if n > 3 or n < 1:

            print("Tarkista syöte!\n")
            time.sleep(1)
            asiakas() 
        n -= 1
        n = n_tuple[n]
        k = e_k_tuple[1]
        e = e_k_tuple[0]
        print("\n")
        nimi = input("Katsojan nimi: ")
        #valitse päivä 1, 2, 3 ... ma ti ke ...
     
        print(f"Varauksen tiedot: \nNimi: {nimi}\nPäivä: {p}\nNäytös: {n}")

        

        #avataan lukumuodossa ja tallennetaan muuttujaan t
        with open("varauskalenteri.txt", "r") as t:
            sisalto = eval(t.read())
            #Löytää tiedot elokuvasta ja listan katsojista, laskee asiakasmäärän salissa ja hyväksyy varauksen vain jos on tilaa.
            if len(sisalto[f"{p}"][f"{s}"][f"{n}"][f"{k}"]) < s_max:
                sisalto[f"{p}"][f"{s}"][f"{n}"][f"{k}"] += [f"{nimi}"]
                print("Elokuva:", sisalto[f"{p}"][f"{s}"][f"{n}"][f"{e}"], "\n")
            else:
                print ("Sali on täynnä, valitse toinen näytösaika tai sali.")
        #avataan kirjoitusmuotoon ja tallenetaan muutettuu kalenteri tiedostoon ( toivottavasti saadaan tieto päivitettyä )
        with open("varauskalenteri.txt", "w") as t:
            t.write(str(sisalto))


        uusi = input("Uusi varaus? kyllä/ei: ")

        if uusi == "ei":
            valikko()

#### Ylläpitäjän funktiot: #### VIRHEKORJATTU
def yllapito():
    print("\nTervetuloa ylläpitojärjestelmään!\n")
    print("1. Lisää elokuva kirjastoon.")
    print("2. Listaa elokuvakirjasto.")
    print("3. Lisää näytösaika.")
    print("4. Selaa varauksia.")
    print("5. Alusta varaukset.")
    print("\nKirjaudu ulos syöttämällä 0 (nolla) ja ENTER\n")

    try:
        valinta = int(input("Valitse toiminto 1 | 2 | 3 | 4 | 5 : "))
    except ValueError:
        print("Syötitkö kirjaimen? Tarkista syöte.")
        time.sleep(1)
        yllapito()
    #Lisäys toimii, mutta tiedoston lataus ja tallennus täytyy lisätä funktioon
    if valinta == 1:
        lisaa_elokuva()
    #Listaus toimii
    elif valinta == 2:
        print("\nKijastossa olevat elokuvat: \n")
        with open("elokuvalista.txt", "r") as t:
            sisalto = eval(t.read())
        for avain in sisalto:
            print(sisalto[avain])
        time.sleep(3)
        yllapito()
    elif valinta == 3:
        lisaa_naytos()
        yllapito()
    elif valinta == 4:
        #Alkuun sama menetelmä kuin valintaan kolme
        print("\nListataan varaukset:\n\n")
        varaukset()
        yllapito()

    #Kalenterin nollaus toimii
    elif valinta == 5:
        print("\nOletko varma?")
        varma = input("kyllä/ei: ")
        if varma != "ei":

            nollaa_kalenteri(paivat_aloitus, elokuvat)
            print("Kalenteri nollattu!\n")
            print("Odota hetki...\n")
            time.sleep(1)
            yllapito()
    elif valinta == 0:
        aloitus()
    else:
        print("Tarkista syöttämäsi arvo!")
        time.sleep(1)
        yllapito()

#!!!Toimii!!!
#Lataa tiedosto kopioksi muuttujaan ==> Viittaa: päivä > sali > kellonaika -> lisää "Elokuva": _nimi_elokuvan_  ==> Tallenna tiedostokopio vanhan päälle
def lisaa_naytos():
    seuraava = input("\nLisää uusi näytösaika elokuvalle? kyllä/ei: ")
    while seuraava != "ei":

        #valitaan päivä ja talennetaan se tuplen avulla oikeaan muotoon jotta voi viitata kalenteriin
        try:
            p = int(input("Valitse päivä: \n1. Maanantai\n2. Tiistai\n3. Keskiviikko\n4. Torstai\n5. Perjantai\n6. Lauantai\nValinta: "))
        except ValueError:
            print("Kirjoititko kirjaimen? Tarkista syöte.")
            time.sleep(1)
            yllapito()
        except UnboundLocalError:
            print("Jotain meni pieleen, palataan valikkoon.")
            time.sleep(1)
            yllapito()

        if p > 6 or p < 1:
            print("Tarkista syöttämäsi arvo!")
            time.sleep(1)
            yllapito()


        p -= 1
        p = p_tuple[p]
        print("\n")
        #valitse sali.. ja muuttujaan
        try:
            s = int(input("Valitse sali: \n1. Sali 1 (max 5 paikkaa)\n2. Sali 2 (max 10 paikkaa)\n3. Sali 3 (max 15 paikkaa)\nValinta: "))
        except ValueError:
            print("Kirjoititko kirjaimen? Tarkista syöte.")
            time.sleep(1)
            yllapito() 
        except UnboundLocalError:
            print("Jotain meni pieleen, palataan valikkoon.")
            time.sleep(1)
            yllapito()
        if s > 3 or s < 1:
            print("Tarkista syöttämäsi arvo!")
            time.sleep(1)
            yllapito()

        s -= 1
        s = s_tuple[s]
        print("\n")
        #valise näytösaika.. ja muuttujaan
        try:
            n = int(input("Valitse näytösaika: \n1. 15:00\n2. 18:00\n3. 21:00\nValinta: "))
        except ValueError:
            print("Kirjoititko kirjaimen? Tarkista syöte.")
            time.sleep(1)
            yllapito()
        except UnboundLocalError:
            print("Jotain meni pieleen, palataan valikkoon.")
            time.sleep(1)
            yllapito()
        if n > 3 or n < 1:
            print("Tarkista syöttämäsi arvo!")
            time.sleep(1)
            yllapito()

        n -= 1
        n = n_tuple[n]
        e = e_k_tuple[0]
        print("\n")
        print("Valitse elokuva: ")

        with open("elokuvalista.txt", "r") as t:
            sisalto = eval(t.read())
        for avain in sisalto:
            print(f"{avain}. {sisalto[avain]}")   
        try:     
            elokuva = int(input("Elokuvan numero: "))
        except ValueError:
            print("Syötitkö kirjaimen? Tarkista syötteen arvo.")
            time.sleep(1)
            yllapito()
        if elokuva < 1 or elokuva > len(sisalto.keys()):
            print("Tarkista syöttämäsi arvo.")
            time.sleep(1)
            yllapito()

        elokuva = sisalto[elokuva]
        #valitse päivä 1, 2, 3 ... ma ti ke ...
     
        print("\nNäytöksen tiedot:", "\nElokuva:", elokuva," Päivä:", p, " Sali:", s, " Näytös:", n)

        

        #avataan lukumuodossa ja tallennetaan muuttujaan t
        with open("varauskalenteri.txt", "r") as t:
            sisalto = eval(t.read())
            #Löytää tiedot elokuvasta ja listan katsojista, laskee asiakasmäärän salissa ja hyväksyy varauksen vain jos on tilaa.
            if len(sisalto[f"{p}"][f"{s}"][f"{n}"][f"{e}"]) < 1:
                sisalto[f"{p}"][f"{s}"][f"{n}"][f"{e}"] = elokuva
                print(sisalto[f"{p}"][f"{s}"][f"{n}"])
            else:
                print("Näytösajalle on kirjattu jo elokuva! Valitse toinen näytösaika tai sali.")
        #avataan kirjoitusmuotoon ja tallenetaan muutettuu kalenteri tiedostoon ( toivottavasti saadaan tieto päivitettyä )
        with open("varauskalenteri.txt", "w") as t:

            t.write(str(sisalto))

        #Tulosta tarjolla olevat salit ja elokuvat
    

        #ohjelma tarkastaa onko näytöksessä tilaa
        #ohjelma tallentaa oikeaan päivään ja näytökseen varauksen
        #tallenna_tiedot(potilastiedot, asiakasnumero, nimi, laji, syntyma, syy)
        #print(potilastiedot)

        uusi = input("\nUusi näytösaika? kyllä/ei: ")

        if uusi == "ei":
            time.sleep(1)
            yllapito()
        

# !! Toimii !!
def lisaa_elokuva():
    print("\nLisää elokuva elokuvakirjastoon.\n")

    with open("elokuvalista.txt", "r") as t:
        sisalto = eval(t.read())
    
    elokuva = input("Anna elokuvan nimi: ")
    n = len(sisalto.keys()) + 1
    sisalto[n] = elokuva
    print("\nElokuvat:\n", sisalto, "\n")

    #avataan kirjoitusmuotoon ja tallentaa elokuvan nimen avaimella tekstinä tiedostoon
    with open("elokuvalista.txt", "w") as t:
        t.write(str(sisalto))
        

    print("1. Lisää uusi elokuva.")
    print("2. Palaa ylläpitäjän valikkoon")
    valinta = int(input("Valitse toiminto: 1 | 2: "))
    if valinta == 1:
        lisaa_elokuva()
    else:
        yllapito()

#printtaa koko varauskalenterin järjestyksessä.   
def varaukset():
    with open("varauskalenteri.txt", "r") as t:
        sisalto = eval(t.read())
        pp = pprint.PrettyPrinter(depth=5, sort_dicts=False)
        
        pp.pprint(sisalto)

  

    tulos = input("Jatkaaksesi paina ENTER. ")

#Kirjoittaa kalenteripohjatn txt tiedostoon eli NOLLAA TIEDOSTON VARAUKSET
def nollaa_kalenteri(sana: dict, elokuvat: dict):
    with open("varauskalenteri.txt", "w") as t:
        sana = str(sana)
        t.write(sana)
    with open("elokuvalista.txt", "w") as t:
        elokuvat = str(elokuvat)
        t.write(elokuvat)




#Ohjelman suoritus
aloitus()