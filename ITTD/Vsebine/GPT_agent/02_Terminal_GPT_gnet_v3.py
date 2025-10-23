from openai import OpenAI
import os
my_api_key=os.environ.get("ITTD_OPENAI_API_KEY")
client = OpenAI(api_key=my_api_key)
navodila_asistenta = [
    {
        "role": "system",   # Nastavitev kako naj pomočnik deluje
        "content": "Ti si pomočnik za pomoč učitelju pri poučevanju tehnike in tehnologije."
    }
]
zgodovina_pogovora = []

def poslji_vprasanje(prompt):
    zgodovina_pogovora.append(
        {
            "role":"user",
            "content": vprasanje,
        }
    )

    try: 
        pogovor = client.chat.completions.create(
            messages = navodila_asistenta + zgodovina_pogovora[-5:],
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
        print("")
        return odgovor_asistenta
    except Exception as e:
        print(f"Prišlo je do napake: {str(e)}")

while True:
    vprasanje=input("Jaz:\n")
    if vprasanje == "q":
        print("Hvala za sodelovanje....")
        break
    odgovor=poslji_vprasanje(vprasanje)
    zgodovina_pogovora.append(
        {
            "role":"assistant",
            "content":odgovor
        }
    )
    

