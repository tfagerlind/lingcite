import re
import txtlatex
from ut import *


reauthor = {}
reauthor[0] = re.compile("(?P<lastname>[^,]+),\s((?P<jr>[JS]r\.|[I]+),\s)?(?P<firstname>[^,]+)$")
reauthor[1] = re.compile("(?P<firstname>[^{][\S]+(\s[A-ZḤ'3][\S]+)*)\s(?P<lastname>([a-z'3]+[-\s])*[A-ZḤ'3][\S]+)(?P<jr>,\s[JS]r\.|[I]+)?$")
reauthor[2] = re.compile("(?P<firstname>\\{[\S]+\\}[\S]+(\s[A-ZḤ'3][\S]+)*)\s(?P<lastname>([a-z]+\s)*[A-ZḤ'3][\S]+)(?P<jr>,\s[JS]r\.|[I]+)?$")
reauthor[3] = re.compile("(?P<firstname>[\s\S]+?)\s\{(?P<lastname>[\s\S]+)\}(?P<jr>,\s[JS]r\.|[I]+)?$")
reauthor[4] = re.compile("\{(?P<firstname>[\s\S]+)\}\s(?P<lastname>[\s\S]+?)(?P<jr>,\s[JS]r\.|[I]+)?$")
reauthor[5] = re.compile("(?P<lastname>[A-Z][\S]+)$")
reauthor[6] = re.compile("\{(?P<lastname>[\s\S]+)\}$")
reauthor[7] = re.compile("(?P<lastname>[aA]nonymous)$")
reauthor[8] = re.compile("(?P<lastname>\?)$")
reauthor[9] = re.compile("(?P<lastname>[\s\S]+)$")
def psingleauthor(n, vonlastname = True):
    for i in sorted(reauthor.keys()):
        o = reauthor[i].match(n)
        if o:
            if vonlastname:
                return lastvon(o.groupdict())
            return o.groupdict()
    print("Couldn't parse name:", n)
    return None

anonymous = ['Anonymous', 'No Author Stated', 'An\'onimo', 'Peace Corps'] 
def authorhash(author):
    return author['lastname'] + ", " + txtlatex.undiacritic(author.get('firstname', ''))[:1] + "."

rebrackauthor = re.compile("([\s\S]+) \{([\s\S]+)\}$")
def commaauthor(a):
    xos = [(rebrackauthor.match(x), x) for x in a.split(' and ')]
    xs = ["%s, %s" % (xo.group(2), xo.group(1)) if xo else x for (xo, x) in xos]
    return ' and '.join(xs)

def pauthor(s):
    pas = [psingleauthor(a.strip()) for a in s.replace(" & ", " and ").split(' and ') if a.strip()]
    if [a for a in pas if not a]:
        print(s)
    return [a for a in pas if a]

def syncauthor(pa, pb, diacritic_sensitive = False):
    pal = pa['lastname']
    pbl = pb['lastname']
    if not diacritic_sensitive:
        if txtlatex.undiacritic(pal) != txtlatex.undiacritic(pbl):
            return None
    else:
        if pal != pbl:
            return None
    
    fa = pa.get('firstname', '')
    fb = pb.get('firstname', '')
    (l, firstlonger) = max((len(fa), fa), (len(fb), fb))
    (l, lastlonger) = max((len(pal), pal), (len(pbl), pbl))

    if pa.get('jr', '') != pb.get('jr', ''):
        jr = max(pa.get('jr', ''), pb.get('jr', ''))
    else:
        jr = pa.get('jr')
    return {'lastname': lastlonger, 'firstname': firstlonger, 'jr': jr}

#{k : {k, k1, k2}} where k1 has overlapping lg and author and type as k
def friends(e):
    lhks = grp2([((lg, hht), k) for (k, (t, f)) in e.items() for lg in lgcode((t, f)) for hht in hhtype((t, f))])
    fr = {}
    for (k, (t, f)) in e.items():
        for lg in lgcode((t, f)):
            for hht in hhtype((t, f)):
                for ko in lhks[(lg, hht)]:
                    if (k == ko) or ("author" not in f) or ("author" not in e[ko][1]):
                        continue
                    klastnames = set([a["lastname"] for a in pauthor(f["author"])])
                    if klastnames.intersection([a["lastname"] for a in pauthor(e[ko][1]["author"])]):
                        setd(fr, k, ko)
    return {k: list(ff.keys()) for (k, ff) in fr.items()}

#def later editions
#fenggram = {k: xks for (k, xks) in friends.items() if set(["grammar", "grammar_sketch"]).intersection(bib.hhtype(e[k])) and "eng" in bib.inlg(e[k]) and "besttxt" in e[k][1]}
#ff = {k: [xk for xk in xks if (bib.getyear(e[k]) and bib.getyear(e[xk])) and bib.getyear(e[k]) > bib.getyear(e[xk]) and bib.getpages(e[k]) < bib.getpages(e[xk]) and bib.hhtype(e[k]) == bib.hhtype(e[xk])] for (k, xks) in fenggram.items()}
#def translations(frnds):
#    trs = stripd({k: [xk for xk in xks if bib.inlg(e[k]) != bib.inlg(e[xk]) and bib.hhtype(e[k]) == bib.hhtype(e[xk])] for (k, xks) in frnds.items()})
    



def syncauthors(atf, btf):
    ((at, af), (bt, bf)) = (atf, btf)
    paa = pauthor(af.get('author', ''))
    pab = pauthor(bf.get('author', ''))
    sa = [syncauthor(pa, pb) for (pa, pb) in zip(paa, pab)]
    if all(sa):
        return (at, putfield(('author', ' and '.join([yankauthorbib(x) for x in sa])), af))
    print("Authors don't match", sa, paa, pab)
    return (at, af)

def standardize_author(s):
    return ' and '.join([yankauthorbib(x) for x in pauthor(s)])

def stdauthor(fields):
    if "author" in fields:
        fields['author'] = standardize_author(fields['author'])
    if "editor" in fields:
        fields['editor'] = standardize_author(fields['editor'])
    return fields

def authalpha(s):
    return ', '.join([txtlatex.undiacritic(unvonstr(x)) for x in pauthor(s)])


#"Adam, A., W.B. Wood, C.P. Symons, I.G. Ord & J. Smith"
#"Karen Adams, Linda Lauck, J. Miedema, F.I. Welling, W.A.L. Stokhof, Don A.L. Flassy, Hiroko Oguri, Kenneth Collier, Kenneth Gregerson, Thomas R. Phinnemore, David Scorza, John Davies, Bernard Comrie & Stan Abbott"

reca = re.compile("\s*[,\&]\s*")
def decommaauthor(a):
    ns = [(n, len(n.split(" "))) for n in reca.split(a)]
    #TODO what is more than the first author is lastname, firstname
    try:
        if [(n, l) for (n, l) in ns if l < 2]:
            return " and ".join(["%s, %s" % (ns[0][0], ns[1][0])] + [n for (n, l) in ns[2:]])
    except IndexError:
         print(ns)
         raise IndexError
    return " and ".join([n for (n, l) in ns])
       

def lint(fn):
    def cfs(f, badfields = ["alnumcodes", "glotto_id", "modified"]):
        return dict([(k, v) for (k, v) in f.items() if not k in badfields])

    txt = load(fn)
    cs = [c for c in txt if ord(c) > 127]
    if cs:
        print("Non ascii-127", cs)
    e = get(fn)
    lint = dict([(k, (t, cfs(f))) for (k, (t, f)) in e.items()])
    funnynames = fd([fn for (k, (t, f)) in e.items() for fn in f.keys()])
    print(s2(funnynames)[-5:])
    return lint



relu = re.compile("\s+|(d\')(?=[A-Z])")
recapstart = re.compile("[\[3']?[A-Z]")
def lowerupper(s):
    parts = [x for x in relu.split(s) if x]
    lower = []
    upper = []
    for (i, x) in enumerate(parts):
        if not recapstart.match(txtlatex.undiacritic(x)):
            lower.append(x)
        else:
            upper = parts[i:]
            break
    return (lower, upper)

def unvon(author):
    r = {}
    (lower, upper) = lowerupper(author['lastname'])
    r['lastname'] = ' '.join(upper)
    r['firstname'] = (author.get('firstname', '') + ' ' + ' '.join(lower)).strip()
    if not r['firstname']:
        r['firstname'] = None

    if 'jr' in author and author['jr']:
        r['jr'] = author['jr']
    
    return r

def lastvon(author):
    if not 'firstname' in author:
        return author
    r = {}
    (lower, upper) = lowerupper(author['firstname'])
    r['lastname'] = (' '.join(lower).strip() + ' ' + author['lastname']).strip()
    r['firstname'] = ' '.join(upper)
    if 'jr' in author and author['jr']:
        r['jr'] = author['jr']
    
    return r

def unvonstr(author):
    a = unvon(author)
    return ' '.join([a[k] for k in ['lastname', 'firstname', 'jr'] if k in a and a[k]])

