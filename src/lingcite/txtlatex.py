# -*- coding: cp1252 -*-
from ut import *
import unicodedata
import re
import six

retag = re.compile("<[^\>\<]+?>")
rerem = re.compile("<!\-\-[\s\S]+?\-\->")
def rmtags(txt):
    txt = rerem.sub(' ', txt)
    a = retag.split(txt)
    b = ''.join(a)
    return b.replace("&nbsp;", " ")

def inv11(d):
    return dict([(v, k) for (k, v) in d.items()])


ll = {}
ll[u'\u02b0'] = "\\textsuperscript{h}" #&#x2b0;
ll[u'\u02b2'] = "\\textsuperscript{j}" #&#x2b2;
ll[u'\u02b7'] = "\\textsuperscript{w}" #&#x2b7;
ll[u'\u0251'] = "\textscripta{}"
ll[u'\u0252'] = "\textturnscripta{}"
ll[u'\u0268'] = "\\textbari{}"
ll[u'\u026f'] = "\\textturnm{}"
ll[u'\u0272'] = "\\textltailn{}" #&#0272;
ll[u'\u027a'] = "\\\textturnlonglegr{}"
ll[u'\u027e'] = "\\textfishhookr{}"
ll[u'\u0282'] = "\\textrtails{}"
ll[u'\u0283'] = "\\textesh{}"
ll[u'\u0289'] = "\\textbaru{}"
ll[u'\u0290'] = "\\textrtailz{}"
ll[u'\u0292'] = "\\textyogh{}"
ll[u'\u0119'] = "\\textpolhook{e}"
ll[u'\u015f'] = "\\,{s}"
ll[u'\u0163'] = "\\,{t}"
ll[u'\u015b'] = "\\'{s}"
ll[u'\u01ce'] = "\\u{a}"
ll[u'\u0103'] = "\\u{a}"
ll[u"\xbf"] = ">"
ll[u"\xa1"] = "<"
ll[u"\xaa"] = "${}^2$"
ll[u'\u2021'] = "\\textdoublebarpipe{}"
ll[u'\u01c2'] = "\\textdoublebarpipe{}"
ll[u"\xf1"] = "\\~n"
ll[u"\xd1"] = "\\~N"
ll[u"\xe1"] = "\\'a"
ll[u"\xe0"] = "\\`a"
ll[u"\xf4"] = "\\^o"
ll[u"\xd4"] = "\\^O"
ll[u'\xd5'] = "\\~O"
ll[u"\xd2"] = "\\`O"
ll[u"\xc0"] = "\\`A"
ll[u"\xc3"] = '\\~{A}'
ll[u"\xc4"] = '\\"{A}'
ll[u"\xf5"] = "\\~o"
ll[u"\xf8"] = "\\o{}"
ll[u"\xd8"] = "\\O{}"
ll[u"\xdd"] = "\\'Y"
ll[u"\xe4"] = '\\"a'
ll[u"\xe3"] = "\\~a"
ll[u"\xe2"] = "\\^a"
ll[u"\xe9"] = "\\'e"
ll[u"\xea"] = "\\^e"
ll[u"\xca"] = "\\^E"
ll[u"\xc8"] = "\\`E"
ll[u"\xc9"] = "\\'E"
ll[u"\xcb"] = '\\"E'
ll[u"\xc1"] = "\\'A"
ll[u"\xc2"] = "\\^A"
ll[u"\xe7"] = "\\c{c}"
ll[u'\x81'] = '\\"u'
ll[u'\x82'] = "\\'e"
ll[u"\x83"] = "\\'{c}"
ll[u'\x86'] = '\\"o'
ll[u'\x8b'] = '\\"i'
ll[u'\x9e'] = '\\"a'
ll[u"\xe8"] = "\\`e"
ll[u"\xdf"] = "\\ss{}"
ll[u"\xfc"] = '\\"u'
ll[u"\xfe"] = '\\textthorn{}'
ll[u"\xa8"] = '\\"u'
ll[u"\xfb"] = '\\^u'
ll[u"\xf9"] = '\\`u'
ll[u"\xf2"] = '\\`o'
ll[u"\xfa"] = "\\'u"
ll[u"\xd9"] = "\\`U"
ll[u"\xda"] = "\\'U"
ll[u"\xee"] = "\\^i"
ll[u"\xec"] = "\\`i"
ll[u"\xed"] = "\\'i"
ll[u"\xcc"] = "\\`I"
ll[u"\xcd"] = "\\'I"
ll[u"\xce"] = '\\^I'
ll[u"\xcf"] = '\\"I'
ll[u"\xd6"] = '\\"O'
ll[u"\xf6"] = '\\"o'
ll[u"\xe5"] = '\\aa{}'
ll[u"\xe6"] = '\\ae{}'
ll[u"\xc5"] = '\\AA{}'
ll[u"\xc6"] = '\\AE{}'
ll[u"\xd3"] = "\\'O"
ll[u"\xfa"] = "\\'u"
ll[u"\xdb"] = '\\^U'
ll[u"\xdc"] = '\\"U'
ll[u"\xef"] = '\\"i'
ll[u"\xfd"] = "\\'y"
ll[u"\xff"] = '\\"y'
ll[u"\x85"] = "\\v{c}"
ll[u"\xf0"] = "\\v{z}"
ll[u"\xaf"] = "\\v{z}"
ll[u"\xc7"] = "\\c{C}"
ll[u"\x88"] = "^"
ll[u"\x8a"] = "\\v{S}"
ll[u"\x9a"] = "\\v{s}"
ll[u'\xa9'] = "(c)"
ll[u"\xbd"] = "\\'n"
ll[u"\xeb"] = '\\"e'
ll[u"\x91"] = "'"
ll[u"\xe2\x80\x99"] = "'"
ll[u"\x92"] = "'"
ll[u"\x93"] = "'"
ll[u"\x94"] = "'"
ll[u"\x98"] = "$\sim{}$"
ll[u"\x84"] = "'"
ll[u"\xa0"] = " "
ll[u"\xab"] = "'"
ll[u'\xa4'] = ""
ll[u"\xbb"] = "'"
ll[u"\xb4i"] = "\\'i"
ll[u"\x87a"] = "\\'a"
ll[u"\x95"] = "*" #vet ej
ll[u"\x99"] = "'" # vet ej
ll[u"\x9b"] = ">"
ll[u"t\xd5"] = "tz"
ll[u'\xb1'] = "\\plusminus{}"
ll[u"\xb4"] = "'"
ll[u"\xb5"] = "\\textmy{}"
ll[u"\xbc"] = "'" #vet ej
ll[u'\u04ab'] = "\\c{c}"
ll[u'\u0259'] = "\\textschwa{}"
ll[u'\u0144'] = "\\'n"
ll[u'\u0107'] = "\\'c"
ll[u'\u0113'] = "\\=e"
ll[u'\u1eca'] = "\\textsubdot{I}"
ll[u'\u1ecd'] = "\\textsubdot{o}"
ll[u'\u1eb9'] = "\\textsubdot{e}"
ll[u'\u1e5b'] = "\\textsubdot{r}"
ll[u'\u1ebd'] = "\\~e"
ll[u'\u2018'] = "'"
ll[u'\u2019'] = "'"
ll[u'\u201c'] = "'"
ll[u'\u201d'] = "'"
ll[u'\u01c0'] = "|"
ll[u'\u02bc'] = "'"
ll[u'\u2013'] = "-"
ll[u'\u2014'] = "-"
ll[u'\u2039'] = "$<$"
ll[u'\u203a'] = "$>$"
ll[u'\u2022'] = "\\middot{}"
ll[u'\u201a'] = ","
ll[u'\uf0bd'] = "\\'n"
ll[u'\u01c3'] = "!"
ll[u"\x8d"] = "\\v{e}"
ll[u"\u011b"] = "\\v{e}"
ll[u'\uf08d'] = "\\v{e}"
ll[u'\uf026'] = "\\v{e}"
ll[u'\uf020'] = "\\v{e}"
ll[u'\u0159'] = "\\v{r}"
ll[u'\uf0cd'] = "\\v{r}"
ll[u'\uf084'] = "\\v{C}"
ll[u'\uf085'] = "\\v{c}"
ll[u'\u010c'] = "\\v{C}"
ll[u'\u010d'] = "\\v{c}"
ll[u'\u014b'] = "\\ng{}"
ll[u'\u0160'] = "\\v{S}"
ll[u'\u0161'] = "\\v{s}"
ll[u'\u017c'] = "\\textdot{z}"
ll[u'\u017d'] = "\\v{Z}"
ll[u'\u017e'] = "\\v{z}"
ll[u'\u012b'] = "\\=i"
ll[u'\u0101'] = "\\=a"
ll[u'\u016b'] = "\\=u"
ll[u'\u012b'] = "\\v{j}"
ll[u'\u0121'] = "\\.{g}"
ll[u'\u1e6d'] = "\\textsubdot{t}"
ll[u'\u0129'] = "\\~i"
ll[u'\u0257'] = "\\textrhooktopd{}"
ll[u'\uf083'] = "\\'c"
ll[u'\ufffd'] = "?" #unknown char
ll[u'\u025b'] = "\\textepsilon{}"
ll[u'\u0254'] = "\\textopeno{}"
ll[u'\uf093'] = "\\textpolhook{e}"
ll[u'\u0142'] = "\\l{}"
ll[u'\u20ac'] = "\\euro{}"
ll[u'\u2020'] = "\\textbarpipe{}"
ll[u'\u2260'] = "\\textdoublebarpipe{}"
ll[u"\xad"] = "-"
ll[u"\x87"] = "\\textdoublebarpipe{}"
ll[u"\x97"] = "-"
ll[u'\xac'] = ""
ll[u'\xb7'] = "-"
ll[u"\x8e"] = "*" #points in a bullet
ll[u"\x96"] = "and"
ll[u"\xf3"] = "\\'o"
ll[u"\xf7s"] = "\\c{s}"
ll[u"\xba"] = "$\\circ{}$"
ll[u"\xb0"] = "$\\circ{}$"
ll[u'\u02da'] = "$\\circ{}$"
ll[u"&nbsp;"] = " "
ll[u"&amp;"] = "&"
ll[u'\xc3\x86'] = "\\AE{}"
ll[u'\xc3\xa6'] = "\\ae{}"
ll[u'\xc3\xa1'] = "\\'a"
ll[u'\xc3\xa3'] = "\\~a"
ll[u'\xc3\xa4'] = '\\"a'
ll[u'\xc3\xad'] = "\\'i"
ll[u'\xc3\xb3'] = "\\'o"
ll[u'\xc3\xb4'] = '\\^o'
ll[u'\xc3\xb6'] = '\\"o'
ll[u'\xc3\xbc'] = '\\"u'
ll[u'\xc3\xa9'] = "\\'e"
ll[u'\xc3\xad'] = "\\'i"
ll[u'\xc4\x8c'] = "\\v{C}"
ll[u'\xc4\x81'] = "\\=a"
ll[u'\xc9\x99'] = "\\textschwa{}"
ll[u'\xd2\xab'] = "\\c{c}"
ll[u'\xe1\xbb\x8a'] = "\\textsubdot{I}"
ll[u'\xe1\xbb\x8d'] = "\\textsubdot{o}"
ll[u'\xe1\xba\xb9'] = "\\textsubdot{e}"
ll[u'c\u0301'] = "\\'c"
ll[u'C\u0301'] = "\\'C"
ll[u'o\u0301'] = "\\'o"
ll[u'e\u0301'] = "\\'{e}"
ll[u'O\u0301'] = "\\'O"
ll[u'E\u0301'] = "\\'{E}"
ll[u'a\u0301'] = "\\'a"
ll[u'u\u0301'] = "\\'{u}"
ll[u'A\u0301'] = "\\'A"
ll[u'U\u0301'] = "\\'{U}"
ll[u'i\u0301'] = "\\'i"
ll[u'y\u0301'] = "\\'{y}"
ll[u'I\u0301'] = "\\'I"
ll[u'Y\u0301'] = "\\'{Y}"
ll[u's\u0301'] = "\\'{s}"
ll[u'S\u0301'] = "\\'{S}"
ll[u'\u01c1'] = "|"
ll[u'\xde'] = "\\textthorn{}"
ll[u'\u014a'] = "\\texteng{}"
ll[u'o\u0323'] = "\\textsubdot{o}"
ll[u'O\u0323'] = "\\textsubdot{O}"
ll[u'n\u0323'] = "\\textsubdot{n}"
ll[u'N\u0323'] = "\\textsubdot{N}"
ll[u'\xe2\x80\x99'] = "'"
ll[u'\xc9\x97'] = "\\textrhooktopd{}"
ll[u'\u0254\u0303'] = "\\~\\textopeno{}"
ll[u'\\textbaru{}\u0303'] = "\\~\\textbaru{}"
ll[u'a\u0303'] = "\\~a"
ll[u'o\u0330'] = "\\textsubtilde{o}"
ll[u'\\textbari{}\u0330'] = "\\textsubtilde{\\textbari{}}"
ll[u'm\u0330'] = "\\textsubtilde{m}"
ll[u'\xc9\x94\xcc\x83'] = "\\~\\textopeno{}"
ll[u'h\u0323'] = "\\textsubdot{h}"
ll[u'c\u0327'] = "\\c{c}"
ll[u'o\u0308'] = '\\"o'
ll[u'O\u0308'] = '\\"O'
ll[u'u\u0308'] = '\\"u'
ll[u'U\u0308'] = '\\"U'
ll[u'a\u0308'] = '\\"a'
ll[u'A\u0308'] = '\\"A'
ll[u'a\u0304'] = "\\=a"
ll[u'A\u0304'] = "\\=A"
ll[u'i\u0304'] = "\\=i"
ll[u'I\u0304'] = "\\=I"
ll[u'e\u0304'] = "\\=e"
ll[u'E\u0304'] = "\\=e"
ll[u'u\u0304'] = "\\=u"
ll[u'U\u0304'] = "\\=U"
ll[u'o\u0304'] = "\\=o"
ll[u'O\u0304'] = "\\=O"
ll[u'i\u0302'] = "\\^i"
ll[u'I\u0302'] = "\\^I"
ll[u'e\u0302'] = "\\^e"
ll[u'a\u0302'] = "\\^a"
ll[u'o\u0302'] = "\\^o"
ll[u'E\u0302'] = "\\^E"
ll[u'A\u0302'] = "\\^A"
ll[u'O\u0302'] = "\\^O"
ll[u'u\u0302'] = "\\^u"
ll[u'U\u0302'] = "\\^U"
ll[u'\u02bb'] = "'"
ll[u'\u02b9'] = "'"
ll[u'i\u0308'] = '\\"i'
ll[u'l\u0323'] = "\\textsubdot{l}"
ll[u't\u0323'] = "\\textsubdot{t}"
ll[u'd\u030c'] = "\\v{c}"
ll[u'D\u030c'] = "\\v{C}"
ll[u'c\u030c'] = '\\v{c}'
ll[u's\u030c'] = '\\v{s}'
ll[u'C\u030c'] = '\\v{C}'
ll[u'S\u030c'] = '\\v{S}'
ll[u'e\u030c'] = '\\v{e}'
ll[u'E\u030c'] = '\\v{E}'
ll[u'z\u030c'] = '\\v{z}'
ll[u'Z\u030c'] = '\\v{Z}'
ll[u'e\u0306'] = '\\u{e}'
ll[u'a\u0306'] = '\\u{a}'
ll[u'e\u0300'] = '\\`e'
ll[u'a\u0300'] = '\\`a'
ll[u'i\u0300'] = '\\`i'
ll[u'o\u0300'] = '\\`o'
ll[u'n\u0303'] = '\\~n'
ll[u'N\u0303'] = '\\~N'
ll[u'o\u0303'] = '\\~o'
ll[u'O\u0303'] = '\\~O'
ll[u'a\u0303'] = '\\~a'
ll[u'A\u0303'] = '\\~A'
ll[u'e\u0303'] = '\\~e'
ll[u'E\u0303'] = '\\~E'
ll[u'e\u0308'] = '\\"e'
ll[u'a\u030a'] = '\\aa{}'
ll[u'A\u030a'] = '\\AA{}'
ll[u'\u03a9'] = "\\textomega{}"
ll[u"\xd7k"] = "?k" #vet ej
ll[u"\x9dita"] = "?"
ll[u"\xae"] = "?"
ll[u'\u2212'] = "-"
ll[u'\u0269'] = "'"

