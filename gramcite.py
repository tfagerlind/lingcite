from ut import *
import regex

rewhsp = re.compile("\s+")
reychar = regex.compile("(?<=[\d\]\s])([a-z]\s*)$")

#renifs = regex.compile("[\s\S]+?\s\p{Lu}\.$")
refinaldot = regex.compile("(?<![^\p{L}](?=\p{L})[^\p{Ll}])([\,\.]\s*)$")
repagespec = regex.compile("[xivcl]*[+,]? ?[\d+]+\s?pp\.?")


#bodymark = "[^%s]+?(?P<newpage>%s?)[^%s]+?([IEie][Nn]|%s|%s|(?:%s)|(?:%s)|(?:%s)|(?:%s)|(?:%s)|[Rr]eview)[^%s]*?(?(newpage)%s?|[^%s])[^%s]*?" % (newpage, newpage, newpage, editorspec, publisher, mathesis, phdthesis, cpp, pagespec, unpublished, newpage, newpage, newpage)"
#refbody = |title \. [] capitalized token eller bodymark


dashes = "(?:[\—\-\–])"



months = {}
months["eng"] = "(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|(Nov|Dec)(?:ember)?)"

month = "|".join([m for m in months.values()])

date = "\d{1,4}(?:[\.\-\/]\d{1,2}[\.\-\—\/]|\s+(?:%s)\.?\s+)\d{1,4}" % month


newpage = "\x0c"
renewpage = regex.compile(newpage)
#dltext = regex.compile("Brought to you by \|\s[^\|]+\s\|\s+[\d\.]+\s+Download Date\s+\|\s+[ \d\/\:PAM]+\s*(?=%s)" % newpage)
#pnrd = regex.compile("\s*This content downloaded from [\d\.]+ on [A-Za-z\:\d]+ All use subject to JSTOR Terms and Conditions\s+(?=%s)" % (newpage))
pnrd = {}
pnrd["bryb"] = regex.compile("Brought to you by \|\s[^\|]+?\s(?:\|\s+[\d\.]+|U?n?[Aa]uthenticated)\s+Download Date\s+\|\s+[ \d\/\:PAM]+\s*(?=%s)" % newpage)
pnrd["dlf"] = regex.compile("\s*This content downloaded from [\d\.]+ on [A-Za-z\:\d]+ All use subject to JSTOR Terms and Conditions\s+(?=%s)" % (newpage))
pnrd["google"] = regex.compile("(?<!\S)(?:Hosted|Digitized) by G\s?oogle\\n+(?=%s)" % newpage)


pnrc = regex.compile("Reproduced with permission of the copyright owner. Further reproduction prohibited without permission.|Scanned by CamScanner|Kopie von subito e\.V\.\, geliefert für MPI für evolutionäre Anthropologie (?:[A-Z\d]+)|\uf6d9 Springer \d\d\d\d|Copyright © \d\d\d\d. John Benjamins Publishing Company. All rights reserved.")
pnrt = regex.compile("(?<=%s)\s*\d+\s+(?:References|REFERENCES|Bibliography|BIBLIOGRAPHY)|(?<=%s)\s*(?:References|REFERENCES|[Bb]ibliograph[iy]e?)\s+\d+" % (newpage, newpage))

allupper = regex.compile("(?<!\\\\)\p{Ll}")
firstupper = regex.compile("(?<=^|\|)\p{Ll}")


accessdate = "(?:\(%s\)|(?:[\[\(\,]?\s+(?:[Ll]ast\s+)?(?:[Vv]iewed|[Aa]ccessed|[Cc]onsulted|[Cc]onsultado|[Aa]ccess [Dd]ate|[Aa]s per)\s+(?:(?:on|en)\s+)?(?P<url_access_date>%s)[\)\]\.]?))?" % (date, date)

reuid = {}
reuid["isbn"] = regex.compile("[Ii][Ss][Bb][Nn]\:?\s+(?P<isbn>[\d\-\—X]+)\.?")
reuid["url"] = regex.compile("\(?(?P<url>(?:http[s]?\:\/\/|www.?\.)(?:[a-zA-Z]|\d|\n|[$-_@.&+]|[!*\(\),]|(?:[0-9a-fA-F][0-9a-fA-F]))+)(?<!\))\)?\s*?%s" % accessdate)
reuid["spaced_url"] = regex.compile("\(?(?P<url>(?:http[s]?\:\/\/|www.?\.)(?:[a-zA-Z]|\d|\s|[$-_@.&+]|[!*\(\),]|(?:[0-9a-fA-F][0-9a-fA-F]))+?)\)?\s*?%s" % accessdate)
reuid["doi"] = regex.compile("[Dd][Oo][Ii]\:\s?(?P<doi>[a-zA-Z\—\-\.\_\;\(\)\/\:A-Z0-9]+|(?<![\d\p{L}])?10\.\d{4,9}[\—\-\.\_\;\(\)\/\:A-Z0-9]+)")
reuid["edition"] = regex.compile("\s+\(?(?P<edition>\d*1st|\d*2nd|3\d*hrd|\d*[4-9]th|First|Second|Third|Fourth|Fifth|Sixth|Seventh|Eighth|Ninth|Primera|Segunda|Tercera|Cuarta|Quinienta|Sexta|Séptima|Octava|Novena|\da)\s+[Ee]dn?(?:(?:ition|ici[óo]n))?\.\)?")


repeatauthor = "[\_\—\-\–][\_\—\-\–\s]*" #Perhaps also ..
rerepeatauthor = regex.compile(repeatauthor)

#firstname(s) + lastname(s) + jr
initial = "(?<!\p{L})(?=\p{L})[^\p{Ll}]\p{L}?\p{Ll}?\.(?:[\—\-\–]?(?=\p{L})[^\p{Ll}]\p{L}?\.)*"
firstname = "(?<!\p{L})(?=\p{L})[^\p{Ll}][\p{L}\—\-\–\']+"
finame = "(?:(%s)|(%s))" % (firstname, initial)
firstnames = "%s(?:\s+%s)*" % (finame, finame)

initialnodot = "(?<!\p{L})(?:(?=\p{L})[^\p{Ll}]\p{L}?\.[\—\-\–]?)*(?=\p{L})[^\p{Ll}]\p{L}?\p{Ll}?"
firstnamesnodot = "(?:%s\s+)*%s" % (finame, initialnodot)

lname = "(?:(?<![^\p{Lu}]\.\s+)(?=[\p{L}\'])[^\p{Ll}][\p{L}\—\-\–\']+ )?(?=\p{L})[^\p{Ll}][\p{L}\—\-\–\']+"
vonlower = "van\s+der|van\s+den|van\s+de|von\s+den|von\s+der|der|ter|ten|den|de|di|da|du|van|von|d'|al"
von = "(?<!\p{L})(?:%s|%s|%s)" % (vonlower, firstupper.sub(lambda o: o.group(0).upper(), vonlower), firstupper.sub(lambda o: o.group(0).upper(), vonlower))
etal = "(?:\s+et\s+al\.?|\s+dkk\.?)"
etaled = "%s?(?:\s+(?P<edsparen>\()?[Ee]ds?\.?(?(edsparen)\)|))?" % etal
spacing_separators = "and|AND|et|ET|y|with|dan"
nonspacing_separators = "[\—]+|[\-]+|[\–]|\&|,\sand" #\.+|\,|"
separators = "\s+(?:%s)\s+|\s*(?:%s)\s*|\,\s+" % (spacing_separators, nonspacing_separators)
revon = regex.compile(von + "$")

fullname = "%s(?:[^\n\S]+%s)?[^\n\S]+%s" % (firstnames, von, lname)
commaname = "(?:%s[^\n\S]+)?(?:%s)(?:\s+%s)?,[^\n\S]+(?:%s)([^\n\S]+%s)?" % (von, lname, initial, firstnames, von)
commanamenodot = "(?:%s[^\n\S]+)?(?:%s),[^\n\S]+(?:%s)" % (von, lname, firstnamesnodot)



