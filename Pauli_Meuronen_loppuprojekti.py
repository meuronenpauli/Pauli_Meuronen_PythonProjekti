#Luokkien tuonti
from Luokka import Treeni
from Luokka import Harjoitus

#Funktiot
def uusiTreeni():
    tempTreeni = []
    valinta = int
    while valinta != 0:
        valinta = int(input("Valitse harjoiteltavat lihasryhmät seuraavista: 1. hartiat, 2. rinta, 3. hauis, 4. ojentaja, 5. vatsa, 6. selkä, 7. jalat. Valitse 0, kun olet valinnut kaikki haluamasi lihasryhmät. "))
        if valinta == 1:
            print("Hartiatreenin suosittelen yhdistämään rinta- ja ojentajatreenin kanssa. Kyse on työntävistä ja kättä suoristavista lihasryhmistä, jotka toimivat yhdessä kineettisenä ketjuna.")
            print("Hartiatreenissä voit tehdä esimerkiksi pystypunnerruksia ja pystysoutuja.")  
            nimi = "hartiat"
            lihasryhma = Treeni(nimi)
            tempTreeni.append(lihasryhma)
        elif valinta == 2:
            print("Rintalihastreenin suosittelen yhdistämään hartia- ja ojentajatreenin kanssa. Kyse on työntävistä ja kättä suoristavista lihasryhmistä, jotka toimivat yhdessä kineettisenä ketjuna.")
            print("Rintalihastreenissä voit tehdä esimerkiksi penkkipunnerruksia ja vinopenkkitoistoja.")
            nimi = "rinta"
            lihasryhma = Treeni(nimi)
            tempTreeni.append(lihasryhma)
        elif valinta == 3:
            print("Hauistreenin suosittelen yhdistämään selkätreenin kanssa. Kyse on vetävistä ja kättä koukistavista lihasryhmistä, jotka toimivat yhdessä kineettisenä ketjuna.")
            print("Hauistreenissä voit tehdä esimerkiksi hammer-kääntöjä ja scott-penkkitoistoja.")
            nimi = "hauikset"
            lihasryhma = Treeni(nimi)
            tempTreeni.append(lihasryhma)
        elif valinta == 4:
            print("Ojentajatreenin suosittelen yhdistämään hartia- ja rintatreenin kanssa. Kyse on työntävistä ja kättä suoristavista lihasryhmistä, jotka toimivat yhdessä kineettisenä ketjuna.")
            print("Ojentajatreenissä voit tehdä esimerkiksi ranskalaisia punnerruksia ja dippejä.")
            nimi = "ojentajat"
            lihasryhma = Treeni(nimi)
            tempTreeni.append(lihasryhma)
        elif valinta == 5:
            print("Vatsatreenin voi yhdistää melkeinpä mihin tahansa muuhun treeniin tai tehdä yksittäisenäkin treeninä. Älä kuitenkaan yhdistä selkätreeniin, sillä kyse on vastasuorittajaparista eli lihasryhmät tekevät työtä toisiaan vastaan.")
            print("Vatsalihastreenissä voit tehdä esimerkiksi vatsarutistuksia ja linkkuveitsitoistoja.")
            nimi = "vatsa"
            lihasryhma = Treeni(nimi)
            tempTreeni.append(lihasryhma)
        elif valinta == 6:
            print("Selkätreenin suosittelen yhdistämään hauistreenin kanssa. Kyse on vetävistä ja kättä koukistavista lihasryhmistä, jotka toimivat yhdessä kineettisenä ketjuna.")
            print("Selkälihastreenissä voit tehdä esimerkiksi kulmasoutuja ja leuanvetoja.")
            nimi = "selkä"
            lihasryhma = Treeni(nimi)
            tempTreeni.append(lihasryhma)
        elif valinta == 7:
            print("Jalat kannattaa tehdä ihan omana treenikokonaisuutenaan tai jopa purkaa pienempiin osiin. Kyse on suurista lihaksista ja useista lihasryhmistä, joiden treenaaminen vie paljon sekä aikaa, että energiaa.")
            print("Jalkatreenissä voit tehdä esimerkiksi jalkaprässitoistoja, päkiänousuja ja pakarasiltatoistoja.")
            nimi = "jalat"
            lihasryhma = Treeni(nimi)
            tempTreeni.append(lihasryhma)
    return tempTreeni

#Ohjelma
print ("Hei! Minä olen salikaverisi GymBuddy. Autan sinua suunnittelemaan ja toteuttamaan salitreenisi.")
print ("Suosittelen treenaamaan maksimissaan kolmea, toisiaan tukevaa lihasryhmää samalla treenikerralla. Autan sinua koostamaan sinua parhaiten hyödyntävän treenikokonaisuuden")

kokoTreeni = uusiTreeni()
for lihasryhma in kokoTreeni:
    valinta = 1
    while valinta != 0:
        print("Minkä", lihasryhma.nimi, "-treenin liikkeen suoritat?:")
        harjoite = input()
        print("Montako sarjaa teet?:")
        sarjat = int(input())
        print("Montako toistoa teet sarjassa?:")
        toistot = int(input())
        print("Arvioi liikesarjan kuormitus (1 = kevyt, 2 = kohtalainen, 3 = raskas):")
        kuormitus = int(input())      
        lihasryhma.liikkeet.append(Harjoitus(harjoite, sarjat, toistot, kuormitus))
        print(harjoite, "lisätty", lihasryhma.nimi, "-treeniin.\nValitse 0 siirtyäksesi seuraavaan lihasryhmään, tai 1 lisätäksesi uuden liikkeen.")
        valinta = int(input())

for lihasryhma in kokoTreeni:
    valinta = 1
    while valinta != 0:
        for lihasryhma in kokoTreeni:
            print("Lihasryhmän", lihasryhma.nimi, "-treenissäsi ovat seuraavat harjoitteet:")
            kokonaisRasitus = 0
            rasitusRaja = 5
            for harjoite in lihasryhma.liikkeet:
                print("-", harjoite.nimi, ", jonka arvioimasi kuormitus on", harjoite.kuormitus)
                kokonaisRasitus += harjoite.kuormitus
            print("Lihasryhmän", lihasryhma.nimi, "liikkeiden arvioimasi kokonaisrasitus on", kokonaisRasitus)
            if kokonaisRasitus > rasitusRaja:
                print("Teet ilmeisesti vähintään useita kevyempiä liikesarjoja, tai muutaman raskaan. Muista lämmittää treenaamasi lihasryhmä hyvin, ennen kuin aloitat varsinaisen treenin, jottet loukkaa itseäsi. Myös venyttelyn merkitys raskaiden treeniessä jälkeen korostuu.")
            elif kokonaisRasitus <= rasitusRaja:
                print("Teet ilmeisesti kevyemmän tai lyhyemmän treenikokonaisuuden. Vaikka siirtyisit suoraan treeniohjelmaan ilman lämmittelyä, tee lopuksi vähintään lyhyitä dynaamisia venytyksiä optimoidaksesi palautumisesi.")
        print("Valitse 0, mikäli haluat minun tulostavan valmiin treenilistasi")
        valinta = int(input())

for lihasryhma in kokoTreeni:
    print("Lihasryhmän", lihasryhma.nimi, "-treenissäsi on seuraavat liikkeet:")
    for harjoite in lihasryhma.liikkeet:
        print("-", harjoite.nimi, ": ", harjoite.sarjat, "x", harjoite.toistot, ", eli yhteensä", harjoite.sarjat*harjoite.toistot, "toistoa.")