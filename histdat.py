import time
import tkinter as tk
import webbrowser

wn = tk.Tk()
wn.title('Histdat by Alexandros Giannakis') # Πρόγραμμα από τον Αλέξανδρο Γιαννάκη
wn.geometry("570x250")

def search_word(event=None):
    if run_lexigram.get() == 1:
        webbrowser.open('https://www.lexigram.gr/lex/arch/'+greek_word_input.get())
    webbrowser.open('https://myria.math.aegean.gr/lds/web/view.php?search='+greek_word_input.get())

def make_clear(word):
    word = word.replace('ΰ', 'υ')
    word = word.replace('ΐ', 'ι')
    word = word.replace('ς', 'σ')
    word = word.upper()
    word = word.replace('Ά', 'Α')
    word = word.replace('Έ', 'Ε')
    word = word.replace('Ή', 'Η')
    word = word.replace('Ί', 'Ι')
    word = word.replace('Ό', 'Ο')
    word = word.replace('Ύ', 'Υ')
    word = word.replace('Ώ', 'Ω')
    word = word.replace('Ϊ', 'Ι')
    word = word.replace('Ϋ', 'Υ')
    return word

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
perseus_urls = ['http://www.perseus.tufts.edu/hopper/searchresults?q=Homer',
                'http://www.perseus.tufts.edu/hopper/searchresults?q=Hesiod',
                'http://www.perseus.tufts.edu/hopper/searchresults?q=Herodotus',
                'http://www.perseus.tufts.edu/hopper/searchresults?q=Thucydides',
                'http://www.perseus.tufts.edu/hopper/searchresults?q=Xenophon',
                'http://www.perseus.tufts.edu/hopper/searchresults?q=Plato',
                'http://www.perseus.tufts.edu/hopper/searchresults?q=Aristotle',
                'http://www.perseus.tufts.edu/hopper/searchresults?q=Lysias',
                'http://www.perseus.tufts.edu/hopper/searchresults?q=Demosthenes',
                'http://www.perseus.tufts.edu/hopper/searchresults?q=Aeschylus',
                'http://www.perseus.tufts.edu/hopper/searchresults?q=Sophocles',
                'http://www.perseus.tufts.edu/hopper/searchresults?q=Euripides',
                'http://www.perseus.tufts.edu/hopper/searchresults?q=Aeschines',
                'http://www.perseus.tufts.edu/hopper/searchresults?q=Aristophanes',
                'http://www.perseus.tufts.edu/hopper/searchresults?q=Arrian',
                'http://www.perseus.tufts.edu/hopper/searchresults?q=Bacchylides',
                'http://www.perseus.tufts.edu/hopper/searchresults?q=Bion',
                'http://www.perseus.tufts.edu/hopper/searchresults?q=Gorgias',
                'http://www.perseus.tufts.edu/hopper/searchresults?q=Theocritus',
                'http://www.perseus.tufts.edu/hopper/searchresults?q=Theophrastus',
                'http://www.perseus.tufts.edu/hopper/searchresults?q=Isocrates',
                'http://www.perseus.tufts.edu/hopper/searchresults?q=Plutarch',
                'http://www.perseus.tufts.edu/hopper/searchresults?q=Pindar',
                'http://www.perseus.tufts.edu/hopper/searchresults?q=Moschus',
                'http://www.perseus.tufts.edu/hopper/searchresults?q=Callimachus',
                'http://www.perseus.tufts.edu/hopper/searchresults?q=Lucian',
                'http://www.perseus.tufts.edu/hopper/searchresults?q=Antiphon',
                'http://www.perseus.tufts.edu/hopper/searchresults?q=Longus'
]
tlg_urls = ['http://stephanus.tlg.uci.edu/Iris/demo/csearch.jsp#doc=tlg&aid=0012&wid=&q=HOMERUS&dt=list&cs_sort=1_sortname_asc&st=author_text&aw=&verndipl=0&per=50&c=2&acp=1&editid=',
            'http://stephanus.tlg.uci.edu/Iris/demo/csearch.jsp#doc=tlg&aid=0020&wid=&q=HESIODUS&dt=list&cs_sort=1_sortname_asc&st=author_text&aw=&verndipl=0&per=50&c=2&acp=1&editid=',
            'http://stephanus.tlg.uci.edu/Iris/demo/csearch.jsp#doc=tlg&aid=0016&wid=&q=HERODOTUS&dt=list&cs_sort=1_sortname_asc&st=author_text&aw=&verndipl=0&per=50&c=3&acp=1&editid=',
            'http://stephanus.tlg.uci.edu/Iris/demo/csearch.jsp#doc=tlg&aid=0003&wid=&q=THUCYDIDES&dt=list&cs_sort=1_sortname_asc&st=author_text&aw=&verndipl=0&per=50&c=4&acp=1&editid=',
            'http://stephanus.tlg.uci.edu/Iris/demo/csearch.jsp#doc=tlg&aid=0032&wid=&q=XENOPHON&dt=list&cs_sort=1_sortname_asc&st=author_text&aw=&verndipl=0&per=50&c=5&acp=1&editid=',
            'http://stephanus.tlg.uci.edu/Iris/demo/csearch.jsp#doc=tlg&aid=0059&wid=&q=PLATO&dt=list&cs_sort=1_sortname_asc&st=author_text&aw=&verndipl=0&per=50&c=4&acp=1&editid=',
            'http://stephanus.tlg.uci.edu/Iris/demo/csearch.jsp#doc=tlg&aid=&wid=&q=ARISTOTELES&dt=list&cs_sort=1_sortname_asc&st=author_text&aw=&verndipl=0&per=50&c=5&acp=&editid=',
            'http://stephanus.tlg.uci.edu/Iris/demo/csearch.jsp#doc=tlg&aid=0540&wid=&q=LYSIAS&dt=list&cs_sort=1_sortname_asc&st=author_text&aw=&verndipl=0&per=50&c=3&acp=1&editid=',
            'http://stephanus.tlg.uci.edu/Iris/demo/csearch.jsp#doc=tlg&aid=0014&wid=&q=DEMOSTHENES&dt=list&cs_sort=1_sortname_asc&st=author_text&aw=&verndipl=0&per=50&c=2&acp=1&editid=',
            'http://stephanus.tlg.uci.edu/Iris/demo/csearch.jsp#doc=tlg&aid=0085&wid=&q=AESCHYLUS&dt=list&cs_sort=1_sortname_asc&st=author_text&aw=&verndipl=0&per=50&c=3&acp=1&editid=',
            'http://stephanus.tlg.uci.edu/Iris/demo/csearch.jsp#doc=tlg&aid=0011&wid=&q=SOPHOCLES&dt=list&cs_sort=1_sortname_asc&st=author_text&aw=&verndipl=0&per=50&c=2&acp=1&editid=',
            'http://stephanus.tlg.uci.edu/Iris/demo/csearch.jsp#doc=tlg&aid=0006&wid=&q=EURIPIDES&dt=list&cs_sort=1_sortname_asc&st=author_text&aw=&verndipl=0&per=50&c=2&acp=1&editid=',
            'http://stephanus.tlg.uci.edu/Iris/canon/csearch.jsp#doc=tlg&aid=0026&wid=&q=AESCHINES&dt=list&cs_sort=1_sortname_asc&st=author_text&aw=&verndipl=0&per=50&c=2&acp=1&editid=',
            'http://stephanus.tlg.uci.edu/Iris/demo/csearch.jsp#doc=tlg&aid=&wid=&q=ARISTOPHANES&dt=list&cs_sort=1_sortname_asc&st=author_text&aw=&verndipl=0&per=50&c=2&acp=&editid=',
            'http://stephanus.tlg.uci.edu/Iris/canon/csearch.jsp#doc=tlg&aid=&wid=&q=Flavius%20ARRIANUS&dt=list&cs_sort=1_sortname_asc&st=author_text&aw=&verndipl=0&per=50&c=3&acp=1&editid=',
            'http://stephanus.tlg.uci.edu/Iris/canon/csearch.jsp#doc=tlg&aid=0199&wid=&q=BACCHYLIDES&dt=list&cs_sort=1_sortname_asc&st=author_text&aw=&verndipl=0&per=50&c=2&acp=1&editid=',
            'http://stephanus.tlg.uci.edu/Iris/canon/csearch.jsp#doc=tlg&aid=0036&wid=&q=BION&dt=list&cs_sort=1_sortname_asc&st=author_text&aw=&verndipl=0&per=50&c=4&acp=1&editid=',
            'http://stephanus.tlg.uci.edu/Iris/canon/csearch.jsp#doc=tlg&aid=0593&wid=&q=GORGIAS&dt=list&cs_sort=1_sortname_asc&st=author_text&aw=&verndipl=0&per=50&c=5&acp=1&editid=',
            'http://stephanus.tlg.uci.edu/Iris/canon/csearch.jsp#doc=tlg&aid=0005&wid=&q=THEOCRITUS&dt=list&cs_sort=1_sortname_asc&st=author_text&aw=&verndipl=0&per=50&c=3&acp=1&editid=',
            'http://stephanus.tlg.uci.edu/Iris/canon/csearch.jsp#doc=tlg&aid=0093&wid=&q=THEOPHRASTUS&dt=list&cs_sort=1_sortname_asc&st=author_text&aw=&verndipl=0&per=50&c=4&acp=1&editid=',
            'http://stephanus.tlg.uci.edu/Iris/demo/csearch.jsp#doc=tlg&aid=0010&wid=&q=ISOCRATES&dt=list&cs_sort=1_sortname_asc&st=author_text&aw=&verndipl=0&per=50&c=5&acp=1&editid=',
            'http://stephanus.tlg.uci.edu/Iris/demo/csearch.jsp#doc=tlg&aid=0007&wid=&q=PLUTARCHUS&dt=list&cs_sort=1_sortname_asc&st=author_text&aw=&verndipl=0&per=50&c=2&acp=1&editid=',
            'http://stephanus.tlg.uci.edu/Iris/canon/csearch.jsp#doc=tlg&aid=0033&wid=&q=PINDARUS&dt=list&cs_sort=1_sortname_asc&st=author_text&aw=&verndipl=0&per=50&c=2&acp=1&editid=',
            'http://stephanus.tlg.uci.edu/Iris/canon/csearch.jsp#doc=tlg&aid=0035&wid=&q=MOSCHUS&dt=list&cs_sort=1_sortname_asc&st=author_text&aw=&verndipl=0&per=50&c=2&acp=1&editid=',
            'http://stephanus.tlg.uci.edu/Iris/canon/csearch.jsp#doc=tlg&aid=0533&wid=&q=CALLIMACHUS&dt=list&cs_sort=1_sortname_asc&st=author_text&aw=&verndipl=0&per=50&c=2&acp=1&editid=',
            'http://stephanus.tlg.uci.edu/Iris/canon/csearch.jsp#doc=tlg&aid=0062&wid=&q=LUCIANUS&dt=list&cs_sort=1_sortname_asc&st=author_text&aw=&verndipl=0&per=50&c=2&acp=1&editid=',
            'http://stephanus.tlg.uci.edu/Iris/demo/csearch.jsp#doc=tlg&aid=0028&wid=&q=ANTIPHON&dt=list&cs_sort=1_sortname_asc&st=author_text&aw=&verndipl=0&per=50&c=2&acp=1&editid=',
            'http://stephanus.tlg.uci.edu/Iris/canon/csearch.jsp#doc=tlg&aid=0561&wid=&q=LONGUS&dt=list&cs_sort=1_sortname_asc&st=author_text&aw=&verndipl=0&per=50&c=2&acp=1&editid='
]
more_urls = [['http://users.sch.gr/ipap/Ellinikos%20Politismos/Yliko/OMHROS-ILIADA/ARXAIO/ILIADA.htm', 'http://users.sch.gr/ipap/Ellinikos%20Politismos/Yliko/OMHROS%20ODYSSEIA/OMHROS%20ODYSSEIA.htm'],
             [],
             [],
             [],
             [],
             [],
             [],
             [],
             [],
             [],
             [],
             [],
             [],
             [],
             [],
             [],
             [],
             [],
             [],
             [],
             [],
             [],
             [],
             [],
             [],
             [],
             [],
             []
]