nocommaname = "(?P<_precomma>%s)(?P<_postcomma>%s)" % (takeuntil(commaname, ","), takeafter(commaname, ","))
nameseries = "(?:%s|%s|%s)(?:(?:%s)(?:%s|%s|%s))*+" % (commaname, nocommaname, repeatauthor, separators, fullname, commaname, nocommaname)
fnameseries = "(?:%s|%s)(?:(?:%s)(?:%s|%s))*+" % (commaname, fullname, separators, fullname, commaname)

splitfnames = "(?P<name>%s|%s|%s)(?=($|%s))" % (commaname, fullname, nocommaname, separators)
resplitnames = regex.compile(splitfnames)


parenname = "(?:%s)\s+\(\s*(?:%s)(?:(?:%s)(?:%s))?(?:\s+%s)?\)" % (lname, firstnames, separators, firstnames, von)
parennameseries = "(?:%s)(?:(?:%s)(?:%s))*+" % (parenname, separators, parenname)
reparenname = regex.compile("(?P<lastname>%s)\s+\(\s*(?P<firstname1>%s)(?:(?:%s)(?P<firstname2>%s))?(?P<von>\s+%s)?\)" % (lname, firstnames, separators, firstnames, von))
reparennameseries = regex.compile(parennameseries + "$")

def splitnames(n):
    return ["%s, %s" % (o.group("_precomma"), o.group("_postcomma")) if o.group("_precomma") and o.group("_postcomma") else o.group("name") for o in resplitnames.finditer(n)]

separators = "\s+(?:%s)\s+|\s*(?:%s)\s*|\,\s+" % (spacing_separators, nonspacing_separators)

cname = "(?:%s\s+)?%s" % (von, lname)
cnameseries = "%s(?:(?:%s)(?:%s))*+%s" % (cname, separators, cname, etaled)

splitcnames = "(?P<name>%s)(?=($|%s))" % (cname, separators)
resplitcnames = regex.compile(splitcnames)

def splitcnames(n):
    return [o.group("name") for o in resplitcnames.finditer(n)]


#lastname = "\p{Lu}[\w\-\']+(?: \p{Lu}[\w\-\']+)?(?:\s+et\s+al\.?)?"
#lastname = "(?:(?<!\. )\p{Lu}[\w\—\-\']+ )?\p{Lu}[\w\—\-\']+(?:\s+et\s+al\.?)?(?:\s+\(?eds?\.?\)?)?"
#nameinitial = "\p{Lu}[\.\w\—\-\']*(?: \p{Lu}[\.\w\—\-\']+)?(?:\s+et\s+al\.?)?"

finalletter = "(?:[a-z]|\s?\([a-z]\)|\s?\[[a-z]\]|[\—\-\–][a-z])"
yearseries = "(?:1[5-9]|20)\d\d(?:\s?[\—\-\–\&\/]\s?\d+|\,\s?(?:1[5-9]|20)\d\d)*+%s?" % finalletter
#year = "[12]\d\d\d\(?[a-z]?\)?\s+\[[12]\d\d\d\]|[12]\d\d\d\(?[a-z]?\)?|s\.f|n\.d\.|n\.y\.|no date|por publicarse|in press|submitted|[Tt]o [Aa]ppear"
year_subst = {}
year_subst["in press"] = "[Ii]n press|[Ee]n prensa"
year_subst["to appear"] = "[Tt]o [Aa]ppear|[Pp]or [Pp]ublicarse|[Nn]on [Pp]ubli[ée]"
year_subst["no date"] = "s\.f\.?|n\.d\.|n\.y\.|no date"
ysubst = "|".join([x for x in year_subst.values()])
#\s*\[[12]\d\d\d\]|(?:%s)
year = "(?:(?:%s)|(?:[Ss]ubmitted|[Ff]orthc(?:\.|oming)|[Ii]n pnrep(?:\.|aration)|%s))(?:\s*\[[12]\d\d\d\])?%s?" % (yearseries, ysubst, finalletter)
pages = "[\d\s\,\-\–xivclXIVCLf]+|\s+et\s+seq\.?|Chapter\s+[\.\d]+|Ch\s+[\.\d]+"

reyear = regex.compile(year)


terminalyear = "(?:\.\s+(?:%s)\.)" % year

preeditorforms = "[EeÉé]ds?[\.\,]?(?:\sby)|[Ee]dited(?:\sby)?|[Ee]ditado(?:\spor)?|[EeÉé]dit[ée]e?(?:\spar)?"
posteditorforms = "[EeÉé]ds?[\.\,]?|coord\.|com[mp]\."
preeditorspec = "(?:%s)" % preeditorforms
posteditorspec = "\((?:%s)\)|(?:%s)" % (posteditorforms, posteditorforms)
editorspec = "%s|%s" % (preeditorspec, posteditorspec)

preeditor = "\(?(?:%s)\s+(?P<preeditor>%s|%s)\)?" % (preeditorspec, fnameseries, cnameseries)
posteditor = "\(?(?P<posteditor>%s|%s)[\,]?\s+(?:%s)\)?" % (fnameseries, cnameseries, posteditorspec)
editor = "%s|%s" % (preeditor, posteditor) 
freeditor = "(?P<editor>%s|%s)" % (fnameseries, cnameseries)
authoreditor = "(?: *\((?:%s)\)| +(?:%s)|\, +(?:%s))" % (posteditorforms, posteditorforms, posteditorforms)



ayp = "(%s)\,?\s+(%s)(?:[,\:]\s*(?:pá?g?s?\.\s)?(%s))?" % (cnameseries, year, pages)
apypp = "(%s)\s+\((%s)(?:[,\:]\s*(?:pá?g?s?\.\s)?(%s))?\)" % (cnameseries, year, pages)
footnotecite = "(?:\d+\t)%s" % ayp
#vlyp = "(?:(%s)\s+)?(%s)\s+(%s)(?:[,\:]\s*(%s))?" % (von, lastname, year, pages)
#vlpypp = "(?:(%s)\s+)?(%s)\s+\((%s)(?:[,\:]\s*(%s))?\)" % (von, lastname, year, pages)
#vlypnp = "(?:(?:%s)\s+)?(?:%s)\s+(?:%s)(?:[,\:]\s*(?:%s))?" % (von, lastname, year, pages)
#vlpyppnp = "(?:(?:%s)\s+)?(?:%s)\s+\((?:%s)(?:[,\:]\s*(?:%s))?\)" % (von, lastname, year, pages)

citation = "(\(%s(?:[,;]\s*%s)*\)|%s|%s)" % (ayp, ayp, apypp, footnotecite)
#(?:[,;]\s*%s)* #vlyp, 
recitation = regex.compile(citation, regex.U)



enum = "(?:\d|[XIVCL])+"
enumerated = "(?:(?P<enumerator>\(%s\)[\.\:\=]?|\[%s\][\.\:\=]?|%s[\.\:\=])\s*)" % (enum, enum, enum)

abbv = "(?:(?=\p{L})[^\p{Ll}])+(?:\s\(?[\d\—\-\–]+\)?)?"
abbreviated = "(?:(?P<abbreviation>\(%s\)[\.\:\=]?|\[%s\][\.\:\=]?|%s[\.\:\=])\s+)" % (abbv, abbv, abbv)

enumabbv = "(?P<local_id>%s|%s)" % (enumerated, abbreviated)

maxonepg = "((?!%s)[^%s])+?%s?((?!%s)[^%s])+?" % (terminalyear, newpage, newpage, terminalyear, newpage)
maxonepgparen = "([^%s\)])+?%s?([^%s\)])+?" % (newpage, newpage, newpage)
maxonepgq = ("([^%s" % newpage) + "%s" + ("])+?%s?([^%s" % (newpage, newpage)) + "%s])+?"

