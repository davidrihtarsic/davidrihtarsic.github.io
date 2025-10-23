UPORABA GPT API ZA USTVARJANJE INTERAKTIVNEGA TUTORJA
================================================================================


Cilji
- Razumeti vlogo `conversation_id` za ohranjanje in identifikacijo pogovora.
- Implementirati ustvarjanje novega pogovora ter uporabo obstoječega ID-ja.
- Testirati več sej in preveriti, kako se kontekst ohranja.

1. Preberi ključne dele kode:
   - Konstantna `CONVERSATION_ID` (vrh datoteke) — prednastavljen ID ali prazen niz.
   - Funkcija `get_conversation_id()` — ustvari nov pogovor, če ID ni določen, in nastavi globalno `CONVERSATION_ID`.
   - V `start_chat()` se pokliče `conversation_id = get_conversation_id()` in naprej `client.responses.create(..., conversation=conversation_id, ...)` — tu se poveže sporočanje z določenim pogovorom.

2. Kratek eksperiment:
   - a) Zaženi skripto z obstoječim `CONVERSATION_ID` in izvedi 2–3 vprašanja. Opazuj, da agent ohranja kontekst.
   - b) Nastavi `CONVERSATION_ID = ""` (prazno) in ponovno zaženi — preveri, da se v konzoli izpiše "[Ustvarjen nov ID pogovora]" in da se ustvari nov kontekst.
   - c) Kopiraj ustvarjeni ID in ponovno zaženi skripto z njim — potrditev, da se kontekst iz prejšnje seje nadaljuje.

3. Razširitev (izbirno, kratko):
   - Logiraj `conversation_id` + čas + uporabnikova sporočila v lokalno datoteko za sledljivost.
   - Dodaj ukaz `"/new"` v `start_chat()` za ročno ustvarjanje novega pogovora (pokliči `CONVERSATION_ID = ""` in `get_conversation_id()`).

Varnost in etika (kratko)
- Ne deli resničnih API ključev; uporabi okoljske spremenljivke (`OPENAI_API_KEY`).
- Pri beleženju pogovorov upoštevaj zasebnost (anominizacija/odobritev, če so občutljivi podatki).


```python
#!/usr/bin/env python3
import os
from openai import OpenAI

# 🔧 Nastavi svoj API ključ
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 🔁 Če želiš ohraniti isti pogovor, vnesi tu ID, npr. "conv_abc123..."
CONVERSATION_ID = ""

# 🧠 Navodila ai agenta
AI_AGENT_INSTRUCTIONS = """
Ti si AI pomočnik učitelju tehnike in tehnologije v osnovni šoli.
Tvoja naloga je pomagati pri pripravi učnih ur, pri iskanju idej za učne dejavnosti,
ter pri oblikovanju preprostih razlag za učence.
"""

def get_conversation_id():
    """Ustvari nov pogovor, če ID še ni določen."""
    global CONVERSATION_ID
    if not CONVERSATION_ID:
        conv = client.conversations.create()
        CONVERSATION_ID = conv.id
        print(f"[Ustvarjen nov ID pogovora]: {CONVERSATION_ID}")
    else:
        print(f"[Uporablja se obstoječi ID pogovora]: {CONVERSATION_ID}")
    return CONVERSATION_ID

def start_chat():
    conversation_id = get_conversation_id()
    print("\nZačni pogovor (vpiši 'exit' za izhod)\n")

    while True:
        user_input = input("👤 Ti: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            print("🔚 Pogovor zaključen.")
            break

        response = client.responses.create(
            model="gpt-5-nano",
            conversation=conversation_id,
            input=[
                {"role": "system", "content": AI_AGENT_INSTRUCTIONS},
                {"role": "user", "content": user_input}
            ]
        )

        print(f"\n🧠 Asistent: {response.output_text}\n")

if __name__ == "__main__":
    start_chat()
```

**Preverite**:

- Ali agent prepozna svojo vlogo vedno znova?
- Ali agent zna povazovati kontekst pogovora?

Če v klicu uporabljamo conversation_id, potem ni treba vsakič znova pošiljati sporočila sistema,

```
({"role": "system", "content": INSTRUCTIONS})
```

saj se pogovor beleži v celoti.  Smiselno pošiljanje ponovnih napotkov pa bi bilo v primeru, če želimo spremeniti sistemska navodila med pogovorom, ali pa da bi ai asistenta radi ponovno spomnili na njegova navodila.

Zato lahko funkcijo `start_chat()` dopolnite tako, da navodila pošljemo le ko pogovor začnemo znova.

```python
def start_chat():
    conversation_id = get_conversation_id()
    print("\nZačni pogovor (vpiši 'exit' za izhod)\n")

    this_is_first_message = True
    while True:
        user_input = input("👤 Ti: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            print("🔚 Pogovor zaključen.")
            break
        
        if this_is_first_message :
            # send system message only once at the beginning of the conversation
            system_message = {"role": "system", "content": AI_AGENT_INSTRUCTIONS}
        else:
            system_message = None

        input_messages = []
        if system_message:
            input_messages.append(system_message)
        input_messages.append({"role": "user", "content": user_input})  

        response = client.responses.create(
            model="gpt-5-nano",
            conversation=CONVERSATION_ID,
            input=input_messages
        )

        print(f"\n🧠 Asistent: {response.output_text}\n")
```

