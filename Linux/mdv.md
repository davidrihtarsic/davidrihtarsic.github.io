# MDW

Is markdown viewer for terminal. It nicely fits with
[Ranger](Ranger.md) file manager.

## Issues

### Not working with python 3.11
New update... since python 3.11 not working with mdv... install it with:

    pip install --upgrade --force-reinstall git+http://github.com/axiros/terminal_markdown_viewer

### Not Working With Python 3.9

... I was wrong...  I should install mdv3, since I'm using python3.9

    pip3 install mdv3
!!!!

Here is an easy fix. Minor changes are needed in file

    ~/.local/lib/python3.9/site-packages/mdv/markdownviewer.py

Here is [patch file](./src/patch_mdv_py_3.9.patch)


