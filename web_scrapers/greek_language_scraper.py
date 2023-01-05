import requests
import bs4
import re

authors = [['ΟΜΗΡΟΣ', 'HOMER', 'HOMERUS'],
           ['ΗΣΙΟΔΟΣ', 'HESIOD', 'HESIODUS'],
           ['ΗΡΟΔΟΤΟΣ', 'HERODOTUS'],
           ['ΘΟΥΚΥΔΙΔΗΣ', 'THUCYDIDES'],
           ['ΞΕΝΟΦΩΝ', 'ΞΕΝΟΦΩΝΤΑΣ', 'XENOPHON'],
           ['ΠΛΑΤΩΝ', 'ΠΛΑΤΩΝΑΣ', 'PLATO'],
           ['ΑΡΙΣΤΟΤΕΛΗΣ', 'ARISTOTLE'],
           ['ΛΥΣΙΑΣ', 'LYSIAS'],
           ['ΔΗΜΟΣΘΕΝΗΣ', 'DEMOSTHENES'],
           ['ΑΙΣΧΥΛΟΣ', 'AESCHYLUS'],
           ['ΣΟΦΟΚΛΗΣ', 'SOPHOCLES'],
           ['ΕΥΡΙΠΙΔΗΣ', 'EURIPIDES'],
           ['ΑΙΣΧΙΝΗΣ', 'AESCHINES'],
           ['ΑΡΙΣΤΟΦΑΝΗΣ', 'ARISTOPHANES'],
           ['ΑΡΡΙΑΝΟΣ', 'ARRIAN'],
           ['ΒΑΚΧΥΛΙΔΗΣ', 'BACCHYLIDES'],
           ['ΒΙΩΝ', 'BION'],
           ['ΓΟΡΓΙΑΣ', 'GORGIAS'],
           ['ΘΕΟΚΡΙΤΟΣ', 'THEOCRITUS'],
           ['ΘΕΟΦΡΑΣΤΟΣ', 'THEOPHRASTUS'],
           ['ΙΣΟΚΡΑΤΗΣ', 'ISOCRATES'],
           ['ΠΛΟΥΤΑΡΧΟΣ', 'PLUTARCH'],
           ['ΠΙΝΔΑΡΟΣ', 'PINDAR', 'PINDARUS'],
           ['ΜΟΣΧΟΣ', 'MOSCHUS'],
           ['ΚΑΛΛΙΜΑΧΟΣ', 'CALLIMACHUS'],
           ['ΛΟΥΚΙΑΝΟΣ', 'LUCIANUS'],
           ['ΑΝΤΙΦΩΝ', 'ΑΝΤΙΦΩΝ ΡΗΤΩΡ', 'ANTIPHON'],
           ['ΛΟΓΓΟΣ', 'LONGUS']
]
greek_language_urls = ['https://www.greek-language.gr/digitalResources/ancient_greek/library/index.html?author_id=194',
                       'https://www.greek-language.gr/digitalResources/ancient_greek/library/index.html?author_id=156',
                       'https://www.greek-language.gr/digitalResources/ancient_greek/library/index.html?author_id=153',
                       'https://www.greek-language.gr/digitalResources/ancient_greek/library/index.html?author_id=160',
                       'https://www.greek-language.gr/digitalResources/ancient_greek/library/index.html?author_id=191',
                       'https://www.greek-language.gr/digitalResources/ancient_greek/library/index.html?author_id=199',
                       'https://www.greek-language.gr/digitalResources/ancient_greek/library/index.html?author_id=122',
                       'https://www.greek-language.gr/digitalResources/ancient_greek/library/index.html?author_id=181',
                       'https://www.greek-language.gr/digitalResources/ancient_greek/library/index.html?author_id=133',
                       'https://www.greek-language.gr/digitalResources/ancient_greek/library/index.html?author_id=102',
                       'https://www.greek-language.gr/digitalResources/ancient_greek/library/index.html?author_id=214',
                       'https://www.greek-language.gr/digitalResources/ancient_greek/library/index.html?author_id=150',
                       'https://www.greek-language.gr/digitalResources/ancient_greek/library/index.html?author_id=101',
                       'https://www.greek-language.gr/digitalResources/ancient_greek/library/index.html?author_id=123',
                       'https://www.greek-language.gr/digitalResources/ancient_greek/library/index.html?author_id=124',
                       'https://www.greek-language.gr/digitalResources/ancient_greek/library/index.html?author_id=127',
                       'https://www.greek-language.gr/digitalResources/ancient_greek/library/index.html?author_id=129',
                       'https://www.greek-language.gr/digitalResources/ancient_greek/library/index.html?author_id=130',
                       'https://www.greek-language.gr/digitalResources/ancient_greek/library/index.html?author_id=158',
                       'https://www.greek-language.gr/digitalResources/ancient_greek/library/index.html?author_id=159',
                       'https://www.greek-language.gr/digitalResources/ancient_greek/library/index.html?author_id=166',
                       'https://www.greek-language.gr/digitalResources/ancient_greek/library/index.html?author_id=201',
                       'https://www.greek-language.gr/digitalResources/ancient_greek/library/index.html?author_id=198',
                       'https://www.greek-language.gr/digitalResources/ancient_greek/library/index.html?author_id=187',
                       'https://www.greek-language.gr/digitalResources/ancient_greek/library/index.html?author_id=169',
                       'https://www.greek-language.gr/digitalResources/ancient_greek/library/index.html?author_id=177',
                       'https://www.greek-language.gr/digitalResources/ancient_greek/library/index.html?author_id=116',
                       'https://www.greek-language.gr/digitalResources/ancient_greek/library/index.html?author_id=175'
]

