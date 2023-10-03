# MARKDOWN TESTING

Najprej nekaj besedila, da vidimo kako se to vidi... Ok.
Tale beseda naj bi bila **BOLD** ali **bold**, nato pa še nekaj v *Italic* in še ~underline~.

## SEZNAMI

1. Element 1
2. element 2
3. element 3.

- element 1,
- element 2,
- element 3.

[ ] element 1,  
[] element 2  
[x] označen element  

V VIM lahko števne elemente, ki jih označimo, avtomatsko povečamo s `C-a` in zmanjšamo s `C-x`.

## KOMENTARJI IN CITATI

> To pa je lahko komentar ali citat neke osebe.  
> \hfill \null - Tomaž Kušar -

## VSTAVLJANJE OPOMB

V besedilo lahko vstavljamo tudi opombe[^ime_opombe]. Opombe so koristne v besedilnih dokumentih, ker omogočajo hiter in enostaven dostop do ključnih informacij. Več informacij[^vec_info] pa lahko opišete spodaj.

[^ime_opombe]:To opombo naredimo tako, da uporabimo`[^ime_popmbe]`.
[^vec_info]:Besedilo spodnjih opomb vpišete med besedilo (npr. po odstavku) z ukazom `[^footnote]:Razalaga dodatnih informacij.`

\pagebreak
## TABELE

| Stolpec1 | Stolpec2 |
|:--------:|:--------:|
| Vrstica1 | Vrstica1 |
| Vrstica2 | Vrstica2 |
Table: Primer tabele. {#tbl:TblExmpl}

## ENAČBE

Lahko pišemo enačbe v vrstičnem načinu $to=Vrsticni*nacin$  

Ali pa enačbo napišemo  v svoji vrstici tako kot na primer za izračun volumna nekega valja z radijem r in višino h:

$$ V = \pi * r^2 * h $${#eq:vol_valja}

in se seveda lahko na to enačbo tudi sklicujemo z referenco [@eq:vol_valja].

## LINKI

Na datoteke se lahko sklicujemo s povezavami, na primer takole:

[dokument](./vim-wiki.md)

Če se s kurzorjem postavimo na povezavo in pritisnemo

    gf

bo **VIM** sledil temu dokumentu in ga skušal odpreti.


\pagebreak
## VSTAVLJANJE SLIK

Na sliko pa se lahko sklicujemo takole [@fig:sklic_na_sliko]
<!--
![Prikaz zaslonske slike.](./slike/image.png){#fig:desktop_img width=5cm}
-->

z latex kodo pa lahko sliko vstavimo takole:

\begin{figure}
  \centering
  \includegraphics[width=5cm]{./slike/image.png}
  \caption{Opis slike.}
  \label{fig:sklic_na_sliko}
\end{figure}

Z vstavljanjem slike z latex kodo sem imel probleme, ker v templatu `eisvogel.latex` ni bilo
vstavljenega `\package{graphicx}`. Zato sem ga vstavil kar brez kakšnega pogoja.

\pagebreak
## PROGRAMSKA KODA ali LISTINGS

Takole pa lahko vstavimo programsko kodo, na katero se lahko
tudi sklicujemo [@lst:main]

```cpp
#include <stdio.h>
int main(void)
{
  char greeting[] = "Hello, world";
  printf("%s\n", greeting);
  return 0;
}
```
: Primer programske kode. {#lst:main}

In programska koda brez specifikacije 

    To pa je kar tako
    nekaj v smislu
    pseudo kode ali bloka

V besedilo pa lahko vstavimo tudi kodo iz neke datoteke

    \lstinputlisting[language=c++, caption={Primer kode.}, label=lst:sklic_na_kodo, linerange={4-6}]{ime_dateteke_s_kodo.cpp}

To je izredno prikladno, saj lahko kodo spremenimo v datoteki in se nato
skompila še v besedilu. Kjer se na to kodo lahko tudi sklicujemo [@lst:sklic_na_kodo].

\lstinputlisting[language=c++, caption={Primer kode.}, label=lst:sklic_na_kodo]{./src/main.c}

Ta oblika vstavljanja kode nudi nekaj več možnosti prikaza, kot naprimer, da vsatimo
le nekatere vrstice iz fila tako, da uporabimo spremenljivko `linerange={4-6}`

\lstinputlisting[language=c++, caption={Primer iste kode od vrstice 4-6.}, linerange={4-6}]{./src/main.c}

\pagebreak
## BESEDILO V VEČ STOLPCIH

\begin{multicols}{2}
\setlength{\columnseprule}{0.1pt}

Pisanje v več stolpcih v markdown ni omogočeno. Zato moramo to narediti z latex kodo.
Začnemo z ukazom \textbf{begin\{multicols\}\{2\}} nato vstavimo nekaj
besedila in končnamo z ukazom \textbf{end\{multicols\}}. Besedilo se bo avtomatsko razporedilo
v dva stolpca s približno enako besedila v vsakem stolpcu. Omenimo naj še nekaj uporabnih
ukazov: \textbf{setlength\{columnseprule\}\{0.1pt\}} - nariše tanko črto med stolpcema,
\textbf{null} - zapolni del stolpca s praznim območjem, \textbf{vfill}.

\end{multicols}

### Slika v dveh stolpcih

\begin{multicols}{2}
\setlength{\columnseprule}{0.1pt}

Vstavljanje slike z opisom slike v sosednjem stolpcu je zelo koristno, saj omogoča lažje razumevanje vsebine. Bralci bodo lahko lažje razumeli vsebino, če bodo lahko videli sliko, skupaj z opisom, da bodo razumeli, kaj prikazuje slika.
Vstavljanje slike z opisom slike v sosednjem stolpcu je zelo koristno, saj omogoča lažje razumevanje vsebine. Bralci bodo lahko lažje razumeli vsebino, če bodo lahko videli sliko, skupaj z opisom, da bodo razumeli, kaj prikazuje slika.
\columnbreak

\null
\vfill
\begin{figure}
  \centering
  \includegraphics[width=7cm]{./slike/image.png}
  \caption{Opis slike.}
  \label{fig:sosednja_slika}
\end{figure}
\vfill
\null

\end{multicols}

### Programska koda v dveh stolpcih

\begin{multicols}{2}
\setlength{\columnseprule}{0.1pt}
\null
\vfill

\begin{lstlisting}[language=c++]
int main(){
    int i = 2;
    for (i=0;i<5;i++){
        cout<"Hello";
    }
}
\end{lstlisting}
\vfill
\null
\columnbreak

Vstavljanje programske kode z opisom kode v sosednjem stolpcu je koristno, ker omogoča hitrejše razumevanje kode in jo lažje razvrščanje. Opisi so lahko zelo uporabni, ko poskušamo razumeti kodo, ki smo jo napisali nekaj časa nazaj. Spodbuja tudi dobre kode, saj je lažje opaziti, kaj se dogaja v kodi, ko jo lahko prikažemo skupaj z opisom. Prav tako lahko pomaga poenostaviti kompleksno kodo.

\end{multicols}

