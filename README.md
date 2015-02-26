# SublimeNarrowing
Sublime Test 3 code narrowing like vim plugin NrrwRgn

Just copy source code from [sublimetext.com/forum/](https://www.sublimetext.com/forum/viewtopic.php?f=3&t=17077)

**Origin Author**: [BugFix](https://www.sublimetext.com/forum/memberlist.php?mode=viewprofile&u=12395)

But origin version cant handle unicode content, so i made little patch here.

My `User/Default (OSX).sublime-keymap`
```javascript
    // open selected region in new window
    { "keys": ["ctrl+shift+n"], "command": "narrow" },
    // close window and write changed text back
    { "keys": ["ctrl+shift+c"], "command": "narrow", "args": {"action": "replace"} },
```