spcud = {}
spcud["\\AA"] = "A"
spcud["\\AE"] = "Ae"
spcud["\\aa"] = "a"
spcud["\\ae"] = "e"
spcud["\\O"] = "O"
spcud["\\o"] = "o"
spcud["\\oslash"] = "o"
spcud["\\Oslash"] = "O"
spcud["\\L"] = "L"
spcud["\\l"] = "l"
spcud["\\OE"] = "OE"
spcud["\\oe"] = "oe"
spcud["\\i"] = "i"
spcud['\\NG'] = "NG"
spcud['\\ng'] = "ng"
spcud['\\texteng'] = "ng"
spcud['\\ss'] = "ss"
spcud['\\textbari'] = "i"
spcud['\\textbaru'] = "u"
spcud['\\textbarI'] = "I"
spcud['\\textbarU'] = "U"
spcud['\\texthtd'] = "d"
spcud['\\texthtb'] = "b"
spcud['\\textopeno'] = "o"
spcud['\\textepsilon'] = "e"

uuc = {}
uuc[u"\xbf"] = '?' #upside down spanish q-mark
uuc[chr(449)] = "||"
uuc[chr(450)] = "/="
uuc[u'\u01c3'] = "!"
uuc[chr(705)] = "'" #ain
uuc[chr(596)] = "o" #(openo)
uuc[chr(603)] = "e" #(epsilon)
uuc[chr(949)] = "e" #(epsilon)
uuc[chr(8580)] = "o" #(openo)
uuc[u'\u05db'] = "o" #(openo)
uuc[chr(618)] = "i"
uuc[chr(638)] = "r" #(tap r)
uuc[chr(651)] = "u" #(upsilon)
uuc[chr(652)] = "a"
uuc[u'\u201b'] = "'" #ain
uuc[u'\u02ba'] = '"' 
uuc[u'\u02bb'] = "'"
uuc[u'\u02bc'] = "'"
uuc[u'\u02bd'] = "'"
uuc[u'\u02be'] = "'" #ain
uuc[u'\u02bf'] = "'" #ain
uuc[u"\u2013"] = '-'
uuc[u"\u201c"] = '"'
uuc[u"\u201d"] = '"'
uuc[u"\u0291"] = "z"
uuc[u"\u0295"] = "'" #ayn
uuc[u"\u0294"] = "'"
uuc[u"\u0167"] = "t"
uuc[u"\u03b3"] = "gh"
uuc[u"\u0263"] = "gh"
uuc[u"\u0111"] = "d" #vietnamese
uuc[u"\u0110"] = "D"
uuc[u"\u0456"] = "i"
uuc[u"\u0259"] = "e" #schwa
uuc[u"\u044c"] = "e" #hard sign sometimes used for schwa in russo-sinitic orthography
uuc[u"\u2014"] = "-"
uuc[u"\xfe"] = "th" #Icelandic
uuc[u"\xf0"] = "dh"
uuc[u"\u2018"] = "'"
uuc[u"\u2019"] = "'"
uuc[u'\u02d0'] = ":"
uuc[u'\u026b'] = "l" #barred l (armenian)
uuc[u"\u026c"] = "l" #barred l
uuc[u'\u2c62'] = "L" #barred L (armenian)
uuc[u"\u026f"] = "u" #w like
uuc[u'\u028a'] = "u" #put-vowel phonetic sign
uuc[u"\u025c"] = "e" #exsilon backwards
uuc[u"\u02b9"] = "'"
uuc[u"\u02bc"] = "'"
uuc[u"\u0283"] = "s" #esh
uuc[u"\u01dd"] = ""
uuc[u'\u03b5'] = "e" #epsilon
uuc[u'\u03c9'] = "o" #omega
uuc[u'\u0277'] = "o" #omega closed at the top
uuc[u'\u03c6'] = "f" #phi
uuc[u'\u043e'] = "o" #Russian o?
uuc[u'\u0264'] = "u" #central vowel
uuc[u'\u0269'] = "'"