greek_letter = ['α', 'β', 'γ', 'δ', 'ε', 'ζ', 'η', 'θ', 'ι', 'κ', 'λ', 'μ', 'ν', 'ξ', 'ο', 'π', 'ρ', ['σ', 'ς'], 'τ', 'υ', 'φ', 'χ', 'ψ', 'ω', ['ά', 'ά'], ['έ', 'έ'], ['ή', 'ή'], ['ί', 'ί'], ['ό', 'ό'], ['ύ', 'ύ'], ['ώ', 'ώ'], 'ὰ', 'ὲ', 'ὴ', 'ὶ', 'ὸ', 'ὺ', 'ὼ', 'ᾶ', 'ῆ', 'ῖ', 'ῦ', 'ῶ']
greek_letter_perseus_format = ['a', 'b', 'g', 'd', 'e', 'z', 'h', 'q', 'i', 'k', 'l', 'm', 'n', 'c', 'o', 'p', 'r', 's', 't', 'u', 'f', 'x', 'y', 'w', 'a/', 'e/', 'h/', 'i/', 'o/', 'u/', 'w/', 'a\\', 'e\\', 'h\\', 'i\\', 'o\\', 'u\\', 'w\\', 'a=', 'h=', 'i=', 'u=', 'w=']
def search_author(event=None):
    author = search_textbox.get()
    for i in range(len(authors)):
        if make_clear(author) in authors[i]:
            webbrowser.open(greek_language_urls[i])
            webbrowser.open(perseus_urls[i])
            for mu in more_urls[i]:
                webbrowser.open(mu)
            time.sleep(1)
            if run_tlg.get() == 1:
                webbrowser.open(tlg_urls[i])

