from pydantic import BaseModel, Field
from typing import List, Optional

class LedgerEntry(BaseModel):
    date: Optional[str] = Field(None, description="Date of the transaction")
    particulars: str = Field(..., description="Account head / Particulars (e.g., 'To Sales A/c')")
    lf: Optional[str] = Field(None, description="Ledger Folio number")
    amount: float = Field(..., description="Transaction amount extracted from the sheet")

class AccountLedger(BaseModel):
    account_name: str = Field(..., description="Name of the Ledger Account")
    debit_entries: List[LedgerEntry] = Field(default_factory=list, description="All entries on the Dr. side")
    credit_entries: List[LedgerEntry] = Field(default_factory=list, description="All entries on the Cr. side")
    debit_total: float = Field(..., description="Calculated total of the debit column")
    credit_total: float = Field(..., description="Calculated total of the credit column")
    balancing_figure: Optional[float] = Field(None, description="Extracted balancing figure (c/d or b/d)")
    
    # Uncertainty flag for Gemini to trigger human review
    extraction_confidence: float = Field(..., description="Confidence score of the OCR/Vision extraction (0.0 to 1.0)")
    needs_human_review: bool = Field(default=False, description="Flagged true if handwriting is illegible")
