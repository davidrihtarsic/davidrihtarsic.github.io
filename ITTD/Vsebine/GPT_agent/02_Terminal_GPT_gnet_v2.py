from openai import OpenAI
import os
my_api_key=os.environ.get("ITTD_OPENAI_API_KEY")
client = OpenAI(api_key=my_api_key)
# -----------------------------------------
# Ustvarimo zgodovino pogovora
# -----------------------------------------
# Zgodovina bo v obliki seznama slovarjev, kjer hranimo celotno zgodovino pogovora.
zgodovina_pogovora = [
    {
        "role": "system",   # Nastavitev kako naj pomočnik deluje
        "content": "Ti si pomočnik za pomoč učitelju pri poučevanju tehnike in tehnologije"
    }
]

while True:
    vprasanje=input("Jaz:\n")

    zgodovina_pogovora.append(
        {
            "role":"user",
            "content": vprasanje,
        }
    )

    try: 
        pogovor = client.chat.completions.create(
        messages = zgodovina_pogovora[-5:],
        model="gpt-4o-mini",  # Izbrani model [gpt-40-mini je najcenejši]
        stream=True,          # Boljša izkušnja, če se delčki besedila dopolnjujejo...
        )

        # Prikaz odgovora modela
        print("GPT-4o-mini:")
        for delcek_besedila in pogovor:
            print(delcek_besedila.choices[0].delta.content or "", end="")
        print("")

    except Exception as e:
        print(f"Prišlo je do napake: {str(e)}")

