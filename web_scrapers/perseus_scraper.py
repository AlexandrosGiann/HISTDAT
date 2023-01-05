import bs4
import requests

def get_results(text):
    html_text = requests.get('http://www.perseus.tufts.edu/hopper/searchresults?q=' + text).text
    soup = bs4.BeautifulSoup(html_text, 'html.parser')
    lst = []
    for element in soup.findAll('li'):
        element = str(element)
        while '<' in element:
            element = element.replace(element[element.find('<'):element.find('>') + 1], '')
        lst.append(element)
    return lst

if __name__ == '__main__':
    while True:
        a = input('>:')
        for result in get_results(a):
            print(result)

