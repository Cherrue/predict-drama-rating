# cleansing video_list

# ver. test
CREATE TABLE tvcast_video_list_re (
SELECT 
    d.drama_id,d.title, v.video_id
FROM
    (select ori.drama_id,ori.video_id from tv.tvcast_video_list as ori,(SELECT drama_id,count(*) cnt FROM tv.tvcast_video_list
group by drama_id having cnt>=98 and cnt<=595) as re
where ori.drama_id=re.drama_id) AS v,
	tv.tvcast_drama_list AS d
WHERE
    d.drama_id = v.drama_id
        AND d.title NOT LIKE '%웹%');

# ver. pre
create table tvcast_video_list_re2 (SELECT d.drama_id,v.video_id FROM tv.tvcast_video_list as v,tvcast_drama_list as d
where d.drama_id = v.drama_id AND d.drama_id != 617 AND d.drama_id != 574 AND d.drama_id != 417 AND d.title not like '%웹%');