def lastnamekey(s):
    (_, upper) = lowerupper(s)
    if not upper:
        return ''
    (_, lnk) = max([(len(u), u) for u in upper])
    return lnk

def yankauthorrev(author):
    author = unvon(author)
    r = author['lastname']
    if 'firstname' in author and author['firstname']:
        #if not renafn.search(author['firstname']):
        #    print "Warning:", author
        r += ", " + author['firstname']
    if 'jr' in author and author['jr']:
        r += " " + author['jr']
    return r

def yankauthorbib(author):
    r = author['lastname']
    if 'jr' in author and author['jr']:
        r += ", " + author['jr']
    if 'firstname' in author and author['firstname']:
        #if not renafn.search(author['firstname']):
        #    print "Warning:", author
        r += ", " + author['firstname']
    return r

def yankauthor(author):
    r = ""
    if 'firstname' in author and author['firstname']:
        #if not renafn.search(author['firstname']):
        #    print "Warning:", author
        r += author['firstname']

    r += " " + author['lastname']
    if 'jr' in author and author['jr']:
        r += " " + author['jr']
    return r

def yankindexauthors(authors, iseditor = False, style = "unified"):
    if authors:
        authstrings = [yankauthorrev(authors[0])] + [yankauthor(x) for x in authors[1:]]
    else:
        authstrings = ["No Author Stated"]
    r = ", ".join(authstrings[:-1])    
    if r != "":
        r += " \& " + authstrings[-1]
    else:
        r += authstrings[-1]

    if iseditor:
        if len(authors) <= 1:
            if style == 'unified':
                r += " (ed.)"
            elif style == 'diachronica':
                r += ", ed."
            else:
                print("UNKNOWN STYLE:", style)
        else:
            if style == 'unified':
                r += " (eds.)"
            elif style == 'diachronica':
                r += ", eds."
            else:
                print("UNKNOWN STYLE:", style)
    if r.endswith("."):
        return r
    else:
        return r + "."


def yankauthors(authors, iseditor = False, style = "unified"):
    authstrings = [yankauthor(x) for x in authors]
    r = ", ".join(authstrings[:-1])    
    if r != "":
        r += " \& " + authstrings[-1] if authstrings else ""
    else:
        r += authstrings[-1] if authstrings else ""

    if iseditor:
        if len(authors) <= 1:
            if style == 'unified':
                r += " (ed.)"
            elif style == 'diachronica':
                r += ", ed."
            else:
                print("UNKNOWN STYLE:", style)
        else:
            if style == 'unified':
                r += " (eds.)"
            elif style == 'diachronica':
                r += ", eds."
            else:
                print("UNKNOWN STYLE:", style)
    return r

def authoryear(tf):
    (typ, fields) = tf
    r = ""
    if 'author' in fields:
        authors = [x['lastname'] for x in pauthor(fields['author'])]
        r = ', '.join(authors[:-1]) + ' and ' + authors[-1]
    elif 'editor' in fields:
        authors = [x['lastname'] for x in pauthor(fields['editor'])]
        r = ', '.join(authors[:-1]) + ' and ' + authors[-1] + " (ed.)"
    if r.startswith(" and "):
        r = r[5:]
    return r + " " + fields.get('year', 'no date')

def rangecomplete(incomplete, complete):
    if len(complete) > len(incomplete):
        return complete[:len(complete)-len(incomplete)] + incomplete
    return incomplete

rebracketyear = re.compile("\[([\d\,\-\/]+)\]")
reyl = re.compile("[\,\-\/\s\[\]]+")
def pyear(s):
    if rebracketyear.search(s):
        s = rebracketyear.search(s).group(1)
    my = [x for x in reyl.split(s) if x.strip()]
    if len(my) == 0:
        return "[nd]"
    if len(my) != 1:
        return my[0] + "-" + rangecomplete(my[-1], my[0])
    return my[-1]

re4y = re.compile("\d\d\d\d$")
def yeartoint(s):
    a = pyear(s)[-4:]
    if re4y.match(a):
        return int(a)
    return None

def getyear(tf, default = lambda x: "no date"):
    (typ, fields) = tf
    return yeartoint(fields.get("year", default((typ, fields))))


def loadfs(fns):
    txt = ""
    for fn in fns:
        f = open(fn, 'r')
        txt += f.read()
        f.close()
    return txt

def loadfsu(fns):
    return ''.join([loadunicode(fn) for fn in fns])


def pall(txt): 
    return ['@' + x for x in re.split('^\s*@', txt, 0, re.MULTILINE)]

#def pall(txt):
#    return reitem.findall(txt)

refields = re.compile('\s*(?P<field>[a-zA-Z\_\d]+)\s*=\s*[{"](?P<data>.*)[}"],\n')
refieldsnum = re.compile('\s*(?P<field>[a-zA-Z\_\d]+)\s*=\s*(?P<data>\d+),\n')
refieldsacronym = re.compile('\s*(?P<field>[a-zA-Z\_\d]+)\s*=\s*(?P<data>[A-Za-z]+),\n')
#refieldslast = re.compile('\s*(?P<field>[a-zA-Z\_\d]+)\s*=\s*[{"]*(?P<data>.+?)[}"]*\n}')
refieldslast = re.compile('\s*(?P<field>[a-zA-Z\_\d]+)\s*=\s*[\{\"]?(?P<data>[^\n]+?)[\}\"]?(?<!\,)[$\n]')
retypekey = re.compile("@(?P<type>[a-zA-Z]+){(?P<key>[^,\s]*)[,\n]")
reitem = re.compile("@[a-zA-Z]+{[^@]+}")

trf = '@Book{g:Fourie:Mbalanhu,\n  author =   {David J. Fourie},\n  title =    {Mbalanhu},\n  publisher =    LINCOM,\n  series =       LWM,\n  volume =       03,\n  year = 1993\n}'

def pitem(item):
    o = retypekey.search(item)
    if not o:
        return None
    key = o.group("key")
    typ = o.group("type")
    fields = refields.findall(item) + refieldsacronym.findall(item) + refieldsnum.findall(item) + refieldslast.findall(item)
    fieldslower = [(x.lower(), y) for (x, y) in fields]
    return key, typ.lower(), dict(fieldslower)

def fuzmatchit(c1, c2):
    w1 = set(c1.lower().split(' '))
    w2 = set(c2.lower().split(' '))
    lu = float(len(w1.intersection(w2)))
    return (lu/len(w1))*(lu/len(w2)) >= 0.25

def fuzmatch(b1, b2):
    #common = [(b1[x], b2[x]) for x in b1.keys() if b2.has_key(x)]
    #if len(common) == 0:
    #    return False
    #check = [fuzmatchit(c1, c2) for (c1, c2) in common]
    #truth = [x for x in check if x]
    
    #print b1
    #print b2
    #print common
    #print check
    ##raw_input()
    #common = set(b1.keys()).intersection(b2.keys())
    #if not common.issuperset(set(['author', 'title'])):
    #    return False
    if not ('title' in b1 and 'title' in b2):
        return False

    if not ((b1.has_key('author') or b1.has_key('editor')) and (b2.has_key('author') or b2.has_key('editor'))):
        return False
    
    #author = fuzmatchit(b1['author'], b2['author'])
    a1 = set([a['lastname'] for a in pauthor(b1.get('author', b1.get('editor', '')))])
    a2 = set([a['lastname'] for a in pauthor(b2.get('author', b2.get('editor', '')))])
    title = fuzmatchit(takeuntil(b1['title'], ":"), takeuntil(b2['title'], ":"))
    return (a1 == a2) and title

def get2(fn = ['eva.bib']):
    if type(fn) != type([]):
        fn = [fn]

    txt = loadfs(fn)
    return get2txt(txt)

def get2u(fn = ['eva.bib']):
    if type(fn) != type([]):
        fn = [fn]

    txt = loadfsu(fn)
    return get2txt(txt)

allbib = ["ling.bib", "numerals.bib", "numwo.bib", "dictionaries_phonologies.bib", "grammars.bib", "donthave.bib"]
def get(fn = allbib):
    if type(fn) != type([]):
        fn = [fn]
    txt = loadfs(fn)
    return gettxt(txt)


def getasu(fn = allbib):
    if type(fn) != type([]):
        fn = [fn]
    try:    
        txt = txtlatex.latex_to_utf8('\n'.join([load(f) for f in fn]))
    except UnicodeDecodeError:
        print([c for c in '\n'.join([load(f) for f in fn]) if not ord(c) < 128])
        for i in [c for c in '\n'.join([load(f) for f in fn]) if not ord(c) < 128]:
            print(i)
        raise
    return gettxt(txt)

def getu(fn = "monsterutf8.bib"):
    if type(fn) != type([]):
        fn = [fn]
    txt = u'\n'.join([loadunicode(f) for f in fn])
    return gettxt(txt)

def getutotex(fn = "monsterutf8.bib"):
    return gettxt(txtlatex.killutf8(load(fn)))