def unemptyparen(txt, resubs = [re.compile("(?<!\S)([^\s\\\\]+)\{(\\\\[^\s\}]+)\}"), re.compile("(\\\\['`" + '"' + "^~=\.]+[a-z])\{(\\\\[^\s\}]+)\}")]):
    for resub in resubs:
        txt = resub.sub("\g<1>\g<2>", txt)
    return txt

def undiacritic(txt, resub = re.compile("\\\\[\S]+\{|\\\\.|\}|(?<!\S)\{")):
    if type(txt) == type(u""):
        return undiacritic_utf8(txt) 
    txt = unemptyparen(txt)
    for (k, v) in spcud.items():
        txt = txt.replace(k + "{}", v)
    for (k, v) in spcud.items():
        txt = txt.replace(k, v)
    return resub.sub("", txt)

def unknownch(c):
    if ord(c) > 127:
        return "?[\\" + "u" + str(ord(c)).zfill(4) + "]"
    return c

def txttolatex(x, verbose = "Smart-verbose"):
    return killutf8(x, verbose).encode("ascii")
    
def killutf8(txt, verbose = "Smart-verbose"):
    try:
        u8 = txt.decode("utf-8")
    except UnicodeDecodeError:
        u8 = unicode(txt, "latin-1") #encode("utf-8")
    for (f, s) in ll.items():
        u8 = u8.replace(f, s)
    return remainutf8(u8)