repeatauthor = "(?:%s++|ders(?:elbe|\.))" % dashes
#separators = "\s\—\-\.,\&andAND"
#rebibentry = regex.compile("\n+(?:%s)[^\d%s]+?(?:%s)[\s\S]+?\.[\]\)]?(?=\n+[^\d%s]+?(?:%s))" % (lastname, newpage, year, newpage, year), regex.U)
be = "(?:\n+|^|%s)%s?(?P<be>(%s|(?P<emptyauthor>[\s]+)|%s\s+%s\s+)%s?[\(\.\s\,\:]*(?:%s)\)?+(?![\—\-\–])(?![\:\,\;]\s?[Pp]*\.?\s?[\dxivcl]+\)?)[\.\,]*(?(emptyauthor)\s*[^\p{Ll}\d\s\)\,\.]|\s*+[^\p{Ll}\s\)\,\.\d])%s(?:[\.\]\)]|(?=\\n\\n)))(?=\s*%s?(?:%s|\s+)%s?[\(\.\s\,]*(?:%s)|\s*?%s|\s*$)" % (newpage, enumabbv, nameseries, parennameseries, repeatauthor, authoreditor, year, maxonepg, enumabbv, nameseries, authoreditor, year, newpage)
#rebe = regex.compile("(?:\n+|^)%s?(?P<be>(%s|(?P<emptyauthor>[\s]+))%s?[\(\.\s\,\:]*(?:%s)(?![\—\-\–])(?![\:\,\;]\s?[Pp]*\.?\s?[\dxivcl]+\)?)[\)\.\,]*(?(emptyauthor)\s*[^\p{Ll}\d\s\)\,\.]|\s*+[^\p{Ll}\s\)\,\.\d])%s[\.\]\)])(?=\s*%s?(?:%s|\s+)[\(\.\s\,]*(?:%s)|\s*?%s|\s*$)" % (enumabbv, nameseries, authoreditor, year, maxonepg, enumabbv, nameseries, year, newpage), regex.U)
#(?:\n+|[\p{Lu}[^\d%s]*?
reseparators = regex.compile(separators)



#lastnameseries = "(?:(?:%s)\s+)?(?:%s)(?:(?:%s)(?:(?:%s)\s+)?(?:%s))*" % (von, lastname, separators, von, lastname)


breakcit = "(?P<author>%s)\s+(?P<years>(?:%s)(?:, (?:%s))*)(?:[,\:]\s*(?P<pages>%s))?" % (cnameseries, year, year, pages)
#(?:[,;]\s*%s)* #vlyp,
rebreakcitation = regex.compile(breakcit, regex.U)
reysplit = regex.compile("[,;]\s+")
regenetive = regex.compile("(\'s|\')$")

recommapages = regex.compile("(?P<prepages>[xivcl\d]+)\, (?P<pages>\d+)$")







reenglishbrackets = regex.compile("(?P<title>[\s\S]+)\s*\[(?P<title_english>[^\]]+)\]\s*\.?\s*")

#https://unicode-table.com/en/sets/quotation-marks/

lquotes = "《«‹“‟‘❝〝〟❛‚「『" + "\u276E\u2E42\u275B"
rquotes = "》»›„”’❞〞〞❜‛」』" + "\u276F\u201D\u275F"



#"\u200b" is zero width space
lrquotes = '"' + "'" + "＂" + "\*" + "\u200b"  
    
#* is a frequent OCR error for guillemetright
quotes = lquotes + rquotes + lrquotes #"\„" + "\'" + '\"' + "\’" + "\`" + "\‘" + "\“" + "\”" + "\«" + "\»" + "\*" + "\u200b"
titlestart = "(?:[%s¿¡[]?(?=[\d\p{L}])[^\p{Ll}])" % quotes
quotetitle = "|".join(["[%s]%s[%s]" % (lq, maxonepgq % (rq, rq), rq) for (lq, rq) in zip(lquotes + lrquotes, rquotes + lrquotes)])
title = "[%s][¿¡([\/\d\p{L}][\s\S]*[%s][\,\.]?|[%s]*\s*(?:[¿¡(]|(?=[\d\p{L}])[^\p{Ll}])[\s\S]*?(?:[\?\.\,]|(?=\s?//)|(?=\s?\:)|(?=\s?\()|(?=\s?\(pp\.))" % (quotes, quotes, quotes)
#noparentitle = "%s [\(\{]" % (maxonepgq % ("\(\{", "\(\{"))


#series = "(\.\s\(?(?P<series>[^\.\d]+?)\,?\s*(?P<volume>[XIVCL\d]+)?\.?\)?)??"
series = "(?:(?<=\.)\s*\((?P<dotparenseries>[^\)]+?)\.?\)|\s*\((?P<parenseries>[^\d\)]+?)\,?\s*(?P<parenseriesvolume>[XIVCL\d][XIVCL\d\/\&\—\-\–\:]*)\.?\)[\.\,]?|(?<=\.)\s*(?P<dotseries>[^\d\.]+)\,?\s*(?P<dotseriesvolume>[XIVCL\d][XIVCL\d\/\&\—\-\–\:]*)[\.\,]?)"
#parenseries behover () och \d
#dot behover . och \d
#dot plus paren series behover . ()
ma = {}
ma["spa"] = "Tesis de [Mm]aestr[ií]a|Tesis de [Ll]icenciatura"
ma["fra"] = "M[ée]moire de ma[îi]trise"
ma["deu"] = "Magisterarbeit"
ma["eng"] = "(?:Unpublished\s+)?(?:[MB]\.?\s*A\.?|[Mm]aster[s\'\’]*|[Bb]achelor[s\']*|[Hh]onou?r[s\']*)\s*[Tt]hesis"
mathesis = "(?:%s)" % "|".join(ma.values())
phd = {}
phd["fra"] = "[Tt]hèse de [Dd]octorat(?: de troisi[eè]me cycle)?"
phd["spa"] = "[Tt][ée]sis (?:de\s)[Dd]octora(?:l|do)"
phd["rus"] = "дис[\.\s]+докт\."
phd["eng"] = "(?:(?:Unpublished\s+)?(?:[Pp][Hh]\.?\s*[Dd]\.?|[Dd]octoral|D\.?\s+Litt?\.?)(?:\s+(?:[Tt]hesis|[Dd]issertation|[Dd]iss\.?))?)"
phdthesis = "(?:%s)" % '|'.join(["(?:%s)" % x for x in phd.values()])
unpublished = "(?:[Uu]npublished\s*)?(?:(?:[Tt]ype|[Mm]anu)scr(?:\.|ipt)|[Mm]imeogr(?:\.|aph|aphed)|[MmTt][Ss])(?=[^\p{L}])"
pagespec = "[\.\,]\s+(?P<pages>[\+\s\,\dXIVCLxivcl]+)\s+[Pp][Pp]?\.?"
publisher = "(?![Pp][Pp]?\.?\s*[\dXIVCLxivcl])(?P<publisher>(?=[\p{L}\[])[^\p{Ll}](?:[^\:\.\d]|(?<=(?=\p{L})[^\p{Ll}])\.)+(\s?\:\s*(?=\p{L})[^\p{Ll}][^\:\d]+?)?)(?<![Pp][Pp])"
voltome = "(?:[\,\s]*(?:(?:[Vv][Oo][Ll](?:\.?|[Uu][Mm][Ee]))|[Tt][Oo][Mm][Ee]|[Tt]\.))"
#(?P<pages>[\dxivcl][\d\–\-\?\,fy\s\;\=\(\)xivcl]*))
pagerange = "(?P<pages>\[?[\dXIVCLxivcl]+\]?\s*%s{1,2}\s*[\dXIVCLxivcl]+)" % (dashes)
cpp = "([\:\,\s\(\.]+(?:[Pp]p?\.?\s*|pages\s*)?%s\)?)" % pagerange

