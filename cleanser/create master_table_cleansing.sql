create table master_table_cleansing as(
SELECT 
        m.master_id,
            delivery,
            COUNT(*) cnt,
            MIN(date) min_date,
            MAX(date) max_date,
            r.drama_id,
            m.naver_id
    FROM
        tv.tv_rating r, master_table m
    WHERE
        (r.drama_id = m.rate_id)
		AND r.area = 'capital'
        #capital -> 159
        #terrestrial -> 149
    GROUP BY 1
    #HAVING COUNT(*) >= 10 AND COUNT(*) < 61
    #선택사항임 159 -> 116개로 줄어듬, 데이터는 좋아짐
);