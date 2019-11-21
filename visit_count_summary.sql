/* 
Following script is written using MS SQL standard
This website can be used for testing if MS SQL is not available
http://sqlfiddle.com 
*/

-- DDL --
CREATE TABLE input_table
    ([Id] int, [Home_Page] int, [Product_Page] int, [Warranty_Page] int)
;

INSERT INTO input_table
    (Id, Home_Page, Product_Page, Warranty_Page)
VALUES
    (1,1,1,1),
    (2,1,1,0),
    (3,1,0,1),
    (4,1,0,0),
    (5,0,1,1),
    (6,0,1,0),
    (7,0,0,1),
    (8,0,0,0)
;

-- Query --
/*
UNPIVOT function turns each column specified into a row.
Then GROUP BY clause is used to summarize visit count for 
each type of page.
*/
SELECT  page, sum(visit_count) AS counts
FROM    input_table
        UNPIVOT (
            visit_count FOR page IN (Home_Page, Product_Page, Warranty_Page)
        ) AS unpvt
GROUP BY page
;