dans = "(?:(?:[EeIi][Nn]|[Dd][Aa][Nn][Ss])\:?)"
##This should be the way to match incollection refs:
#1. There are hard separators, namely: 
#quotes, //, ed, pp, in:
#2. There are grabs (always take if you can), namely
#parenseries, dotseries, ed, pp, in:
#3. otherwise order is title booktitle? publisher? note?

#[0] editor + booktitle + pages + series + publisher
#[1] editor + booktitle + series + publisher + pages
#[2] booktitle + editor + pages + series + publisher
#[3] booktitle + editor + series + publisher + pages
#[4] booktitle + editor.
#[5] IN editor (NO EDS.) + booktitle + pages OBL + series + publisher + OBL 
#[6] NO in, booktitle + editor + pages + publisher
#[7] NO in, booktitle + editor + publisher + pages 
#[8] NO in, booktitle + NO editor
#[9] NO booktitle



reat = {}
reat[0] = ("incollection", regex.compile("(?P<title>%s)[\s]+%s\s(%s)[\,\.]?\s+(?P<booktitle>%s)(?<!(?:Vol|V|Tome))%s?(%s)?\s*(?:\.\s+%s)\.?\s*$" % (title, dans, posteditor, title, cpp, series, publisher)))
reat[1] = ("incollection", regex.compile("(?P<title>%s)[\s]+%s\s(%s)[\,\.]?\s+(?P<booktitle>%s)(%s)?\s*(?:\s+%s)?%s?\.?\s*$" % (title, dans, posteditor, title, series, publisher, cpp)))
reat[2] = ("incollection", regex.compile("(?P<title>%s)[\s]+%s\s(?P<booktitle>%s)[\,\.]?\s+(%s)%s?(%s)?\s*(?:\.?\s+%s)\.?\s*$" % (title, dans, title, editor, cpp, series, publisher)))
reat[3] = ("incollection", regex.compile("(?P<title>%s)[\s]+%s\s(?P<booktitle>%s)[\,\.]?\s+(%s)(%s)?(?:\s+%s)?%s?\.?\s*$" % (title, dans, title, editor, series, publisher, cpp)))
reat[4] = ("incollection", regex.compile("(?P<title>%s)[\s]+%s\s(?P<booktitle>%s)[\,\.]?\s+(%s)\.?\s*$" % (title, dans, title, editor)))
reat[5] = ("incollection", regex.compile("(?P<title>%s)[\s]+%s\s(%s)[\,\.]?\s+(?P<booktitle>(?!%s)%s)(?<!(?:Vol|V|Tome))%s(%s)?\s*(?:\.\s+%s)\.?\s*$" % (title, dans, freeditor, editorspec, title, cpp, series, publisher)))
reat[6] = ("incollection", regex.compile("(?P<title>%s)[\s]+(?://\s+)?(?P<booktitle>%s)[\,\.]?\s+(%s)%s?(%s)?\s*(?:\.\s+%s)\.?\s*$" % (title, title, editor, cpp, series, publisher)))
reat[7] = ("incollection", regex.compile("(?P<title>%s)[\s]+(?://\s+)?(?P<booktitle>%s)[\,\.]?\s+(%s)(%s)?\s*(?:\s+%s)?%s?\.?\s*$" % (title, title, editor, series, publisher, cpp)))
reat[8] = ("incollection", regex.compile("(?P<title>%s)[\s]+(?://\s+)?(?P<booktitle>%s)%s?(%s)?\s*(?:\.\s+%s)\.?\s*$" % (title, title, cpp, series, publisher)))
reat[9] = ("incollection", regex.compile("(?P<title>%s)[\s]+(%s\s)?(%s)%s?\.?\s*$" % (title, dans, editor, cpp)))
reat[10] = ("phdthesis", regex.compile("(?P<title>%s)[\s]+\[?(?P<thesistype>%s)(?:,\s(?P<pages>[XLIVC]+))?[\.\,]\s+(?P<school>[^\.]+)\]?(?:\s*\[?(?P<note>[^\.][\s\S]*?)[]\s]*)?\.?$" % (title, phdthesis)))
reat[11] = ("phdthesis", regex.compile("(?P<title>%s)[\s]+(?P<school>[^\.]+)\s+(?P<thesistype>%s)(?:,\s(?P<pages>[XLIVC]+))?(?:[\.\,]?\s*\[?(?P<note>[^\.][\s\S]*?)[]\s]*)?\.?$" % (title, phdthesis)))
reat[12] = ("mastersthesis", regex.compile("(?P<title>%s)[\s]+\[?(?P<thesistype>%s)(?:,\s(?P<pages>[XLIVC]+))?[\.\,]\s+(?P<school>[^\.]+)\]?(?:\s*\[?(?P<note>[^\.][\s\S]*?)[]\s]*)?\.?$" % (title, mathesis)))
reat[13] = ("mastersthesis", regex.compile("(?P<title>%s)[\s]+(?P<school>[^\.]+)\s+(?P<thesistype>%s)(?:,\s(?P<pages>[XLIVC]+))?(?:[\.\,]?\s*\[?(?P<note>[^\.][\s\S]*?)[]\s]*)?\.?$" % (title, mathesis)))
#reat[3] = ("book", re.compile("(?P<editor>[^\d]+?)\(eds?\.\)\s" + year + "\s?(?P<title>[^\\n]+?)\.\s(?P<publisher>[^\[][^\:\.]+(\:\s[^\.]+)?)\.\s?"))
#reat[11] = ("article", regex.compile("(?P<title>%s)[\s]+(?:[Ii][Nn]\:?\s+)?(?P<journal>(?=\p{L})[^\p{Ll}][^\:\d]+?)%s?\,?\s+\#?(?P<volume>[XIVCL\d\?\d\—\-\–\/]+)(\s*[NnOo/\(\.\,\:]\s*(?P<number>[XIVCLxivcl\d\—\-\–\?\/]+?)\)?)?%s?(\.\s(?P<address>[^\.]+))?\.?\s?$" % (title, voltome, cpp)))
reat[14] = ("article", regex.compile("(?P<title>%s)[\s]+(?:%s|//)\s+?(?P<journal>(?=\p{L})[^\p{Ll}][^\d]+?)%s?\,?\s+\#?(?P<volume>[XIVCL\d\?\d\—\-\–\/]++)([NnOoRrÚúMm°/\(\.\,\:\s]*(?P<number>[XIVCLxivcl\d\—\-\–\?\/]+?)\)?)?%s(\.\s(?P<address>[^\.]+))?\.?\s?$" % (title, dans, voltome, cpp)))
reat[15] = ("article", regex.compile("(?P<title>%s)[\s]+(?P<journal>(?=\p{L})[^\p{Ll}][^\:\d]+?)%s?\,?\s+\#?(?P<volume>[XIVCL\d\?\d\—\-\–\/]++)([NnOoRrÚúMm/\(\.\,\:\s]*(?P<number>[XIVCLxivcl\d\—\-\–\?\/]+?)\)?)?%s(\.\s(?P<address>[^\.]+))?\.?\s?$" % (title, voltome, cpp)))
#reat[12] = ("misc", regex.compile("(?P<title>%s)\s+\[?(?P<howpublished>%s[\.\,\s]\s*[\s\S]*?)\]?(%s)?\.?\s*$" % (title, unpublished, pagespec)))
reat[16] = ("misc", regex.compile("(?P<title>%s)\s+\[?(?P<howpublished>%s[\s\S]*?)\]?(%s)?\.?\s*$" % (title, unpublished, pagespec)))
reat[17] = ("book", regex.compile("\s+(?P<_editedvolume>%s)\s+(?P<title>%s)\s+(%s)(%s)?\s*(?:\[(?P<note>[^\]]+)\])?\s*$" % (posteditorspec, title, publisher, pagespec)))
reat[18] = ("book", regex.compile("(?P<title>%s)(\s+|(?:%s))\s*%s\.?(%s)?\s*(?:\[(?P<note>[^\]]+)\])?\s*$" % (title, series, publisher, pagespec)))
reat[19] = ("book", regex.compile("(?P<title>%s)\s+%s\.?\s*(%s)?(%s)?\s*(?:\[(?P<note>[^\]]+)\])?\s*$" % (title, publisher, pagespec, series)))
reat[20] = ("book", regex.compile("(?P<title>%s)\s+%s\.?(%s)?\s*(?:\[(?P<note>[^\]]+)\])?\s*$" % (title, publisher, pagespec)))
reat[21] = ("misc", regex.compile("(?P<title>%s)\s+\[?(?P<howpublished>(?=\p{L})[^\p{Ll}][\s\S]+?)\]?\.?(%s)?\s*$" % (title, pagespec)))
reat[22] = ("misc", regex.compile("(?P<title>%s)\s+\[?(?P<howpublished>[\s\S]+?)\]?\.?(%s)?\s*$" % (title, pagespec)))
reat[23] = ("misc", regex.compile("(?P<title>%s)(%s)?\s*$" % (title, pagespec)))
reat[24] = ("misc", regex.compile("(?P<title>Review\sof\s[\s\S]+?)\.?\s*$"))
#reat[8] = ("misc", re.compile(".+?v\.\s.+?\s\(?\d\d\d\d[a-z]?\)?\s\[rese\\\\\\~na\]\.?"))
#reat[9] = ("misc", re.compile("[_\s-]+\s?v\.\s.+?\s\d\d\d\d[^\\n]+\.?"))
requoted = regex.compile("^\s*[%s]([\s\S]+?)\.?[%s][\.\,]?\s*$" % (quotes, quotes))
remidspc = regex.compile("(?<!\,)(\s+)")

