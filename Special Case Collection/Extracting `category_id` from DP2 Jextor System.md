# **Extracting `category_id`**

When working with the **DP2** Jextor system, you might need to extract specific information, such as `category_id`, from the `TASK_extra_data` field. This field typically contains a JSON-formatted string with nested information. Correctly extracting this information requires following specific steps and formatting. Below are detailed steps and code examples, including common mistakes and their avoidance methods:

##  `TASK_extra_data`

`TASK_extra_data` is a field in Jextor task configurations that contains additional data related to the task, usually stored in JSON format. For example:

```json
{
  "category_id": "21",
  "row_idx": 0,
  "step_num": 2
}
```

## Editing Task Elements

In the task's `elements` object, you need to define how to extract `category_id`. You need to specify a key, such as `category_id`, and use appropriate `col` and `callback` key-value pairs.

## Using the Correct Callback Function

To extract `category_id` from the `TASK_extra_data` field, you need to use a callback function. This function will parse the JSON string and extract the value you need.

## Configuration Example

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

In this configuration, `json_extract##category_id` is a callback function used to extract the value of the `category_id` field from `TASK_extra_data`.

## Common Mistakes

- **Direct Reference**: Directly referencing `TASK_extra_data` will not extract any specific field.

    Incorrect configuration example:
    
    ```json
    {
      "category_id": "TASK_extra_data" // This will directly return the entire TASK_extra_data content
    }
    ```
    
- **Missing Callback Function**: If you do not specify a callback function or specify it incorrectly, you will not be able to extract any value from the JSON string.
    
    Incorrect configuration example:
    
    ```json
    {
      "category_id": {
        "col": "TASK_extra_data",
        "callback": "category_id" // This is incorrect; should use json_extract##category_id
      }
    }
    ```
    

## Correct Outcome

With the correct configuration, you will obtain the following extraction result:

```json
{
  "TotalPageNum": "2",
  "category_id": "21"
}
```

In this result, `"category_id": "21"` correctly reflects the `category_id` value extracted from `TASK_extra_data`.
