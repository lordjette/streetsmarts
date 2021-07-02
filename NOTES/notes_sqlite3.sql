INSERT INTO post(title, date_posted, content, user_id)  
SELECT 
	Title as title,
	CASE 
		WHEN publicationdate = '' THEN '2020' || '-07-31 09:34:40'
		ELSE publicationdate || '-07-31 09:34:40'
	END AS date_posted,
	CASE 
		WHEN Summary = '' THEN 'No Description'
		ELSE Summary
	END AS content,
	5 AS  user_id
 FROM lookup_rice

-- || concat