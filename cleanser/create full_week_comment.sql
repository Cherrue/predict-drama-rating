# ver. pre
CREATE TABLE pre_full_week_comment AS (SELECT vdl.master_id,
    vdl.tvrating_id,
    vdl.tvcast_id,
    vdl.delivery,
    vdl.min_broad_date,
    ct.*,
    DATEDIFF(ct.upload_date, vdl.min_broad_date) FROM
    (SELECT 
        mtc.*, tvv.video_id
    FROM
        (SELECT 
        master_id, drama_id, naver_id, delivery, min_date
    FROM
        tv.master_table_cleansing) AS mtc, tv.tvcast_video_list_re AS tvv
    WHERE
        mtc.tvcast_id = tvv.drama_id) AS vdl,
    tv.tvcast_comment_list_re AS ct
WHERE
    vdl.video_id = ct.video_id);
# and ((vdl.min_broad_date+7)>=ps.upload_date and ps.upload_date>=vdl.min_broad_date);


# ver. new
CREATE TABLE full_week_comment AS (
SELECT vdl.master_id,
    vdl.drama_id,
    vdl.naver_id,
    vdl.delivery,
    vdl.min_date,
    ct.video_id,
    ct.writter,
    ct.comment,
    ct.upload_date,
    ct.good,
    ct.bad,
    DATEDIFF(ct.upload_date, vdl.min_date) FROM
    (SELECT 
        mtc.*, tvv.video_id
    FROM
        (SELECT 
        master_id, drama_id, naver_id, delivery, min_date
    FROM
        tv.master_table_cleansing) AS mtc, tv.tvcast_video_list_re AS tvv
    WHERE
        mtc.naver_id = tvv.drama_id) AS vdl,
	# tv.tvcast_comment_list as ct
    tv.tvcast_comment_list AS ct
WHERE
    vdl.video_id = ct.video_id);