def gettxt(txt):
    pentries = [pitem(x) for x in pall(txt)]
    entries = [x for x in pentries if x]

    e = {}
    for (key, typ, fields) in entries:
        if key in e:
            print("Duplicate key: ", key)
        e[key] = (typ, fields)

    return e

def get2txt(txt):
    pentries = [pitem(x) for x in pall(txt)]
    entries = [x for x in pentries if x]
    
    e = {}
    i = 0
    for (key, typ, fields) in entries:
        while key in e:
            i = i + 1
            key = str(i)
            #print "Duplicate key: ", key
        e[key] = (typ, fields)

    return e

reka = re.compile("([A-Z]+[a-z]*)|(?<![a-z])(de|di|da|du|van|von)")
def sepkeyauthor(k):
    return [x for x in reka.split(k) if x and x != "-"]

def sepkeyauthorform(k):
    auths = sepkeyauthor(k)
    xs = []
    c = ''
    for a in auths:
        if a.islower():
            c = c + a
        else:
            xs.append(c + a)
            c = ''
    return [a.lower() for a in xs]

def key_to_author(k):
    i = k.find(":")
    tp = k[:i]
    au = k[i+1:]
    
    i = au.find(":")
    if i == -1:
        return (au, tp)
    else:
        return (au[:i], au[i+1:] + tp)

def key_to_authors(k):
    n = takeuntil(takeafter(k, ":"), ":")
    js = [i for i in range(len(n)) if n[i].isupper()] + [len(n)]
    auths = []
    i = 0
    for j in js:
        auths = auths + [n[i:j]]
        i = j
    return [auth for auth in auths if auth.strip()]
    
def insert_field(bib = "grammars.bib", keyfield = {}):
    def repl_snip(snip, keyfield):
        o = retypekey.search("@" + snip)
        if not o:
            return snip
        if not o.group('key') in keyfield:
            return snip
        insdata = keyfield[o.group('key')]
        insplace = snip.find("\n}\n")
        if insplace >= 0:
            print("INSERT:", o.group('key'), insdata)
            return snip[:insplace] + ",\n  " + insdata + snip[insplace:]
        return snip
    
    snips = load(bib).split("@")
    newbib = '@'.join([repl_snip(snip, keyfield) for snip in snips])
    sav(newbib, bib)
    print("Wrote:", bib)
    return

reabbs = re.compile('@[Ss]tring\{(?P<abb>[A-Za-z]+)\s*\=\s*[\{\"](?P<full>[^\\n]+)[\}\"]\}\\n')
def getabbs(fn):
    txt = load(fn)
    return dict(reabbs.findall(txt))

reabbrep1 = re.compile("\s*\=\s*([A-Za-z]+)\,\n")
reabbrep2 = re.compile("\s*\=\s*([A-Za-z]+)\s*\#\s*\{")
reabbrep3 = re.compile("\}\s*\#\s*([A-Za-z]+)\s*\#\s*\{")
reabbrep4 = re.compile("\}\s*\#\s*([A-Za-z]+)\,\n")
def killabbs(fn, outfn = None):
    def sb(o, ins = " = {%s},\n"):
        z = o.group(1).upper()
        return ins % abbs.get(z, z)
 
    abbs = opk(getabbs(fn), lambda x: x.upper())
    if not outfn:
         outfn = takeuntil(fn, ".") + "_deabb.bib"

    txt = load(fn)
    txt = reabbrep1.sub(lambda x: sb(x, ins = " = {%s},\n"), txt)
    txt = reabbrep2.sub(lambda x: sb(x, ins = " = {%s "), txt)
    txt = reabbrep3.sub(lambda x: sb(x, ins = "%s"), txt)
    txt = reabbrep4.sub(lambda x: sb(x, ins = "%s},\n"), txt)
    return sav(txt, outfn)

#	Author = ac # { and Howard Coate},
#	Author = ad,





bibord = {}
bibord['author'] = 0
bibord['editor'] = 1
bibord['title'] = 2
bibord['booktitle'] = 3
bibord['journal'] = 5
bibord['school'] = 6
bibord['publisher'] = 7
bibord['address'] = 8
bibord['series'] = 9
bibord['volume'] = bibord['series'] + 1
bibord['number'] = bibord['volume'] + 1
bibord['pages'] = 20
bibord['year'] = 30
bibord['issn'] = 40
bibord['url'] = 50

def showbib(ktb, abbs = {}):
    (key, (typ, bib)) = ktb
    r = "@" + typ + "{" + str(key) + ",\n"
    
    order = [(bibord.get(x, 1000), x) for x in bib.keys()]
    order.sort()
    for (_, k) in order:
        v = txtlatex.txttolatex(bib[k].strip())
        r = r + "    " + k + " = {" + abbs.get(v, v) + "},\n"
    r = r[:-2] + "\n" + "}\n"
    #print r
    return r

def showbibu(ktb, abbs = {}):    
    (key, (typ, bib)) = ktb
    r = u"@" + typ + u"{" + key + u",\n"
    
    order = [(bibord.get(x, 1000), x) for x in bib.keys()]
    try:
    	order.sort()
    except UnicodeDecodeError:
        print("UNICODE ERROR", key)
        print(order)
        raise UnicodeDecodeError
    for (_, k) in order:
        v = bib[k].strip()
        try:
            r = r + u"    " + k + u" = {" + abbs.get(v, v) + u"},\n"
        except UnicodeDecodeError:
            print("UNICODE ERROR", key)
            print(k, [k])
            print(v, [v])
            raise UnicodeDecodeError
    r = r[:-2] + u"\n}\n"
    #print r
    return r


def showbibhtml(ktb, abbs = {}):    
    (key, (typ, bib)) = ktb
    r = "@" + typ + "{" + str(key) + ",\n"
    
    order = [(bibord.get(x, 1000), x) for x in bib.keys()]
    order.sort()
    for (_, k) in order:
        #v = txtlatex.latex_to_html(txtlatex.txttolatex(bib[k].strip()))
        v = bib[k].strip()
        r = r + "    " + k + " = {" + abbs.get(v, v) + "},\n"
    r = r[:-2] + "\n" + "}\n"
    #print r
    return r.replace("\n", "<br>")

def decrossref(e):
    def decrossitem(to, tfr, crffields = [("publisher", "publisher"), ("editor", "author"), ("booktitle", "title"), ("series", "series"), ("volume", "volume")]):
        (t, fr) = tfr
        for (ft, f) in crffields:
            if not ft in to:
                add = fr.get(ft, fr.get(f, ""))
                if add:
                    to[ft] = add
        return to

    edcr = dict([(k, (t, decrossitem(f, e.get(f["crossref"], ("", {}))) if "crossref"  in f else f)) for (k, (t, f)) in e.items()])
    return edcr


def srtyear(e, descending = True):
    order = [(fields.get('year', '[n.d.]'), k) for (k, (typ, fields)) in e.items()]
    return [(k, e[k]) for (sk, k) in sorted(order, reverse = descending)]

def srtauthor(e):
    order = [(authalpha(fields.get('author', fields.get('editor', '{[No author stated]}'))) + "-" + fields.get('year', '[n.d.]') + "-" + takeafter(k, ":"), k) for (k, (typ, fields)) in e.items()]
    return [(k, e[k]) for (sk, k) in sorted(order)]
    
def put(e, abbs = {}, srtkey = "author"):
    order = [(fields.get(srtkey, '') + takeafter(k, ":"), k) for (k, (typ, fields)) in e.items()]
    return ''.join([showbib((k, e[k]), abbs) for (sk, k) in sorted(order)])

def putu(e, abbs = {}, srtkey = "author"):
    order = [(fields.get(srtkey, '') + takeafter(k, ":"), k) for (k, (typ, fields)) in e.items()]
    return u''.join([showbibu((k, e[k]), abbs) for (sk, k) in sorted(order)])


def putlist(e, abbs = {}):
    return ''.join([showbib(x, abbs) for x in e])


resplittit = re.compile("[\(\)\[\]\:\,\.\s\-\?\!\;\/\~\=]+")
resplittittok = re.compile("([\(\)\[\]\:\,\.\s\-\?\!\;\/\~\=\'" + '\"' + "])")
def wrds(txt):
    return [x for x in resplittit.split(txtlatex.undiacritic(txt.lower()).replace("'", "").replace('"', "")) if x]

def tokens(txt):
    return [x for x in resplittittok.split(txt) if x.strip()]

def tokenjoin(xs):
    r = ""
    nospc = True
    for x in xs:
        if nospc:
            r = r + x
            nospc = resplittittok.match(x)
            continue
        nospc = resplittittok.match(x)
        if nospc:
            r = r + x
        else:
            r = r + " " + x
    return r

def fdt(e):
    return fdall([wrds(fields['title']) for (typ, fields) in e.values() if 'title' in fields])


