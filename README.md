# WordLift Getting Started Notebook

A Jupyter notebook to jumpstart a Knowledge Graph with WordLift by providing an XML sitemap and a WordLift Key.

## Overview

This notebook allows you to:
- Import web pages from a sitemap into a Knowledge Graph
- Enrich entities with additional properties (like keywords)
- Query the Knowledge Graph to retrieve entity data

## Prerequisites

- Python 3.12
- A [WordLift Key](https://wordlift.io)
- An XML sitemap URL

## Installation

### Using Poetry (recommended)

```bash
# Install dependencies
poetry install
```

## Configuration

Configure the notebook using one of these methods:

1. Create a file `config/default.py` with:
   ```python
   WORDLIFT_KEY = "your-wordlift-key"
   SITEMAP_URL = "https://example.com/sitemap.xml"
   OUTPUT_TYPE = "http://schema.org/WebPage"  # Optional
   ```

2. When using Google Colab, set `WORDLIFT_KEY` in Google Colab Secrets

## Usage

1. Open the notebook in Jupyter:
   ```bash
   jupyter notebook getting_started_notebook.ipynb
   ```

2. Run all cells to:
   - Import URLs from your sitemap
   - Enrich entities with keywords
   - Query and display the resulting Knowledge Graph

## Customization

The notebook provides two customizable callbacks:
- `import_url`: Controls how URLs are imported into the Graph
- `parse_html`: Extracts additional properties from web pages

## License

Apache-2.0