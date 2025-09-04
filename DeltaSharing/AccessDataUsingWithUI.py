# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC # Access Data using Databricks UI
# MAGIC
# MAGIC In the previous demo, we shared a table using a share and granted read access to our recipient account. In this demo, we will demonstrate how to access the shared data using Databricks UI. Databricks supports UI and Databricks SQL commands to access shared data. We will use SQL commands for the same workflow demonstrated here in next demos.
# MAGIC
# MAGIC
# MAGIC **Task:**
# MAGIC
# MAGIC - Access shared data using the UI
# MAGIC - View and manage shared data using the UI
# MAGIC

# COMMAND ----------

# MAGIC %md 
# MAGIC
# MAGIC ## Sharing Identifier
# MAGIC
# MAGIC In order to allow a data provider on Databricks to share data with you through Delta Sharing, they would need to know a globally unique identifier of the Unity Catalog metastore where you are going to access the shared data. It has a format of `<cloud>:<region>:<uuid>`. You can acquire that globally unique identifier by visiting **Shared with me** page (Catalog → Delta Sharing → Shared with me).
# MAGIC
# MAGIC In the previous demo, we used this unique metastore identifier to share data with our recipient account. 
# MAGIC
# MAGIC ## View Providers and Shared Data
# MAGIC
# MAGIC A provider is a named object that represents the data provider in the real world who shares the data with you. For a data provider in Databricks, the provider object has an authentication type of `DATABRICKS`, which suggests that it uses Databricks-managed Delta Sharing to share the data. For data providers who use the open source protocol and recipient profile authentication method to share the data, its provider object has an authentication of `TOKEN`. 
# MAGIC
# MAGIC When a data provider shares data with your current Unity Catalog metastore, provider objects are automatically created under the metastore. To view available data providers under your Unity Catalog metastore;
# MAGIC
# MAGIC - Navigate to **Shared with me** screen (Catalog → Delta Sharing → Shared with me)
# MAGIC - The **Providers** tab shows a list of providers who shared the data with you.
# MAGIC - Click on the provider name to view **shares***.* The provider name is the *organization name* defined in Databricks account console of account shared data with you. A share is a collection of datasets shared by the data provider. **A share belongs to a data provider and you need to create a catalog from a share to access the dataset inside.**
# MAGIC - Click on **Create Catalog** button for the share you want to access.
# MAGIC     - Enter "shared_data_catalog" as **Catalog Name**
# MAGIC     - Enter Comment as desired
# MAGIC     - Click on **Create** button
# MAGIC - This will create a new catalog and you will see **Schemas** and **Tables** that are shared with you.
# MAGIC - You can view Catalog, Schema(s) and Table(s) details and access sample data in **Data Explorer (**Catalog → Data Explorer**).**
# MAGIC - If you want to grant permissions for the shared Schema(s) or Table(s) to another user or a group, you can set these permissions in **Permissions** tabs.
# MAGIC
# MAGIC 📝 **Note that the Catalog Type of this catalog is DELTASHARING and it is read-only. Which means data inside a Delta Sharing Catalog are read-only and can not be created, modified or deleted. You can perform read operations like `DESC`, `SHOW`, `SELECT`but can’t perform write or update operations like `MODIFY`, `UPDATE`, or `DROP`. The only exception to this rule is that the owner of the data object or the metastore admin can update the owner of the data objects to other users or groups.**