-- 코드를 입력하세요
SELECT fh.flavor
FROM first_half as fh
INNER JOIN icecream_info as ii
ON fh.flavor = ii.flavor
WHERE total_order > 3000 AND ingredient_type = 'fruit_based'