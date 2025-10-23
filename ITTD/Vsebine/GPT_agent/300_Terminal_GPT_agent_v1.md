 Uporaba GPT API za izdelavo pomočnika za učitelje**
================================================================================

Cilji
- Študent razume osnovno strukturo Python programa za klepet z AI.
- Študent zažene program in vodi preprost pogovor z agentom.
- Študent prilagodi navodila agenta in opazi razliko v odzivih.


1. Uvod (2 min)
   - Pojasnite namen: preprost klepetalni agent za pomoč učiteljem (glej `AI_AGENT_INSTRUCTIONS` v kodi).

2. Pregled kode (5 min)
   - `client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))` — pojasnite pomen API ključa in varnega shranjevanja v okoljski spremenljivki.
   - `AI_AGENT_INSTRUCTIONS` — razložite, kako sistemska navodila usmerjajo vedenje agenta.
   - Funkcija `start_chat()` in zanka `while True` — kako program bere uporabnikov vhod in omogoča večizmenjave.
   - `response = client.responses.create(...)` — kje kličemo model; poudarite parameter `model="gpt-5-nano"`.
   - Izhodišče za izhod: vnos `exit` ali `quit`.

3. Zagon in testiranje (8–12 min)
   - Študenti zaženejo skripto (`python ime_datoteke.py`).
   - Vpišejo nekaj vprašanj učne narave (npr. "Predlagaj aktivnost za 5. razred o vezjih").
   - Opazujejo odzive in zapišejo eno izboljšavo navodil.

4. Kratka modifikacija (5–8 min)
   - Spremenite `AI_AGENT_INSTRUCTIONS` (npr. dodajte omejitev dolžine odgovora ali primer ciljne starosti) in ponovno zaženite klepet.
   - Primer spremembe: dodajte "Odgovarjaj kratko in preprosto, primerno za 10–11 let stare učence."

5. Zaključek in refleksija (2–3 min)
   - Povprašajte, kako so spremembe navodil vplivale na odgovore.
   - Etika/sigurnost: ne vnesti občutljivih podatkov v pogovor; preveriti dejstva, preden se uporabi v učnem procesu.

Hitri nasveti
- Če model ne odgovarja, preverite `OPENAI_API_KEY` in internetno povezavo.
- Za podaljšane funkcije lahko dodate orodja v parameter `tools` (trenutno zakomentirano).


```python
#!/usr/bin/env python3
import os
from openai import OpenAI

# 🔧 Nastavi svoj API ključ
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# 🧠 Navodila ai agenta
AI_AGENT_INSTRUCTIONS = """
Ti si AI pomočnik učitelju tehnike in tehnologije v osnovni šoli.
Tvoja naloga je pomagati pri pripravi učnih ur, pri iskanju idej za učne dejavnosti,
ter pri oblikovanju preprostih razlag za učence.
"""

def start_chat():
    print("\nZačni pogovor (vpiši 'exit' za izhod)\n")

    while True:
        user_input = input("👤 Ti: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            print("🔚 Pogovor zaključen.")
            break

        response = client.responses.create(
            model="gpt-5-nano",
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