def greek_words():
    canvas.grid_forget()
    search_textbox.grid_forget()
    search_button.grid_forget()
    tlg_checkbox.grid_forget()
    greek_word_input.grid(row=0, column=2)
    greek_word_submit_button.grid(row=0, column=3)
    lexigram_checkbox.grid(row=1, column=1, sticky=tk.W)
    

def greek_authors():
    wn.configure(bg="dark orange")
    greek_word_input.grid_forget()
    greek_word_submit_button.grid_forget()
    lexigram_checkbox.grid_forget()
    canvas.grid(row=2, column=1, columnspan=4)           
    canvas.create_image(20,20, anchor=tk.NW, image=bg)
    search_textbox.grid(row=0, column=2, sticky=tk.W+tk.E)
    search_button.grid(row=0, column=3, sticky=tk.W+tk.E)
    tlg_checkbox.grid(row=1, column=1, sticky=tk.W)

bg = tk.PhotoImage(file = "greek_authors_img.png")
f1_button = tk.Button(wn, text='Greek\nAuthors', width=7, height=2, command=greek_authors)
f2_button = tk.Button(wn, text='Greek\nWords', width=7, height=2, command=greek_words)
f1_button.grid(row=1, column=0, sticky=tk.NW)
f2_button.grid(row=2, column=0, sticky=tk.NW)
greek_word_input = tk.Entry(wn, width=32, font=32)
greek_word_input.bind('<Return>', search_word)
greek_word_submit_button = tk.Button(wn, text="Search", command=search_word)
canvas = tk.Canvas(wn, width = 500, height = 200, bg='dark orange', highlightthickness=0)
search_textbox = tk.Entry(wn, width=50)
search_textbox.bind('<Return>', search_author)
run_tlg = tk.IntVar()
run_lexigram = tk.IntVar()
search_button = tk.Button(wn, text="Search", command=search_author)
lexigram_checkbox = tk.Checkbutton(wn, bg='dark orange', text='Lexigram',variable=run_lexigram, onvalue=1, offvalue=0)
tlg_checkbox = tk.Checkbutton(wn, bg='dark orange', text='TLG',variable=run_tlg, onvalue=1, offvalue=0)
greek_authors()
wn.mainloop()