reay = regex.compile("^(?P<author>%s|\s*|%s)(?P<_editedvolume>%s)?[\(\.\s\,\:]*(?P<year>%s)[\)\.\s\:\,\•\—\-\–\,]*" % (nameseries, parennameseries, authoreditor, year), regex.U)


#rebey = regex.compile("(?<=(?:\n+|^)%s?)(?P<be>(?P<author>%s|(?P<emptyauthor>[\s]++))(?:(?<=[\.])|[\.\,\:])\s+(?!\(?(%s))(?P<content>%s%s)(?P<yeartoken>\,\s(%s)|\s\((%s)\))[\:\.](\s?(%s)\.)?)" % (enumabbv, nameseries, year, titlestart, maxonepg, year, year, pagerange))
#efter year:
#: pages        .\n
# ()            .\n
#(?=\s*%s?(?:%s|\s+)[\(\.\s\,]*(?:%s)|\s*?%s)" % enumabbv, nameseries, year, newpage
#men vi kör bara .*?\n"
bey = "(?<=(?:\n+|^|%s)%s?)(?P<bey>(?P<yauthor>%s|(?P<yemptyauthor>[\s]++))(?:(?<=[\.])|[\.\,\:])\s+(?!\(?(%s))(?P<content>%s%s)(?P<yyeartoken>\,\s(%s)|\s\((%s)\))([\:]\s?(%s))?[^\\n%s]*\.?[\\n%s])" % (newpage, enumabbv, nameseries, year, titlestart, maxonepg, year, year, pagerange, newpage, newpage)
#rebey = regex.compile("(?<=(?:\n+|^)%s?)(?P<be>(?P<author>%s|(?P<emptyauthor>[\s]++))(?:(?<=[\.])|[\.\,\:])\s+(?!\(?(%s))(?P<content>%s%s)(?P<yeartoken>\,\s(%s)|\s\((%s)\))([\:]\s?(%s))?[^\\n%s]*\.?[\\n%s])" % (enumabbv, nameseries, year, titlestart, maxonepg, year, year, pagerange, newpage, newpage))

bep = "(?<=\n+|^|\)\.\s?|%s)%s?(?P<bep>(?P<pauthor>(?:%s)\s*+(?:\:|%s|ders\.)++\s*+|[\s]+)(?:(?:%s)|(?:%s))\s*[\(\{](?:%s)(?P<pyeartoken>\,?\s+(?:%s))[^\)]*[\)\}]\.)" % (newpage, enumabbv, parennameseries, dashes, quotetitle, maxonepgparen, maxonepgparen, year)

rebea = regex.compile("(?:%s)|(?:%s)|(?:%s)" % (be, bey, bep))



retoptitle = regex.compile("(?:%s\d+\s++(?P<otitle>[^\\n]+)|%s(?P<etitle>[^\\n]++)\s*\d+)" % (newpage, newpage))
remove_toptitle = "(?<=%s)\d+\s++%s|(?<=%s)%s\s+\d+"

