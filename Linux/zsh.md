# ZSH

Kako nastaviti zsh, ne da bi uporabili oh-my-zsh lahko najdete na tej strani: https://thevaluable.dev/zsh-install-configure-mouseless/

- Kako nastaviti zsh kot primarne `shell` : z ukazom `chsh`
```shell
chsh -s $(which zsh)
```

## Nastavitve terminala

Terminal lahko nastavljamo z datoteko `~/.config/zsh/.zshrc`
Odličen vodnik je v tem [videu](https://www.youtube.com/watch?v=uOnL4fEnldA)

## Zanimivi plugini

 zsh-autocomplete
 zsh-autosuggestions
 zsh-syntax-highlighting

```bash
source /usr/share/zsh/plugins/zsh-autocomplete/zsh-autocomplete.plugin.zsh
source /usr/share/zsh/plugins/zsh-autosuggestions/zsh-autosuggestions.zsh
source /usr/share/zsh/plugins/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
```

