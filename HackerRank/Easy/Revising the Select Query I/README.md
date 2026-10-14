# Revising the Select Query I

**Difficulty:** Easy  
**Topics:** N/A  
**HackerRank URL:** [Revising the Select Query I](https://www.hackerrank.com/challenges/revising-the-select-query/problem)

## Problem Description

Query all columns for all American cities in the **CITY** table with populations larger than `100000`. The **CountryCode** for America is `USA`.

The **CITY** table is described as follows:

![CITY.jpg](https://s3.amazonaws.com/hr-challenge-images/8137/1449729804-f21d187d0f-CITY.jpg)

## Examples



## Constraints



## Solution

```mysql
-- HackerRank Problem: Revising the Select Query I
-- Link: https://www.hackerrank.com/challenges/revising-the-select-query/problem
-- Difficulty: Easy
-- Language: mysql

select * 
from city
where population >100000 and countrycode='USA';
```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
