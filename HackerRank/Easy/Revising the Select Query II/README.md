# Revising the Select Query II

**Difficulty:** Easy  
**Topics:** N/A  
**HackerRank URL:** [Revising the Select Query II](https://www.hackerrank.com/challenges/revising-the-select-query-2/problem)

## Problem Description

Query the **NAME** field for all American cities in the **CITY** table with populations larger than `120000`. The *CountryCode* for America is `USA`.

The **CITY** table is described as follows:

![CITY.jpg](https://s3.amazonaws.com/hr-challenge-images/8137/1449729804-f21d187d0f-CITY.jpg)

## Examples



## Constraints



## Solution

```mysql
-- HackerRank Problem: Revising the Select Query II
-- Link: https://www.hackerrank.com/challenges/revising-the-select-query-2/problem
-- Difficulty: Easy
-- Language: mysql

SELECT NAME
FROM CITY
WHERE POPULATION>120000 AND COUNTRYCODE='USA';
```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
