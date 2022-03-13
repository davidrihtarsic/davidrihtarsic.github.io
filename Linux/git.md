# GIT

Git is a free and open source distributed version control system designed to handle everything from small to very large projects with speed and efficiency (https://git-scm.com/).

## COMMON COMANDS

## ADVANCES USFUL COMMANDS

#### remove history and start fresh init

    git checkout --orphan tmp_branch
    git add -A
    git commit -am "delete history and fresh init"
    git branch -D master
    git branch -m master
    git gc --aggressive --prune=all

#### squash

da združimo več komitov v enega samega narimer:

    A---B---C---D
                 \
                  a--b--c

 in tako lahko dobimo 

    A---B---C---D--f

Naprimer v nekem dir je .git  ditektorij velik 759.2 MiB
Nato združimo 20 commits

      git rebase -i HEAD~20

nato se odpre nvim in spremenimo `pick` v `squash`

      pick 73d9116 typo
      squash 21cc5bd rezultati PIZE
      squash f8cf7dc prisotnost
      squash e25984a rezultati zrob
      squash 4f59ce6 Set theme jekyll-theme-slate
      squash 19fc01b typo
      squash 5f07202 poročila ocene
      squash 244809a rezultati modelarstvo

za tem še dodamo nov povzetek commita

in direktorij `.git ` ima tedaj 759.3 MiB
