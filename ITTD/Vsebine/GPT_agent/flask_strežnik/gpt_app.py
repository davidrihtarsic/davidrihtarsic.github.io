import openai # dodamo openai knjižnico
from flask import Flask, request, render_template

openai.api_key="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"

app = Flask(__name__) 

@app.route("/", methods=["GET", "POST"])
def index():
    odgovor = ""
    if request.method == "POST":
        uporabnikov_vnos = request.form["user_input"]
        #odgovor = f"Prejeli smo vaše vprašanje: {uporabnikov_vnos}"
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role":"system", "content":"Ti si pomočnik učitelju ali učencu za tehniko in tehnologijo"},
                {"role":"user", "content":uporabnikov_vnos},
            ]
        )
        odgovor = response['choices'][0]['message']['content']
    return render_template("index.html", odgovor=odgovor)

if __name__ == "__main__":
    app.run(debug=True)  # Zaženi strežnik v načinu za razvoj
