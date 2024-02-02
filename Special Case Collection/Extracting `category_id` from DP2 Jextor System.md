# **从Jextor系统中提取 `category_id`**

在**DP2** Jextor系统中工作时，您可能需要从`TASK_extra_data`字段中提取特定信息，如`category_id`。此字段通常包含有嵌套信息的JSON格式字符串。正确提取信息需要遵循特定的步骤和格式。以下是详细的步骤和代码示例，包括常见错误及其避免方法：

## 步骤1：了解`TASK_extra_data`

`TASK_extra_data`是Jextor任务配置中包含与任务相关的附加数据的字段。这些数据通常以JSON格式存储。例如：

```json
{
  "category_id": "21",
  "row_idx": 0,
  "step_num": 2
}
```

## 步骤2：编辑任务元素

在任务的`elements`对象中，您需要定义如何提取`category_id`。您需要指定一个键，如`category_id`，并使用适当的`col`和`callback`键值对。

## 步骤3：使用正确的回调函数

要从`TASK_extra_data`字段提取`category_id`，您需要使用一个回调函数。该函数将解析JSON字符串并提取您需要的值。

## 步骤4：配置示例

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

在此配置中，`json_extract##category_id`是一个回调函数，用于从`TASK_extra_data`提取`category_id`字段的值。

## 常见错误

- **直接引用**：直接引用`TASK_extra_data`将不会提取任何特定字段。

    错误配置示例：
    
    ```json
    {
      "category_id": "TASK_extra_data" // 这将直接返回整个TASK_extra_data内容
    }
    ```
    
- **缺少回调函数**：如果您没有指定回调函数或指定错误，您将无法从JSON字符串中提取任何值。
    
    错误配置示例：
    
    ```json
    {
      "category_id": {
        "col": "TASK_extra_data",
        "callback": "category_id" // 这是错误的，应使用json_extract##category_id
      }
    }
    ```
    

## 正确结果

使用正确的配置，您将得到以下提取结果：

```json
{
  "TotalPageNum": "2",
  "category_id": "21"
}
```

在此结果中，`"category_id": "21"`正确反映了从`TASK_extra_data`提取的`category_id`值。
