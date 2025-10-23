SHRANJEVANJE POGOVORA
================================================================================

Cilji
- Razumeti, kje program hrani `conversation_id` in kako se upravlja s pogovori.
- Nadgraditi program, da poleg `conversation_id` dosledno shranjuje tudi vsebino pogovora v JSON datoteko.

1. Pregled kode:
   - `CONVERSATIONS_FILE = "conversations.json"` — ime datoteke za shranjevanje.
   - `load_conversations()` — naloži obstoječe pogovore iz JSON (če obstaja).
   - `save_conversations(conversations)` — SHRANJEVALNA funkcija, uporablja `json.dump(..., ensure_ascii=False, indent=4)`.
   - `get_conversation(conversations)` — ustvari nov pogovor z `client.conversations.create()` in nastavi `CONVERSATION_ID`, ter takoj kliče `save_conversations(conversations)` po kreaciji.
   - V zanki `start_chat()` ob uspešnem odgovoru:
     - Dodajanje v sporočila: `conversation["messages"].append({ "question": user_input, "response": answer })`
     - Posodobitev slovarja: `conversations[CONVERSATION_ID] = conversation`
     - Shranjevanje: `save_conversations(conversations)`

2. Naloga študentom (implementacija / preverjanje):
   - Zaženi program in začni nov pogovor — preveri, da se ob ustvarjanju novega ID-ja v `conversations.json` pojavi prazen vnos (funkcija `get_conversation` + `save_conversations`).
   - Pošlji nekaj vprašanj in preveri, da se v `conversations.json` pojavi polje `messages` z elementi, ki imajo `question` in `response` (del v `start_chat()` kjer se uporablja `conversation["messages"].append(...)` in `save_conversations(conversations)`).
   - Spremljaj, ali `load_conversations()` pravilno naloži shranjeno strukturo ob ponovnem zagonu.

3. Kratka razširitev (dodatna točka):
   - Dodajte časovni žig (timestamp) na vsak vnos v `messages` pred klicem `save_conversations`. To uredite v bloku:
     ```
     conversation["messages"].append({
         "question": user_input,
         "response": answer,
         "timestamp": ...
     })
     save_conversations(conversations)
     ```
   - Preverite JSON z orodjem (npr. `jq` ali tekstovni urejevalnik).

Kaj naj učenci preverijo kot rezultat
- `conversations.json` vsebuje ključ z `CONVERSATION_ID` in polje `messages` z vprašanji in odgovori.
- Funkcije `load_conversations()` in `save_conversations()` delujejo brez napak pri zapiranju/odpiranju datoteke.
- Ob ponovnem zagonu se program lahko poveže na obstoječi pogovor (če nastavite `CONVERSATION_ID`) in naloži zgodovino.

Posebno poudarjeno (koda za shranjevanje)
- Funkcija za pisanje v datoteko: `save_conversations(conversations)` (uporablja `json.dump`).
- Mesto kjer se dodaja zapis in takoj shranjuje: v `start_chat()` po prejemu `answer`:
  ```
  conversation["messages"].append({
      "question": user_input,
      "response": answer
  })
  conversations[CONVERSATION_ID] = conversation
  save_conversations(conversations)
  ```

Varnost in dobra praksa
- Ne shranjujte občutljivih podatkov brez soglasja.
- Uporabite `ensure_ascii=False` in `encoding="utf-8"` (že prisotno) za pravilno kodiranje slovenskih znakov.
- Pri večprocesnem dostopu bi razmislili o zaklepanju datoteke (out of scope za vajo).

Končni rezultat
- Kratek eksperiment: izvedite pogovor, zaprite program, ponovno zaženite in potrdite, da se zgodovina iz `conversations.json` naloži in prikaže.


```python
import os
import json
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 🧠 Navodila asistenta
AI_AGENT_INSTRUCTIONS = """
Ti si AI pomočnik učitelju tehnike in tehnologije v osnovni šoli.
Tvoja naloga je pomagati pri pripravi učnih ur, pri iskanju idej za učne dejavnosti,
ter pri oblikovanju preprostih razlag za učence. 
"""

# 🔁 Če želiš nadaljevati obstoječi pogovor, sem vnesi npr. "conv_abc123..."
CONVERSATION_ID = ""
CONVERSATIONS_FILE = "conversations.json"


def load_conversations():
    """Naloži pogovore iz datoteke, če obstaja."""
    if os.path.exists(CONVERSATIONS_FILE):
        with open(CONVERSATIONS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


def save_conversations(conversations):
    """Shrani pogovore v datoteko."""
    with open(CONVERSATIONS_FILE, "w", encoding="utf-8") as f:
        json.dump(conversations, f, indent=4, ensure_ascii=False)


def get_conversation(conversations):
    """Preveri, ali obstaja pogovor, sicer ustvari novega."""
    global CONVERSATION_ID
    if not CONVERSATION_ID or CONVERSATION_ID not in conversations:
        conv = client.conversations.create()
        CONVERSATION_ID = conv.id
        print(f"[Ustvarjen nov ID pogovora]: {CONVERSATION_ID}")
        conversations[CONVERSATION_ID] = {"messages": []}
        save_conversations(conversations)
    else:
        print(f"[Nadaljujem pogovor]: {CONVERSATION_ID}")
    return conversations[CONVERSATION_ID]


def start_chat():
    conversations = load_conversations()
    conversation = get_conversation(conversations)

    print("\nZačni pogovor (vpiši 'exit' za izhod)\n")

    # Naloži prejšnje pogovore
    if conversation["messages"]:
        print("📜 Prejšnji pogovori:")
        for msg in conversation["messages"]:
            print(f"👤 {msg['question']}")
            print(f"🧠  {msg['response']}\n")

    while True:
        user_input = input("👤 Ti: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            print("🔚 Pogovor zaključen.")
            break

        response = client.responses.create(
            model="gpt-4.1-mini",
            conversation=CONVERSATION_ID,
            input=[
                {"role": "system", "content": AI_AGENT_INSTRUCTIONS},
                {"role": "user", "content": user_input},
            ],
            tools=[
               # {
               #     "type": "file_search",
               #     "vector_store_ids": ["vs_68f0014fe51c819184b6c36568f1ade0"],
               # }
            ],
        )

        answer = response.output_text
        print(f"🧠 Asistent: {answer}\n")

        # Shrani vprašanje in odgovor v datoteko
        conversation["messages"].append({
            "question": user_input,
            "response": answer
        })
        conversations[CONVERSATION_ID] = conversation
        save_conversations(conversations)


if __name__ == "__main__":
    start_chat()
```
