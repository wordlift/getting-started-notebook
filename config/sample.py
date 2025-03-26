# The sitemap.xml must contain `loc` items pointing to webpages URLs, not other sitemaps.
import os

SITEMAP_URL = "https://example.org/sitemap.xml"
WORDLIFT_KEY = os.getenv('WORDLIFT_KEY')
OUTPUT_TYPE = "http://schema.org/WebPage"
URL = []
