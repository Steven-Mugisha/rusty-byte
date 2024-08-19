# Write your MySQL query statement below
# check where author_id == viewer_id
# return dinstict tuples and sort in asce
# the name of the out should be rename to id

SELECT DISTINCT(viewer_id) AS id
FROM Views WHERE author_id = viewer_id
ORDER BY id ASC;



