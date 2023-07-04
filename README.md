## bank2table
*Project skeleton - Currently work in progress...*

Convert text from PDF bank statements into data.  
**Note:** Only text-based PDFs, not graphic document images (e.g. scanned).

(c) 2023. This project is licensed under the terms of the MIT License.

## Description
Electronic bank statements, for example when downloaded from a bank's online banking site, are usually provided as text-based PDF files.
Although the PDF statement will be visually accurate, it can be difficult and laborious to extract the details in a workable format.
Most of the time, Copy&Paste just won't do.

This tool reads one or more bank statement PDF files and converts the transactional contents into a single flat data table (Excel, comma/tab delimited, etc.) for further processing, for example bank reconciliation of the accounts ledger.

### Output Table Columns
- **Global Details**
  - Path and filename of PDF statement file
  - Statement main bank account number/ID
  - Statement date
  - Statement number/ID (if provided)
- **Transaction Line Items**
  - Sub-account ID (current/checking account, credit/debit card, investment account, etc.)
  - Transaction (voucher) date
  - Bank processing (reconciliation) date
  - Transaction type (transfer, cheque, ATM, etc.)
  - Debit amount (payments, out-flows)
  - Credit amount (receipts, in-flows)
    or
  - Combined debit (negative)/credit (positive) amount
  - Details 1 (usually 3rd party, payee, origininator, etc. - can be multiple lines)
  - Details 2 (usually details of transaction and reference(s) - can be multiple lines)
  - Running balance (if provided)  

**Note:** Global and line items appear on the same line. That means that each transaction line will repeat its global details, i.e. not "normalized".

## Development

### Functionality:
- Process PDF statement file and extract data
- Analyse and parse entries
- Append data to sheet(s)/table(s) and update state in catalog
- Interact through simple graphical user interface (GUI) forms

### Future:
- Automatically check/monitor availability of new statement(s)
- Connect to online bank account and collect PDF file, apply renaming rules and save locally
- Normalized global and line items in separate tables

