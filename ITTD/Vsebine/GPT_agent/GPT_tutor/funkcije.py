from openai import OpenAI
import json
import os
my_api_key=os.environ.get("ITTD_OPENAI_API_KEY")
def shrani_pogovor(zgodovina_pogovora, ime_datoteke="pogovor.json"):
    """
    Shrani zgodovino pogovora v JSON datoteko.
    Args:
        zgodovina_pogovora (list): Seznam sporočil v zgodovini pogovora.
        ime_datoteke (str): Ime datoteke, kamor se shrani pogovor (privzeto: "pogovor.json").
    Delovanje:
    - Pretvori seznam sporočil v JSON format.
    - Shrani JSON podatke v datoteko.
    - Preveri, če datoteka že obstaja, in jo prepiše, če je to potrebno.
    """
    try:
        # Odpremo datoteko za pisanje
        with open(ime_datoteke, "w", encoding="utf-8") as datoteka:
            json.dump(zgodovina_pogovora, datoteka, indent=4, ensure_ascii=False)
        #print(f"Pogovor je bil uspešno shranjen v datoteko '{ime_datoteke}'.")
    except Exception as e:
        print(f"Prišlo je do napake pri shranjevanju pogovora: {str(e)}")

def nalozi_pogovor(ime_datoteke="pogovor.json"):
    """
    Naloži zgodovino pogovora iz JSON datoteke.
    Args:
        ime_datoteke (str): Ime datoteke, iz katere se naloži pogovor (privzeto: "pogovor.json").
    Returns:
        list: Seznam sporočil iz zgodovine pogovora (če datoteka obstaja in je veljavna).
              Če datoteka ne obstaja ali je prazna, vrne prazen seznam.
    Delovanje:
    - Preveri, ali datoteka obstaja.
    - Če obstaja, prebere podatke iz datoteke in jih pretvori v Pythonov seznam.
    - Če datoteka ne obstaja ali je prazna, vrne prazen seznam.
    """
    try:
        # Poskusi odpreti in prebrati datoteko
        with open(ime_datoteke, "r", encoding="utf-8") as datoteka:
            pogovor = json.load(datoteka)
            print(f"Zgodovina pogovora je uspešno naložena iz '{ime_datoteke}'.")
            return pogovor
    except FileNotFoundError:
        print(f"Datoteka '{ime_datoteke}' ne obstaja. Ustvarjen bo nov pogovor.")
        return []
    except json.JSONDecodeError:
        print(f"Datoteka '{ime_datoteke}' je poškodovana ali ni veljaven JSON. Ustvarjen bo nov pogovor.")
        return []
    except Exception as e:
        print(f"Prišlo je do napake pri nalaganju pogovora: {str(e)}")
        return []


zgodovina_pogovora = nalozi_pogovor()

#######################################
# OpenAI
#######################################
client = OpenAI(api_key=my_api_key)

def GPT_tutor(navodila, prompt):
    zgodovina_pogovora.append(
        {
            "role":"user",
            "content":prompt
        }
    )
    try: 
        pogovor = client.chat.completions.create(
            messages = navodila + zgodovina_pogovora[-5:],
            model="gpt-4o-mini",  # Izbrani model [gpt-40-mini je najcenejši]
            stream=True,          # Boljša izkušnja, če se delčki besedila dopolnjujejo...
        )

        # Prikaz odgovora modela
        odgovor_asistenta=""
        print("GPT-4o-mini:")
        for delcek_besedila in pogovor:
            nov_zlog = delcek_besedila.choices[0].delta.content or ""
            print(nov_zlog, end="")
            odgovor_asistenta += nov_zlog 
        print(" ")
        zgodovina_pogovora.append(
            {
                "role":"assistant",
                "content":odgovor_asistenta
            }
        )
        shrani_pogovor(zgodovina_pogovora)
    except Exception as e:
        print(f"Prišlo je do napake: {str(e)}")
    
