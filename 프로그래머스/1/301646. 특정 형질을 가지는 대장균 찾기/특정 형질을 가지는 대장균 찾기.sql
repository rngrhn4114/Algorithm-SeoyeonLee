-- 코드를 작성해주세요
SELECT COUNT(*) AS COUNT
FROM ecoli_data
WHERE SUBSTRING(BIN(genotype), -2, 1) != '1'
AND (SUBSTRING(BIN(genotype), -1, 1) = '1' OR SUBSTRING(BIN(genotype), -3, 1) = '1')