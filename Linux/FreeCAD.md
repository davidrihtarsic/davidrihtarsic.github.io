FREECAD
================================================================================


1. New document
2. Workbench = Part Design
3. Create new object
4. Create sketch
    - Choose plane
    - Choose polyline tool
      + z `M` spreminjaš način risanja
    - Kotiraš
      + `Shift+h` horizontalno
      + `Shift+v` navpično
5. Task -> Use 3D tools
    - Pad
    - Pocket
    - ...
6. Označiš ploskev na kateri želiš dodati element predmeta
7. Repeat from #4.

Shoortcuts
--------------------------------------------------------------------------------

0 - Isometric View

## Tips & Tricks

- [Izdelava zobnikov](https://www.youtube.com/watch?v=0zxjOB2Cao8)
    - Gear workbench

## Workarounds

### Redraw GRID
Narišeš večji pravokotnik v področju kjer ni mreže in nato se mreža nariše tudi tam.

## Workbenches

Nove `workbench` -e lahko dodajamo tako:  

Tools -> Addon Manager -> ...

in nato izbereš workbench, ki ga potrebuješ nekaj zelo uporabnih workbenchow:
- fasterners = navoji, matice, vijaki

## Parametrično načrtovanje

### Parametri iz tabele

Ena možnost parameteričnega načrtovanja je, da ključne mere vpišemo v tabelo:

    WB(SpreadSheer) -> Create Spreadsheet

V neko celico vpišemo željeno mero in ji določimo enoto mere:

    Desni klik na celici -> Properties -> Display unit

in nato še poimenujemo ime te mere:

    Desni klik na celici -> Properties -> Alias

### Parametri iz skice

Druga možnost je ta, da lahko poimenujete mere v sami skici in le-te uporabite v drugih 
skicah. Ta možnost je bolj primerna, saj s skico bolj nazorno predstavimo neman mere.

Lahko si pripravimo celotno skico s pomembnimi prerezi in merami ter jih smiselno poimenujemo.
Na primer, da ustvarimo skico in jo poimenujemo `SkicaMer`. V tej skici narišemo tehniško risbo
in mere poimenujemo tako, da v oknu za dodajanje mere izpolnimo:

    Name (optional): poimenovana_mera

Nato pripravimo skico s katero bomo dejansko izvedli operacijo na 3D modelu in se lahko sklicujemo
na prejšnje določene mere. V polje za dodajanje mere klilnemo na `(fx)` in vpišemo:

    <<SkicaMer>>.Constrains.poimenovana_mera

Tako lahko spremenite mero le v prvi tehniški risbi `SkicaMer` in se bodo posodobile vse mere, ki se
na določeno spremenjeno mero sklicujejo.

## FEM

Za izračune simulacij napetostnih obremenitev moramo namestiti še:

- calculix
- elmerfem

## ISSUES

### OpenCascade not loaded

> Težave, da ni mogel naložit nekih objektov... OpenCascade..

Rešitev je bila, da nimaš zadnje verzije opencascada:

    sudo pacman -U /var/cache/pacman/pkg/opencascade-1:7.5.3-3-x86_64.pkg.tar.zst

### Velikost ikon je velika

Rešitev je bila, da nastaviš 96 dpi. To lahko narediš tako, da najprej preveriš kolikšna je dpi na monitorjih:

    xdpyinfo | grep -B 2 resolution

in če ni `96x96 dots per inch`, to lahko narediš z ukazom:

    xrandr --dpi 96

