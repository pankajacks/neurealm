# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC # Sharing Data using Databricks UI
# MAGIC
# MAGIC
# MAGIC Databricks-managed Delta Sharing allows data providers to share data and data recipients to access the shared data. In this course, we are going to share data within Databricks, which means both data provider and recipient will be Databricks users. 
# MAGIC
# MAGIC Databricks-managed Delta Sharing allows administrators to create and manage providers, shares, and recipients with a simple-to-use UI and SQL commands.
# MAGIC
# MAGIC
# MAGIC
# MAGIC **Task**
# MAGIC
# MAGIC 1. Create and manage shares using the Databricks UI
# MAGIC 1. Create and manage recipients using the Databricks UI
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC ### Create sample data

# COMMAND ----------

# MAGIC %sql
# MAGIC USE CATALOG main;
# MAGIC
# MAGIC -- Step 1: Create schema (if not exists)
# MAGIC CREATE SCHEMA IF NOT EXISTS demo_share;
# MAGIC
# MAGIC -- Step 2: Create product table in Unity Catalog
# MAGIC CREATE OR REPLACE TABLE demo_share.products (
# MAGIC     product_id   INT,
# MAGIC     product_name STRING,
# MAGIC     category     STRING,
# MAGIC     price        DECIMAL(10,2),
# MAGIC     in_stock     BOOLEAN
# MAGIC );
# MAGIC
# MAGIC -- Step 3: Insert sample data
# MAGIC INSERT INTO demo_share.products VALUES
# MAGIC  (1, 'Laptop', 'Electronics', 899.99, TRUE),
# MAGIC  (2, 'Headphones', 'Electronics', 199.99, TRUE),
# MAGIC  (3, 'Office Chair', 'Furniture', 149.99, FALSE),
# MAGIC  (4, 'Coffee Machine', 'Appliances', 89.99, TRUE),
# MAGIC  (5, 'Notebook', 'Stationery', 2.99, TRUE);
# MAGIC
# MAGIC CREATE OR REPLACE TABLE demo_share.sales (
# MAGIC     sale_id       INT,
# MAGIC     product_id    INT,
# MAGIC     customer_id   INT,
# MAGIC     quantity      INT,
# MAGIC     sale_date     DATE,
# MAGIC     sale_amount   DECIMAL(10,2)
# MAGIC );
# MAGIC
# MAGIC INSERT INTO demo_share.sales VALUES
# MAGIC  (101, 1, 1001, 2, '2025-09-01', 1799.98),
# MAGIC  (102, 2, 1002, 1, '2025-09-01', 199.99),
# MAGIC  (103, 3, 1003, 1, '2025-09-02', 149.99),
# MAGIC  (104, 4, 1004, 3, '2025-09-02', 269.97),
# MAGIC  (105, 5, 1005, 10, '2025-09-03', 29.90);

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Create & Manage Shares
# MAGIC
# MAGIC The first of data sharing process is to create a share. In Delta Sharing, a share is a named object that contains a collection of tables in a metastore that you wish to share as a group. A share can contain tables from only a single metastore. You can add or remove tables from a share at any time.
# MAGIC
# MAGIC ### Create A Share
# MAGIC
# MAGIC - Click on **Catalog**.
# MAGIC - From Catalog Explorer, click **Delta Sharing**.
# MAGIC - Select **Shared by me** to see a list current shares or create a new share.
# MAGIC - On the top right, click **Share Data** button.
# MAGIC - Enter *"product_data_share"* as name of the share.
# MAGIC - Enter any description you want in the comment section.
# MAGIC - Click **Save and Continue** button.
# MAGIC
# MAGIC ### Add tables to the Share
# MAGIC
# MAGIC A share is a read-only collection of tables and table partitions to be shared with one or more recipients. Share details page lists data tables and recipients for the selected share. 
# MAGIC
# MAGIC
# MAGIC ### Manage A Share
# MAGIC
# MAGIC Managing existing shares is done on the same screen as described above. 
# MAGIC
# MAGIC - Navigate to **Shared by me** screen (Catalog → Delta Sharing → Shared by me).
# MAGIC - Click on *"flights_data_share"* share you to edit.
# MAGIC - In share details page;
# MAGIC     - You can edit share details such as comment, owner etc.
# MAGIC     - View list of data tables in the share.
# MAGIC     - View list of recipients who have access to the share.
# MAGIC
# MAGIC
# MAGIC
# MAGIC - To add a table to the share;
# MAGIC     - Click **Edit Assets under Manage Assets** button on the top right.
# MAGIC     - Select the catalog → schema → table to add it to the share.
# MAGIC     
# MAGIC - To grant a recipient access to the share, click **Add Recipient** button on the top right or select the recipient from the dropdown list. Follow steps below to create a new recipient and share data with.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ---

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Create & Manage Recipients
# MAGIC
# MAGIC A recipient represents an organization with whom to share data. Grant the recipient access to shares after they are created.
# MAGIC
# MAGIC ### Create a Recipient
# MAGIC
# MAGIC To create a *New recipient*;
# MAGIC
# MAGIC - Navigate to **Shared by me** screen (Catalog → Delta Sharing → Shared by me).
# MAGIC - Click **New recipient** button.
# MAGIC - Enter *"data_recipient"* as the name of new recipient.
# MAGIC - A recipient can be a Databricks user or an external user. For recipients who are not Databricks users, an authentication file is generated which can be shared with recipient and they can download it. For this example, we will use Databricks-to-Databricks data sharing, therefore, we need to define user identifier and Databricks takes care of the token management process.
# MAGIC - Enter **Sharing Identifier** of the recipient. Sharing Identifier is the global unique identifier of a Unity Catalog metastore owned by the data recipient with whom you’d like to share data. It has a format of `<cloud>:<region>:<uuid>`. Example: `aws:eu-west-1:b0c978c8-3e68-4cdf-94af-d05c120ed1ef`.
# MAGIC - A user can view their **Sharing Identifier** in **Shared with me** page.
# MAGIC - Enter a description you want to define for the recipient in Comment box.
# MAGIC - Click **Create** button.
# MAGIC
# MAGIC ### Manage Recipients
# MAGIC
# MAGIC To view and edit recipients;
# MAGIC
# MAGIC - Navigate to **Shared by me** screen (Catalog → Delta Sharing → Shared by me).
# MAGIC - Click **Recipients** tab.
# MAGIC - This page lists all recipients along with authentication type, status and creation date. To view a recipient click on recipient name.
# MAGIC - Recipients details page shows list of *Shares* that the recipient has access and *IP Access List*.

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ---

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Grant Access and Manage Access Level
# MAGIC
# MAGIC We have created a *share* and a *recipient*. The next step is to make sure the *recipient* has access permissions on the *share*. 
# MAGIC
# MAGIC To add a recipient to a share;
# MAGIC
# MAGIC - Navigate to **Shared by me** screen (Data → Delta Sharing → Shared by me).
# MAGIC - Click on the "flights_data_share" *share*.
# MAGIC - Click on **Add recipient** button on the top right.
# MAGIC - Select the "flights_data_recipient" *recipient* that we created in the previous step.
# MAGIC
# MAGIC To `revoke` access for a recipient;
# MAGIC
# MAGIC - Click on the "flights_data_share" *share*.
# MAGIC - Click **Recipients** tab
# MAGIC - Select **Revoke** from the action context menu on the right of the row. This will revoke recipient’s permission for the selected share.