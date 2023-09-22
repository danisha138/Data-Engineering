Does data in external stage count towards your Snowflake storage?

No. External stages point to external cloud storage locations. Data in those external locations are managed and maintained independently and is managed by the respective cloud provider. An external stage only refers to an external location and doesn't physically hold any data.


CREATE OR REPLACE FILE FORMAT my_csv_format
  TYPE = CSV
  FIELD_DELIMITER = '|'
  SKIP_HEADER = 1
  NULL_IF = ('NULL', 'null')
  EMPTY_FIELD_AS_NULL = true
  COMPRESSION = gzip;

  

USE DATABASE testdb;
SHOW FILE FORMATS;


SHOW FILE FORMATS IN DATABASE testdb;

ALTER FILE FORMAT IF EXISTS my_format RENAME TO my_new_format;

ALTER FILE FORMAT my_format SET FIELD_DELIMITER=',';

DESC FILE FORMAT my_csv_format;

DROP FILE FORMAT [ IF EXISTS ] <name>

SHOW FILE FORMATS IN SCHEMA testdb.public;



CREATE STAGE my_s3_stage
  STORAGE_INTEGRATION = s3_int
  URL = 's3://mybucket/encrypted_files/'
  FILE_FORMAT = my_csv_format;



CREATE OR REPLACE STAGE flights_stage
 url='s3://ca-flight-data-daily/2020/06/01/'
 file_format = (type = 'CSV' field_delimiter = ',' field_optionally_enclosed_by = '"' skip_header = 1);