def etos(e):
    r = {}
    for (k, (typ, fields)) in e.items():
        keyinf = k.split(":")
        if len(keyinf) < 2:
            print(keyinf)
        for w in sepkeyauthorform(keyinf[1]):
            setd3(r, 'author', w, k)
        for w in wrds(':'.join(keyinf[2:])):
            setd3(r, 'title', w, k)
        for (f, v) in fields.items():
            if f == 'year':
                v = v.replace("no date", "[nd]")
            for w in wrds(v):
                if f == 'volume':
                    w = roman(w).lower()
                setd3(r, f, w, k)
    return r

#If publisher has Place: Publisher, then don't take address
def fuse(dps, union = ['lgcode', 'fn', 'asjp_name', 'hhtype', 'isbn'], onlyifnot = {'address': 'publisher', 'lgfamily': 'lgcode', 'publisher': 'school', 'journal': 'booktitle'}):
    otyp = None
    ofields = {}
    for (typ, fields) in dps:
        if not otyp:
            otyp = typ
        for (k, v) in fields.items():
            if k in onlyifnot:
                if not onlyifnot[k] in ofields:
                    ofields[k] = v
            elif not k in ofields:
                ofields[k] = v
            elif k in union:
                if ofields[k].find(v) == -1:
                    ofields[k] = ofields[k] + ", " + v
            
    return (otyp, ofields)


def add_inlg(into = 'hh.bib'):
    bak(into)
    e = getu(into)
    savu(putu(add_inlg_e(e), srtkey = 'macro_area'), into, encoding = "utf-8", ucc = True)

def renfn(e, ups):
    for (k, field, newvalue) in ups:
        (typ, fields) = e[k]
        #fields['mpifn'] = fields['fn']
        fields[field] = newvalue
        e[k] = (typ, fields)
    return e

def addcitekey(tf):
    f["key"] = authoryear(tf)
    return tf

def add_inlg_e(e):
    h = {}
    h['Swedish [swe]'] = [u'fran', u'och', u'svenska', u'studier', u'folkmal', u'ordbok', u'av', u'till', u'om', u'det', u"ljud", u"formlara"]
    h['English [eng]'] = ['the', 'of', 'and', 'for', 'its', 'among', 'study', 'indians', 'sociolinguistic', 'coast', 'sketch', 'native', 'other', 'literacy', 'among', 'sociolinguistic', 'sketch', 'indians', 'native', 'coast', 'literacy', 'its', 'towards', 'eastern', 'clause', 'southeastern', 'grammar', 'linguistic', 'syntactic', 'morphology', 'spoken', 'dictionary', 'morphosyntax', 'course', 'language', 'primer', 'yourself', 'chrestomathy', 'colloquial', "sentence", "sentences", "phonetics", "phonology", "vocabulary", "bibliography", "noun", "ethnography", "vocabularies", "ethnographic", "toward", "sign", "overview", "tribe", "survey", "word", "words", "south", "north", "west", "east", "research", "phonological", "wordlist", "pronoun", "pronouns", "with", "grammatical", "some", "from", "to", "dialectology", "discourse", "studies"]
    h['French [fra]'] = ['et', 'du', 'le', 'verbe', 'grammaire', 'sociolinguistique', 'syntaxe', 'dune', 'au', 'chez', 'avec', 'langue', 'langues', 'grammaire', 'au', 'aux', 'chez', 'et', 'le', 'du', 'dune', 'verbe', 'syntaxe', 'au', 'haut', 'dictionnaire', 'pratique', 'parlons', 'parlers', 'parler', 'lexique', "linguistique", "vocabulaire", "textes"]
    h['German [deu]'] = ['eine', 'das', 'reise', 'beitrag', 'unter', 'die', 'jahren', 'und', 'stellung', 'einer', 'ihrer', 'reise', 'beitrag', 'unter', 'jahren', 'die', 'stellung', 'und', 'eine', 'jahre', 'bemerkungen', 'sprache', 'sprachkontakt', 'untersuchungen', 'zu', 'zur', 'auf', 'aus', 'skizze', "forschung", "forschungen", "lautlehre", "worterbuch", "handworterbuch", "mundart"]
    h['Spanish [spa]'] = ['idioma', 'los', 'las', 'lengua', 'lenguas', 'y', 'pueblos', 'algunos', 'educacion', 'castellano', 'poblacion', 'diccionario', "conversemos", "investigaciones", "consideraciones", "hablado", "vocabulario"]
    h['Portuguese [por]'] = ['do', 'dos', 'os', 'regiao', 'anais', 'povos', 'seus', 'mudanca', 'dicionario', 'falantes', 'gramaticais', "em", "nas", "introducao"]
    h['Italian [ita]'] = ['della', 'dello', 'vocabolario', 'vocaboli', 'dizionario', 'dei', 'lessico', 'linguaggio', 'sulla', 'grammaticali', 'studi', 'degli', 'fra']
    h['Russian [rus]'] = ['v', 'jazyk', 'yazyk', 'jazyka', 'yazyka', 'yazykov', 'jazykov', 'slov', 'iazyke', 'okolo', 'jazykach', 'jazyke', 'jazyka', 'yazyki', "sravnitel'no", "jazyki", "slovar", "slovar'", "po", "materialy"]
    h['Dutch [nld]'] = ['van', 'het', 'kommunikasieaangeleenthede', 'deel', 'morfologie', 'onderzoek', 'gebied', 'spraakleer', 'reis', 'een', 'goede', 'taal', 'taalstudien']
    h['Mandarin Chinese [cmn]'] = ['jianzhi', 'jiu', 'jian', 'qian', 'yan', 'hui', 'wen', 'ci', 'zang', 'dian', "cidian", "zidian", "fangyan", "yuyan", "gaikuang", u"yanjiu", "yu", "ren", "zhongguo", "wenhua", "yufa"]
    h['Tibetan [bod]'] = ['bod', 'kyi']
    h['Indonesian [ind]'] = ['bahasa', 'dialek']
    h['Hindi [hin]'] = ['hindi', 'vyakaran']
    h['Thai [tha]'] = ['phasa', 'laksana', 'akson', 'lae', 'siang', 'khong']
    h['Vietnamese [vie]'] = ['viec', 'cach', 'trong', 'phap', 'hien', 'dung', 'nghia', 'dien', 'thong', 'ngu']
    h['Finnish [fin]'] = ['suomen', 'kielen', 'ja']
    h['Turkish [tur]'] = ['turkce', 'uzerine', 'terimleri', 'turkiye', 'hakkinda', 'halk', 'uzerinde', 'turkcede', 'tarihi', 'kilavuzu']
    h['Hungarian'] = ['szotar', 'nyelvtana']
    
    dh = dict([(v, k) for (k, vs) in h.items() for v in vs])
    ts = [(k, wrds(fields['title']) + wrds(fields.get('booktitle', ''))) for (k, (typ, fields)) in e.items() if 'title' in fields and not 'inlg' in fields]
    print(len(ts), "without", 'inlg')
    ann = [(k, fd([dh[w] for w in tit if w in dh])) for (k, tit) in ts]
    unique = [(k, set(allmax(lgs).keys()).pop()) for (k, lgs) in ann if len(allmax(lgs)) == 1]
    print(len(unique), "cases of unique hits")
    fnups = [(k, 'inlg', v) for (k, v) in unique]
    t2 = renfn(e, fnups)
    #print len(unique), "updates"

    newtrain = grp2fd([(fields['inlg'], w) for (k, (typ, fields)) in t2.items() if 'title' in fields and 'inlg' in fields if len(lgcodestr(fields['inlg'])) == 1 for w in wrds(fields['title'])])
    #newtrain = grp2fd([(cname(lgc), w) for (lgcs, w) in alc if len(lgcs) == 1 for lgc in lgcs])
    for (lg, wf) in sorted(newtrain.items(), key = lambda x: len(x[1])):
        cm = [(1+f, float(1-f+sum([owf.get(w, 0) for owf in newtrain.values()])), w) for (w, f) in wf.items() if f > 9]
        cms = [(f/fn, f, fn, w) for (f, fn, w) in cm]
        cms.sort(reverse=True)
        print(lg, cms[:10])
        print(("h['%s'] = " % lg) + str([x[3] for x in cms[:10]]))
    return t2

def showdups(fn = ['hh.bib']):
    (e, r) = mrg(fn)
    dups = [(x, ys) for (x, ys) in r.items() if len(ys) != 1]
    for (x, ys) in dups:
        print(x)
        for (fny, y) in ys:
            print("* " + bibhtml.txt({y: e[fny][y]}))
        print("\n")
    return

def maphhtype(fn = 'hh.bib'):
    bak(fn)
    e = getu(fn)
    e2 = dict([(k, (typ, putfield(('hhtype', ';'.join([wcs[x] for x in pcat(takeuntil(k, ":"))])), fields))) for (k, (typ, fields)) in e.items() if k.find(":") != -1])
    e3 = dict([(k, (typ, fields)) for (k, (typ, fields)) in e.items() if k.find(":") == -1])
    if len(e3) > 0:
        print(len(e3), "without colon-key-hhtype")
        print(list(e3.keys())[:100])
    savu(putu(dict(list(e2.items()) + list(e3.items()))), fn, encoding = "utf-8", ucc = True)