def get_author(name):
    gl_to_remove = ['απ. XI Gow (ΕΣΠΕΡΟΣ) ', ' ΒΙΩΝ - ', ' ', '1']
    lst = []
    for author in authors:
        if name in author:
            html = requests.get(greek_language_urls[authors.index(author)]).text
            soup = bs4.BeautifulSoup(html, 'html.parser')
            result = [x for x in soup.findAll(text=True) if x != '\n']
            result = [result[i] for i in range(1, len(result)) if author[0] in result[i - 1]]
            index = 0
            for res in result:
                if 'εγγραφές' in res or 'εγγραφή' in res:
                    break
                index += 1
            for res in result[index:][1:]:
                if res not in gl_to_remove:
                    lst.append(res)
            num = int(result[index].split()[0])
            for i in range(1, num//5 + 1):
                url = greek_language_urls[authors.index(author)]
                url1 = url[:url.find('author_id=')]
                url = url1 + f'start={i*5}&' + url[url.find('author_id='):]
                html = requests.get(url).text
                soup = bs4.BeautifulSoup(html, 'html.parser')
                result = [x for x in soup.findAll(text=True) if x != '\n']
                result = [result[i] for i in range(1, len(result)) if author[0] in result[i - 1]]
                index = 0
                for res in result:
                    if 'εγγραφές' in res or 'εγγραφή' in res:
                        break
                    index += 1
                for res in result[index:][1:]:
                    if res not in gl_to_remove:
                        lst.append(res)
            return lst

def get_period_that_lived(name):
    periods = ['geometric', 'archaic', 'classic', 'hellenistic', 'roman_rule']
    lst2 = []
    for period_name in periods:
        url = f"https://www.greek-language.gr/digitalResources/ancient_greek/navigator/periods.html?period_name={period_name}_period"
        res = requests.get(url)
        period_info = res.text[res.text.find('<h3 style="line-height: 2em; color: #fff; text-align: center; background: #666;">') + 81:]
        period_info = period_info[:period_info.find('<')].replace('\n', '')
        lst = [content.end() for content in re.finditer("(data-content=|<div style=\"padding: 1px 5px;\">)", res.text)]
        lst1 = []
        tag = ''
        
        for l in lst:
            text = res.text[l:]
            text = text[:text.find('>')]
            text = u':'.join(text.split('&lt;/')).replace('&lt;', '')
            text = text.replace('</div', '')
            if len(text) > 8:
                lst1.append(text.replace('br&gt;', '').replace('b&gt;', ''))

        for l in lst1:
            if l[0] != '\"':
                tag = l
            if name in l:
                lst2.append(l.replace('\"', '') + f' -> {tag} -> {period_info}')
    return lst2

if __name__ == '__main__':
    while True:
        a = input('>:')
        found = False
        for author in authors:
            if a in author:
                print(get_author(a))
                for info in get_period_that_lived(author[0]):
                    print(info)
                found = True
        if not found:
            for info in get_period_that_lived(a):
                print(info)
