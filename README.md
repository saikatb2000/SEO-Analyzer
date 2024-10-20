# SEO Analyzer

## Overview
**SEO Analyzer** is a web application that performs a basic SEO audit of any website. It provides key insights into the site's SEO elements such as title, meta description, headings, image alt attributes, keyword frequency, and bigram analysis. Built using `Streamlit`, it offers a simple and intuitive user interface for users to input a URL and view SEO-related information.

## Features
- **Title and Meta Description Check**: Identifies if a webpage contains a title and meta description.
- **Headings**: Analyzes heading tags (H1-H6) present on the page.
- **Image Alt Attributes**: Detects missing alt attributes in images.
- **Keyword Frequency**: Displays the most frequent keywords used on the webpage.
- **Bigrams**: Displays the most common bigrams (pairs of adjacent words) found on the webpage.
- **User-Friendly Interface**: Built with Streamlit, allowing users to input a URL and visualize results across multiple tabs easily.

## Libraries Used
- `bs4` (BeautifulSoup): For parsing HTML content.
- `pandas`: For data manipulation (although not yet used in the current script).
- `requests`: To send HTTP requests and fetch website content.
- `nltk`: For natural language processing tasks such as tokenization and bigram extraction.
- `streamlit`: For building the web interface.

## Functionality
- Input URL: Users can input a website URL for analysis.
- SEO Checks:
    - Title and Meta Description: Checks if the page has a title and meta description and displays their content.
    - Headings: Analyzes the presence of H1 to H6 tags.
    - Image Alt Attributes: Lists images without alt text.
    - Keyword and Bigram Analysis:

- Keywords: Shows the most frequent words on the page, excluding stop words.
- Bigrams: Displays common bigrams (two-word sequences) found on the page.
- Warnings and Suggestions:
  - Good: Displays SEO elements that are properly implemented.
  - Bad: Lists missing or improperly configured SEO elements (e.g., missing titles or alt text in images).

## Installation

To install the necessary libraries, you can use the following commands:

```bash
pip install beautifulsoup4 pandas requests nltk streamlit



