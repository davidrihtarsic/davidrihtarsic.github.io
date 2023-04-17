# BASIC SHELL

## COMMANDS

!! - repeat last command

## VARIABLES

```bash
foo=bar
echo $foo
```

## ARGUMENTS

$0     - name of script
$#     - number of arguments
$@     - all argumets in list (separated by space)
$*     - all arguments as a single string
$1..$9 - arguments
$?     - get the error code from prewious if OK then this is 0
$_     - get the last argument from last cmd

## CONDITIONAL COMMAND EXECUTION

```bash
false || echo "Will be printed"
true && echo "This wet ok"
true; false; echo "will execute secuentally"
```

## COMMAND OUTPUT INTO VARIABLE

```bash
foo=$(pwd)
echo $foo

echo "We are in $(pwd)"
```

## SAVE OUTPUT TO TMP_FILE

```bash
cat <(ls) <(ls ..)
```

## FLUSH COMMAND OUTPUT & ERROR

```bash
grep foobar "$file" > /dev/null 2> /dev/null
```

## IF STATEMENT

glej:

    man test

```bash
if [[ $? -ne 0 ]]; then
  echo "Error found..."
  echo "... Fixing error."
fi
```

## GLOBBING (EXPAND TO DIFFERENT FILES)

```bash
ls filename?.txt
ls ?.txt
```

## EXPANDING THE COMMANDS ARGUMENTS

```bash
touch test_file{1,2,3}.md
touch test_file_{a..z}.md
```

## COMPARE FILES

```bash
diff file1 file2
#compare the dirrectory content
diff <(ls dir1) <(ls dir2)
```

## DEBUGGING

```bash
shellcheck bash_script.sh
#give you more info where and how the program is broken
```

## NAVODILE

za skoraj vse ukaze najdemo navodila tako da:
```bash
# navodila kako uporabljati ukaz
man ukaz
# primeri kako uporabljati ukaz
tldr ukaz
```

## HISTORY OF COMMANDS

```bash
#use arrows
history
history 1 | grep convert
# CTRL+R .. search trough history
fzf
# history substring search
```

## LISTING AND FILE HANDELING

```bash
ls -R
tree
broot
nnn
ranger
```
