from pymongo import MongoClient as MC

CONNECTION_STRING = "mongodb+srv://kvnvg2:GEepZ7Mf7zqVWP5G@cluster0.dniynqz.mongodb.net/"
DATABASE = "RH_db"


def get_collection(col):
    cluster = MC(CONNECTION_STRING)
    database = cluster[DATABASE]
    collection = database[col]
    return collection

#henter ut all data som ligger i en mappe i mongodv.
#in data er navn på mappen jeg ønsker og hente.
def print_mappe(inndata="elever"):
    col = get_collection(inndata).find()
    listeOfdata = []
    for c in col:
        listeOfdata.append(c)
    return listeOfdata


def lagre_objekt(indata="elever"):
    fornavn = input("legg til ditt fornavn: ")
    etternavn = input("legg til ditt etternavn: ")
    alder = input("alder: ")
    skole = input("skole: ")
    nyelev = {"fornavn": fornavn, "etternavn": etternavn, "alder": alder, "skole": skole}
    get_collection(indata).insert_one(nyelev)



def slett_objekt(indata="elever"):
    col = get_collection(indata)
    fornavn = input("skriv in fornavn på personen du ønsker og slette: ")
    etternavn = input("skriv in etternavnet på personen du ønsker og slette: ")
    col.delete_one({"fornavn": fornavn, "etternavn": etternavn})

    print(f"vi har sletten eleven med navn: {fornavn} {etternavn}")

def rediger_objekt(indata="elever"):
    col = get_collection(indata)
    fornavn = input("skriv in fornavn på personen du ønsker og redigere: ")
    etternavn = input("skriv in etternavnet på personen du ønsker og redigere: ")
    nyttfornavn = input("skriv in nytt fornavn: ")
    nyttetternavn = input("skriv in nytt etternavn: ")
    nyttalder = input("skriv in ny alder: ")
    nyskole = input("skriv in ny skole: ")
    filter = {"fornavn": fornavn, "etternavn": etternavn}
    updatering = {'$set': {'fornavn': nyttfornavn, 'etternavn': nyttetternavn, 'alder': nyttalder, 'skole': nyskole}}
    col.update_one(filter, updatering)




def menu_menu():
    while True:
        print("Velkommen til mitt fengsel: ")
        print("1. får og legge til elev: ")
        print("2. får og slette elver: ")
        print("3. får og skrive ut alle elever: ")
        print("4 får og rediger elever status: ")
        print("0. får og piss off: ")
        valg = input("velg et nummer fra listen over: ")
        if valg == "1":
            lagre_objekt()
        
        elif valg == "2":
            slett_objekt()

        elif valg == "3":
            liste = print_mappe()
            print(liste)

        elif valg == "4":
            rediger_objekt()

        elif valg == "0":
            print("Will you kindly piss off my good sir, have a nightmare filled night :)")
            break

menu_menu()
