SELECT 
    master_id,
    tvrating_id,
    delivery,
    min_broad_date,
    min_diff_cmt,
    FLOOR(min_diff_cmt / 7),
    COUNT(*)
FROM
    tv.full_week_comment AS wc
GROUP BY master_id , min_diff_cmt;