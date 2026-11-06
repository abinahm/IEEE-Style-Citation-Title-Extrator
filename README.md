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

### Results (single curator, estimated hours)

| Period | Workflow | Hours | Publications reviewed | Pubs/hour | Min/pub | Speedup vs. manual |
|---|---|---|---|---|---|---|
| Spring 2025 | Manual | 180 | 119 | 0.66 | 90.8 | 1x |
| Summer 2025 | Script (all-in, incl. development time) | 408 | 6,190 | 15.2 | 3.9 | 23x |
| Fall 2025 | Script | 180 | 17,503 | 97.2 | 0.6 | 147x |
| Spring 2026 | Script | 180 | 4,161 | 23.1 | 2.6 | 35x |
| **Script-era pooled (excl. Fall 2025)** | Script | 588 | 10,351 | **17.6** | 3.4 | **~27x** |

Fall 2025 is excluded from the headline figure because it accounts for about 63% of
all publications handled and likely reflects a few very large profiles.

### Limitations

- The manual baseline (Spring 2025) was my first semester, so it includes
  training time and likely understates my steady-state manual speed.
- Publication count depends on profile size, not only effort. Hours are estimated
  from average weekly schedule, not time-tracked.
- Figures describe one curator's throughput. A team-wide time-savings estimate
  requires a timed comparison of manual vs. scripted title transfer (see below).


