# NIBSS Reconciliation Tool

**Automated tool to reconcile NIBSS settlement reports with internal transaction records.**

### What it does
- Compares NIBSS settlement file vs your company's internal ledger
- Automatically flags unmatched transactions and amount mismatches
- Generates a clear discrepancy report with total variance
- Exactly the same process I used to identify and resolve a **₦1.2 million** NIBSS system error

### Why this matters for Revenue Assurance
This tool automates one of the most critical daily tasks in Nigerian microfinance banks and fintech companies — NIBSS reconciliation and settlement error detection.

### How to use
1. Install dependencies: `pip install pandas openpyxl`
2. Place your NIBSS report and internal transaction files in the folder
3. Run: `python nibss_reconciliation_tool.py`

### Technologies
- Python
- Pandas (for data analysis)

Built by **Ezeoka Godwill Ebuka** — Revenue Assurance Specialist (6+ years)
