# Weather Observation Station 4

**Difficulty:** Easy  
**Topics:** N/A  
**HackerRank URL:** [Weather Observation Station 4](https://www.hackerrank.com/challenges/weather-observation-station-4/problem)

## Problem Description

Find the difference between the total number of **CITY** entries in the table and the number of distinct **CITY** entries in the table. **
The STATION** table is described as follows:

![](https://s3.amazonaws.com/hr-challenge-images/9336/1449345840-5f0a551030-Station.jpg)

where **LAT_N** is the northern latitude and **LONG_W** is the western longitude.

For example, if there are three records in the table with **CITY** values 'New York', 'New York', 'Bengalaru', there are 2 different city names: 'New York' and 'Bengalaru'.  The query returns , because .

## Examples



## Constraints



## Solution

```db2
// HackerRank Problem: Weather Observation Station 4
// Link: https://www.hackerrank.com/challenges/weather-observation-station-4/problem
// Difficulty: Easy
// Language: db2


SELECT COUNT(CITY)- COUNT(DISTINCT CITY)
FROM STATION;

```

---
<div align="center">

**🔄 Synced with [CommitSync](https://www.google.com/search?q=CommitSync+extension)**

*Automatically organized and synced by CommitSync.*

</div>