def remainutf8(u8, verbose = "Smart-verbose"):
    try:
        u8.encode("ascii")
    except UnicodeEncodeError:
        if verbose == "Smart-verbose":
            print("NON-ASCII CHAR")
            for (i, c) in [(i, c) for (i, c) in enumerate(u8) if ord(c) > 127]:
                print(c, [c], u8[i-10:i+10])
        elif verbose == "Verbose":
            print("NON-ASCII CHAR", u8)
            print([c for c in u8 if ord(c) > 127])
        u8 = u''.join([unknownch(c) for c in u8])
        #print u8
    return u8

lathtml = {}
#lathtml["l"] = "lig"
lathtml["s"] = "slash"
lathtml["r"] = "ring"
lathtml['"'] = "uml"
#lathtml['`'] = "grave"
#lathtml["'"] = "acute"
lathtml['c'] = "cedil"
#lathtml['v'] = "caron"
#lathtml['^'] = "circ"
#lathtml['~'] = "tilde"
lathtml['b'] = "raised"

htmllat = inv11(lathtml)
htmllat["grave"] = '`'
htmllat["acute"] = "'"
htmllat["caron"] = 'v'
htmllat["circ"] = '^'
htmllat["tilde"] = '~'
htmllat["uml"] = '"'
htmllat["x0301"] = "'"
htmllat["x0303"] = '~'
htmllat["x0302"] = '^'
htmllat["x0300"] = '`'
htmllat["x0308"] = '"'
htmllat["x0323"] = 'textsubdot'
htmllat["x030c"] = 'u'
htmllat["x0307"] = '.'
htmllat["x0304"] = '='
htmllat["x0328"] = 'textpolhook'
htmllat["x0331"] = 'textsubbar'
htmllat["x030b"] = 'H'
htmllat["x032a"] = 'textsubbridge'
htmllat["x0335"] = '-'
htmllat["x0330"] = 'textsubtilde'
htmllat["x032c"] = 'textsubwedge'
htmllat["x032e"] = 'textsubbreve'
htmllat["x0329"] = 'textsyllabic'
#def textsubdot(x):
#    if charnum2.has_key(x):
#        return "&#" + str(charnum2[x] + 7864) + ";"
#    return x + "&#x0323;"

#def acute(x):
#    if x in ['s', 'S', 'c', 'C', 'n', 'N']:
#        return x + "&#x0301;"
#    return "&" + x + "acute;"

#def tilde(x):
#    if x in ['e', 'E', 'i', 'I', 'y', 'Y', 'u', 'U', 'm', 'M']:
#        return x + "&#x0303;"
#    return "&" + x + "tilde;"