reroman = re.compile("([xivmcl]+)$")
rerpgs = re.compile("([xivmcl]+)\-?([xivmcl]*)")
repgs = re.compile("[esA]?([\d]+)\-?[esA]?([\d]*)")
def pagecount(pgstr):
    rpgs = rerpgs.findall(pgstr)
    pgs = repgs.findall(pgstr)
    rsump = sum([romanint(b)-romanint(a)+1 for (a, b) in rpgs if b] + [romanint(a) for (a, b) in rpgs if not b])
    sump = sum([int(rangecomplete(b, a))-int(a)+1 for (a, b) in pgs if b] + [int(a) for (a, b) in pgs if not b])
    if rsump !=0 and sump != 0:
        return "%s+%s" % (rsump, sump)
    if rsump ==0 and sump == 0:
        return ''
    return str(rsump+sump)

#Supplementary/Appendix
reappendixpgs = re.compile("^[aAsS]|(?<=\-)[aAsS]")
def pagerange(pgstr, forgiving = False):
    def pt_to_range(pt):
        if forgiving:
            pt = reappendixpgs.sub("", pt) 
        rpgs = rerpgs.match(pt)
        pgs = repgs.match(pt)
        if rpgs:
            (a, b) = rpgs.groups()
            return [roman("%s" % i).lower() for i in (range(romanint(a), romanint(b)+1) if b else range(1, romanint(a)+1))]
        else:
            if not pgs:
                print("NO PAGERANGE", pgstr)
                return []
            (a, b) = pgs.groups()
            return ["%s" % i for i in (range(int(a), int(b)+1) if b else range(1, int(a)+1))]
    pts = re.split("[,+\s]+", pgstr)
    return [p for pt in pts for p in pt_to_range(pt)]

def fullpage(pgstr):
    def fullify(o):
        (a, b) = (o.group(1), o.group(2))
        if not b:
            return a
        if int(b) < int(a) and len(b) < len(a):
            return a + "-" + a[:(len(a)-len(b))] + b
        return a + "-" + b
    return repgs.sub(fullify, pgstr) 

def putfield(kv, d):
    (k, v) = kv
    r = dict([(x, y) for (x, y) in d.items()])
    r[k] = v
    return r

    
def addfield(kv, d):
    return dict([kv] + [(x, y) for (x, y) in d.items()])

from collections import OrderedDict
def introman(num):
    roman = OrderedDict()
    roman[1000] = "m"
    roman[900] = "cm"
    roman[500] = "d"
    roman[400] = "cd"
    roman[100] = "c"
    roman[90] = "xc"
    roman[50] = "l"
    roman[40] = "xl"
    roman[10] = "x"
    roman[9] = "ix"
    roman[5] = "v"
    roman[4] = "iv"
    roman[1] = "i"

    def roman_num(num):
        for r in roman.keys():
            x, y = divmod(num, r)
            yield roman[r] * x
            num -= (r * x)
            if num > 0:
                roman_num(num)
            else:
                break

    return "".join([a for a in roman_num(num)])

def romanint(r):
    z = {'m': 1000, 'd': 500, 'c': 100, 'l': 50, 'x': 10, 'v': 5, 'i': 1}
    i = 0
    prev = 10000
    for c in r:
        zc = z[c]
        if zc > prev:
            i = i - 2*prev + zc
        else:
            i = i + zc
        prev = zc
    return i


rerom = re.compile("(\d+)")
def roman(x):
    return rerom.sub(lambda o: introman(int(o.group(1))), x).upper()


bibe = {}
bibe['title'] = 100
bibe['year'] = 90
bibe['booktitle'] = 80
bibe['author'] = 70
bibe['editor'] = 60
bibe['journal'] = 50
bibe['school'] = 40
bibe['publisher'] = 30
bibe['howpublished'] = 30
bibe['address'] = 20
bibe['pages'] = 10
bibe['typ'] = 10
bibe['series'] = 9
bibe['volume'] = 8
bibe['number'] = 7

def dist(t1f1, t2f2):
    ((t1, f1), (t2, f2)) = (t1f1, t2f2)
    f1p = [('typ', t1) + f1.items()]
    f2p = [('typ', t1) + f1.items()]
    bf1 = [dt(wrds(v), wrds(f2p.get(k)))*bibe[k] for (k, v) in f1p if bibe.has_key(k)]
    bf2 = [dt(wrds(v), wrds(f1p.get(k)))*bibe[k] for (k, v) in f2p if bibe.has_key(k)]
    return bf1*bf2

rewrdtok = re.compile("[a-zA-Z].+")
reokkey = re.compile("[^a-z\d\-\_\[\]]")
def keyid(fields, fd = {}, ti = 2):
    if not 'author' in fields:
        if not 'editor' in fields:
            return reokkey.sub("_", ''.join(fields.values()))
        else:
            astring = fields['editor']
    else:
        astring = fields['author']

    authors = pauthor(astring)    
    if len(authors) != len(astring.split(' and ')):
        print("Unparsed author in", authors)
        print("   ", astring, astring.split(' and '))
        print(fields['title'])

    ak = [txtlatex.undiacritic(x) for x in sorted([lastnamekey(a['lastname']) for a in authors])]
    yk = pyear(fields.get('year', '[nd]'))[:4]
    tks = wrds(fields.get("title", "no.title")) #takeuntil :
    tkf = sorted([w for w in tks if rewrdtok.match(w)], reverse = True, key = lambda w: fd.get(w, 0))
    tk = tkf[-ti:]
    if 'volume' in fields and not 'journal' in fields and not 'booktitle' in fields and not 'series' in fields:
        vk = roman(fields['volume'])
    else:
        vk = ''

    if 'extra_hash' in fields:
        yk = yk + fields['extra_hash']

    key = '-'.join(ak) + "_" + '-'.join(tk) + vk + yk
    return reokkey.sub("", key.lower())

def insert_field(bib = "grammars.bib", keyfield = {}):
    def repl_snip(snip, keyfield):
        o = retypekey.search("@" + snip)
        if not o:
            return snip
        if not o.group('key') in keyfield:
            return snip
        insdata = keyfield[o.group('key')]
        insplace = snip.find("\n}\n")
        if insplace >= 0:
            print("INSERT:", o.group('key'), insdata)
            return snip[:insplace] + ",\n  " + insdata + snip[insplace:]
        return snip
    
    snips = load(bib).split("@")
    newbib = '@'.join([repl_snip(snip, keyfield) for snip in snips])
    sav(newbib, bib)
    return

def bibktf(ktf):
    (k, (t, f)) = ktf
    return '|||'.join(["%s:::%s" % z for z in [(k, t)] + stdauthor(f).items()])

def cfnode(tf):
    (typ, fields) = tf
    k = lgcode((typ, fields))
    if not k:
        fms = fields.get('lgfamily', '').split("; ")
        return [f.split(", ")[-1] for f in fms if f]
    return k



renamelgcode = re.compile("(?P<name>[^\[]+)\s+\[(?P<iso>[a-z][a-z][a-z]|NOCODE\_[A-Z][^\s\]]+)\]")
hooks = ["=", "probably", "possibly", "looks like", "geographically", "count", "counts"]
rehooksplit = re.compile("|".join(["\s%s\s" % hook for hook in hooks]))


repginter = re.compile("([Pp][Pp]\.?\~?\s?[\d\s\-\,]+)")
def altnames(lgcodestr):
    def unifname(x):
        return repginter.sub("", x)
    
    def part_to_altnames(x):
        hparts = rehooksplit.split(x)
        o = renamelgcode.match(hparts[-1])
        if o:
            name = o.group('name')
            iso = o.group('iso')
        else:
            return []
        names = [unifname(x).strip() for x in [name] + hparts[:-1]]
        return [(n, iso) for n in names if n]

    return [x for p in lgcodestr.split(",") if p.strip() for x in part_to_altnames(p.strip())]
    
    #expp = [lf.cname(p) if reiso.match(p) else p for p in parts]
    #exnm = [x for x in expp if not renamelgcode.match(x)]
    #print exnm



        
   
    
    return [normf(p) for p in expp]
    


reisobrack = re.compile("\[([a-z][a-z][a-z]|NOCODE\_[A-Z][^\s\]]+)\]")
recomma = re.compile("[\,\/]\s?")
reiso = re.compile("[a-z][a-z][a-z]$|NOCODE\_[A-Z][^\s\]]+$")
def lgcode(tf):
    (typ, fields) = tf
    if not 'lgcode' in fields:
        return []
    return lgcodestr(fields['lgcode'])

def inlg(tf):
    (typ, fields) = tf
    if not 'inlg' in fields:
        return []
    return lgcodestr(fields['inlg'])

def lgcodestr(lgcstr):
    lgs = reisobrack.findall(lgcstr)
    if lgs:
        return lgs
    
    parts = [p.strip() for p in recomma.split(lgcstr)]
    codes = [p for p in parts if reiso.match(p)]
    return codes

