# LIBRARIES

> Če kak program ne najde kake knjižnice gre verjetno le za neko strarejšo verzijo...
> Glej primer za Fritzing, ki ni našel libgit2.so.1.2.

    ╭=[ArchLaptopDR|~]==--
    ╰> Fritzing
    Fritzing: error while loading shared libraries: libgit2.so.1.2: cannot open shared object file: No such file or directory
    ╭=[ArchLaptopDR|~]==--
    ╰> ls -all /usr/lib/libgit*
    lrwxrwxrwx 1 root root      14 Aug 16 15:54 /usr/lib/libgit2.so -> libgit2.so.1.5
    lrwxrwxrwx 1 root root      16 Aug 16 15:54 /usr/lib/libgit2.so.1.5 -> libgit2.so.1.5.0
    -rwxr-xr-x 1 root root 1226024 Aug 16 15:54 /usr/lib/libgit2.so.1.5.0
    ╭=[ArchLaptopDR|~]==--
    ╰> sudo ln -s /usr/lib/libgit2.so.1.5.0 /usr/lib/libgit2.so.1.2
    ╭=[ArchLaptopDR|~]==--
    ╰> ls -all /usr/lib/libgit*
    lrwxrwxrwx 1 root root      14 Aug 16 15:54 /usr/lib/libgit2.so -> libgit2.so.1.5
    lrwxrwxrwx 1 root root      25 Sep 20 18:59 /usr/lib/libgit2.so.1.2 -> /usr/lib/libgit2.so.1.5.0
    lrwxrwxrwx 1 root root      16 Aug 16 15:54 /usr/lib/libgit2.so.1.5 -> libgit2.so.1.5.0
    -rwxr-xr-x 1 root root 1226024 Aug 16 15:54 /usr/lib/libgit2.so.1.5.0
    ╭=[ArchLaptopDR|~]==--
    ╰>