latind = {}
latind["superscript"] = lambda x: "<sup>" + x + "</sup>"
latind["textsuperscript"] = lambda x: "<sup>" + x + "</sup>"
latind["'"] = lambda x: x + "&#x0301;"
latind["`="] = lambda x: latind["`"](latind['='](x))
latind["'="] = lambda x: latind["'"](latind['='](x))
latind["'"  + '"'] = lambda x: latind["'"](latind['"'](x))
latind["~"] = lambda x: x + "&#x0303;"
latind["^"] = lambda x: x + "&#x0302;"
latind["`"] = lambda x: x + "&#x0300;"
latind['"'] = lambda x: x + "&#x0308;"
latind['textsubdot'] = lambda x: x + "&#x0323;"
latind['u'] = lambda x: x + "&#x030c;" #TODO
latind['='] = lambda x: x + "&#x0304;"
latind['-'] = lambda x: x + "&#x0335;"
latind['v'] = lambda x: x + "&#x030c;" #TODO
latind['.'] = lambda x: x + "&#x0307;"
latind['r'] = lambda x: x + "&#x030a;"
latind['textacutemacron'] = lambda x: latind["'"](latind['='](x))
latind['textsubbar'] = lambda x: x + "&#x0331;"
latind['textsubline'] = lambda x: x + "&#x0331;"
latind['b'] = lambda x: x + "&#x0331;"
latind['textsubbreve'] = lambda x: x + "&#x032e;"
latind['textpolhook'] = lambda x: x + "&#x0328;"
latind['textsyllabic'] = lambda x: x + "&#x0329;"
latind['textsubtilde'] = lambda x: x + "&#x0330;"
latind['textsubwedge'] = lambda x: x + "&#x032c;"
latind['textsubring'] = lambda x: x + "&#x0325;"
latind['textsubbridge'] = lambda x: x + "&#x032a;"
latind['H'] = lambda x: x + "&#x030b;"
latind['textstrike'] = lambda x: x + "&#x0336;"


latlig = {}
latlig['&'] = "amp "
latlig['aa'] = "aring"
latlig['Aa'] = "Aring"
latlig['AA'] = "Aring"
latlig['ae'] = "aelig"
latlig['AE'] = "AElig"
latlig['oe'] = "oelig"
latlig['OE'] = "OElig"
latlig['o'] = "oslash"
latlig['O'] = "Oslash"
latlig['oslash'] = "oslash"
latlig['Oslash'] = "Oslash"
latlig['i'] = "#305"
latlig['ss'] = "szlig"
latlig['NG'] = "#330"
latlig['ng'] = "#331"
latlig["cb{S}"] = "#x218"
latlig["cb{s}"] = "#x219"
latlig["cb{T}"] = "#x21a"
latlig["cb{t}"] = "#x21b"
latlig["textsuperscript{h}"] = "#x2b0"
latlig["textsuperscript{j}"] = "#x2b2"
latlig["textsuperscript{w}"] = "#x2b7"
latlig['textltailn'] = "#x0272"
latlig['textlambda'] = "lambda"
latlig['texthtd'] = "#599"
latlig['textrhooktopd'] = "#599"
latlig['texthtb'] = "#595"
latlig['textrhooktopb'] = "#595"
latlig['texthtd'] = "#599"
latlig['texthtb'] = "#595"
latlig['textopeno'] = "#596"
latlig['textbari'] = "#616"
latlig['textbaru'] = "#649"
latlig['textbarI'] = "#407"
latlig['textbarU'] = "#580"
latlig['textltailn'] = "#626"
latlig['textupsilon'] = "#965"
latlig['textepsilon'] = "#603"
latlig['textomega'] = "#937"
latlig['plusminus'] = "#177"
latlig['eurosign'] = "#8364"
latlig['textschwa'] = '#601'
latlig['textgamma'] = '#611'
latlig['textless'] = 'lt'
latlig['textgreater'] = 'gt'
latlig['textthorn'] = 'thorn'
latlig['textesh'] = '#154'
latlig['texteta'] = '#951'
latlig['texttheta'] = '#952'
latlig['textbeta'] = '#946'
latlig['circ'] = 'deg'
latlig['textdoublebarpipe'] = "#x01c2"
latlig['textdoublebarpipevar'] = "#x01c2"
latlig['texteng'] = '#x014a'
latlig['texteuro'] = '#x20ac'
latlig['textglotstop'] = "#660"
latlig['textvertline'] = "#124"
latlig['textdoublevertline'] = "#2016"
latlig['textraiseglotstop'] = "#x02c0"
latlig['DH'] = "ETH"
latlig['dh'] = "eth"
latlig['textturna'] = "#x250"
latlig['textscriptv'] = "#x28b"
latlig['textrtaild'] = "#x256"
latlig['textltailn'] = "#x272"
latlig['textsubrhalfring'] = "#x339"
latlig['textsci'] = "#x26a"
latlig['textphi'] = "#x278"
latlig['textchi'] = "chi"
latlig['textscu'] = "#x28a" #textupsilon
latlig['L'] = "#321"
latlig['l'] = "#322"
latlig['textchi'] = "#967"
latlig['ldots'] = 'hellip'
latlig['textrevepsilon'] = "#604"
latlig['textrtails'] = "#537"
latlig['textrtailr'] = "#637"
latlig['Ohorn'] = "#416"
latlig['ohorn'] = "#417"
latlig['texthardsign'] = "#1098"
latlig['textquestiondown'] = "iquest"
latlig['textturnv'] = "#652"
latlig['textquotedblleft'] = "ldquo"
latlig['textquotedblright'] = "rdquo"
latlig['guillemotleft'] = "laquo"
latlig['guillemotright'] = "raquo"
latlig['textemdash'] = "mdash"
latlig['textemdash'] = "ndash"

liglat = inv11(latlig)

def latexsub(o, warnings = True):
    typ = o.group('typ')
    ch = o.group('ch')
    if typ in lathtml:
        return "&" + ch + lathtml[typ] + ";"
    if typ in latind:
        return latind[typ](ch)
    if typ in latlig:
        return "&" + latlig[typ] + ";"

    print("Warning: Latex-to-Html Unknown latex symbol '%s', '%s'" % (typ, ch))
    return typ + ch

def latexsubutf8(o):
    typ = o.group('typ')
    ch = o.group('ch')
    #if typ == "" or typ == "f" or ch == "f":
    #    print typ, ch
    if typ in lathtml:
        return "&" + ch + lathtml[typ] + ";"
    if typ in latind:
        return latind[typ](ch)
    if typ in latlig:
        return "&" + latlig[typ] + ";"
    return "\\" + typ + (ch if ch in [' ', "\n"] else "{" + ch + "}")

def htmlsub(o):
    typ = o.group('typ')
    ch = o.group('ch')
    if typ in htmllat:
        return "\\" + htmllat[typ] + "{" + ch + "}"
    #if latind.has_key(typ):
    #    return latind[typ](ch)
    if (typ + ch) in liglat:
        return "\\" + liglat[typ+ch] + "{}"
    if (ch + typ) in liglat:
        return "\\" + liglat[ch+typ] + "{}"
    if ("#" + typ) in liglat:
        return ch + "\\" + liglat["#" + typ] + "{}"
    if typ == "#":
        if ch.startswith("x"):
            return "\\unichar{%s}" % int(ch[1:], 16) 
        return "\\unichar{%s}" % ch

    print("Warning: Unknown html symbol", typ, ch)
    return typ + ch