ret = {}
respcomma = re.compile(",\s*")
respdash = re.compile("\s*[\-]+\s*")
ret['subject_headings'] = lambda x: [tuple(respdash.split(x)) for z in respcomma.split(x)]
#subject_headings comma serated then subcats -- separated

rekillparen = re.compile(" \([^\)]*\)")

respcomsemic = re.compile("[;,]\s?")
ret['hhtype'] = lambda x: respcomsemic.split(rekillparen.sub("", x))
#wcs = {"h": 'handbook/overview', "el": 'endangered language', "w": 'wordlist', "typ": '(typological) study of a specific feature', "b": 'bibliographically oriented', "e": 'ethnographic work', "g": 'grammar', "d": 'dictionary', "s": 'grammar sketch', "v": 'comparative-historical study', "phon": 'phonology', "soc": 'sociolinguistically oriented', "ld": 'some very small amount of data/information on a language', "dial": 'dialectologically oriented', "t": 'text', "nt": 'new testament'}

reinbrack = re.compile("\[([^\]]+)]\]") 
ret['subject'] = reinbrack.findall

ret['keywords'] = lambda x: [z for z in respcomsemic.split(x) if z]
ret['lgcode'] = lgcodestr
ret['macro_area'] = lambda x: [x]

#siltype, hhtype, mahotype, evatype, macro_area
def bibtoann(tf):
    (typ, fields) = tf
    return [(k, ann) for (k, v) in ret.items() if k in fields for ann in v(fields[k])]

def hhtypestr(s):
    return ret['hhtype'](s)

def hhtype(tf):
    (t, f) = tf
    return hhtypestr(f.get("hhtype", "unknown"))

def sel(e, field, v):
    return dict([(k, (typ, fields)) for (k, (typ, fields)) in e.items() if fields.get(field, None) == v])

def delta(a, b, case_sensitive = False):
    if a and b:
        if not case_sensitive:
            a = a.lower()
            b = b.lower()
        if a == b:
            return 0
        else:
            return 1
    else:
        return 0.5

def deltaw(a, b, case_sensitive = False):
    if a and b:
        (md, align) = edist(a, b, delta, case_sensitive = case_sensitive)
        return md
    return 1.0

def align(d, x, y):
    i = len(x)
    j = len(y)
    r = {}
    k = 0
    #print d
    while (0, 0) != (i, j):
        #print i, j
        (_, t) = d[i, j]
        if t == 'S':
            r[k] = (x[i-1], y[j-1])
            i = i - 1
            j = j - 1
        elif t == 'I':
            r[k] = ("", y[j-1]) #'-'.ljust(len(y[j-1]))
            j = j - 1
        elif t == 'D':
            r[k] = (x[i-1], "") #'-'.ljust(len(x[i-1]))
            i = i - 1
        k = k + 1
    return [r[k] for k in sorted(r, reverse=True)]
        

def edist(x, y, delta = delta, case_sensitive = False):
    lx = len(x)
    ly = len(y)

    d = {}
    d[(0,0)] = (0, 'None')
    for i in range(lx):
        d[(i+1, 0)] = (d[(i, 0)][0] + delta(x[i], None, case_sensitive = case_sensitive), 'D')
    for j in range(ly):
        d[(0, j+1)] = (d[(0, j)][0] + delta(None, y[j], case_sensitive = case_sensitive), 'I')

    for i in range(lx):
        for j in range(ly):
            d[(i+1, j+1)] = min((d[(i, j)][0] + delta(x[i], y[j], case_sensitive = case_sensitive), 'S'),
                                (d[(i, j+1)][0] + delta(x[i], None, case_sensitive = case_sensitive), 'D'),
                                (d[(i+1, j)][0] + delta(None, y[j], case_sensitive = case_sensitive), 'I'))

    nrm = float(max(lx, ly))
    (md, _) = d[(lx, ly)]
    return (md/nrm, align(d, x, y))

def c(a, b, case_sensitive = False):
    return edist(tokens(a), tokens(b), delta = deltaw, case_sensitive = False)

def pa(ab):
    abl = [(max(len(a), len(b)), a, b) for (a, b) in ab]
    la = ' '.join([a.rjust(l, ' ') for (l, a, _) in abl]) + '\n'
    lb = ' '.join([b.rjust(l, ' ') for (l, _, b) in abl]) + '\n'
    return la + lb


def mkup(alg, markup):
    #abl = [(max(len(a), len(b)), a, b) for (a, b) in ab]
    la = tokenjoin([ifel(a == b, a, markup(a)) for (a, b) in alg])
    lb = tokenjoin([ifel(a == b, b, markup(b)) for (a, b) in alg])
    return (la, lb)

def conso(cmps, atf, btf, markup = lambda x: x.upper()):
    ((at, af), (bt, bf)) = (atf, btf)
    a = {}
    b = {}
    for (k, (_, alg)) in cmps:
        (a[k], b[k]) = mkup(alg, markup)
        
    for (k, v) in af.items():
        if not k in a:
            a[k] = v
    for (k, v) in bf.items():
        if not k in b:
            b[k] = v
    return ((at, a), (bt, b))
        
def trydiff(atf, btf, markup = lambda x: x.upper(), fields = bibe.keys(), case_sensitive = False):
    ((at, af), (bt, bf)) = (atf, btf)
    try:
        return diff((at, af), (bt, bf), markup = markup, fields = fields, case_sensitive = case_sensitive)
    except ZeroDivisionError:
        return (True, ((at, af), (bt, bf)), [])

def diff(atf, btf, markup = lambda x: x.upper(), fields = bibe.keys(), case_sensitive = False):
    ((at, af), (bt, bf)) = (atf, btf)
    chk = dict.fromkeys(fields + ['typ'])
    if not (at in ['article', 'incollection']) and not (bt in ['article', 'incollection']):
        del chk['pages']
    
    a = stdauthor(dict([('typ', at)] + af.items()))
    b = stdauthor(dict([('typ', bt)] + bf.items()))

    cmps = [(k, c(a.get(k, ""), b.get(k, ""), case_sensitive = case_sensitive)) for k in chk if a.has_key(k) or b.has_key(k)]
    isd = [(k, (md, alg)) for (k, (md, alg)) in cmps if md != 0.0]
    if not isd:
        return (False, ((at, af), (bt, bf)), [])
    
    return (True, conso(isd, (at, af), (bt, bf), markup), isd)
    #return yes, no [whats the diff] [markup]

reyear = re.compile("\d\d\d\d")
def same23(atf, btf):
    ((at, af), (bt, bf)) = (atf, btf)    
    alastnames = [x['lastname'] for x in pauthor(txtlatex.undiacritic(af.get("author", "")))]
    blastnames = [x['lastname'] for x in pauthor(txtlatex.undiacritic(bf.get("author", "")))]
    ay = reyear.findall(af.get('year', ""))
    by = reyear.findall(bf.get('year', ""))
    ta = txtlatex.undiacritic(takeuntil(af.get("title", ""), ":")).lower()
    tb = txtlatex.undiacritic(takeuntil(bf.get("title", ""), ":")).lower()
    if ta == tb and set(ay).intersection(by):
        return True
    if set(ay).intersection(by) and set(alastnames).intersection(blastnames):
        return True
    if ta == tb and set(alastnames).intersection(blastnames):
        return True
    return False

    


def matchtrig(ws, t):
    return all([(w in ws) == stat for (stat, w) in t])

def matchtrigsig(tf, ts):
    (typ, fields) = tf
    ws = set(wrds(fields.get('title', '')))
    chks = [(t, matchtrig(ws, t)) for t in ts]
    ms = [t for (t, m) in chks if m]
    mstr = ';'.join([' and '.join([ifel(stat, '', 'not ') + w for (stat, w) in m]) for m in ms])
    return mstr

def indextrigs(ts):
    return grp2([(tuple(sorted(disj)), clslab) for (clslab, t) in ts.items() for disj in t])
    
def sd(es):
    #most signficant piece of descriptive material
    #hhtype, pages, year
    mi = [(k, (hhtypestr(fields.get('hhtype', 'unknown')), fields.get('pages', ''), fields.get('year', ''))) for (k, (typ, fields)) in es.items()]
    d = accd(mi)
    ordd = [sorted([(p, y, k, t) for (k, (p, y)) in d[t].items()], reverse = True) for t in wcrank if t in d]
    return ordd

def msd(es):
    #most signficant piece of descriptive material
    #hhtype, pages, year
    return flatten(sd(es))[:1]

def pcy(pagecountstr):
    #print pagecountstr
    if not pagecountstr:
        return 0
    return eval(pagecountstr) #int(takeafter(pagecountstr, "+"))

def getplace(tf):
    (typ, fields) = tf
    place = fields.get("publisher", fields.get("address", fields.get("school", ""))) 
    if place.find(":") != -1:
        place = takeuntil(place, ":")
    else:
        if typ not in ["misc", "mastersthesis", "phdthesis", "article"]:
            print("No place", fields["title"])
    return place

