# IEEE Style Citation Title Extractor

Extracts titles from IEEE-style citations, or from any citations where the title appears in quotation marks.

## Background

I originally wrote this to pull titles out of CVs so I could cross-check them against another system and an Excel sheet. It's been used mostly for **data validation** rather than scraping (scraping support is in the works).

## Usage

1. Create a text file named `references.txt` in the same folder as the script.
2. Copy the citation section of the CV into Copilot and ask it to reformat the citations into IEEE style (the script works best with this style).
3. Paste the output into `references.txt`.
4. Run the script: python Extractor.py

## Example

**Input (`references.txt`):**
[1] J. Smith and A. Lee, "Deep learning for image recognition," IEEE Trans. Pattern Anal., vol. 5, no. 2, pp. 10-20, 2020.

**Output:**
Deep learning for image recognition


## Tip

If you don't want to set up anything locally, [OnlineGDB](https://www.onlinegdb.com/) works well. It shows all your files in one place, which makes it easy to run the script alongside `references.txt`.

## Planned improvements

- Web scraping support
- Export titles directly to Excel/CSV

Have fun!
