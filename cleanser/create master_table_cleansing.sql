# ver. test
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
        #capital -> 159, 4382 row
        #terrestrial -> 149, 4478 row
    GROUP BY 1
    #HAVING COUNT(*) >= 10 AND COUNT(*) < 61
    #선택사항임 159 -> 116개로 줄어듬, 데이터는 좋아짐
);

# ver. pre
create table master_table_cleansing(
#data cleansing
select ma.master_id,ma.drama_id tvrating_id,ma.tvcast_id,ma.delivery,ma.cnt episode,ma.max_date max_broad_date,ma.min_date min_broad_date,ca.max_date max_video_date,ca.min_date min_video_date from 
(#tvrating : 103
SELECT m.master_id,delivery,count(*) cnt,min(date) min_date,max(date) max_date,r.drama_id,m.tvcast_id FROM tv.tv_rating r,master_table_re m
where (r.drama_id = m.tvrating_id) AND r.area='nationwide'
group by 1 having count(*)>10 AND count(*)<61
) as ma,
(#tvcast : 661
SELECT drama_id,min(update_date) min_date,max(update_date) max_date FROM tv.tvcast_video_list as v, tv.tvcast_video_solid_data as s
where v.video_id=s.video_id
group by drama_id
) as ca
where ma.tvcast_id=ca.drama_id  AND ma.max_date > ca.min_date);