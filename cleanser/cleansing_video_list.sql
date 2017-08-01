SELECT 
    d.drama_id, d.title
FROM
    (SELECT 
        ori.drama_id, ori.video_id
    FROM
        tv.tvcast_video_list AS ori, (SELECT 
        drama_id, COUNT(*) cnt
    FROM
        tv.tvcast_video_list
    GROUP BY drama_id
    #HAVING cnt >= 98 AND cnt <= 595
    HAVING cnt >= 98 
    ) AS re
    WHERE
        ori.drama_id = re.drama_id) AS v,
    tv.tvcast_drama_list AS d
WHERE
    d.drama_id = v.drama_id
        AND d.title NOT LIKE '%웹%'
GROUP BY d.drama_id;
