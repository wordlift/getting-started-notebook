```markdown
# WordLift Getting Started Notebook (DEPRECATED)

This repository has been deprecated. Please use the newer KG Build Notebook Template instead:

https://github.com/wordlift/kg-build-notebook-template/blob/74b8cb4bf9985d9e8e250791b31698a7bdaf817e/README.md

This project remains available for reference, but it will not receive further updates. The KG Build Notebook Template is the maintained, recommended starting point for importing web pages into a WordLift knowledge graph using the WordLift Python SDK.

## Quick migration notes

- The replacement repository uses a minimal, notebook-driven workflow and provides improved configuration and tooling.
- Key files to look for in the new template:
  - `kg_import.ipynb` — the primary notebook for importing pages
  - `config/default.py` — configuration pattern for sitemap and credentials
  - `app/overrides/web_page_import_protocol.py` — example callback to customize import handling
- Follow the new repo's Quick start and Prerequisites sections to set up your environment.

## Original README (kept for reference)

A Jupyter notebook to jumpstart a Knowledge Graph with WordLift by providing an XML sitemap and a WordLift Key.

Overview
- Import web pages from a sitemap into a Knowledge Graph
- Enrich entities with additional properties (like keywords)
- Query the Knowledge Graph to retrieve entity data

Prerequisites
- Python 3.12
- A WordLift Key
- An XML sitemap URL

Installation
- Using Poetry (recommended)
  ```bash
  # Install dependencies
  poetry install
  ```

Configuration
Configure the notebook using one of these methods:

1. Create a file `config/default.py` with:
   ```python
   WORDLIFT_KEY = "your-wordlift-key"
   SITEMAP_URL = "https://example.com/sitemap.xml"
   OUTPUT_TYPE = "http://schema.org/WebPage"  # Optional
   ```

2. When using Google Colab, set `WORDLIFT_KEY` in Google Colab Secrets

Usage
1. Open the notebook in Jupyter:
   ```bash
   jupyter notebook getting_started_notebook.ipynb
   ```

2. Run all cells to:
   - Import URLs from your sitemap
   - Enrich entities with keywords
   - Query and display the resulting Knowledge Graph

Customization
The notebook provides two customizable callbacks:
- `import_url`: Controls how URLs are imported into the Graph
- `parse_html`: Extracts additional properties from web pages

License
Apache-2.0
```
