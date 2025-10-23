### Kaj je API in zakaj potrebujemo API ključ?

#### Kaj je API?  
API (Application Programming Interface) je vmesnik, ki omogoča, da se različne aplikacije ali programske komponente med seboj povežejo in izmenjujejo podatke. Predstavljaj si ga kot "posrednika", ki omogoča komunikacijo med programom, ki ga razvijamo, in storitvijo, ki jo želimo uporabiti, kot je npr. GPT model.

#### Kako deluje API?  
API deluje tako, da razvijalec pošlje zahtevo (request) API-ju, ta pa vrne odgovor (response). Na primer, ko želimo uporabiti GPT asistenta:
1. Pošljemo vprašanje (request) na API.
2. GPT vrne generirano besedilo kot odgovor (response).

To komunikacijo običajno izvajamo prek protokola HTTP, podobno kot spletni brskalniki pridobivajo spletne strani.

#### Zakaj potrebujemo **API ključ**?  
API ključ deluje kot identifikator in varnostni mehanizem. Uporablja se za:
- **Avtentikacijo**: Dokaže, da imaš dovoljenje za uporabo API-ja.
- **Omejevanje dostopa**: Nekatere storitve omejujejo, koliko zahtev lahko pošlješ na uro ali dan, odvisno od tvojega ključa.
- **Zaračunavanje**: Če je API plačljiv, ključ omogoča spremljanje uporabe za pravilno obračunavanje.

API ključ je torej tvoja "vstopnica", ki omogoča dostop do funkcionalnosti storitve. Brez njega API ne bo deloval, saj sistem ne bo vedel, kdo si in ali imaš pravice za uporabo.

#### Primer:
Ko učitelj ustvari GPT asistenta, bo njihov program potreboval dostop do OpenAI API-ja za komunikacijo z GPT modelom. OpenAI zahteva, da vsak uporabnik uporabi svoj API ključ, ki ga dobi na svojem računu pri OpenAI. Ključ se nato vključuje v program za avtentikacijo.

### Kako pridobiti API ključ od OpenAI? 

Za pridobitev API ključa, ki ga potrebujete za uporabo GPT modelov, sledite spodnjim korakom:

---

#### **1. Ustvarite račun pri OpenAI**
   - Obiščite spletno stran [OpenAI](https://www.openai.com/).
   - Kliknite na gumb **"Sign Up"** ali **"Get Started"**.
   - Registrirajte se s svojim e-poštnim naslovom ali uporabite obstoječi račun Google ali Microsoft.
   - Če že imate račun, se prijavite s klikom na **"Log In"**.

---

#### **2. Dostop do uporabniškega portala**
   - Ko se prijavite, boste preusmerjeni na uporabniški portal OpenAI.
   - Če niste samodejno preusmerjeni, kliknite na povezavo **"Manage Account"** ali pojdite neposredno na stran [platform.openai.com](https://platform.openai.com/).

---

#### **3. Poiščite razdelek za API ključe**
   - V navigacijskem meniju na levi strani izberite **"API Keys"** (morda je pod razdelkom "Settings").
   - Na tej strani lahko vidite seznam obstoječih ključev ali možnost za ustvarjanje novega.

---

#### **4. Ustvarite nov API ključ**
   - Kliknite na gumb **"Create new secret key"**.
   - Sistem bo samodejno generiral vaš API ključ.
   - **Pomembno**: API ključ bo prikazan le enkrat. Skopirajte ga in ga varno shranite, na primer v geslovniku ali varni datoteki. Če ga izgubite, boste morali ustvariti novega.
   - Naprimer: `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`

---

#### **5. Shranite API ključ na varno mesto**
   - **Ne delite ključa z drugimi**: Ključ je osebni identifikator, ki omogoča dostop do storitev OpenAI.
   - Predlagamo, da ga shranite na eno od naslednjih mest:
     - V okoljski spremenljivki vašega računalnika (npr. `~/.bashrc` za Linux).
     - V namenski konfiguracijski datoteki za projekt (npr. `.env`).
     - V geslovniku, ki podpira varno shranjevanje (npr. LastPass ali Bitwarden).

---

#### **6. Preverite omejitve in pogoje**
   - Preden začnete uporabljati ključ, preverite svoje **kvote** in **omejitve**, ki jih določa OpenAI. Te omejitve so pogosto vezane na vrsto računa:
     - Brezplačni uporabniki imajo omejeno število zahtev.
     - Plačljivi uporabniki lahko pošiljajo več zahtev, vendar je uporaba zaračunana.
     - Vse nastavitve glede plačila lahko urejamo v `Billing` zavihku:
        - Dodamo način plačila (vpišemo veljavne podatke kreditne kartice)
        - Nato v `Overview` dodmo nekaj kredita - `Add credit balace`

---

#### **7. Pripravljeni za uporabo**
   - API ključ je zdaj pripravljen za uporabo.
   - Uporabite ga v svojih aplikacijah ali Python projektih, tako da ga vključite v ustrezno konfiguracijo.

---

### Nasveti za študente:
- **Ne shranjujte ključa neposredno v kodo**, ker lahko koda postane dostopna drugim (npr. če jo objavite na GitHubu).
- Vadite ustvarjanje in brisanje ključev, da se naučite osnov varne rabe API-jev.

Naj nadaljujem s pripravo navodil za vključitev API ključa v Python kodo?
