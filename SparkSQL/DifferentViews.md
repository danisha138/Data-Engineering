# Difference between View and Temporary View and Global Temporary view
View scope is spark catalog. which can be accessed any user in any session , in any cluster.
temporary view scope is User level. this view will be available only that user. other users cannot be accessed.
Global Temporary view Scope is spark session (cluster). this view is available only at spark cluster level. any one can access within the cluster.

# Global Temporary View
Temporary views in Spark SQL are session-scoped and will disappear if the session that creates it terminates.
If you want to have a temporary view that is shared among all sessions and keep alive until the Spark application terminates,
when you can create a global temporary view. Global temporary view is tied to a system preserved database global_temp,
and we must use the qualified name to refer it, e.g. SELECT * FROM global_temp.view1.


`Create or replace view will be stored in metadata and its available for all sessions and all users and all clusters.`

`create or replace temporary view will be available in only current session.`

`create or replace global temporary view will be available in other sessions`


