-- HackerRank Problem: Revising the Select Query I
-- Link: https://www.hackerrank.com/challenges/revising-the-select-query/problem
-- Difficulty: Easy
-- Language: mysql

select * 
from city
where population >100000 and countrycode='USA';