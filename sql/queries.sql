-- 1. Total funds
SELECT COUNT(*) FROM fact_performance;

-- 2. Top 5 funds by AUM
SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- 3. Average NAV
SELECT AVG(nav)
FROM fact_nav;

-- 4. Maximum NAV
SELECT MAX(nav)
FROM fact_nav;

-- 5. Minimum NAV
SELECT MIN(nav)
FROM fact_nav;

-- 6. Transaction count
SELECT COUNT(*)
FROM fact_transactions;

-- 7. Total transaction amount
SELECT SUM(amount_inr)
FROM fact_transactions;

-- 8. Transactions by type
SELECT transaction_type, COUNT(*)
FROM fact_transactions
GROUP BY transaction_type;

-- 9. Investors by state
SELECT state, COUNT(*)
FROM fact_transactions
GROUP BY state;

-- 10. Funds with expense ratio below 1%
SELECT scheme_name, expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;