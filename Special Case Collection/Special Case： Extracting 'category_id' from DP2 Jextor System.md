# Special Case： Extracting 'category_id' from DP2 Jextor System

**Introduction**

When extracting data from the DP2 Jextor system, it is often necessary to retrieve specific information, such as the `category_id`, from the `TASK_extra_data` field. This field contains a JSON-formatted string with nested data. To accurately extract the `category_id`, follow the steps and formatting guidelines provided below, along with common pitfalls and how to avoid them.

**TASK_extra_data Overview**

The `TASK_extra_data` field in Jextor task configurations holds supplementary data related to the task, typically in JSON format. An example of such data might look like this:

```json
{
  "category_id": "21",
  "row_idx": 0,
  "step_num": 2
}
```

**Editing Task Elements**

To extract the `category_id`, you must configure the task's elements object to specify the key and use the appropriate `col` and `callback` key-value pairs.

**Using the Correct Callback Function**

Employing a callback function is essential for parsing the JSON string within `TASK_extra_data` and extracting the desired `category_id`. Here's an example configuration:

```json
{
  "elements": {
    "category_id": {
      "col": "TASK_extra_data",
      "callback": "json_extract##category_id"
    }
  }
}
```

In this configuration, the `json_extract##category_id` callback function is responsible for extracting the `category_id` value.

**Common Pitfalls**

1. **Direct Reference**: Directly referencing `TASK_extra_data` without a callback function will not yield the specific field you seek. For example:

   ```json
   {
     "category_id": "TASK_extra_data" // Incorrect, returns the entire `TASK_extra_data` content
   }
   ```

2. **Missing or Incorrect Callback Function**: Omitting or misconfiguring the callback function will prevent extraction of the `category_id`. For example:

   ```json
   {
     "category_id": {
       "col": "TASK_extra_data",
       "callback": "category_id" // Incorrect, should be "json_extract##category_id"
     }
   }
   ```

**Correct Configuration and Outcome**

With the proper configuration, the extraction result will be as follows:

```json
{
  "TotalPageNum": "2",
  "category_id": "21"
}
```

Here, `category_id`: "21" accurately reflects the extracted value from `TASK_extra_data`.

**Conclusion**

By following these guidelines and avoiding common mistakes, you can effectively extract the `category_id` from the `TASK_extra_data` field in the DP2 Jextor system. This ensures that your data extraction process is both accurate and efficient.
