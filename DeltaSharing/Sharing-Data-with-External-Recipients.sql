-- Databricks notebook source
-- MAGIC %md
-- MAGIC
-- MAGIC # Sharing Data with External Recipients using Databricks SQL 
-- MAGIC
-- MAGIC In this course we are going to demonstrate the data sharing process with external users. In this typical scenario, the data *provider* is a Databricks user and the *recipient* can connect to the data using a Delta Sharing *connector*. 
-- MAGIC
-- MAGIC Databricks-managed Delta Sharing allows administrators to create and manage providers, shares, and recipients with a simple-to-use UI and SQL commands. In the previous course, we demonstrated how to share and access data using both Databricks UI and SQL commands. In this course, we are going to use Databricks SQL, but you can follow along using the UI as well.  
-- MAGIC
-- MAGIC **Learning Objectives:**
-- MAGIC - Explain the difference between internal and external data sharing
-- MAGIC - Share data externally using Databricks SQL
-- MAGIC

-- COMMAND ----------

USE CATALOG main;

-- COMMAND ----------

USE CATALOG main;

-- Step 1: Create schema for flights data
CREATE SCHEMA IF NOT EXISTS db_flights_ext;

-- Step 2: Create flights table partitioned by origin
DROP SHARE IF EXISTS flights_data_share_ext;
DROP TABLE IF EXISTS db_flights_ext.flights_ext;
CREATE OR REPLACE TABLE db_flights_ext.flights_ext (
    flight_id    INT,
    flight_date  DATE,
    origin       STRING,
    destination  STRING,
    airline      STRING,
    passengers   INT,
    price        DECIMAL(10,2)
)
USING DELTA
PARTITIONED BY (origin)
TBLPROPERTIES (
    delta.enableChangeDataFeed = true,
    delta.enableDeletionVectors = false
    );
    
-- Step 3: Insert sample data
INSERT INTO db_flights_ext.flights_ext VALUES
 (1001, '2025-09-01', 'JFK', 'LAX', 'Delta', 180, 320.00),
 (1002, '2025-09-01', 'SFO', 'ORD', 'United', 150, 280.50),
 (1003, '2025-09-02', 'JFK', 'MIA', 'American', 200, 350.00),
 (1004, '2025-09-02', 'ATL', 'SEA', 'Alaska', 170, 290.75),
 (1005, '2025-09-03', 'JFK', 'DFW', 'JetBlue', 190, 310.40);

-- COMMAND ----------

-- MAGIC %md
-- MAGIC
-- MAGIC ## Create A Share
-- MAGIC
-- MAGIC The first of data sharing process is to create a share. In Delta Sharing, a share is a named object that contains a collection of tables in a metastore that you wish to share as a group. A share can contain tables from only a single metastore. You can add or remove tables from a share at any time.
-- MAGIC
-- MAGIC *Share* creation and management process is the same as sharing data within Databricks. Share creation and management was covered in depth in the "Sharing Data within Databricks with Delta Sharing" course.
-- MAGIC

-- COMMAND ----------

-- Create a share to be shared with external recipient

CREATE SHARE IF NOT EXISTS flights_data_share_ext 
COMMENT 'Delta Sharing share for flights data to share with external recipient.';

-- COMMAND ----------

-- Let's check the share and review the details

DESCRIBE SHARE flights_data_share_ext;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC
-- MAGIC ### Add Tables to the Share 
-- MAGIC
-- MAGIC As next step fo data sharing, we need to add table(s) to the share. A share can have multiple tables. To keep it simple, we will add only one table with CDF (Change Data Feed) is enabled. This will allow the recipient to query shared table by version. 

-- COMMAND ----------

select * from main.db_flights_ext.flights_ext;

-- COMMAND ----------

-- Add flights table to the share

ALTER SHARE flights_data_share_ext
  ADD TABLE db_flights_ext.flights_ext
  COMMENT "Flights table with CDF enabled to be shared with external recipient"
  WITH CHANGE DATA FEED;

-- COMMAND ----------

-- Check the tables in the share. This should show details of the table we just added to the share. Note the `partitions` and `cdf_shared` options.

SHOW ALL IN SHARE flights_data_share_ext;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC ### Create a New Version of the Table
-- MAGIC
-- MAGIC As we enabled CDF for the shared table, let's insert a new record to create a new version of the table. The recipient will see the version details and can query based the table by version. 

-- COMMAND ----------

-- Insert a new record
INSERT INTO db_flights.flights VALUES (1006, '2025-09-04', 'JFK', 'LAX', 'Delta', 160, 320.00)

-- COMMAND ----------

-- View changes as of version 1

SELECT * FROM table_changes('db_flights_ext.flights_ext', 1)

-- COMMAND ----------

-- MAGIC %md
-- MAGIC
-- MAGIC ---

-- COMMAND ----------

-- MAGIC %md
-- MAGIC
-- MAGIC ## Create An External Recipient
-- MAGIC
-- MAGIC A recipient represents an organization with whom to share data. A recipient can be a Databricks user or an external user. For recipients who are not Databricks users, an authentication file is generated which can be shared with recipient and they can download it.
-- MAGIC
-- MAGIC The credentials are typically saved as a file containing access token. The Delta Server identify and authorize consumer based on these identifiants.
-- MAGIC
-- MAGIC **📌 Note that the "activation link" is single use. You can only access it once (it'll return null if already used). Make sure to save it in a secure place.**
-- MAGIC

-- COMMAND ----------

-- Create an external recipient

CREATE RECIPIENT IF NOT EXISTS flights_data_recipient_ext
  COMMENT "Flights data recipient (External User)";

-- COMMAND ----------

-- MAGIC %md
-- MAGIC
-- MAGIC The authentication file is shown in **"activation_link"** field of the recipient. The activation link can be viewed in the recipients details page on Databricks as well.

-- COMMAND ----------

--  View Recipient details. Note the "activation link" 

DESC RECIPIENT flights_data_recipient_ext;

-- COMMAND ----------

-- MAGIC %md
-- MAGIC
-- MAGIC ---

-- COMMAND ----------

-- MAGIC %md
-- MAGIC
-- MAGIC ## Provide Read Access to the Recipient
-- MAGIC
-- MAGIC We have created a *share* and a *recipient*. The last step is to make sure the *recipient* has access permissions on the *share*. 
-- MAGIC

-- COMMAND ----------

-- Grant permissions to the share we just created

GRANT SELECT 
  ON SHARE flights_data_share_ext
  TO RECIPIENT flights_data_recipient_ext;

-- COMMAND ----------

-- Check if recipient can access to the share. You should see Flights_Data_Recipient with SELECT privilege  

SHOW GRANT ON SHARE flights_data_share_ext;