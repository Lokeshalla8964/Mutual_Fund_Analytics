# Data Dictionary

## fact_nav
- amfi_code : Mutual fund identifier
- date : NAV date
- nav : Net Asset Value

## fact_transactions
- investor_id : Investor ID
- transaction_date : Date of transaction
- amfi_code : Fund code
- transaction_type : SIP / Lumpsum / Redemption
- amount_inr : Transaction amount
- state : Investor state
- city : Investor city
- city_tier : Tier classification
- age_group : Investor age group
- gender : Gender
- annual_income_lakh : Annual income
- payment_mode : Payment mode
- kyc_status : KYC status

## fact_performance
- scheme_name : Mutual fund name
- return_1yr_pct : One year return
- return_3yr_pct : Three year return
- return_5yr_pct : Five year return
- expense_ratio_pct : Expense ratio
- aum_crore : Assets under management
- risk_grade : Risk category