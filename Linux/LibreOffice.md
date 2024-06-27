# LibreOffice

## WRITER
### How to Change ICONS
1. run libreoffice
2. Tools -> Options
3. View
4. Icon style ...

__Short Cuts__

| Short cut      | Action              |
|                |                     |
| [Ctrl] + [Ent] | Insert Break Page   |
| []+[]          | Insert greek letter |

## CALC
### How To   Insert DATE:

1. Tools  > Customize  > Keyboard  >
2. Short Keys :Ctrl+.
3. Category: Insert
4. Function: Insert Current Ddate
5. [Modify]

### How To   Insert TIME:

1. Tools  > Customize  > Keyboard  >
2. Short Keys :Ctrl+Shift.
3. Category: Insert
4. Function: Insert Current Time
5. [Modify]

### __Short Cuts__

| Short cut     | Action              |
|               |                     |
| [Ct]+[.]      | Insert Date         |
| [Ct]+[Sh]+[.] | Insert Time         |

### How to   Filter duplicated

Ko imamo tabelo:

|  ime  | vpisna |  smer |
|       |        |       |
| DAvid | 123456 | Fi Te |
| DAvid | 123456 | Fi Te |
| Mija  | 345678 | Ma Te |
| Jure  | 098765 | Fi Ma |

1. vklnjučiš filter
2. nato greš v meni [ime v]
      Standard Filter
      ime = NotEmpty
      > Options : No Duplicates
[ok]

## BASE

Data field
DAY([dat_odhod])&". "&MONTH([dat_odhod])&". "&YEAR([dat_odhod])-2000
YEAR([dat_odhod])&"-"&[ID]

## Plugins

- Report builder dela le v *full version,
    To verzijo lahko dobiš z AppImage na strani:
    https://www.libreoffice.org/download/appimage/

### Zotero

Zotero Standalone. Is a free, easy-to-use tool to help you collect, organize, cite, and share your research sources.
za urejanje bibtex fileov in jih lahko uporabiš v LibreOffice

    yay -S zotero
