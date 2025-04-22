# Meta Scraper (Python)

A simple Docker-powered Python tool to extract website metadata and Open Graph info from a list of URLs.

## 🔍 Features

- Extracts:
  - `<title>`, `<meta name="description">`, `<h1>`
  - `<link rel="canonical">`
  - Open Graph tags: `og:title`, `og:description`, `og:image`
  - HTTP status codes and broken link flags
- Outputs to `result.csv`
- Docker-ready for easy setup

## 🛠 How to Use

### 1. Prepare a `urls.txt` file
Each line should contain one URL:
https://www.example.com
https://www.example.net


### 2. Build and run with Docker
```bash
docker build -t meta-scraper .
docker run --rm -v $PWD:/app meta-scraper

The output file result.csv will appear in the same folder.

MIT (free to use and modify)
