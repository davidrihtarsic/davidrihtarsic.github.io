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
