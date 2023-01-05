import wikipedia
import warnings
warnings.filterwarnings('ignore')
wikipedia.set_lang('el')

def get_data(text):
    lst = []
    for result in wikipedia.search(text):
        try:
            res = wikipedia.summary(result, sentences=5)
            lst.append([result, res])
        except:
            pass
    return lst

if __name__ == '__main__':
    while True:
        a = input('>:')
        print('Collecting data...')
        for data in get_data(a):
            print('============================= ' + data[0] + ' =============================')
            print(data[1])
