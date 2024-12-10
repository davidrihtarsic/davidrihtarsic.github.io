from openai import OpenAI
client = OpenAI(
    api_key="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"  # Tukaj pridobimo API ključ iz okoljske spremenljivke
)
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

