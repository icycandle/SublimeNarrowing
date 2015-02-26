# SublimeNarrowing
 Sublime Test 3 code narrowing like vim plugin NrrwRgn

just copy from [sublimetext.com/forum/](https://www.sublimetext.com/forum/viewtopic.php?f=3&t=17077)
Origin Author is [BugFix](https://www.sublimetext.com/forum/memberlist.php?mode=viewprofile&u=12395)

But origin version cant handle unicode content, so i made little patch here.

My `User/Default (OSX).sublime-keymap`
```javascript
    // Custom package Narrow
    { "keys": ["ctrl+shift+n"], "command": "narrow" },
    { "keys": ["ctrl+shift+c"], "command": "narrow", "args": {"action": "replace"} },
```
