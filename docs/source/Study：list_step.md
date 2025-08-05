# Step Configuration ③ - List Step

## Configuring List Steps (`list_step`)

### Step Description
In this step, your goal is to extract detailed information from each product on a medical product listing page, including product name, link, description, etc. This data will be used for subsequent detailed analysis and processing. To achieve this goal, you need to configure the `list_step` step so that the system can traverse all relevant pages and extract the required data.

### Data Input (data_in)
In the `list_step`, data input (data_in) usually includes the total number of pages (TotalPageNum) determined in the previous `totalpage_step`. This information is crucial for configuring iteration parameters, as it determines the range of pages you need to process. For example, if `TotalPageNum` is 4, then the iteration parameters will start from page 1 and continue to page 4.

### Configuring URL Pattern and Iteration Parameters
- **URL Pattern**: You need to design a URL pattern so that the system can dynamically generate the URL of each page based on the iteration parameters. For example, if the URL structure is `https://www.examplemed.com/main/list.html?cId={category_id}&pn={page_number}`, you can use this pattern to construct the URL for all listing pages.

- **Iteration Parameters**: In `list_step`, the iteration parameters include `start` (starting page number), `stop` (ending page number), and `format` (page number formatting). `start` is usually set to 1, indicating the start from the first page; `stop` is set to `{TotalPageNum}`, indicating up to the last page; `format` is used to insert the page number into the placeholder `{page_number}` during iteration.

### Example Configuration
Below is a typical example of a `list_step` configuration, demonstrating how to use the aforementioned parameters:

```json
{
  "data_in": {
    "data_for_test": {
      "TotalPageNum": "4"
    }
  },
  "project_name": "{STU}.list",
  "url": {
    "pattern": "https://www.examplemed.com/main/list.html?cId={category_id}&pn={page_number}",
    "iteration": {
      "start": 1,
      "stop": "{TotalPageNum}",
      "format": "{page_number}"
    }
  },
  "type": "one-off",
  "priority": 2,
  "data_out": {
    "jpath": ""
  },
  "interval": "86400",
  "excluded_workers": "{excluded_workers}"
}
```

### Considerations
- Ensure the URL pattern is correct and can adapt to changes in the URL structure of the listing pages.
- When setting iteration parameters, consider the pagination logic to ensure all relevant pages are visited.
- When outputting data, if the link is a relative path, it should be converted to an absolute path to ensure it can be correctly accessed in subsequent steps.


## Common Error Cases
### Error Case 1: Incorrect Starting Page Number (start) Setting
#### Problem Description
Incorrectly setting the starting page number (start) to 2, assuming the first page does not contain important information or can be skipped.

#### Example Code
```json
{
  "project_name": "{STU}.list",
  "url": {
    "pattern": "https://www.examplemed.com/main/list.html?cId={category_id}&pn={page_number}",
    "iteration": {
      "start": 2, // Incorrectly skipped the first page
      "stop": "{TotalPageNum}",
      "format": "{page_number}"
    }
  }
}
```

### Error Case 2: Improper Handling of Special First Page URL Format
#### Problem Description
When the first page has a special URL format, but the `first` parameter is not correctly used or the starting page number (start) is set incorrectly, it can lead to data omission or duplication.

#### Example Code
```json
{
  "project_name": "{STU}.list",
  "url": {
    "pattern": "https://www.examplepharm.com/main/product-list.html?cId={category_id}&pn=(*).html",
    "iteration": {
      "first": "1",  // If the first page is special, should be set to actual conditions
      "start": 1,    // If the first page is special, start from the second page
      "stop": "{TotalPageNum}",
      "format": "{}"
    }
  }
}
```

### Error Case 3: Inaccurate TotalPageNum Setting
#### Problem Description
Hardcoding `TotalPageNum` as an estimated value, rather than dynamically obtaining the actual total number of pages.

#### Example Code
```json
{
  "project_name": "{STU}.list",
  "url": {
    "pattern": "https://www.examplemed.com/main/list.html?cId={category_id}&pn={page_number}",
    "iteration": {
      "start": 1,
      "stop": 5, // Assuming the total number of pages is 5, which may not match the actual situation
      "format": "{page_number}"
    }
  }
}
```

### Error Case 4: Improper URL Pattern Configuration
#### Problem Description
Forgetting to replace `{category_id}` or the page number placeholder `{page_number}` in the URL pattern, leading to the inability to access the correct pages.

#### Example Code
```json
{
  "project_name": "{STU}.list",
  "url": {
    "pattern": "https://www.examplemed.com/main/list.html?cId=&pn={page_number}",   // Forgot to replace `{category_id}`
    "iteration": {
      "start": 1,
      "stop": "{TotalPageNum}",
      "format": "{page_number}"
    }
  }
}
```
### Testing `list_step`
Accurately configuring `list_step`is key to extracting vital information from listing pages, setting the stage for in-depth content analysis and data processing. Tailor adjustments to the specific requirements of the target website to enhance accuracy and efficiency. Avoid common pitfalls such as incorrect starting page numbers and improper handling of unique first-page URLs. Such measures are imperative to ensure comprehensive and accurate data collection, pivotal for [extracting drug links](https://github.com/HzaCode/DP2-for-Beginners/blob/main/Jexter%20Configuration%EF%BC%9AExtract%20Page%20Information%20in%20the%20list_step%20.md) subsequently.
