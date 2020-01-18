# auto_key_map
automatically map typed keys to strings on Linux/Mac!

for this to work, you need `xdotool`. You can't get it on Windows.
for mac, just `brew install xdotool`. For linux, just `sudo {package-manager} install xdotool`.
for Ubuntu/Debian/Linux mint the package manager is apt-get, for Fedora it's yum, etc.

Basically, what this does is when you type specific key combinations it autocorrects to the intended character. Kinda like the 'compose' key.

inside config you'll find an example of how this works:
```
/
not ¬
and ∧
or ∨
xor ⊕
impl →
eq ↔
nand ⊼
```
basically,the first line is just the special character. If the special character is typed and then the word on the left is typed, then the text on the right will appear. For example, `/not` corrects to `¬` in this config file. You can configure the file however you want.

To make it work, just modify the config file and run the python script. You might need root privelages to run it.

This project was made because I was tired of typing CTRL+SHIFT+U+00AC to type out `¬` in my cse 311 class. Too many symbols and no good plug in to just make stuff work led to the creation of this handy little script.
