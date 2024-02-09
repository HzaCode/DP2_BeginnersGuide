

# Configuring API Settings to Save Data

 **Description:**
In the DP2 system, configuring API settings is a key step in saving extracted data to a database. This document details how to set up the API to save data to databases, including MySQL and MongoDB.

### Step 1: Define the API Endpoint

Firstly, you need to define the API endpoint, which is the URL where the data will be sent. This URL should point to the API provided by your database service, used for receiving and processing data.

### Step 2: Specify the Table Name

The table name identifies where in the database the data will be stored. Ensure this table already exists in your database and that it has the appropriate structure to receive your data.

### Step 3: Set a Unique Identifier

A unique identifier (such as `uniqueId`) is crucial for ensuring the uniqueness of data and for updating existing records. Include this field in your API request so that the database can identify and update the corresponding record.

### Step 4: Configure Data Fields

Use JMESPath or jq expressions to map the extracted data fields to the corresponding fields in your database table. This step allows you to customize the data output according to the structure and needs of your database.

### Step 5: Choose the Data Operation Type

In the API request, you can select the data operation type, such as "merge" (to combine), "create" (to make a new record), or "update" (to refresh an existing one). This determines how the database will process the received data.

### Step 6: Handle Attachments

If your data includes attachments, you need to configure the API to properly handle these files. This might involve uploading the attachments to a cloud storage service and updating the corresponding file link in the database.

### Sample Configuration: MySQL

```json
{
  "url": "http://api.example.com",
  "table": "your_table_name",
  "where": {
    "goodsId": "{goodsId}"
  },
  "data": {
    "registeredMedicineModel": "{registeredMedicineModel}",
    "drugCategory": "{drugCategory}"
  }
}
```

### Sample Configuration: MongoDB

```json
{
  "url": "http://api.example.com",
  "table": "your_collection_name",
  "type": "merge",
  "where": {
    "uniqueId": "{uniqueId}"
  },
  "data": {
    "registeredMedicineModel": "{registeredMedicineModel}",
    "drugCategory": "{drugCategory}"
  }
}
```

### Handling Attachments in MongoDB

For MongoDB, you can directly include attachment information by updating the `data` field of the document:

```json
{
  "url": "http://api.example.com",
  "table": "your_collection_name",
  "where": {
    "uniqueId": "{uniqueId}"
  },
  "data": {
    "data": {
      "registeredMedicineModel": "{registeredMedicineModel}",
      "drugCategory": "{drugCategory}",
      "attachments": [
        {
          "key": "{attachmentKey}",
          "row_idx": "{row_idx}"
        }
      ]
    }
  }
}
```

### Summary

Configuring API settings in DP2 involves specifying the endpoint, table name, unique identifier, data fields, and handling attachments. This ensures that the extracted data can be correctly saved and updated. Always test your configuration before going live to ensure its accuracy. Following these steps will ensure a smooth data extraction process.