def getpages(tf):
    (typ, fields) = tf
    return pcy(pagecount(fields.get("pages", "")))

def accd(mi):
    r = {}
    for (k, (hhts, pgs, year)) in mi:
        #print k
        pci = pcy(pagecount(pgs))
        for t in hhts:
            setd(r, t, k, (pci/float(len(hhts)), year))
    return r

def byid(es, idf = lgcode, unsorted = False):
    def tftoids(tf):
        z = idf(tf)
        if unsorted and not z:
            return ['!Unsorted']
        return z
    return grp2([(cfn, k) for (k, tf) in es.items() for cfn in tftoids(tf)])

oldwcrank = ['long grammar', 'grammar', 'grammar sketch', 'dictionary', '(typological) study of a specific feature', 'phonology', 'text', 'new testament', 'wordlist', 'comparative-historical study', 'some very small amount of data/information on a language', 'endangered language', 'sociolinguistically oriented', 'dialectologically oriented', 'handbook/overview', 'ethnographic work', 'bibliographically oriented', 'unknown']

#wcs = {"h": 'handbook/overview', "el": 'endangered language', "w": 'wordlist', "typ": '(typological) study of a specific feature', "b": 'bibliographically oriented', "e": 'ethnographic work', "g": 'grammar', "d": 'dictionary', "s": 'grammar sketch', "v": 'comparative-historical study', "phon": 'phonology', "soc": 'sociolinguistically oriented', "ld": 'some very small amount of data/information on a language', "dial": 'dialectologically oriented', "t": 'text', "nt": 'new testament'}
oldwcs = {"h": 'handbook/overview', "el": 'sociolinguistically oriented', "w": 'wordlist', "typ": '(typological) study of a specific feature', "b": 'bibliographically oriented', "e": 'ethnographic work', "g": 'grammar', "d": 'dictionary', "s": 'grammar sketch', "v": 'comparative-historical study', "phon": 'phonology', "soc": 'sociolinguistically oriented', "ld": 'some very small amount of data/information on a language', "numbers": "some very small amount of data/information on a language", "dial": 'dialectologically oriented', "t": 'text', "nt": 'new testament'}

ucats = ["ling", "evol", "lex", "sign", "script", "hist", "ling", "writing", "arch", "acq", "samp", "zipf", "gen", "f", "cont", "cl", "freq", "writ", "pc", "numbers", "cn", "en", "mn", "creole"]
wcats = ["h", "el", "w", "typ", "b", "e", "g", "d", "s", "v", "phon", "soc", "ld", "dial", "t", "nt"]
hhcats = ucats + wcats


newwcs = {}
newwcs['handbook/overview'] = 'overview'
newwcs['some very small amount of data/information on a language'] = 'minimal'
newwcs['grammar sketch'] = 'grammar_sketch'
newwcs['new testament'] = 'new_testament'
newwcs['(typological) study of a specific feature'] = 'specific_feature'
newwcs['dialectologically oriented'] = 'dialectology'
newwcs['sociolinguistically oriented'] = 'socling'
newwcs['comparative-historical study'] = 'comparative'
newwcs['bibliographically oriented'] = 'bibliographical'
newwcs['ethnographic work'] = 'ethnographic'
newwcs['dictionary'] = 'dictionary'
newwcs['grammar'] = 'grammar'
newwcs['long grammar'] = 'long grammar'
newwcs['text'] = 'text'
newwcs['wordlist'] = 'wordlist'
newwcs['phonology'] = 'phonology'
newwcs['endangered language'] = 'endangered language'
newwcs['unknown'] = 'unknown'

hhtype_to_abbv = {}
hhtype_to_abbv['overview'] = 'O'
hhtype_to_abbv['minimal'] = 'M'
hhtype_to_abbv['grammar_sketch'] = 'S'
hhtype_to_abbv['new_testament'] = 'N'
hhtype_to_abbv['specific_feature'] = 'F'
hhtype_to_abbv['dialectology'] = 'X'
hhtype_to_abbv['socling'] = 'SL'
hhtype_to_abbv['comparative'] = 'C'
hhtype_to_abbv['bibliographical'] = 'B'
hhtype_to_abbv['ethnographic'] = 'E'
hhtype_to_abbv['dictionary'] = 'D'
hhtype_to_abbv['grammar'] = 'G'
hhtype_to_abbv['text'] = 'T'
hhtype_to_abbv['wordlist'] = 'W'
hhtype_to_abbv['phonology'] = 'P'
hhtype_to_abbv['unknown'] = 'U'

hhtype_to_texttype = {}
hhtype_to_texttype['grammar_sketch'] = 1
hhtype_to_texttype['grammar'] = 1
hhtype_to_texttype['specific_feature'] = 1
hhtype_to_texttype['dictionary'] = 2
hhtype_to_texttype['wordlist'] = 2
hhtype_to_texttype['bibliographical'] = 3
hhtype_to_texttype['new_testament'] = 4
hhtype_to_texttype['text'] = 4
hhtype_to_texttype['phonology'] = 5
hhtype_to_texttype['overview'] = 6
hhtype_to_texttype['socling'] = 6
hhtype_to_texttype['minimal'] = 6
hhtype_to_texttype['ethnographic'] = 7
hhtype_to_texttype['dialectology'] = 8
hhtype_to_texttype['comparative'] = 8
hhtype_to_texttype['unknown'] = 10
texttype_label = {} 
texttype_label[1] = "GRAM" 
texttype_label[2] = "LEX" 
texttype_label[3] = "BIB"
texttype_label[4] = "TEXT"
texttype_label[5] = "PHON" 
texttype_label[6] = "SOC" 
texttype_label[7] = "ETHNO"
texttype_label[8] = "CMP" 
texttype_label[10] = "UNKNOWN" 

hhtype_to_n5 = {}
hhtype_to_n5["grammar_sketch"] = 3
hhtype_to_n5["grammar sketch"] = 3
hhtype_to_n5["wordlist"] = 1
hhtype_to_n5["long_grammar"] = 5
hhtype_to_n5["long grammar"] = 5
hhtype_to_n5["grammar"] = 4
hhtype_to_n5["minimal"] = 0
hhtype_to_n5["specific_feature"] = 2
hhtype_to_n5["specific feature"] = 2
hhtype_to_n5["phonology"] = 2
hhtype_to_n5["overview"] = 0
hhtype_to_n5["dictionary"] = 2
hhtype_to_n5["text"] = 2
hhtype_to_n5['new_testament'] = 2
hhtype_to_n5['new testament'] = 2
hhtype_to_n5["unknown"] = 0
hhtype_to_n5['dialectology'] = 0
hhtype_to_n5['socling'] = 0
hhtype_to_n5['comparative'] = 0
hhtype_to_n5['bibliographical'] = 0
hhtype_to_n5['ethnographic'] = 0

n5_to_col = {}
n5_to_col[5] = "green" 
n5_to_col[4] = "green"
n5_to_col[3] = "orange"
n5_to_col[2] = "orangered"
n5_to_col[1] = "red"
n5_to_col[0] = "red"

wcs = dict([(k, newwcs[v]) for (k, v) in oldwcs.items()])
wcrank = [newwcs[k] for k in oldwcrank]
hhtype_to_n = dict([(x, len(wcrank)-i) for (i, x) in enumerate(wcrank)])
hhtype_to_expl = inv11(newwcs)

def sdlgs(e, unsorted = False):
    eindex = byid(e, unsorted = unsorted)
    fes = {x: dict([(k, e[k]) for k in ks]) for (x, ks) in eindex.items()}
    fsd = {k: sd(v) for (k, v) in fes.items()}
    return (fsd, fes)


def pcat(ok):
    r = []
    k = ok
    while k:
        try:
            (_, m) = max([(len(x), x) for x in hhcats if k.startswith(x)])
        except ValueError:
            print(ok, k)
            
        r = r + [m]
        k = k[len(m):]
    return r


def lstat(e, unsorted = False):
    (lsd, lse) = sdlgs(e, unsorted = unsorted)
    return {k: (xs + [[[None]]])[0][0][-1] for (k, xs) in lsd.items()}

def lstat5(e, unsorted = False):
    (lsd, lse) = sdlgs(e, unsorted = unsorted)
    lsdd = {k: (xs + [[(0, "", "", None)]])[0][0] for (k, xs) in lsd.items()}
    return {x: "long_grammar" if t == "grammar" and p > 300.0 else t for (x, (p, y, k, t)) in lsdd.items()}


def lstat_numeric(e, unsorted = False):
    (lsd, lse) = sdlgs(e, unsorted = unsorted)
    lsdd = {k: (xs + [[(0, "", "", None)]])[0][0] for (k, xs) in lsd.items()}

    return {x: (hhtype_to_n.get(t, 0), p, t, k) for (x, (p, y, k, t)) in lsdd.items()}

def lstat_witness(e, unsorted = False):
    def statwit(xs):
        if len(xs) == 0:
            return (None, [])
        [(typ, ks)] = grp2([(t, k) for [p, y, k, t] in xs[0]]).items()
        return (typ, ks)
    (lsd, lse) = sdlgs(e, unsorted = unsorted)
    return {k: statwit(v) for (k, v) in lsd.items()}


