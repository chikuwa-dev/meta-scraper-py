import requests
from bs4 import BeautifulSoup
import csv

def fetch_meta(url):
    try:
        response = requests.get(url, timeout=10)
        status_code = response.status_code
        broken = "No" if status_code == 200 else "Yes"

        if status_code != 200:
            return [url, "", "", "", "", "", "", "", "", status_code, broken]

        soup = BeautifulSoup(response.text, 'html.parser')

        # 通常のMeta情報
        title = soup.title.string.strip() if soup.title else ''

        description = ''
        desc_tag = soup.find('meta', attrs={'name': 'description'})
        if desc_tag and 'content' in desc_tag.attrs:
            description = desc_tag['content'].strip()

        h1 = soup.find('h1').get_text(strip=True) if soup.find('h1') else ''

        # canonical
        canonical = ''
        canonical_tag = soup.find('link', attrs={'rel': 'canonical'})
        if canonical_tag and 'href' in canonical_tag.attrs:
            canonical = canonical_tag['href'].strip()

        # Open Graph
        og_title = ''
        og_desc = ''
        og_image = ''
        og_title_tag = soup.find('meta', attrs={'property': 'og:title'})
        og_desc_tag = soup.find('meta', attrs={'property': 'og:description'})
        og_image_tag = soup.find('meta', attrs={'property': 'og:image'})

        if og_title_tag and 'content' in og_title_tag.attrs:
            og_title = og_title_tag['content'].strip()

        if og_desc_tag and 'content' in og_desc_tag.attrs:
            og_desc = og_desc_tag['content'].strip()

        if og_image_tag and 'content' in og_image_tag.attrs:
            og_image = og_image_tag['content'].strip()

        return [url, title, description, h1, canonical, og_title, og_desc, og_image, status_code, broken]
    
    except Exception as e:
        return [url, f"Error: {e}", "", "", "", "", "", "", "", "Error", "Yes"]

def main():
    input_file = 'urls.txt'
    output_file = 'result.csv'
    
    with open(input_file, 'r') as f:
        urls = [line.strip() for line in f if line.strip()]

    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([
            'URL', 'Title', 'Meta Description', 'H1',
            'Canonical', 'OG Title', 'OG Description', 'OG Image',
            'HTTP Status', 'Broken Link'
        ])

        for url in urls:
            print(f"Processing: {url}")
            row = fetch_meta(url)
            writer.writerow(row)

if __name__ == "__main__":
    main()
