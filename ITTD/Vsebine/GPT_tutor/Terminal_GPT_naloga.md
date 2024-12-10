TERMINAL GPT NALOGA
================================================================================

Trenutno program deluje, vendar ima dve težavi, ki jih je treba odpraviti:

- Asistent pozabi svojo nalogo:
    - Asistent (GPT model) pozabi svojo začetno nalogo, ko se zgodovina pogovora zmanjša na zadnjih 5 sporočil. To se zgodi, ker je začetno sporočilo s role: "system" izključeno iz konteksta.
    - Rešitev: Vedno vključite začetno sporočilo z nalogo asistenta v zgodovino, ne glede na dolžino zgodovine pogovora.

- Preverite, če uporabnik vpiše konec
    - V glavni zanki preverite, ali je uporabnik vpisal konec. Če je, naj se program zaključi s prijaznim sporočilom.
        - program lahko končate z ukazom `break`

- Berljivost in organizacija kode:
    - Koda je trenutno napisana kot monolitna zanka, kar jo dela manj pregledno in težje vzdrževano.
    - Rešitev: Ločite logiko za pošiljanje vprašanj in obdelavo odgovorov v funkcijo poslji_vprasanje(uporabnikovo_vprasanje), da postane program bolj modularen in berljiv.


