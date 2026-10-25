# Weather Observation Station 13

**Difficulty:** Easy  
**Topics:** N/A  
**HackerRank URL:** [Weather Observation Station 13](https://www.hackerrank.com/challenges/weather-observation-station-13/problem)

## Problem Description

Query the sum of *Northern Latitudes* (*LAT_N*) from **STATION** having values greater than  and less than . Truncate your answer to  decimal places.

**Input Format**

The **STATION** table is described as follows:

*

where LAT_N* is the northern latitude and *LONG_W* is the western longitude.

## Examples



## Constraints



## Solution

```mysql
-- HackerRank Problem: Weather Observation Station 13
-- Link: https://www.hackerrank.com/challenges/weather-observation-station-13/problem
-- Difficulty: Easy
-- Language: mysql

/*
Enter your query here.
*/
SELECT TRUNCATE(SUM(LAT_N), 4)
FROM STATION
WHERE LAT_N > 38.7880
  AND LAT_N < 137.2345;

```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
