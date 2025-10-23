
# Programska koda - kaj je to?

Zaporedje
Izbira
Ponavljanje

# Kako pisati pregledno kodo programa

- [Clean CODE](https://www.youtube.com/watch?v=7EmboKQH8lM)

Proces pisanja kode je izredno NE-linearen, naše misli skačejo na različne težave in različne potrebe, ki se utegnejo pripetiti med programiranjem. Zato ni čudno, da bo prva delujoča koda zapletena in raztresena. Zato jo moramo po končnem testiranju NUJNO urediti.

    Ko napišete delujočo kodo in ste jo stestirali, ste na pol-poti. Potrebno jo je še urediti in narediti berljivo! (Uncle Bob)

Organizacija programa naj bo podobna pisanju članka v časopisu:  
1. Začnemo z naslovom, nato
2. napišete povzetek
3. nato sledijo odstavki, ki razkrivajo zgodbo v podrobnosti in 
4. na koncu je zaključek z rezultati.

Taka ureditev omogoča bralcu, da besedilo lahko zapusti takoj, ko vsaj približno razume namen vsebine. Zamislite si, da berete časopis z novicami, a preberete le tiste, ki vas zanimajo, ostale pa le preletite.

## Manj je več

Krajše koščke programa je lažje razumeti. Zato se moramo potruditi, da vsako zaključeno celoto strnimo v podprogram ali funkcijo.

## Funkcije

Pri funkcijah naj bi se držali nekaj previl:

### Koda v funkcijah naj bo kratka

Funkcija naj naredi le eno stvar. To pomeni, da iz kode, ki je v funkciji ne moremo izvleči programske stavke in jih logično ločiti v svojo funkcijo. Seveda pa, moramo vse te majhne funkcije primerno poimenovati.

    Imena funkcije naj bodo GLAGOLI in ne samostalniki, ker funkcije OPRAVLJAJO neko nalogo. (Uncle BOB)

### Oblikovanje funkcij v razrede

Pri oblikovanju funkcij lahko opazimo, da funkcije operirajo s podatki. Če se ti podatki ponavljajo ali pa so podobni moramo razmisliti o uporabi RAZREDA (callses). Naprimer krmiljenje DC motorja je tak primer. Lahko imamo več motorjev in za vsakega posebej želimo nastavljati smer in hitrost. V ta namen bi bilo smiselno pripraviti class:

```cpp
class Motor
{
  public:
    int smer;
    int hitrost;
};
```

## Da je koda pregledana je verjetno bolj pomembno kot, da deluje... zakaj?

Če imamo delujočo kodo in je ta nepregledna, se lahko zgodi, da ko se bodo zahteve spremenile (posodobili bomo program) bomo skušali kodo popraviti in je ne bomo mogli. Da o možnosti, da bi nam jo popravil nekdo tretji sploh ne razmišljamo.
Če pa je koda pregledna, pa ne deluje nam jo lahko pomaga rešiti bolj izkušenj programer.

Pregledno kodo lahko uporabi nekdo drug in je prenosljiva.

## Koda naj gre iz višjega nivoja v nižji

Med posameznimi vrsticami naj ne bo velikih prehodov med nivoji programiranja. Naprimer ne mešajmo deklaracij objektov z deklaracijami konstant.

## Razlagalna spremenljivka

Te spremenljivke določimo zato, da bodo if-stavki bolj berljivi. Samo spremenljivko določimo predhodno in ji damo tako ime, ki nakazuje na neko logično stanje. Izogibamo se negaciji.

```cpp
stikaloJeSklenjeno = digitalRead(3);
if (stikaloJeSklenjeno) {
  digitalWtire(3, HIGH);
}
```

# Kakšna so naša pričakovanja glede programske kode?

## Vmesne različice naj bodo delujoče

Postaviti si moramo kratke roke ob katerih bomo izdali delujočo kodo. Koda je lahko še podhranjena z uporabnimi funkcijami, a vse funkcije morajo delovati. Izdajanje vmesne različice naj vsebuje:
- vse delujoče elemente kode,
- njihovo dokumentacijo in
- koda naj bo urejena ter
- vsak njen del stestiran.

## Dodajanje novih funkcij v program ne sme upočasniti dela

Dodajanje novih funkcij v program ne sme upočasniti dela, če se to zgodi, je verjetno zaradi tega, ker smo pred tem naredili zmedo v programski kodi. Še en razlog več zakaj **mora** biti koda urejena.

## Spremembe programske kode morajo biti enostavne

Že iz besedne zveze SOFT-WARE je razvidno, da je to MEHAK - IZDELEK in ga je zato enostavno spremeniti. Zato vsaj majhne spremembe ne smejo biti težava in morajo biti hitro implementirane. K temu koraku pripomore zopet:
- pregledna koda in
- dobro napisan testni program

## Program naj bo s časom vedno boljši

## Popravljanje kode brez strahu

Kadar imamo občutek, da bi morali kodo izboljšati, jo dokumentirati ali narediti preglednejšo - imamo verjetno prav. Vendar se tega dela lahko ustrašimo, češ, da bomo kodo morda uničili. Tega se ne smemo nikoli ustrašiti! V veliko pomoč nam je lahko dober testni algoritem kode. Tako brez težav počasi spreminjamo kodo in jo sproti testiramo. Tak proces je zanesljiv in enostaven.

## Seznanjanje svojega sodelavca s kodo

Pametno je seznanjanje svojih sodelavcev z vašim delom (programiranjem) zato, da vas lahko nadomestijo, če ste vi odsotni z dela. Poleg tega pa je to dobra praksa pregleda kode in tako pogosto kodo izboljšamo z idejami sodelavcev.

# Testiranje kode

## Ne napiši kode dokler nisi napisal testa zanjo in je le-ta spodletel, ker koda ne obstaja

## Ne napiši daljšega testa kode, le toliko, da je dovolj, da spodleti.

## Na napiši daljše kode, le toliko, da popraviš spodleteli test.

# Arhitektura kode

Iz arhutekture kode mora biti jasno za kakšen projekt gre. Podobno kot lahko iz tlorisa stavbe lahko povemo za kater namen je zgrajena. Enako je, če pogledamo kako je urejena arhitektura računalniške matične plošče.

Ker gre pri robotiki v najosnovnejšem primeru za S-R-A loop bi verjetno bilo primerno, da je tudi arhitektura kode taka.

# Managing the software project

[Clean code (by Unkle Bob)](https://www.youtube.com/watch?v=l-gF0vDhJVI)

0:18       Leds / Introduction.
6:54       How do you manage a software project?
12:54     Finding the optimum solution / Data.
21:04     What is the firts thing know about project / The Management Paradox.
23:33     The Waterfall Model.
34:13     Iterative Development / Calculate Day.
39:09     The Control Knobs of project mgt.
48:51     Short Cycles / Agile Software Development Practices / Extreme Programming.

1. na kartice napišemo katere funkcije mora program imeti
2. z relativno številko ocenimo koliko nam vsaka funkcija na kartici vzame časa (primerna številka je od 0 - 5)
3. vsak "sprint" pogledamo koliko teh točk smo lahko naredili in tako lahko ocenimo kdaj bomo projekt zaključili.
4. iz kupa "to-do" vedno vzamemo le tiste funkcije, ki imajo največje razmerje med funkcionalnostjo in vloženim delom.

# Clean Code - by Uncle Bob

## [Clean Code - Lesson 1](https://www.youtube.com/watch?v=7EmboKQH8lM)

0:00:00  Event Presentation
0:02:03  Presenter Introduces Uncle Bob
0:03:41  Uncle Bob Introduction / My Tribe
0:04:49  How Far is the Sun?
0:10:52  Introduction to Clean Code
0:12:21  The current Society works with Software
0:19:47  Volkswagen case / Introduction to the Ethics of Software Development
0:24:28  Why are Programmers so slow?
0:32:13  What is a Clean Code?
0:40:09  Analyzing some lines of code
0:43:43  Long code is not Good Code
0:49:25  Good Code / Refactored Function
0:52:40  Polite Code / Rules for writing a news paper article
0:55:25  Shrunk Code / The Rules of Functions
1:00:23  Shrunk Code / Drawing a Function
1:05:36  When and why was Java invented?
1:08:52  Prose Code / Arguments
1:16:13  Avoid Switch Statements / Problems and Evolution of some programming languages
1:26:15  The Uncle Bob's wife message (funny moment)
1:27:22  Output Arguments No Side Effects / Garbage Collection
1:32:21  No Side Effects / Using Lambda
1:34:26  No Side Effects / Command and Query Separation
1:35:30  No Side Effects / Prefer Exceptions to returning error codes
1:37:05  DRI Principle (Don't Repeat Yourself)
1:39:21  Structured Programming / Edsger Dijkstra Vision vs Actual Vision of the programming
1:45:32  Science and Correct Software)

## [Comments - Lesson 2](https://youtu.be/2a_ytyt9sf8)

0:00:00  Where did the moon come from?
0:04:56  What is the Purpose of the Comment? / About Fortran
0:08:47  Schindler List / Right and Wrong reason to do comment
0:10:02  Comments are a last resort / The proper use of comments
0:11:02  Comments Lie
0:13:07  Comments do not make up for bad code / Explain Yourself in code
0:15:11  Legal and  Informative Comments / About Design Patterns book
0:20:43  Explanation of Intent / Clarification
0:23:21  Warning of Consequences / TODO Comments
0:25:59  Amplification / Javadocs in Public APIs
0:27:35  Bad and Redundant Comments / Mumbling 
0:31:25  Mandated Comments
0:33:01  Journal Comments / Source code control system
0:34:16  Noise Comments / Scary Noise / Use explanatory code, not comments
0:36:20  Position Markers / Closing Brace Comments / Attributions and Bylines
0:37:43  Commented - Out Code / HTML in comments ICK!
0:40:05  Non - Local Information
0:41:45  How many lines should there be in a source file?
0:46:31  Analysis of the lengths of lines
0:50:11  Names are Everywhere / Reveal your intent / Rules to write Names
0:58:44  Disambiguate / Avoid Convenient Mispellings
1:00:41  Number Series / Noise Words / Distinguish Names Meaninfully
1:02:55  How much time should you spend on a Code Review?

## [Lesson 3](https://www.youtube.com/watch?v=Qjywrq2gM8o)

0:00:00  Start
0:00:23  About our genetic origins.
0:09:36  I am your new CTO / About the growth rate of programmers and it effects.
0:17:25  Expectations / We will Not Ship Shit.
0:21:36  We will always be ready / Iteration Length.
0:25:51  Stable Productivity.
0:28:14  Inexpensive Adaptability / The software must be changeable.
0:30:38  Continuous Improvement / The code should improve over time.
0:31:46  Fearless Competence / Conquer the fear with Test.
0:42:35  We will not dump on QA / QA will find nothing.
0:46:30  Automation!
0:51:20  We cover for each other / Teamwork.
0:55:40  Introduction to "Honest Estimates".

## [Test Driven Development - Lesson 4](https://www.youtube.com/watch?v=58jGpV2Cg50)

0:00:00  Opening.
0:00:51  Honest Estimates / What is the chemical formula of water?
0:07:16  Selection, Secuence and Interaction / No innovations have been made in the software for decades.
0:13:48  The Hardware has gone crazy!: comparison between the innovation level of hardware and software today.
0:17:33  You to say "No".
0:21:40  Test-Driven Development / TDD rules.
0:36:14  Our code is a document / Double entry Bookkeeping.
0:40:22  About inheritance / Mutation Testing.
0:43:48  Demo of Test-Driven Development.
1:12:23  Some tips to learn and practice Test-Driven Development.
1:15:03  Questions and Answers.

## [Architecture - Lesson 5](https://www.youtube.com/watch?v=sn0aFEMVTpA)

0:00:00  Opening.
0:03:25  Dick Vlot about Architecture and Agile Software Development.
0:09:30  Presentation of Uncle Bob.
0:11:19  Diffraction: Why do incandescent lights glow?
0:15:27  Architecture Introduction / I've built lots of apps / "I want to be a programmer" anecdote.
0:26:09  The Architecture rules are independent of every other variable.
0:29:21  Working vs. Right.
0:30:45  What is Design in Architecture?
0:31:50  What is the goal of Software Architecture?
0:33:28  Case study of bad Architecture.
0:38:55  Executive View / What went wrong / Secret to going fast.
0:44:43  Messes aren't faster even in the short term.
0:48:15  Solution of the Executive's Dilema / Two Values of Sofware.
0:52:41  Behavior  / Are we going to see self driving cars?
1:00:14  Scope vs. Shape / Stakeholders want changes.
1:10:33  Urgency and Importance / Eisenhower Matrix.
1:13:09  Fight for the Architecture.
1:15:14  A Rails App / The web is a Ddelivery Mechanism.
1:19:06  Architecture Floor Plans / A Use Case Driven Approach.
1:24:05  Interactors / Entities / Interfaces Objects.
1:27:11  Request Model.
1:30:21  What about MCV? / Design Patterns / How MCV goes wrong as a web Architecture.
1:34:53  Model View Presenter / Dependency Rule.
1:39:10  What about the Database? / The Database is a detail / ORM
1:48:00  Fitnesse: a wiki page porject development.
1:53:54  A good Architecture allows major decisions to be defered!  / About IntelliJ and Visual Studio.
2:03:44  Frameworks / Plugin Model.

## [Lesson 6](https://www.youtube.com/watch?v=l-gF0vDhJVI)

0:00:00  Start
0:00:18  Leds / Introduction.
0:06:54  How do you manage a software project?
0:12:54  Finding the optimum solution / Data.
0:21:04  What is the firts thing know about project / The Management Paradox.
0:23:33  The Waterfall Model.
0:34:13  Iterative Development / Calculate Day.
0:39:09  The Control Knobs of project mgt.
0:48:51  Short Cycles / Agile Software Development Practices / Extreme Programming.
1:14:16  Questions and Answers.
