# IEEE Style Citation Title Extractor

Extracts titles from IEEE-style citations, or from any citations where the title appears in quotation marks.

## Background

I originally wrote this to pull titles out of CVs so I could cross-check them against another system and an Excel sheet. It's been used mostly for **data validation** rather than scraping (scraping support is in the works).

## Usage

1. Create a text file named `references.txt` in the same folder as the script.
2. Copy the citation section of the CV into Copilot and ask it to reformat the citations into IEEE style (the script works best with this style).
3. Paste the output into `references.txt`.
4. Run the script: python main.py

## Example When Running Through Terminal
***Ensure all files are in the same directory***
python3 main.py references.txt

references.txt would contain something like:

[1] J. Smith and A. Lee, "Deep learning for image recognition," IEEE Trans. Pattern Anal., vol. 5, no. 2, pp. 10-20, 2020.

**Output:**
Deep learning for image recognition

This would be shown in a text file called TITLEONLY.txt

## Tip

If you don't want to set up anything locally, [OnlineGDB](https://www.onlinegdb.com/) works well. It shows all your files in one place, which makes it easy to run the script alongside `references.txt`.

## Planned improvements

- Web scraping support
- Export titles directly to Excel/CSV

Have fun!

## Impact: Workflow Speed Improvement

This tool extracts publication titles from IEEE-style citations in CVs and writes
them to an Excel sheet, replacing the manual copy/paste step used to hand out
curation assignments to student workers.

## Methodology

**Edits per hour = |Total After − Total Before| ÷ Hours worked**
**Speedup = median(script-era edits/hour) ÷ manual edits/hour**

| Period | Workflow | Edits | Hours | Edits/hour |
|---|---|---|---|---|
| Spring 2025 | Manual | 80 | 180 | 0.44 |
| Summer 2025 | Script | 2,042 | 408 | 5.0 |
| Fall 2025 | Script | 14,633 | 180 | 81.3 |
| Spring 2026 | Script | 1,275 | 180 | 7.1 |

**Result: ~16x speedup** (median 7.1 vs. 0.44 edits/hour).

### Limitations
- Hours are estimated from my average weekly schedule.
- The manual baseline was my first semester, so it includes training time.
- This is one person's throughput, not a team-wide measurement, but I was doing the title extraction for them (5 Student Workers)

