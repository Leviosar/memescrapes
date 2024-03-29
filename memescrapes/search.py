from bs4 import BeautifulSoup
import requests

HEADERS = {'User-Agent': ('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 '
        '(KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36')}

def search_meme(text):
    """Return a meme name and url from a meme keywords."""
    r = requests.get('http://knowyourmeme.com/search?q=%s' % text, headers=HEADERS)
    soup = BeautifulSoup(r.text, 'html.parser')
    memes_list = soup.find(class_='entry_list')
    if memes_list:
        meme_path = memes_list.find('a', href=True)['href']
        return meme_path.replace('-', ' '), 'https://knowyourmeme.com%s' % meme_path
    return None, None

def search(text):
    """Return a meme definition from a meme keywords."""
    meme_name, url = search_meme(text)
    if meme_name:
        r = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(r.text, 'html.parser')
        entry = soup.find('h2', {'id': 'about'})
        return '%s. %s' % (meme_name.split('/')[-1].title(), entry.next.next.next.text)

def search_image(text):
    """Return a meme definition from a meme keywords."""
    meme_name, url = search_meme(text)
    if meme_name:
        r = requests.get(url, headers=HEADERS)
        soup = BeautifulSoup(r.text, 'html.parser')
        entry = soup.find('a', {'class': 'photo'})
        img = entry.find('img')
        return img['src']
