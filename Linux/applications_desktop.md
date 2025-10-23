Za vsak program lahko določimo v katero katero spada in kako ga zaženemo. Te možnosti programa so zapisane v:  
`/usr/share/applications/IME_PROGRAMA.desktop`

katere kategorije so vpisane v vseh programih lahko pogledamo z ukazom:  

```bash
#! /bin/zsh
grep Categories /usr/share/applications/* | sed 's/^.*=//;s/\;/\n/g' | sort | uniq
echo "To je test..."
```

