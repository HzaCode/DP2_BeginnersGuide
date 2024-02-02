## **Extracting category_id from DP2 Jextor System**

When working in the DP2 Jextor system, you may need to extract specific information like category_id from the TASK_extra_data field. This field usually contains a JSON-formatted string with nested information. Extracting information properly requires following certain steps and formats. Here are the detailed steps and code examples, including common mistakes and how to avoid them:

### Step 1: Understand TASK_extra_data

`TASK_extra_data` is a field in the Jextor task configuration that contains additional data related to the task. This data is usually stored in JSON format. For example:

```json
{
"category_id": "21",
"row_idx": 0,

"step_num": 2
}
```

### Step 2: Edit the task elements

In the `elements` object of the task, you need to define how to extract the `category_id`. You need to specify a key like `category_id` and use the proper `col` and `callback` key-value pairs.

### Step 3: Use the right callback function

To extract `category_id` from the `TASK_extra_data` field, you need to use a callback function. This function will parse the JSON string and extract the value you need.

### Step 4: Configuration example

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

In this configuration, `json_extract##category_id` is a callback function to extract the `category_id` field's value from `TASK_extra_data`.

### Common mistakes

Direct reference
Directly referencing `TASK_extra_data` will not extract any specific field.

Wrong configuration example:

```json
{
"category_id": "TASK_extra_data" // This will directly return the whole TASK_extra_data content

}
```

Missing callback function
If you don't specify a callback function or specify it incorrectly, you won't be able to extract any values from the JSON string.

Wrong configuration example:

```json
{
"category_id": {
"col": "TASK_extra_data",
"callback": "category_id" // This is wrong, should use json_extract##category_id
}
}

```

### Correct result

With the proper configuration, you will get the following extraction result:

```json
{
"TotalPageNum": "2",
"category_id": "21"

}
```

In this result, `"category_id": "21"` correctly reflects the `category_id` value extracted from `TASK_extra_data`.
