#!/usr/bin/bash
iconv -f EUCJP -t UTF8 mazegaki.dic | ./kigou.py | iconv -f UTF8 -t EUCJP > kigou.mdic
iconv -f EUCJP -t UTF8 mazegaki.dic | ./hyougai-kanji.py | iconv -f UTF8 -t EUCJP > r0.mdic
skkdic-expr2 r0.mdic - /usr/share/skk/SKK-JISYO.jinmei - /usr/share/skk/SKK-JISYO.geo - /usr/share/skk/SKK-JISYO.fullname > r1.mdic
skkdic-expr2 r0.mdic - r1.mdic > misc.mdic
iconv -f EUCJP -t UTF8 r1.mdic | ./restrain.py | iconv -f UTF8 -t EUCJP > r2.mdic
iconv -f EUCJP -t UTF8 r2.mdic | ./wago.py | iconv -f UTF8 -t EUCJP > wago.mdic
skkdic-expr2 r2.mdic - wago.mdic > r3.mdic
iconv -f EUCJP -t UTF8 r3.mdic | ./hyougai-yomi.py | iconv -f UTF8 -t EUCJP > k0.mdic
skkdic-expr2 r3.mdic - k0.mdic > r4.mdic
skkdic-expr2 r4.mdic + kigou.mdic + misc.mdic + dousi.mdic + my.mdic > restrained.dic
