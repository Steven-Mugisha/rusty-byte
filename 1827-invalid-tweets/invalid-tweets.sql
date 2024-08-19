-- Write your PostgreSQL query statement below
SELECt tweet_id FROM Tweets WHERE LENGTH(content) > 15;