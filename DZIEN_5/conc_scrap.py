import concurrent.futures
import requests
from bs4 import BeautifulSoup


# Funkcja do pobierania treści strony
def fetch_url(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Sprawdza, czy żądanie zakończyło się błędem
        return response.text
    except requests.RequestException as e:
        print(f'Błąd pobierania {url}: {e}')
        return None


# Funkcja do parsowania treści strony
def parse_html(html):
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        title = soup.title.string if soup.title else 'Brak tytułu'
        return title
    return 'Brak treści'


# Lista URL-i do pobrania
urls = [
    'https://www.foxnews.com/',
    'https://edition.cnn.com/',
    'https://www.bbc.com/',
    'https://www.wp.pl/',
    'https://www.gov.pl/web/obrona-narodowa',
    'https://mil.ru/'
]


# Główna funkcja do uruchamiania równoległych zadań
def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as executor:
        # Uruchomienie pobierania URL-i równolegle
        future_to_url = {executor.submit(fetch_url, url): url for url in urls}

        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                html = future.result()
                title = parse_html(html)
                print(f'{url} - Tytuł: {title}')
            except Exception as e:
                print(f'Błąd przetwarzania {url}: {e}')


if __name__ == '__main__':
    main()
