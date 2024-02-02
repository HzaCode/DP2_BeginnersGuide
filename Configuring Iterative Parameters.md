# Configuring Iterative Parameters

When executing data collection tasks, correctly configuring iterative parameters is a fundamental and critical step, especially when the task involves traversing websites with multiple pages. Here is a standard example and a detailed explanation of the parameters.

```json

{
  "project_name": "{STU}.list",
  "url": {
    "pattern": " https://www.examplemed.com/main/list.html?cId={category_id}&pn={page_number}.html ", 
    "iteration": {
      "start": 1,
      "stop": "{TotalPageNum}",
      "format": "{page_number}"
    }
  }
}

```

### Parameter Explanation

- **project_name**: Identifies the name of the current project, formatted as `"{STU}.list"`, where **`{STU}`** represents the study name.
- **url**:
    - **pattern**: A template for the web page URL, where `{category_id}` and `{page_number}` are dynamic parameters that will be replaced during the process.
    - **iteration**: Defines the iteration mechanism.
        - **start**: The page number to start from, `1` indicates starting from the first page.
        - **stop**: The condition to stop, `"{TotalPageNum}"` represents stopping at the last page of the website.
        - **format**: The formatting of the page number, `{"{page_number}}"` indicates the page number is directly replaced in the corresponding position in the URL.

## Common Error Cases and Code Examples

### Error Case 1: Incorrect `start` Value

### Problem Description

Incorrectly setting the `start` value to 2, mistakenly assuming that the first page does not contain important information or can be skipped.

### Example Code

```json
{
  "project_name": "{STU}.list",
  "url": {
    "pattern": " https://www.examplemed.com/main/list.html?cId={category_id}&pn={page_number}.html ", 
    "iteration": {
      "start": 2, // Incorrectly skipped the first page
      "stop": "{TotalPageNum}",
      "format": "{page_number}"
    }
  }
}

```

### Error Case 2: Incorrect Use of `first` Parameter

### Problem Description

When the first page has a special URL format but the `first` parameter is not used correctly or the `start` parameter is set incorrectly, it may lead to data omission or duplication.

### Example Code

```json
{
  "project_name": "{STU}.list",
  "url": {
    "pattern": " https://www.examplepharm.com/main/product-list.html?cId={category_id}&pn=(*).html ", 
    "iteration": {
      "first": "1",  // If the first page is special, it should be set to the actual situation
      "start": 1,    // If the first page is special, start from 2
      "stop": "{TotalPageNum}",
      "format": "{}"
    }
  }
}

```

### Error Case 3: Inaccurate `TotalPageNum`

### Problem Description

Hardcoding `TotalPageNum` as an estimated value instead of dynamically obtaining the actual total number of pages.

### Example Code

```json
{
  "project_name": "{STU}.list",
  "url": {
    "pattern": " https://www.examplemed.com/main/list.html?cId={category_id}&pn={page_number}.html ", 
    "iteration": {
      "start": 1,
      "stop": 5, // Assuming the total number of pages is 5, which may not match reality
      "format": "{page_number}"
    }
  }
}

```

### Error Case 4: Improper URL Pattern Configuration

### Problem Description

Forgetting to replace `{category_id}` or the page number placeholder `{page_number}` in the URL pattern, resulting in the inability to access the correct page.

### Example Code

```json
{
  "project_name": "{STU}.list",
  "url": {
    "pattern": " https://www.examplemed.com/main/list.html?cId=&pn={page_number}.html ",   // Forgot to replace `{category_id}`
    "iteration": {
      "start": 1,
      "stop": "{TotalPageNum}",
      "format": "{page_number}"
    }
  }
}

```

## Conclusion

Correctly configuring the `first`, `start`, and `stop` parameters is key to ensuring the completeness and accuracy of data collection tasks. Paying close attention to the following points can help you effectively prevent data omission or duplication:

- Use the `first` parameter to explicitly specify the special URL for the first page (if any).
- Adjust the start parameter appropriately based on the actual page layout to ensure it commences from the correct page.
- Dynamically set the `stop` parameter to cover all pages, ensuring the completeness of data collection.
