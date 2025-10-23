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
                {"role": "user", "content": user_input},
            ],
            tools=[
               # {
               #     "type": "file_search",
               #     "vector_store_ids": ["vs_68f0014fe51c819184b6c36568f1ade0"],
               # }
            ],
        )

        print(f"\n🧠 Asistent: {response.output_text}\n")

if __name__ == "__main__":
    start_chat()
