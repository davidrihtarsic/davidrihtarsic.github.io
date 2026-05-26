#!/usr/bin/env python3
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
