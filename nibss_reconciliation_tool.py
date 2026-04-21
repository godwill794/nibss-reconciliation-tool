import pandas as pd

def nibss_reconciliation(nibss_file: str, internal_file: str, output_file: str = "nibss_reconciliation_report.csv"):
    """
    Reconciles NIBSS settlement report against internal transaction records.
    Flags unmatched transactions and amount differences.
    """
    # Load files (supports CSV or Excel)
    nibss = pd.read_csv(nibss_file) if nibss_file.endswith('.csv') else pd.read_excel(nibss_file)
    internal = pd.read_csv(internal_file) if internal_file.endswith('.csv') else pd.read_excel(internal_file)
    
    # Standardize column names
    nibss.columns = nibss.columns.str.strip().str.lower()
    internal.columns = internal.columns.str.strip().str.lower()
    
    # Merge on common transaction reference (change 'reference' or 'transaction_id' to match your files)
    merged = pd.merge(nibss, internal, on='reference', how='outer', suffixes=('_nibss', '_internal'))
    
    # Calculate differences
    merged['amount_difference'] = merged.get('amount_nibss', 0) - merged.get('amount_internal', 0)
    
    # Flag mismatches
    discrepancies = merged[
        (merged['amount_difference'] != 0) | 
        merged['reference'].isna() | 
        merged['reference'].isnull()
    ].copy()
    
    # Save detailed report
    discrepancies.to_csv(output_file, index=False)
    
    total_variance = discrepancies['amount_difference'].abs().sum()
    
    print(f"✅ NIBSS Reconciliation Complete!")
    print(f"📊 Total transactions analyzed: {len(merged)}")
    print(f"⚠️  Discrepancies found: {len(discrepancies)}")
    print(f"💰 Total potential revenue impact / variance: ₦{total_variance:,.2f}")
    print(f"📄 Full report saved as {output_file}")
    
    return discrepancies

# Example usage (uncomment to test)
# nibss_reconciliation("nibss_settlement_report.csv", "internal_transactions.csv")
