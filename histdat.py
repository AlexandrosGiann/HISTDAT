import time
import tkinter as tk
import webbrowser

wn = tk.Tk()
wn.title('Histdat by Alexandros Giannakis') # Πρόγραμμα από τον Αλέξανδρο Γιαννάκη
wn.geometry("570x250")

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

authors = [['ΟΜΗΡΟΣ'], ['ΗΣΙΟΔΟΣ'], ['ΗΡΟΔΟΤΟΣ'], ['ΘΟΥΚΥΔΙΔΗΣ'], ['ΞΕΝΟΦΩΝ', 'ΞΕΝΟΦΩΝΤΑΣ'], ['ΠΛΑΤΩΝ', 'ΠΛΑΤΩΝΑΣ'], ['ΑΡΙΣΤΟΤΕΛΗΣ'], ['ΛΥΣΙΑΣ'], ['ΔΗΜΟΣΘΕΝΗΣ'], ['ΑΙΣΧΥΛΟΣ'], ['ΣΟΦΟΚΛΗΣ'], ['ΕΥΡΙΠΙΔΗΣ'], ['ΑΙΣΧΙΝΗΣ'], ['ΑΡΙΣΤΟΦΑΝΗΣ'], ['ΑΡΡΙΑΝΟΣ'], ['ΒΑΚΧΥΛΙΔΗΣ'], ['ΒΙΩΝ'], ['ΓΟΡΓΙΑΣ'], ['ΘΕΟΚΡΙΤΟΣ'], ['ΘΕΟΦΡΑΣΤΟΣ'], ['ΙΣΟΚΡΑΤΗΣ'], ['ΠΛΟΥΤΑΡΧΟΣ'], ['ΠΙΝΔΑΡΟΣ'], ['ΜΟΣΧΟΣ'], ['ΚΑΛΛΙΜΑΧΟΣ'], ['ΛΟΥΚΙΑΝΟΣ'], ['ΑΝΤΙΦΩΝ', 'ΑΝΤΙΦΩΝ ΡΗΤΩΡ'], ['ΛΟΓΓΟΣ']]
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
more_urls = [[],
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

def get_search(event=None):
    author = search_textbox.get()
    for i in range(len(authors)):
        if make_clear(author) in authors[i]:
            webbrowser.open(greek_language_urls[i])
            webbrowser.open(perseus_urls[i])
            for mu in more_urls[i]:
                webbrowser.open(mu)
            time.sleep(1)

def greek_words():
    wn.configure(bg="dark orange")
    canvas.grid(row=2, column=1, columnspan=4)           
    canvas.create_image(20,20, anchor=tk.NW, image=bg)
    search_textbox.grid(row=0, column=2, sticky=tk.W+tk.E)
    search_button.grid(row=0, column=3, sticky=tk.W+tk.E)
   
bg = tk.PhotoImage(file = "greek_authors_img.png")
canvas = tk.Canvas(wn, width = 500, height = 200, bg='dark orange', highlightthickness=0)
search_textbox = tk.Entry(wn, width=50)
search_textbox.bind('<Return>', get_search)
search_button = tk.Button(wn, text="Αναζήτηση", command=get_search)
greek_authors()
wn.mainloop()
