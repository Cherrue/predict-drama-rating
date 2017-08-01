# cleansing video_list
CREATE TABLE tvcast_video_list_re2 (
SELECT 
    d.drama_id,d.title, v.video_id
FROM
    (select ori.drama_id,ori.video_id from tv.tvcast_video_list_pre as ori,(SELECT drama_id,count(*) cnt FROM tv.tvcast_video_list_pre
group by drama_id having cnt>=98 and cnt<=595) as re
where ori.drama_id=re.drama_id) AS v,
	tv.tvcast_drama_list_pre AS d
WHERE
    d.drama_id = v.drama_id
        AND d.title NOT LIKE '%웹%');