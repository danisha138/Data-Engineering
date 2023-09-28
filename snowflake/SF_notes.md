Snowflake Time Travel:

• Time Travel allows accessing historical data that was changed or deleted within a specified period.
• It provides Continuous Data Protection (CDP) for maintaining and preserving historical data.
• We can restore dropped tables, schemas, and databases from the past.
• Query data that has been updated or deleted within the defined period.
• Create clones of entire tables, schemas, and databases at specific points in the past.

Snowflake Fail-Safe period:

• Fail-Safe is a non-configurable 7-day period provided by Snowflake.
• It starts immediately after the Time Travel retention period ends.
• During Fail-Safe, historical data may be recoverable by Snowflake.
• Accessing this data requires intervention by Snowflake Support.
• Fail-Safe is not meant for accessing historical data after the Time Travel retention period has expired.

Snowflake Zero Copy Cloning:

• Zero Copy Cloning in Snowflake allows quick and easy copying of tables, schemas, or databases.
• The copy shares the same storage, saving storage costs.
• Cloned and original objects are independent, ensuring changes to one don't affect the other.


The COPY command allows unloading or exporting data from a table or a view and also allows using queries (SELECT) to unload data.

The COPY command can load data using a SELECT query. 
Yes
