# BEETS

Programlek za označevanje skladb (file-ov).

## Uporabni ukazi:

Izbrišemo podatke z bazo ivoženih skladb (priporočljivo je delati v kosih...)

    beet remove

Najverjetneje imamo skladbe nekega avtorja v nekem dirrektorjiju s skladbami
ali pa si jih takole uredimo:

    MAN2TALL-PsalM II
    ├── 01 Offnung.mp3
    ├── 02 Hisa Strahov.mp3
    ├── 03 Enotirnium.mp3
    ├── 04 7.mp3

V `~/.config/beets/config.yaml` vključimo:

    ...
    # fromfilename - razbere ime pesmi iz imena datoteke.mp3
    plugins: [fromfilename]
    ...
    paths:
        #default: $albumartist/$album%aunique{}/$track $title
        # spodnja nastavitev ne bo imela dvojne zaporedne števike v imenu datoteke.mp3
        default: $albumartist/$album%aunique{}/$title

... lahko uporabimo ukaz:

    beet import ./ --set artist="Man2Tall" --set album="PsalM II"

in potrdimo z `U`as-is

Nazadnje dodamo skladbam še thumbnail albuma:

    beet embedart -f ./cover_1.jpg Saprabolt