platexspc = {}
platexspc[0] = re.compile("\\\\(?P<typ>[^\%\'\`\^\~\=\_" + '\\"' + "\s\{]+)\{(?P<ch>[a-zA-Z]?)\}")
platexspc[1] = re.compile("\\\\(?P<typ>[\'\`\^\~\=\_" + '\\"' + "]+?)\{(?P<ch>[a-zA-Z])\}")
platexspc[2] = re.compile("\\\\(?P<typ>[^a-zA-Z\s\%\_])(?P<ch>[a-zA-Z])")
platexspc[3] = re.compile("\\\\(?P<typ>[^a-zA-Z\s\%\{\_]+)(?P<ch>[a-zA-Z])")
platexspc[4] = re.compile("\\\\(?P<typ>[^\{\%\_]+)\{(?P<ch>[^\}]+)\}")
platexspc[5] = re.compile("\\\\(?P<typ>[^\{\_\\\\\s\%]+)(?P<ch>\s)")


refilename = re.compile("[\S\.]+\.[a-zA-Z][a-zA-Z][a-zA-Z][a-zA-Z]?")

#TODO nestade och combinations, da maste det som ar inuti {} kunna vara langre
#an en bokst lineunder, subline

def latex_to_html(txt, warnings = True):
    txt = txt.replace("\&", "&amp;")
    txt = txt.replace("\#", "&#35;")
    txt = txt.replace("\%", "&#37;")
    txt = reuch.sub(lambda o: "&#" + o.group(1) + ";", txt)
    #txt = txt.replace("\\iuml;", "&iuml;")

    txt = emphtohtml(txt)
    for i in sorted(platexspc.keys()):
        txt = platexspc[i].sub(latexsub, txt)
    

    #txt = txt.replace("&zcaron;", "&#158;")
    #txt = txt.replace("&Zcaron;", "&#142;")
    #txt = txt.replace("&ccaron;", "&#269;")
    #txt = txt.replace("&Ccaron;", "&#268;")

    #txt = txt.replace("&scaron;", "&#253;")
    #txt = txt.replace("&Scaron;", "&#252;")

    i = txt.find('\\')
    if i >= 0 and warnings:
        if not refilename.match(txt[i+1:]):
            print("Warning tex-to-html: No subst for " + txt[max(i-10, 0):i] + txt[i:i+30])

    txt = txt.replace("~", "&nbsp;")
    txt = txt.replace("{", "")
    txt = txt.replace("}", "")
    
    return txt

def unichrrep(o):
    try:
        return six.unichr(int(o.group(1))) #six.unichr(int("0x" + o.group(1), 16))
    except ValueError:
        print("Unicode not in range", o.group(1)) #int("0x" + o.group(1), 16), "from",
        return o.group(1)


accents = {
    0x0300: '`', 0x0301: "'", 0x0302: '^', 0x0308: '"',
    0x030B: 'H', 0x0303: '~', 0x0327: 'c', 0x0328: 'k',
    0x0304: '=', 0x0331: 'b', 0x0307: '.', 0x0323: 'd',
    0x030A: 'r', 0x0306: 'u', 0x030C: 'v',
}

#TODO ta alla htmllat som borjar med x

def utf8_to_tex(text):
    if type(text) == type(""):
        return text
    out = ""
    txt = tuple(text)
    i = 0
    while i < len(txt):
        char = text[i]
        code = ord(char)

        # combining marks
        if unicodedata.category(char) in ("Mn", "Mc") and (code in accents) and  (i + 1) < len(txt):
            out += "\\%s{%s}" %(accents[code], txt[i+1])
            i += 1
        # precomposed characters
        elif unicodedata.decomposition(char):
            try:
                base, acc = unicodedata.decomposition(char).split()
                acc = int(acc, 16)
                base = int(base, 16)
                if acc in accents:
                    out += "\\%s{%s}" %(accents[acc], six.unichr(base))
                else:
                    out += char
            except ValueError:
                print("Unicodeerror", i, char, text)
                out += char
        else:
            out += char

        i += 1

    for (k, v) in ll.items():
        out = out.replace(k, v)

    return remainutf8(out)

rehorn = re.compile("\\\\(?P<c>[a-zA-Z])horn\{?\}?")
def killT5(txt):
    return rehorn.sub("\\g<c>", txt)

def texurl(o):
    return "\\href{%s}{%s}" % (o.group("url"), o.group("label").replace("_", "\_")) 

reahref = re.compile("""\<[Aa]\s[Hh][Rr][Ee][Ff]\=['"](?P<url>[^'"]+)['"]\>(?P<label>[^<]+)\<\/[Aa]\>""")
def htmlurl_to_latex(txt):
    return reahref.sub(texurl, txt)


