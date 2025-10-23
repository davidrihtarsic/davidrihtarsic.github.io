from openai import OpenAI

# -----------------------------------------
# Konfiguracija API-ja
# -----------------------------------------
# Nastavimo ključ za dostop do OpenAI API-ja.
# Prepričajte se, da je API ključ shranjen kot okoljska spremenljivka z imenom OPENAI_API_KEY.

import os
my_api_key=os.environ.get("ITTD_OPENAI_API_KEY")
client = OpenAI(api_key=my_api_key)
# Nastavitev kjuča na takle način ni varna...
#client = OpenAI(
#    api_key="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"  # Tukaj pridobimo API ključ iz okoljske spremenljivke
#)

# -----------------------------------------
# Pošljemo sporočilo modelu
# glej navodila na:
#    https://github.com/openai/openai-python?tab=readme-ov-file#streaming-responses
# -----------------------------------------
try:
    pogovor = client.chat.completions.create(
        messages=[
            {
                "role": "system",   # Nastavitev kako naj pomočnik deluje
                "content": "Ti si pomočnik za pomoč učitelju pri poučevanju tehnike in tehnologije"
            },
            {
                "role": "user",     # Vloga pošiljatelja (uporabnik)
                "content": "Predstavi se in nelo na kratko opiši tvojo nalogo.",  # Vsebina sporočila
            }
        ],
        model="gpt-4o-mini",  # Izbrani model [gpt-40-mini je najcenejši]
        stream=True,          # Boljša izkušnja, če se delčki besedila dopolnjujejo...
    )

    # Prikaz odgovora modela
    print("GPT-4o-mini:")
    for delcek_besedila in pogovor:
        print(delcek_besedila.choices[0].delta.content or "", end="")

except Exception as e:
    print(f"Prišlo je do napake: {str(e)}")
