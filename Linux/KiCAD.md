# KiCAD

kicad library dirrectory:

    /usr/share/kicad
      ├── 3dmodels
      ├── demos
      ├── footprints
      ├── plugins
      ├── resources
      ├── schemas
      ├── scripting
      ├── symbols
      └── template

## Spice simulations

Trenutno imam spice modele raznih elementov v:

    ~/KiCAD/KiCad-Spice-Library/Models
        ├── Digital Logic
        ├── Diode
        ├── Manufacturer
        ├── Operational Amplifier
        ├── Optocoupler
        ├── Transistor
        └── uncategorized

... verjetno bi bilo bolj pravilno, če bi bili ti dokumenti v

    ~/.local/KiCAD/

## Migracija na novejšo različico



### Migracija na Novo Različico KiCad-a

Migracija na novo različico KiCad-a vključuje prenos vaših knjižnic z vsemi simboli, tiskanimi vezji (footprints) in 3D pogledi na novo lokacijo ter posodobitev ustreznih tabel s knjižnicami. Tukaj je kratek vodič, kako to izvesti:

1. **Kopiranje Datotek Knjižnic**

   - **Simboli, footprinti in 3D pogledi:**
     - Kopirajte vse relevantne datoteke iz `~/.local/share/kicad/8.0` v `~/.local/share/kicad/9.0`.
     - Alternativno lahko ustvarite simbolične povezave za te datoteke, da se izognete podvajanju:
       ```bash
       ln -s ~/.local/share/kicad/8.0 ~/.local/share/kicad/9.0
       ```

2. **Posodobitev Tabel Knjižnic**

   - **Simbolne tabele:**
     - Kopirajte datoteko tabele simbolov:
       ```bash
       cp ~/.config/kicad/8.0/sym-lib-table ~/.config/kicad/9.0/sym-lib-table
       ```

   - **Tabele za knjižnice footprintov:**
     - Na podoben način kopirajte datoteko s tabelo za footprinte:
       ```bash
       cp ~/.config/kicad/8.0/fp-lib-table ~/.config/kicad/9.0/fp-lib-table
       ```

3. **Preverjanje**

   - Po prenosu ali ustvarjanju povezav za datoteke, odprite KiCad 9.0 in preverite, če so vse knjižnice pravilno nastavljene in dostopne.
   - Preverite simbole, footprinte in 3D poglede v vaših projektih, da zagotovite pravilno delovanje v novi različici.

S temi koraki boste uspešno migrirali vaše KiCad knjižnice na novo različico, pri tem ohranili konsistenten dostop do vseh potrebnih virov in bili pripravljeni na nadaljnje delo s posodobljeno programsko opremo.