phtmlspc = {}
phtmlspc[0] = re.compile("&(?P<typ>[\#])(?P<ch>[\da-f]+);")
phtmlspc[1] = re.compile("&(?P<ch>[a-zA-Z])(?P<typ>[a-zA-Z]+);")
phtmlspc[2] = re.compile("(?P<ch>[a-zA-Z])&\#(?P<typ>[^\;]+?);")
phtmlspc[3] = re.compile("(?P<ch>\\\\[\'\`\^\~\=" + '\\"' + "]\{[a-zA-Z]\})&\#(?P<typ>[^\;]+?);")
phtmlspc[4] = re.compile("&(?P<typ>[\#])(?P<ch>x[\da-f]+);")
def html_to_latex(txt, debug = ''):
    txt = htmlurl_to_latex(txt)
    
    txt = txt.replace("&amp;", "\&")
    txt = txt.replace("&nbsp;", " ")
    txt = txt.replace("&lt;", "'")
    txt = txt.replace("&gt;", "'")
    txt = txt.replace("&quot;", '"')
    #txt = txt.replace("&laquo;", "'")
    #txt = txt.replace("&raquo;", "'")
    txt = txt.replace("&#35;", "\#")
    txt = txt.replace("&#37;", "\%")
    txt = txt.replace("&#8212;", "\=")
    txt = txt.replace("&#8217;", "'")
        
    #txt = reuch.sub(lambda o: "&#" + o.group(1) + ";", txt)
    
    txt = htmltoemph(txt)
    for i in sorted(phtmlspc.keys()):
        txt = phtmlspc[i].sub(htmlsub, txt)

    #There may be some combining ones left
    for (xht, ltx) in htmllat.items():
        txt = re.sub("(?P<c>\\\\[^\\{]+\\{[^\\}]*\})\\&\\#%s;" % re.escape(xht), "\\\\" + "%s{\\g<c>}" % ltx, txt)

    #for i in sorted(platexspc.keys()):
    #    txt = platexspc[i].sub(latexsub, txt)

    #txt = txt.replace("&zcaron;", "&#158;")
    #txt = txt.replace("&Zcaron;", "&#142;")
    #txt = txt.replace("&ccaron;", "&#269;")
    #txt = txt.replace("&Ccaron;", "&#268;")

    #txt = txt.replace("&scaron;", "&#253;")
    #txt = txt.replace("&Scaron;", "&#252;")
    
    txt = txt.replace("&nbsp;", "~")

    i = txt.find('&')
    if i >= 0 and txt[i-1:i] != "\\":
        print("Warning: No subst for " + txt[max(i-10, 0):i] + txt[i:i+30])
        print("Debug:", debug)

    #txt = txt.replace("{", "")
    #txt = txt.replace("}", "")
    
    return killT5(txt) 

htmltxt = {}
htmltxt["&amp;"] = "&"
htmltxt["&#35;"] = "#"
htmltxt["&#37;"] = "%"
htmltxt["&rsquo;"] = "'"
htmltxt["&lsquo;"] = "'"
htmltxt["&atilde;"] = "ã"
htmltxt["&Atilde;"] = "Ã"
htmltxt["&ntilde;"] = "ñ"
htmltxt["&Ntilde;"] = "Ñ"
htmltxt["&ecirc;"] = "ê"
htmltxt["&Ecirc;"] = "Ê"
htmltxt["&auml;"] = "ä"
htmltxt["&Auml;"] = "Ä"
htmltxt["&ouml;"] = "ö"
htmltxt["&Ouml;"] = "Ö"
htmltxt["&aring;"] = "å"
htmltxt["&Aring;"] = "Å"
htmltxt["&aring;"] = "å"
htmltxt["&Aring;"] = "Å"
htmltxt["&iacute;"] = "í"
htmltxt["&Iacute;"] = "Í"
htmltxt["i&#x0301;"] = "í"
htmltxt["I&#x0301;"] = "Í"
htmltxt["&uacute;"] = "ú"
htmltxt["&Uacute;"] = "Ú"
htmltxt["&aacute;"] = "á"
htmltxt["&Aacute;"] = "Á"
htmltxt["u&#x0301;"] = "ú"
htmltxt["U&#x0301;"] = "Ú"
htmltxt["&oacute;"] = "ó"
htmltxt["&Oacute;"] = "Ó"

htmltxt["o&#x0301;"] = "ó"
htmltxt["O&#x0301;"] = "Ó"
htmltxt["n&#x0303;"] = "ñ"
htmltxt["N&#x0303;"] = "Ñ"
    
htmltxt["&uuml;"] = 'ü'
htmltxt["&Uuml;"] = 'Ü'
htmltxt["&eacute;"] = "é"
htmltxt["&Eacute;"] = "É"
htmltxt["&euml;"] = "ë"
htmltxt["&Euml;"] = "Ë"
htmltxt["e&#x0301;"] = "é"
htmltxt["E&#x0301;"] = "É"
htmltxt["&egrave;"] = "è"
htmltxt["&Egrave;"] = "È"
htmltxt["&ugrave;"] = "ù"
htmltxt["&Ugrave;"] = "Ù"
htmltxt["e&#x0300;"] = "è"
htmltxt["E&#x0300;"] = "È"
htmltxt["i&#x0300;"] = "ì"
htmltxt["I&#x0300;"] = "Ì"
htmltxt["u&#x0300;"] = "ù"
htmltxt["U&#x0300;"] = "Ù"
htmltxt["e&#x0302;"] = "ê"
htmltxt["E&#x0302;"] = "Ê"
htmltxt["a&#x0302;"] = "â"
htmltxt["A&#x0302;"] = "Â"
htmltxt["i&#x0302;"] = "î"
htmltxt["I&#x0302;"] = "Î"
htmltxt["o&#x0302;"] = "ô"
htmltxt["O&#x0302;"] = "Ô"
htmltxt["a&#x0300;"] = "à"
htmltxt["A&#x0300;"] = "À"
htmltxt["a&#x0301;"] = "á"
htmltxt["A&#x0301;"] = "Á"
htmltxt["a&#x0303;"] = "ã"
htmltxt["A&#x0303;"] = "Ã"
htmltxt["o&#x0303;"] = "õ"
htmltxt["O&#x0303;"] = "Õ"
htmltxt["&szlig;"] = chr(223)
htmltxt["&AElig;"] = chr(198)
htmltxt["&aelig;"] = chr(230)


htmltxt["&Oslash;"] = chr(216)
htmltxt["&oslash;"] = "ø"
htmltxt["&ccedil;"] = "ç"
htmltxt["&Ccedil;"] = "Ç"
htmltxt["&hellip;"] = "..."
htmltxt["&lt;"] = "<"
htmltxt["&gt;"] = ">"
htmltxt["&iuml;"] = 'ï'
#phtmlspc = {}
#phtmlspc[0] = re.compile("&(?P<typ>[\#])(?P<ch>\d+);")
#phtmlspc[1] = re.compile("&(?P<ch>[a-z])(?P<typ>[a-z]+);")
def html_to_txt(txt, warnings = False):
    for (h, t) in htmltxt.items():
        if type(txt) == type(u""):
            t = t if type(t) == type(u"") else t.decode("latin-1") 
        txt = txt.replace(h, t)
    
    i = txt.find('&')
    if i >= 0 and txt[i+1] != ' ':
        if warnings:
            print("Warning html-to-txt: No subst for " + txt[max(i-10, 0):i] + txt[i:i+30])

    txt = txt.replace("&nbsp;", " ")
    return txt 

#&aacute;

