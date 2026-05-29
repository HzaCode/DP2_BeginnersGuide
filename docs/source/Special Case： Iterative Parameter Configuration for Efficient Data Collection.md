# Special Case: Iterative Parameter Configuration



Iterative parameter configuration is a critical aspect that allows for systematic navigation through multi-page data sources in the [`list_step`](Study：list_step.md).




 **A typical configuration**

```json
{
  "project_name": "{STU}.list",
  "url": {
    "pattern": "https://www.examplemed.com/main/list.html?cId={category_id}&pn={page_number}.html",
    "iteration": {
      "start": 1,
      "stop": "{TotalPageNum}",
      "format": "{page_number}"
    }
  }
}
```

This configuration specifies the project name, URL pattern with dynamic placeholders for category ID and page number, and the iteration parameters that dictate the start and stop conditions for the data collection process.

**Common Errors and Detailed Examples**

1. **Incorrect Start Value**
   - **Problem Description**: Setting the `start` value to a number greater than 1 can result in missing data from the initial pages.
   - **Incorrect Example**:
     ```json
     {
       "iteration": {
         "start": 2,
         "stop": "{TotalPageNum}",
         "format": "{page_number}"
       }
     }
     ```
     This is incorrect because it skips the first page.
  

2. **Special First Page Handling**
   - **Problem Description**: If the first page has a unique URL format, not accounting for this can lead to data omission or duplication.
   - **Incorrect Example**:
     ```json
     {
       "url": {
         "pattern": "https://www.examplepharm.com/main/product-list.html?cId={category_id}&pn=(*).html",
         "iteration": {
           "first": "1",
           "start": 2,
           "stop": "{TotalPageNum}",
           "format": "{}"
         }
       }
     }
     ```
     This is incorrect when it assumes the first page is standard and starts iteration from the second page.
 

3. **Hardcoded Total Page Number**
   - **Problem Description**: Assuming a fixed total number of pages (`TotalPageNum`) can lead to incomplete or excessive data collection.
   - **Incorrect Example**:
     ```json
     {
       "iteration": {
         "start": 1,
         "stop": 5,
         "format": "{page_number}"
       }
     }
     ```
     This is incorrect because it hardcodes the total page count.


4. **URL Placeholder Errors**
   - **Problem Description**: Forgetting to replace placeholders in the URL pattern can prevent the scraper from accessing the correct pages.
   - **Incorrect Example**:
     ```json
     {
       "url": {
         "pattern": "https://www.examplemed.com/main/list.html?cId=&pn={page_number}.html",
         "iteration": {
           "start": 1,
           "stop": "{TotalPageNum}",
           "format": "{page_number}"
         }
       }
     }
     ```
     This is incorrect because the `{category_id}` placeholder is missing from the URL.

**Conclusion**

Revisiting iterative parameter configuration and addressing common errors is crucial for maintaining the efficiency and accuracy of data collection tasks. By adhering to the correct approaches outlined above, you can avoid the pitfalls previously discussed and ensure a comprehensive and precise data extraction process. Always perform thorough testing to validate your configuration before deploying it in a live environment.
