Order by will apply on entire data set.(global sorting in ascending or descening order)
Sort by (if table does not have multiple partitions then its same as Order By. means if it is having single partition then it will do global sorting)
If table is having multiple partitions. then sort by will do partition wise sorting. and its not a global sorting. local sorting.(partition wise sorting)

`select /*+ REPARTITION(3,zip_code) */ * from person order by age ;`

`select /*+ REPARTITION(3,zip_code) */ * from person sort by age ;`