rehtmlhex = re.compile("\&\#x([^\;]+)\;")
rehtmlch = re.compile("\&\#(\d+)\;")
rehtmls = re.compile("\&\S+\;")
def html_to_utf8(txt, warnings = True):
    txt = html_to_txt(txt, warnings = False)
    if type(txt) != type(u""):
        txt = unicode(txt, "latin-1")
    txt = rehtmlhex.sub(lambda o: six.unichr(int("0x" + o.group(1), 16)), txt)
    txt = rehtmlch.sub(lambda o: six.unichr(int(o.group(1))), txt)

    txt = txt.replace("&ETH;", six.unichr(208))
    txt = txt.replace("&eth;", six.unichr(240))
    txt = txt.replace("&OElig;", six.unichr(338))
    txt = txt.replace("&oelig;", six.unichr(339))
    txt = txt.replace("&nu;", six.unichr(957))
    txt = txt.replace("&Nu;", six.unichr(925))
    txt = txt.replace("&chi;", six.unichr(935))
    txt = txt.replace("&nacute;", six.unichr(324))
    txt = txt.replace("&Nacute;", six.unichr(323))
    txt = txt.replace("&scedil;", six.unichr(351))
    txt = txt.replace("&Scedil;", six.unichr(350))
    txt = txt.replace("&iquest;", six.unichr(191))
    txt = txt.replace("&laquo;", six.unichr(171))
    txt = txt.replace("&raquo;", six.unichr(187))
    txt = txt.replace("&ldquo;", six.unichr(8220))
    txt = txt.replace("&rdquo;", six.unichr(8221))
    txt = txt.replace("&mdash;", six.unichr(2014))
    txt = txt.replace("&ndash;", six.unichr(2013))
    txt = txt.replace("&hellip;", "...")

    txt = txt.replace("&quot;", "'")
    #txt = txt.replace("&amp;", "&")

    txt = txt.replace(six.unichr(450), "/=")
    txt = txt.replace("$\\sim{}$", six.unichr(int("0x223c", 16)))

    o = rehtmls.search(txt)
    if o:
        i = o.start()
        if warnings:
            print("Warning html-to-utf8: No subst for " + txt[max(i-10, 0):i] + txt[i:i+30])
    return txt


#links, bold, italic
abtemplate = '{\\\\field{\\\\*\\\\fldinst{HYPERLINK "%s"}}{\\\\fldrslt{\\\\ul %s}}}'
#    wrap = ('<a title="%s">' % ('; '.join([x for x in onmouse if x]))) + cit + '</a>'

rehtmllink = re.compile('\<[aA] [hH][rR][eE][fF]="(?P<link>[^"]+)"\>(?P<name>[^\<]+)\</[aA]\>')
def html_to_rtf(txt):
    txt = txt.replace('<I>', '{\\i ') 
    txt = txt.replace('<i>', '{\\i ') 
    txt = txt.replace('</I>', '}') 
    txt = txt.replace('</i>', '}') 
    txt = txt.replace('<B>', '{\\b ') 
    txt = txt.replace('<b>', '{\\b ') 
    txt = txt.replace('</B>', '}') 
    txt = txt.replace('</b>', '}')
    txt = txt.replace('(', "\\'28")
    txt = txt.replace(')', "\\'29")
    txt = txt.replace('[', "\\'5b")
    txt = txt.replace(']', "\\'5d")
    return rehtmllink.sub(abtemplate % ('\g<link>', '\g<name>'), txt)
    #txt = txt.replace('<SMALL>', '{\\b') 
    #txt = txt.replace('<small>', '{\\b') 
    #txt = txt.replace('</SMALL>', '}') 
    #txt = txt.replace('</small>', '}') 


def ascii_to_unicode(txt):
    return unicode(txt, 'iso-8859-1')

def emphtohtml(txt, repl = {'emph': ('<I>', '</I>'), 'url': ('<A href="', '">link</A>'), 'russianquotes': ("&laquo;", "&raquo;"), 'textsuperscript': ('<sup>', '</sup>')}):
    t = txt
    for (e, (r1, r2)) in repl.items():
        rep = re.compile('\\\\' + e + '{(?P<c>(([^{}])|({[^{}]*}))*)}')
        t = rep.sub(r1 + '\g<c>' + r2, t)
    return t

def emphtomarkdown(txt, repl = {'emph': ('_', '_'), 'url': ('<', '>')}):
    t = txt
    for (e, (r1, r2)) in repl.items():
        rep = re.compile('\\\\' + e + '{(?P<c>(([^{}])|({[^{}]*}))*)}')
        t = rep.sub(r1 + '\g<c>' + r2, t)
    return t


def htmltoemph(txt, repl = {'emph': ('<I>', '</I>'), 'url': ('<A href="', '">[^\<\>]*</A>'), 'textsuperscript': ('<sup>', '</sup>')}):
    for (e, (r1, r2)) in repl.items():
        rep = re.compile(re.escape(r1) + '(?P<c>[^\<\>]*)' + re.escape(r2))
        txt = rep.sub('\\\\' + e + '{\g<c>}', txt)
    return txt

def latex_to_rtf(txt):
    return rmtags(html_to_rtf(latex_to_html(txt)))

def latex_to_txt(txt):
    return html_to_txt(latex_to_html(txt, warnings = False))

#, grace = {"&": "\&"}):
#    for (a, b) in grace.items():
#        txt = txt.replace(a, b)
reampfix = re.compile("(?=[^\\\\])&")

reuch = re.compile('\?\[\\\\u(\d+)\]')


def latex_to_utf8(txt):
    #txt = reampfix.sub("\&{}", txt)
    txt = reuch.sub(unichrrep, txt)
    
    for i in sorted(platexspc.keys()):
        txt = platexspc[i].sub(latexsubutf8, txt)
        
    return html_to_utf8(txt)

def cjk(c):
    return (ord("\uac00") <= ord(c) <= ord("\ud7a3")) or (ord("\u3040") <= ord(c) <= ord("\u30ff")) or (ord("\u4e00") <= ord(c) <= ord("\u9FFF"))


#
uspcud = {latex_to_utf8(c + "{}"): rpl for (c, rpl) in spcud.items()}
import unicodedata
def undiacritic_utf8(input_str):
    nkfd_form = unicodedata.normalize('NFKD', input_str)
    return u"".join([uspcud.get(uuc.get(c, c), uuc.get(c, c)) for c in nkfd_form if not unicodedata.combining(c) and not cjk(c)])


