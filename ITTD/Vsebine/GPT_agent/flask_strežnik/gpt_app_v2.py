from openai import OpenAI
from flask import Flask, request, render_template #dodamo Flask knjižnico
client = OpenAI(
    api_key="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"  # Tukaj pridobimo API ključ iz okoljske spremenljivke
)

app = Flask(__name__) # Inicializacija Flask aplikacije

zgodovina_pogovora = [
    {
        "role": "system",
        "content": "Ti si pomočnik za pomoč učitelju pri poučevanju tehnike in tehnologije"
    }
]

@app.route("/", methods=["GET", "POST"])
def index():
    odgovor = ""
    if request.method == "POST":
        vprasanje=request.form["user_input"]

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
                stream=False,         
            )

            # Prikaz odgovora modela
            #print("GPT-4o-mini:")
            #for delcek_besedila in pogovor:
            #    print(delcek_besedila.choices[0].delta.content or "", end="")
            #print("")

            print(pogovor)
            odgovor=pogovor.choices[0].message.content
            zgodovina_pogovora.append(
                {
                    "role":"assistant",
                    "content":odgovor
                }
            )

        except Exception as e:
            odgovor="Prišlo je do napake:" + str(e)
    
    return render_template("index.html", odgovor=odgovor)

if __name__ == "__main__":
    app.run(debug=True)
