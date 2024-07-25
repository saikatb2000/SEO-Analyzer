# Libraries
from bs4 import BeautifulSoup
import pandas as pd
import requests
import nltk
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
import streamlit as st
nltk.download('stopwords')
nltk.download('punkt')

st.title("SEO Analyzer")
st.write("By Saikat Bhattacharjee")
url = st.text_input("Enter URL")


# Add a slider for the number of keywords and bigrams
num_keywords = st.slider("Number of Keywords", 1, 50, 10)
num_bigrams = st.slider("Number of BiGrams", 1, 50, 10)

# Warnings, Title, Meta Description, Headings, Image Alt, Keywords
def seo_analysis(url):
    # send a request to get the url content
    response = requests.get(url)
    # Check the response status code
    if response.status_code != 200:
        st.error('Error: Unable to access the website')
        return
    # parse the html of the url content using Beautiful Soup
    soup = BeautifulSoup(response.text, 'html.parser')
    # create lists to store values
    bad = []
    good = []
    keywords = []

    # Title
    title = soup.find('title')
    if title:
        good.append(f"Title Exists: {title.text}")
    else:
        bad.append("No Title!")

    # Meta
    meta_d = soup.find('meta', attrs={'name': 'description'})
    if meta_d and 'content' in meta_d.attrs:
        good.append(f"Meta Description Exists: {meta_d['content']}")
    else:
        bad.append("No Meta Description!")

    # Headings
    hs = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
    h_tags = []
    for h in soup.find_all(hs):
        good.append(f"{h.name}--->{h.text.strip()}")
        h_tags.append(h.name)

    if 'h1' not in h_tags:
        bad.append("No H1 found!")

    # Image Alt
    for i in soup.find_all('img'):
        if not i.get('alt'):
            bad.append(f"No Alt: {i}")

    # Grab the keywords
    bod = soup.find('body').text
    words = [i.lower() for i in word_tokenize(bod)]

    # Extract the bigrams from the tokens
    bi_grams = ngrams(words, 2)
    freq_bigrams = nltk.FreqDist(bi_grams)
    bi_grams_freq = freq_bigrams.most_common(num_bigrams)

    # Find the list of Stopwords
    sw = nltk.corpus.stopwords.words('english')
    new_word = []
    for i in words:
        if i not in sw and i.isalpha():
            new_word.append(i)

    # Extract the frequency of the words and get the 10 most common ones
    freq = nltk.FreqDist(new_word)
    keywords = freq.most_common(num_keywords)

    # Print the results
    tab1, tab2, tab3, tab4 = st.tabs(['Keywords', 'BiGrams', 'Good', 'Bad'])
    with tab1:
        for i in keywords:
            st.text(i)
    with tab2:
        for i in bi_grams_freq:
            st.text(i)
    with tab3:
        for i in good:
            st.success(i)
    with tab4:
       for i in bad:
            st.error(i)

# Call the Function
if url:
    seo_analysis(url)


st.divider()

st.markdown('''
    <html>
        <h3>About SEO Analyzer</h13>
        <br>
        <h4>Keywords</h4>
        <ul>
            <li> The maximum repetition of words on a website. </li>
            <li>Also, provide how many times each word repeats.</li>
        </ul>
        <br>
        <h4>Bigrams</h4>
        <p> A bigram is a sequence of two adjacent words. For example, in the sentence "I love ice cream," the bigrams are "I love," "love ice," and "ice cream."</p>
        <ul>
            <li>The maximum repetition of words on a website. </li>
            <li>Also, provide how many times each word repeats.</li>
        </ul>
        <br>
        <h4>Good</h4>
        <p>This section provides information related to the title, meta tags, headings, alt text in images, and more.</p>
        <br>
        <h4>Bad</h4>
        <p>Show missing info related to the title, meta tags, headings, and alt text in images.</p>
    </html>''', unsafe_allow_html=True)