def toppagetitle(txt):
    tts = fd([o.group("otitle") or o.group("etitle") for o in retoptitle.finditer(txt)])
    npgsl = max(2, ((txt.count(newpage)+1) // 4) + 1)
    #print(tts, npgsl)
    if [tt for (tt, ttn) in tts.items() if ttn >= npgsl]:
        print("Found toppagetitle", [(tt, ttn) for (tt, ttn) in tts.items() if ttn >= npgsl])
    return [tt for (tt, ttn) in tts.items() if ttn >= npgsl]
#rebe = regex.compile("(?:\n+|^)%s?(?P<be>(%s|(?P<emptyauthor>[\s]+))[\(\.\s\,\:]*(?:%s)(?![\—\-\–])(?![\:\,\;]\s?[Pp]*\.?\s?[\dxivcl]+\)?)[\)\.\,]*(?(emptyauthor)\s*[^\p{Ll}\d\s\)\,\.]|\s*[^\p{Ll}\s\)\,\.])%s[\.\]\)])(?=\s*%s?(?:%s|\s+)[\(\.\s\,]*(?:%s)|\s*?%s)" % (enumabbv, nameseries, year, maxonepg, enumabbv, nameseries, year, newpage), regex.U)
#(?:\n+|[\p{Lu}[^\d%s]*?

#"\n- 37 -\n\n\x0c"

repgn = regex.compile("(?<=\\n+)((?:%s )?\d+(?: %s)?)(?=\\n+%s)" % (dashes, dashes, newpage))
def remove_pagenumbers(txt):
    return repgn.subn("", txt)

def remove_toppagetitle(txt):
    tts = toppagetitle(txt)
    if tts:
        ortts = "(?:%s)" % "|".join(["%s" % regex.escape(tt) for tt in tts])
        return regex.subn(remove_toptitle % (newpage, ortts, newpage, ortts), "", txt)
    return (txt, 0)

# if , 1999. and pages -> remove \s(year)\. = yeartoken, fast kanske ska byta ut punkten efter till komma?
# if , 1999. and not pages -> remove \, year = yeartoken
# if  (1999) -> remove yeartoken
def moveyear(o):
    authorend = o.end("yauthor")-o.start("yauthor")
    return o.group("bey")[:authorend] + o.group("yyeartoken") + o.group("bey")[authorend:o.start("yyeartoken")-o.start("bey")] + o.group("bey")[o.end("yyeartoken")-o.start("bey"):] 

"Peterson (M. and S.)"
def unspousename(n):
    return " and ".join([("%s, %s%s" % (o.group("lastname"), o.group("firstname1"), o.group("von") or "")) + (" and %s, %s%s" % (o.group("lastname"), o.group("firstname2"), o.group("von") or "") if o.group("firstname2") else "") for o in reparenname.finditer(n)])
  
def moveparen(o):
    #print(o.groupdict())
    authorend = o.end("pauthor")-o.start("pauthor")
    authors = unspousename(o.group("bep")[:authorend])
    body = o.group("bep")[authorend:o.start("pyeartoken")-o.start("bep")] + o.group("bep")[o.end("pyeartoken")-o.start("bep"):]
    year = o.group("pyeartoken").replace(",", "").strip() 
    be = authors + " " + year + ". " + body.replace(" (", ". ").replace(" {", ". ").replace(")", "").replace("}", "")
    return be

def unspace(s):
    return remidspc.sub("", s)

def unquote(s):
    o = requoted.match(s)
    if o:
        return o.group(1)
    return s

def mac(x):
    if x.startswith("Mc"):
        return x[:2] + x[2:].title()
    return x

def uncapitalize(name):
    return " ".join([x.lower() if revon.match(x) else mac(x.title()) for x in name.split()])

def replaceauthor(s, inheritauthor = ""):
    if not s.strip():
        return inheritauthor
    o = rerepeatauthor.match(s.strip())
    if o:
        return (inheritauthor + " " + s[o.end():]).strip()
    return s

def andit(txt, inheritauthor = ""):
    return " and ".join([uncapitalize(n).strip() for n in splitnames(replaceauthor(refinaldot.sub("", txt), inheritauthor))])

def candit(txt):
    return " and ".join([uncapitalize(x).strip() for x in splitcnames(refinaldot.sub("", txt))])

def dict_to_bib(el, inheritauthor = ""):
    r = {}
    for (k, v) in sorted(el.items()):
        #fieldname = k.lower()
        #fieldname = xlate.get(fieldname, fieldname)
        if (k != "author") and (not v or not v.strip()):
            continue
        v = v.strip()
        if k == "author":
            if reparennameseries.match(v):
                v = unspousename(v)
            r['editor' if el.get("_editedvolume") else 'author'] = andit(v, inheritauthor = inheritauthor)
        elif k in ["preeditor", "posteditor", "editor"]:
            r['editor'] = andit(v)
        elif k == "title" or k == "booktitle":
            v = refinaldot.sub("", unquote(v))
            o = reenglishbrackets.match(v)
            if o:
                r[k + "_english"] = o.group("title_english")
                v = o.group("title") 
            r[k] = v
        elif k == 'thesistype':
            pass
        elif k == 'year':
            #v = v.replace(" ", "").replace("[", "").replace("]", "")
            #key = v med bokstaven 1997a
            r["citation_year"] = v
            y = reychar.sub("", v)
            for (uform, ys) in year_subst.items():
                if regex.match("(%s)$" % ys, y):
                    y = uform
                    break
            r[k] = y
        elif k == 'note':
            v = v.replace(" ", "")
            o = repagespec.search(v.lower())
            if o:
                r["pages"] = o.group().replace(", ", "+").replace("pp", "").replace(".", "").strip()
                v = (v[:o.start()] + v[o.end():]).strip()
            if v:
                r[k] = v
        elif k == 'pages':
            #key = v med bokstaven
            v = unspace(v.replace(" y ", ", "))
            v = recommapages.sub(lambda o: "%s+%s" % (o.group("prepages"), o.group("pages")), v.lower())
            r[k] = v 
        elif k == "journal":
            r[k] = refinaldot.sub("", v)
        elif k in ["url", "spaced_url"]:
            r["url"] = refinaldot.sub("", v)
        elif k in ["series", "parenseries", "dotseries"]:
            r["series"] = v
        elif k in ["volume", "parenseriesvolume", "dotseriesvolume"]:
            r["volume"] = v
        elif k == "publisher":
            r[k] = v.replace(" :", ":")
        elif k.startswith("_"):
            pass
        else:
            r[k] = v

    return r

def extract_uids(s, reuid = reuid):
    r = {}
    for (uid_type, rgx) in reuid.items():
        o = rgx.search(s)
        if o:
            r.update(o.groupdict())
            s = s[:o.start()] + s[o.end():]
    return (r, s)

def pitem(origitem, inheritauthor = ""):
    (uidd, item) = extract_uids(origitem, reuid)
    o = reay.match(item)
    if not o:
        print("NO AUTHOR YEAR:", item)
        return None
    r = o.groupdict()
    remain = item[o.end():]
    for i in range(len(reat)):
        (typ, regex) = reat[i]
        o = regex.match(remain)
        if o:
            return (typ, dict_to_bib({**{"item": origitem}, **uidd, **r, **o.groupdict()}, inheritauthor = inheritauthor))
    return None

def breakcitation(s):
    return [(candit(regenetive.sub("", o.group("author"))), year, o.group("pages")) for o in rebreakcitation.finditer(s.replace("(", "").replace(")", "")) for year in reysplit.split(o.group("years"))]

def ye(e):
    return grp2([(f.get("citation_year", f.get("year", "")).lower(), k) for (k, (t, f)) in e.items()])

reetal = regex.compile(etal + "$")
import bib
def matchauthor(a1, a2):
    #unvon
    #undiacritic
    #uncapitalize
    #andra delen av space:ade namn och and namn
    #1962[a-z]? sokning om ej traff
    #OCR errors
    (a1, isetal) = reetal.subn("", a1)
    
    pas1 = bib.pauthor(a1)
    pas2 = bib.pauthor(a2)
    if len(pas1) == 0:
        print("ERROR: empty author", [a1]) 
        return 0

    #print(pas1, pas2)
    ia = {i: a["lastname"] for (i, a) in enumerate(pas2)}
    nm = sum([1 for (i, a) in enumerate(pas1) if ia.get(i) == a["lastname"]])/len(pas1)
    if nm <= 0 and len(pas1) > 1:
        nm = sum([1 for (i, a) in enumerate(pas1[1:]) if ia.get(i) == a["lastname"]])/len(pas1)
    return nm if isetal > 0 else nm/(len(pas2)-nm+1)

#Correct mismatching citations
#- OCR errors
#- de errors
#- single / multiple last name

import difflib
def amendmatchauthor(a1, a2, nposs = 1):
    (a1, isetal) = reetal.subn("", a1)
    
    pas1 = bib.pauthor(a1)
    pas2 = bib.pauthor(a2)
    if len(pas1) == 0:
        print("ERROR: empty author", [a1]) 
        return 0

    #print(pas1, pas2)
    ia = {i: a["lastname"] for (i, a) in enumerate(pas2) if a["lastname"]}
    lnps = [(i, lnp) for (i, a) in enumerate(pas1) for lnp in a["lastname"].split() if (not revon.match(lnp) or len(a["lastname"].split()) == 1)]
    nms = [(i, difflib.SequenceMatcher(None, a, ap).quick_ratio()) for (i, a) in lnps if i in ia for ap in ia[i].split()]
    nmss = sum([delta for (i, delta) in nms if delta > (1-1/(1+nposs))])
    nm = nmss/len(lnps)
    #if nm <= 0 and len(pas1) > 1:
    #    nm = sum([1 for (i, a) in enumerate(pas1[1:]) if ia.get(i) == a["lastname"]])/len(pas1)
    return nm if isetal > 0 or (len(pas2)-nm+1) == 0 else nm/(len(pas2)-nm+1)

def grepcitation(ay, e):
    (a, y) = ay
    yks = ye(e)
    yksy = yks.get(y.lower(), yks.get(reychar.sub("", y.lower()), []))
    
    mas = [(matchauthor(candit(a), e[k][1].get("author", e[k][1].get("editor", ""))), k) for k in yksy]
    pmas = [(mav, mak) for (mav, mak) in mas if mav > 0]
    (mav, mak) = max(pmas) if pmas else (None, None)

    if not mak:
        mas = [(amendmatchauthor(candit(a), e[k][1].get("author", e[k][1].get("editor", ""))), k) for k in yksy]
        pmas = [(mav, mak) for (mav, mak) in mas if mav > 0]
        (mav, mak) = max(pmas) if pmas else (None, None)
        if mak:
            print("Amend match found: ", ay, mak, [e[k][1].get("author", e[k][1].get("editor", "")) for k in yksy])
    return mak

def citationform(tf):
    (t, f) = tf
    return "%s %s" % (f.get("author", f.get("editor", "-")), f.get("citation_year", f.get("year", "no date")))

#z = recitation.findall("Hej (1967) dhksghfkjhf d van der Sar (1978:17); (Niss 2018:56, 58) fhdkg (Cortes 1978; Hammasrtrsom 2007:10-11)")
#print(z)

#ktest = ['b:AbbinkUnseth:Surmic', 'w:Campbell:Mechis', 's:Salminen:Nenets'] #, 'g:MacDonell:Vedic', 't:Nakano:Gzira', 'g:Evans:Kayardild', 'phon:Michael:Anaang', 'e:Iverson:Navajo', 'soc:Hochstetler:Eastern-Maninakan']
#for k in ktest:
#    for (i, p) in readpages(e[k][1]["besttxt"]):
#        ws = tokenize(p)


#case insensitive
refsign = {}
refsign["rus"] = "ЛИТЕРАТУРА"
refsign["eng"] = "references?|bibliography"
refsign["fra"] = "bibliographie"
rerefsign = regex.compile("(?<!\S)(?:%s)" % "|".join(refsign.values()), regex.IGNORECASE)


def beharmonize(o):
    if o.group("be"):
        return (o.start("be"), o.group("be"))
    if o.group("bey"):
        return (o.start("bey"), moveyear(o))
    if o.group("bep"):
        return (o.start("bep"), moveparen(o))
    return None

def ranges(xs):
    cs = {}
    c = []
    i = 0
    lp = None
    for x in xs:
        if lp == (x - 1):
            c = c + [x]
        else:
            if c:
                cs[i] = c
                i += 1
            c = [x]
        lp = x
    if c:
        cs[i] = c
    return [cs[i] for i in range(len(cs))]

def yearsearchreferences(txt):
    pospg = txt_to_pospg(txt)
    pg_to_pos = {pg+1: pospg+1 for (pospg, pg) in [(-1, -1)] + pospg}
    yearpos = [o.start() for o in reyear.finditer(txt)]
    prs = ranges(sorted(set([x for p in set([pos_to_pg(pos, pospg) for pos in yearpos]) for x in [p, p+1] if x < len(pospg)])))
    bs = [(i+pg_to_pos[pr[0]], b) for pr in prs for (i, b) in searchreferences(txt[pg_to_pos[pr[0]]:pg_to_pos[pr[-1]+1]-1])]
    return bs

def pos_to_pg(pos, pospg):
    return next(pg for (pgpos, pg) in pospg if pos < pgpos)

def txt_to_pospg(txt):
    pospg = [(o.start(), i) for (i, o) in enumerate(renewpage.finditer(txt))]
    return pospg + [(len(txt)+1, len(pospg))]

def bibsection(txt):
    pospg = txt_to_pospg(txt)
    #pospg = [(end_of_pg, pg), ...]
    pg_to_pos = {pg+1: pospg+1 for (pospg, pg) in [(-1, -1)] + pospg}
    #pg_to_pos {pg: start_of_pg}
    bs = findreferences(txt)
    pagehits = fd([pos_to_pg(pos, pospg) for (pos, b) in bs])
    pss = pagesection(sorted(pagehits.items()))
    refsections = grp2([(pos_to_pg(o.start(), pospg), o.start()) for o in rerefsign.finditer(txt)])
    prfs = {page: min(refposs) for (page, refposs) in refsections.items()}
    bse = [(min(ps), max(ps)) for ps in pss]
    return [(start, end, max(prfs.get(start, 0), pg_to_pos[start]), pg_to_pos[end]) for (start, end) in bse]
    
def pagesection(pagehits):
    cs = {}
    c = []
    i = 0
    lp = None
    #print(pagehits)
    for (page, hits) in pagehits:
        if lp == (page - 1):
            c = c + [(page, hits)]
        else:
            if c and max([h for (p, h) in c]) > 1:
                cs[i] = c
                i += 1
            c = [(page, hits)]
        lp = page
    if c and max([h for (p, h) in c]) > 1:
        cs[i] = c
    return [[p for (p, h) in cs[i]] for i in range(len(cs))]



bebra = "(?:\n+|^|%s)%s?(?P<be>(%s|%s\s+%s\s+)%s?[\(\.\s\,\:]*(?:%s)(?![\—\-\–])(?![\:\,\;]\s?[Pp]*\.?\s?[\dxivcl]+\)?)[\)\.\,]*\s*+[^\p{Ll}\s\)\,\.\d]%s(?:[\.\]\)]|(?=\\n\\n)))(?=\s*%s?(?:%s|\s+)%s?[\(\.\s\,]*(?:%s)|\s*?%s|\s*$)" % (newpage, enumabbv, nameseries, parennameseries, repeatauthor, authoreditor, year, maxonepg, enumabbv, nameseries, authoreditor, year, newpage)
beybra = "(?<=(?:\n+|^|%s)%s?)(?P<bey>(?P<yauthor>%s)(?:(?<=[\.])|[\.\,\:])\s+(?!\(?(%s))(?P<content>%s%s)(?P<yyeartoken>\,\s(%s)|\s\((%s)\))([\:]\s?(%s))?[^\\n%s]*\.?[\\n%s])" % (newpage, enumabbv, nameseries, year, titlestart, maxonepg, year, year, pagerange, newpage, newpage)
bepbra = "(?<=\n+|^|\)\.\s?|%s)%s?(?P<bep>(?P<pauthor>(?:%s)\s*+(?:\:|%s|ders\.)++\s*+)(?:(?:%s)|(?:%s))\s*[\(\{](?:%s)(?P<pyeartoken>\,?\s+(?:%s))[^\)]*[\)\}]\.)" % (newpage, enumabbv, parennameseries, dashes, quotetitle, maxonepgparen, maxonepgparen, year)
rebra = regex.compile("(?:%s)|(?:%s)|(?:%s)" % (bebra, beybra, bepbra))

def findreferences(txt, rebr = rebra):
    return [beharmonize(o) for o in rebr.finditer(txt)]

def getreferences(txt):
    return parsereferences(searchreferences(txt))

def searchreferences(txt):
    bibsecs = bibsection(txt)
    #print("Found %s" % len(bibsecs), "bibsecs", [(startpg, endpg) for (startpg, endpg, startpos, endpos) in bibsecs]),
    i = 0
    r = {}
    for (startpg, endpg, startpos, endpos) in bibsecs:
        r[i] = findreferences(txt[i:startpos], rebra)
        r[startpos] = findreferences(txt[startpos:endpos], rebea)
        i = endpos
    r[i] = findreferences(txt[i:len(txt)], rebra)
    bs = [(i+bpos, b) for (i, bsi) in r.items() for (bpos, b) in bsi]
    return bs

noparse = ""
def parsereferences(bs, clean = True):
    global noparse
    e = {}
    inheritauthor = ""
    #pgs = {}
    for (i, (pos, b)) in enumerate(bs): # + bys):
        #print([inheritauthor], [rewhsp.sub(" ", b).strip()])
        try:
            z = pitem(rewhsp.sub(" ", b).strip(), inheritauthor = inheritauthor)
        except MemoryError:
            print("MemoryError")
            z = None
        #print(b)
        #print(z)
        if not z:
            print("NO PARSE", i, [b.strip()], "\n\n\n")
            noparse += "%s\n\n\n" % [b.strip()]
        else:
            z[1]["item_position"] = "%s" % pos
            if clean:
                zc = {k: v for (k, v) in z[1].items() if k not in ["citation_year", "item", "item_position"]}
                z = (z[0], zc)
            e["%02d" % i] = z
            inheritauthor = z[1].get("author", "")
            #print("SET", inheritauthor, z[1].keys())
            #page = pos_to_pg(pos, pospg)
            #pgs[page] = pgs.get(page, 0) + 1

    return e

def bibtex(txt):
    return bib.putu(getreferences(txt))

#noparse = ""
#def getreferences(txt):
#    global noparse
#    #bs = [(o.start("be"), o.group("be")) for o in rebe.finditer(txt)]
#    #bys = [(o.start("be"), moveyear(o)) for o in rebey.finditer(txt)]
#    bs = findreferences(txt)
#    print("Regexp refs", len(bs)) #+len(bys), len(bs), len(bys), len(bxs))

#    #for b in bys:
#    #    print([b[1]])
#    #    print(pitem(b[1].strip()))
#    #    print("\n\n\n")

#    #for by in bys:
#    #    if not rebe.match(by):
#    #        print("CANT MATCH MOVEDYEAR SEC", [by])
#    #        print("\n\n\n") + bys

#    pospg = [(o.start(), i) for (i, o) in enumerate(renewpage.finditer(txt))]
#    e = {}
#    inheritauthor = ""
#    pgs = {}
#    for (i, (pos, b)) in enumerate(bs): # + bys):
#        #print([inheritauthor], [rewhsp.sub(" ", b).strip()])
#        z = pitem(rewhsp.sub(" ", b).strip(), inheritauthor = inheritauthor)
#        #print(b)
#        #print(z)
#        if not z:
#            print("NO PARSE", i, [b.strip()], "\n\n\n")
#            noparse += "%s\n\n\n" % [b.strip()]
#        else:
#            e["%02d" % i] = z
#            inheritauthor = z[1].get("author", "")
#            #print("SET", inheritauthor, z[1].keys()) 
#            page = next(pg for (pgpos, pg) in pospg + [(len(txt)+1, len(pospg))] if pos < pgpos)
#            pgs[page] = pgs.get(page, 0) + 1

#    print("References found on pgs", sorted(pgs.items()))
#    return e




#bes = rebibentry.findall(txt)
#print(len(bes))


def getcitations(txt):
    cits = [(o.start(),) + cx for o in recitation.finditer(txt) for cx in breakcitation(o.group(0))]
    return cits


reocr = {}
reocr["Iyear"] = (regex.compile("(?<!\d)[Iil](?P<yyy>\d\d\d)(?!\d)"), lambda o: "1" + o.group("yyy"))
reocr["1 year"] = (regex.compile("(?<=\. )1 (?P<yyy>\d\d\d)(?!\d)"), lambda o: "1" + o.group("yyy"))
reocr["spcpagerange"] = (regex.compile("(?<=[Pp][Pp]?\.?\s*)(?P<pagestart>\d++) (?P<pageend>\d++)"), lambda o: "%s-%s" % (o.group("pagestart"), o.group("pageend")))
reocr["crpagerange"] = (regex.compile("(?<=[Pp][Pp]?\.?\s*)(?P<pagestart>\d++)%s\\n+(?P<pageend>\d++)" % dashes), lambda o: "%s-%s" % (o.group("pagestart"), o.group("pageend")))
reocr["authorinitialdot"] = (regex.compile("(?<=%s)(\s|\,\s?)(?=(?:[\(\.\s\:]*%s|%s))" % (commanamenodot, year, separators), regex.U), lambda o: "." if len(o.group(0)) == 1 else ". ")
#perhaps also correct Tucker A. N, 1987
reocr["pags"] = (regex.compile("(?<!\S)päg(?=s?\. \d)"), "pág")



def ocr_correct(txt):
    n = 0
    for (name, (regexp, ocrr)) in reocr.items():
        (txt, nc) = regexp.subn(ocrr, txt)
        n += nc
    return (txt, n)

def citations_vs_references(cits, e):
    cps = grp2([((a, y), (pos, p)) for (pos, a, y, p) in cits])
    cg = {(a, y): grepcitation((a, y), e) for (a, y) in cps.keys()}

    #for (a, y) in cps.keys():
    #    gc = grepcitation((a, y), e)
        #if not gc:
        #    print(a, y, len(cps[(a, y)]), citationform(e[gc]) if gc else gc)
    print(len(cits), "citations tokens")
    print(len(cps), "citations unique")
    print(len(e), "references")
    hits = [1 for gc in cg.values() if gc]
    mis = [(a, y) for ((a, y), gc) in cg.items() if not gc]
    print(mis)
    if len(cps) > 0:
        print(len(hits), "found in references, precision", len(hits)/len(cps))
    if len(e) > 0:
        print(len(e)-len(hits), "references not cited", (len(e)-len(hits))/len(e))
    return len(hits)/len(cps) if len(cps) > 0 else 0.0

def remove_download_notices(txt):
    nd = 0
    for (dln, dlnre) in pnrd.items():
        (txt, ndln) = dlnre.subn("", txt)
        nd += ndln
    return (txt, nd)


#import timeit


preprocess_report_template = """
Removed %s 'downloaded-from' watermarks
Removed %s references headings
Removed %s copyright notices
Corrected %s OCR errors
Removed %s toppagetitles
Removed %s page numbers""".strip()
def preprocess(txt):
    (txt, nd) = remove_download_notices(txt)
    (txt, nt) = pnrt.subn("", txt)
    (txt, nc) = pnrc.subn("", txt)
    (txt, no) = ocr_correct(txt)
    (txt, np) = remove_toppagetitle(txt)
    (txt, nn) = remove_pagenumbers(txt)
    return (txt, preprocess_report_template % (nd, nt, nc, no, np, nn))

#e = bib.getu("gramcite\\testset.bib")
#r = {}
##e = {"s:Laanest:Izorskij": e["s:Laanest:Izorskij"]}
#for (i, (k, (t, f))) in enumerate(list(e.items())[:10]):
#    print("Starting", i, k, bib.getpages(e[k]), "pgs")
#    
#    start = timeit.default_timer()
#    (txt, preprocess_report) = preprocess(loadu("dbs\\" + f["besttxt"]))
#    pp_time = timeit.default_timer()
#    #bs = searchreferences(txt)
#    bs = yearsearchreferences(txt)
#    findref_time = timeit.default_timer()
#    ek = parsereferences(bs)
#    parseref_time = timeit.default_timer()    
#    cits = getcitations(txt)
#    cit_time = timeit.default_timer()    
#    print(preprocess_report)
#
#    pospg = txt_to_pospg(txt)
#    pgs = fd([pos_to_pg(int(f["item_position"]), pospg) for (k, (t, f)) in ek.items()])
#    rpos = [(int(f["item_position"]), len(f["item"])) for (k, (t, f)) in ek.items()]
#    citsnr = [(cpos, a, y, p) for (cpos, a, y, p) in cits if not [rp for (rp, l) in rpos if (rp <= cpos <= (rp+l))]]
#              
#    v = citations_vs_references(citsnr, ek)
#
#    print("References found on pgs", sorted(pgs.items()))
#    print("Time preprocess", pp_time - start)
#    print("Time find references", findref_time - pp_time)
#    #print("Time find references", bsy_etime - bsy_stime)
#    print("Time parse references", parseref_time - findref_time)
#    print("Time citations", cit_time - parseref_time)
#    #print("BS == BSY", bs == bsy, len(bs), len(bsy))
#    #if bs != bsy:
#    #    print([bs])
#    #    print([bsy])
#    print("\n\n\n")
#    r[k] = (v, cits, ek)


#gramcitebib = {k + "_" + ekk: tf for (k, (v, c, ek)) in r.items() for (ekk, tf) in ek.items()}
#savu(bib.putu(gramcitebib, srtkey=""), "gramcite_testset10.bib") #inlg)


#print("AVG v", avg([v for (k, (v, c, ek)) in r.items()]))
#print("SUM entries", sum([len(ek) for (k, (v, c, ek)) in r.items()]))
#print("SUM citations", sum([len(c) for (k, (v, c, ek)) in r.items()]))
#print("size(noparse)", len(noparse))
#raise ValueError

#txtfn = "ptxt2\\australia\\evans_kayardild1995.txt"
#txt = pnrt.sub("", dltext.sub("", loadu("dbs\\" + txtfn)))
#e = getreferences(txt)
#cits = getcitations(txt)
#citations_vs_references(cits, e)

#TODO känn igen OCLC och journal title som är typ 3e serie och sånt