#b = bib.get('hh.bib')
#a = bib.get(..)
#returnerar en e a \ b 

def mrg(fs = ['hh.bib', 'mpieva.bib', "sil16.bib", "asjp2010.bib", "eballiso2009.bib", "fabreall2009ann.bib", "silpng.bib", "wals.bib", "weball.bib", "seifart.bib", "sala.bib", "ozbib.bib", "stampe.bib", "lapolla-tibeto-burman.bib", "guldemann.bib", "schikowski_chintang.bib", "otomanguean.bib", "bahasa.bib", "sn.bib", 'anla.bib', "APiCS.bib", "Zurich.bib", "hedvig-tirailleur.bib", "bowern.bib"]):
    e = {}
    r = {}
    for f in fs:
        e[f] = get2(f)
        print(f, len(e[f]))
        
    ft = sumds([fdt(e[f]) for f in fs])
    
    for f in fs:
        rp = len(r)
        bk = [(keyid(fields, ft), (f, k)) for (k, (typ, fields)) in e[f].items()]
        for (hk, k) in bk:
            setd(r, hk, k)
        print(len(r) - rp, "new from total", len(e[f]))
    return (e, r)

def authoreditor(tf):
    (t, f) = tf
    if t == "book" and "editor" in f and f.get("author", "").find("Anonymous") != -1:
        f["author"] = f["editor"]
        del f["editor"]        
    return (t, f)

redotsubtitle = re.compile("(?P<title>[\s\S]+?[a-z])\.\s(?P<subtitle>[\s\S]+)")
def titledelim(t, delims = ["Volume", ":", "Chast", " - "]):
    for delim in delims:
        t = takeuntil(t, delim)
    o = redotsubtitle.match(t)
    if o:
        t = o.group("title")
    return t

def normalizebib(tf):
    (t, f) = authoreditor(tf)
    if "title" in f:
        f["title"] = titledelim(rekillparen.sub("", f["title"]))
    if "author" in f:
        f["author"] = takeuntil(rekillparen.sub("", f["author"]), " with ")
    return (t, f) 
    
def mrgu(fs = ['hh.bib', 'mpieva.bib', "sil16.bib", "asjp2010.bib", "eballiso2009.bib", "fabreall2009ann.bib", "silpng.bib", "wals.bib", "weball.bib", "seifart.bib", "sala.bib", "ozbib.bib", "stampe.bib", "lapolla-tibeto-burman.bib", "guldemann.bib", "schikowski_chintang.bib", "otomanguean.bib", "bahasa.bib", "sn.bib", 'anla.bib', "APiCS.bib", "Zurich.bib", "hedvig-tirailleur.bib", "bowern.bib"], normalize = lambda x: x):
    e = {}
    r = {}
    for f in fs:
        e[f] = {k: normalizebib(v) for (k, v) in get2u(f).items()}
        print(f, len(e[f]))
        
    ft = sumds([fdt(e[f]) for f in fs])
    
    for f in fs:
        rp = len(r)
        bk = [(keyid(fields, ft), (f, k)) for (k, (typ, fields)) in e[f].items()]
        for (hk, k) in bk:
            setd(r, hk, k)
        print(len(r) - rp, "new from total", len(e[f]))
    return (e, r)


#from monster2010 import mrg
def bibminus(p = "aymeric_refgrams.bib", minus = "hh.bib"):
    (e, r) = mrg([p, minus])
    sm = [k for ks in r.values() if len(ks) != 1 for (f, k) in ks.keys() if f == p]
    df = set(e[p].keys()).difference(sm)
    return dict([(k, e[p][k]) for k in df])

def sameas(r):
    q = {}
    for (_, dps) in r.items():
        if len(dps) != 1:
            grp = dps.keys()
            for x in grp:
                q[x] = grp
    return q

def grabu(what = 'macro_area', into = 'mpieva.bib', froms = ['hh.bib', 'fabreall2009ann.bib', 'eballiso2009.bib', 'umi.bib'], overwrite = False):
    (e, r) = mrgu(froms)
    q = sameas(r)
    t = getu(into)
    bak(into)
    cs = [(k, q[(into, k)]) for (k, (typ, fields)) in t.items() if (not fields.has_key(what) or overwrite) and q.has_key((into, k))]
    csw = [(k, [((dpf, dpk), e[dpf][dpk][1][what]) for (dpf, dpk) in d if e[dpf][dpk][1].has_key(what)]) for (k, d) in cs]
    poss = [(k, list(set(dict(v).values()))) for (k, v) in csw if v]
    print(len(poss), "cases of friends non-zero values")
    unique = [(k, v) for (k, v) in poss if len(v) == 1]
    print(len(unique), "cases of friends unique values")
    fnups = [(k, what, v[0]) for (k, v) in unique if not t[k][1].get(what) == v[0]]
    t2 = renfn(t, fnups)
    print(len(fnups), "updates")
    savu(putu(t2, srtkey = 'macro_area'), into)
    #bib.insert_field(into, dict([(k, what + ' = {' + v[0][1] + '}') for (k, v) in fnups]))
    return csw


def graboclc(fn = "hh.bib", fr = "hhwc.bib", obase = "hhalloclc.bib", grab = ["pages", "oclc", "isbn"]): #, grablistfn = "hhoclcgrab.tab"):
    e = getu(fn)
    oclc = getu(fr)
    hhoclcall = grp2([(f["hhquery"], k) for (k, (t, f)) in oclc.items() if t != "done" and f.has_key("hhquery")])
    hhoclc = dict([(hhk, [ok for ok in oks if e.has_key(hhk) and same23(oclc[ok], e[hhk])]) for (hhk, oks) in hhoclcall.items()])
    print("OCLC-HH matchup", fd([len(v) for v in hhoclc.values()]))
    ex = [(hhk, oks[0]) for (hhk, oks) in hhoclc.items() if len(oks) == 1]
    oclc = get(obase)
    bak(fn)
    for g in grab:
        grabhits = [(hhk, ok) for (hhk, ok) in ex if oclc[ok][1].has_key(g) and not e[hhk][1].has_key(g)]
        for (hhk, ok) in grabhits:
            (t, f) = e[hhk]
            f[g] = oclc[ok][1][g]
            e[hhk] = (t, f)
    savu(putu(e), fn)
    return

def hhoclc(fn = "hh.bib", fr = "hhwc.bib", obase = "hhalloclc.bib", outfn = "hhoclc.bib"):
    e = getu(fn)
    oclc = getu(fr)
    oclcall = getu(obase)
    hhoclcall = grp2([(f["hhquery"], k) for (k, (t, f)) in oclc.items() if t != "done" and "hhquery" in f])
    hhoclc = dict([(hhk, [ok for ok in oks if hhk in e and (same23(oclc[ok], e[hhk]) or same23(oclcall.get(ok, (None, {})), e[hhk]))]) for (hhk, oks) in hhoclcall.items()])
    print("OCLC-HH matchup", len(stripd(hhoclc)))
    #ex = [(hhk, oks[0]) for (hhk, oks) in hhoclc.items() if len(oks) == 1]
    hhoclce = {}
    for (hhk, oks) in hhoclc.items():
        if "oclc" in e.get(hhk, (None, {}))[1]:
            oks = [e[hhk][1]["oclc"]]
        if not oks:
            continue
        hhoclce[hhk] = fuse([oclcall[ok] for ok in oks if ok in oclcall] + [oclc[ok] for ok in oks if ok in oclc])
    bak(outfn)
    savu(putu(hhoclce), outfn)
    return



def checklatex(e, backslashfields = ['fn', 'cfn', 'url', 'delivered', 'besttxt', 'bestfn']):
    for (k, (t, fs)) in e.items():
        for (f, v) in fs.items():
            if f in backslashfields:
                continue
            i = v.find("\\")
            if i != -1 and v[i:i+4] != "\\url":
                print("Latex?", k, f, v)


#"hhgb.bib", "hhoclc.bib"
def counterpart(e, fr = "hhgb.bib", fields = ["pages", "oclc", "inlg", "isbn"]):
    #e = getu(fn)
    gb = getu(fr)
    r = {}
    for (k, (t, f)) in e.items():
        for field in fields:
            if field in gb.get(k, (None, {}))[1]:
                r[k, field] = (f.get(field, ""), gb[k][1][field])
    return r

                
#e = get()
#ft = fdt(e)
#g = grp2([(keyid(fields, ft), k) for (k, (typ, fields)) in e.items()])
#print len(e), len(g)
#print s2(opv(g, len))[:20]


#Python 3.5.2 (default, Nov 12 2018, 13:43:14) 
#[GCC 5.4.0 20160609] on linux
#Type "help", "copyright", "credits" or "license" for more information.
#>>> from pybtex.database import parse_file
#>>> res = parse_file('source.bib', bib_format='bibtex')
#>>> len(res.entries)
#327712
