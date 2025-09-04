# Databricks notebook source
# MAGIC %md
# MAGIC
# MAGIC # Enable Delta Sharing
# MAGIC
# MAGIC In this demo we are going to demonstrate how to enable Delta Sharing on Databricks. First, we are going to enable external data sharing, then, we are going to configure a metastore to enable Delta Sharing.
# MAGIC
# MAGIC **Learning Objectives**
# MAGIC
# MAGIC * Enable external data sharing for an account
# MAGIC
# MAGIC * Configure Delta Sharing on a metastore
# MAGIC
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Prerequisites
# MAGIC
# MAGIC Before moving forward, please make sure that following requirements are met.
# MAGIC
# MAGIC - Unity Catalog must be enabled, and at least one metastore must exist.
# MAGIC
# MAGIC - Account admin role to enable Delta Sharing for a Unity Catalog metastore.
# MAGIC
# MAGIC - Metastore admin role to share data using Delta Sharing.
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC
# MAGIC ## Enable Delta Sharing on a metastore
# MAGIC
# MAGIC **📌 Note:** You do not need to enable Delta Sharing on your metastore if you intend to use Delta Sharing only to share data with users on other Unity Catalog metastores in your account. Metastore-to-metastore sharing within a single Databricks account is enabled by default.
# MAGIC
# MAGIC To enable Delta Sharing on a metastore;
# MAGIC
# MAGIC - Login to **account console**.
# MAGIC - In the sidebar, click **Data**.
# MAGIC - Click the name of a metastore to open its details.
# MAGIC - Click the checkbox next to **Enable Delta Sharing to allow a Databricks user to share data outside their organization**.
# MAGIC - Configure the recipient token lifetime.
# MAGIC
# MAGIC We are going to dive into token management details in “Delta Sharing Best Practices” section.