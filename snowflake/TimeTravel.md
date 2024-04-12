TimeTravel:

Snowflake Time Travel enables accessing historical data (i.e. data that has been changed or deleted)
at any point within a defined period. It serves as a powerful tool for performing the following tasks:

1.Restoring data-related objects (tables, schemas, and databases) that might have been accidentally or intentionally deleted.

2.Duplicating and backing up data from key points in the past.

3.Analyzing data usage/manipulation over specified periods of time.




Using Time Travel, you can perform the following actions within a defined period of time:

1.Query data in the past that has since been updated or deleted.
2.Create clones of entire tables, schemas, and databases at or before specific points in the past.
3.Restore tables, schemas, and databases that have been dropped.

Once the defined period of time has elapsed, the data is moved into Snowflake Fail-safe and these actions can no longer be performed.

---------------------------------------------
Specifies the query ID of a statement to use as the reference point for Time Travel. 
This parameter supports any statement of one of the following types:
*DML (e.g. INSERT, UPDATE, DELETE)
*TCL (BEGIN, COMMIT transaction)
*SELECT

The query ID must reference a query that has been executed within the last 14 days. 
If the query ID references a query over 14 days old, the following error is returned:

Error: statement <query_id> not found
To work around this limitation, use the timestamp for the referenced query.
--------------------------------------------

select current_timestamp: --2023-09-28 22:48:40.209 -0700

select * from store before(TIMESTAMP => 2023-09-28 22:48:40.209 -0700 :: TIMESTAMP_LTZ):

select * from store aT (TIMESTAMP => 2023-09-28 22:48:40.209 -0700'::TIMESTAMP_LTZ):

select from store before (STATEMENT => 01af4e82-3200-e2b8-0000-00065bdef091'
select * from store BEFORE (OFFSET => -600):

