# Openai API modeli

OpenAI nam ponuja različne modele. Najosnovnejši je **text-davinci-003**, ki je tudi najbolj ugoden, a so t.i. **chat-based models** bistveno bolj zmogljivi in enostavnejši za uporabo. Namesto stare funkcionalnosti `messages` najdemo sodobnejše primere z uporabo **Responses**. Uporaba strukturiranega vnosa z vlogami (`system`, `user`, `assistant`) omogoča ohranjanje konteksta pogovora brez ponovnega pošiljanja celotne zgodovine. Če uporabljamo modele, ki ne podpirajo strukturiranih pogovorov, je še vedno potrebno ročno vključiti zgodovino v vsak nov klic (npr. pri starejših completions modelih).

Če imamo možnost uporabe chat-based modelov (npr. GPT‑4 preko Responses), lahko namesto ročnega sestavljanja zgodovine uporabimo strukturiran pristop z uporabo `input` (vloge) in ohranjanjem seznama sporočil v aplikaciji.

### Prednosti uporabe Responses s chat modelom:

1. Optimizacija: Ni potrebno pošiljati celotne zgodovine kot en dolg niz, ampak uporabimo strukturirane objekte.
2. Ohranjanje konteksta: Model prepozna vloge (`user`, `assistant`, `system`).
3. Enostavnost upravljanja zgodovine: Dovolj je le seznam sporočil, ki jih dodajamo sproti.

---

## Minimalni primeri kode (Python, Responses)

Python (Responses API, minimalno)
```python
import os
from openai import OpenAI

# 🔧 Nastavi svoj API ključ
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Začetni kontekst (seznam vlog)
conversation_input = [
    {"role": "system", "content": "Ti si pomočnik za poučevanje tehnike in tehnologije."},
    {"role": "user", "content": "Kaj je spajkanje?"}
]

response = client.responses.create(
    model="gpt-5-nano",     # prilagodi model glede na dostopnost
    input=conversation_input
)

# Pridobitev besedila odgovora (minimalno)
assistant_reply = response.output_text
print(assistant_reply)
```

Minimalna funkcija za ohranjanje pogovora v aplikaciji (shranjujemo seznam vlog in ga ponovno pošljemo)
```python
from openai import OpenAI

client = OpenAI(api_key="your-api-key")

conversation = [
    {"role": "system", "content": "Ti si pomočnik za poučevanje tehnike in tehnologije."}
]

def gpt_response(user_input):
    conversation.append({"role": "user", "content": user_input})
    resp = client.responses.create(model="gpt-4o-mini", input=conversation)
    assistant_text = resp.output_text
    conversation.append({"role": "assistant", "content": assistant_text})
    return assistant_text

print(gpt_response("Kaj je spajkanje?"))
print(gpt_response("Kako se uporablja spajkalnik?"))
```

Opomba: prilagodi ime modela glede na razpoložljivost (npr. `gpt-4`, `gpt-4o-mini`). Če uporabljaš SDK brez parametra api_key, nastavi ključ prek okoljske spremenljivke.

<!--

# Openai API modeli

Openai nam ponuja različne modele. Najosnovnejši je **text-davinci-003**, ki je tudi najbolj ugoden, a so t.i. **chat-based models** bistveno bolj zmogljivi in enostavnejši za uporabo. Na primer uporaba `.thread` funkcionalnosti omogoča ohranjanje konteksta pogovora brez ponovnega pošiljanja celotne zgodovine. To funkcionalnost ima model GPT-4 API s funkcijo **chat-based models**. Če uporabljamo **text-davinci-003** ali podobne modele, pa moramo zgodovino pogovora sami vključiti v vsak nov klic.

Če imamo možnost uporabe **chat-based models (npr. GPT-4)**, lahko namesto ročnega sestavljanja zgodovine uporabimo strukturiran pristop z uporabo `messages` in ohranjanjem `thread`. Primer:  

### **Koda za ohranjanje pogovora s chat modelom**
**Python (GPT-4 chat)**  
```python
import openai

# Nastavi API ključ
openai.api_key = "your-api-key"

# Začetni kontekst pogovora
conversation = [{"role": "system", "content": "Ti si pomočnik za poučevanje tehnike in tehnologije."}]

def gpt_response(user_input):
    global conversation
    conversation.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=conversation
    )
    assistant_reply = response['choices'][0]['message']['content']
    conversation.append({"role": "assistant", "content": assistant_reply})
    return assistant_reply

# Testiranje
print(gpt_response("Kaj je spajkanje?"))
print(gpt_response("Kako se uporablja spajkalnik?"))
```

### **Prednosti uporabe `messages` z GPT-4 chat modelom:**
1. **Optimizacija:** Ni potrebno pošiljati celotne zgodovine kot en dolg niz, ampak uporabimo strukturirane objekte.
2. **Ohranjanje konteksta:** Model sam prepozna vloge (`user`, `assistant`, `system`).
3. **Enostavnost upravljanja zgodovine:** Dovolj je le seznam sporočil, ki jih dodajamo sproti.

### Če pa uporabljamo **text-davinci-003**, je ročno dodajanje zgodovine nujno:  
- Model ne podpira strukturiranih pogovorov.  
- Celoten kontekst mora biti znova poslan v vsakem klicu.

-->
