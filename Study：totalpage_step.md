# Creating a Study

## Configuring the First Step (totalpage_step)

### Understanding the Purpose of totalpage_step

- **Step Description:**
  `totalpage_step` is the initial step in a Study, primarily aimed at determining the total number of pages in the data source. This step is critical for planning the entire data extraction task, as it dictates the number of pages that subsequent steps will need to process. Knowing the total number of pages aids in efficiently allocating resources, optimizing extraction strategies, and ensuring no data is missed.

### Configuring URL

- **Step Description:**
  On the DP2 platform, you need to specify a URL for `totalpage_step`, which should lead to a page containing pagination navigation. This page typically includes all pagination links, or at least elements indicating the total number of pages. For instance, if pagination links are displayed numerically, like `page=1`, `page=2`, ..., `page=N`, then this URL might be the homepage of a list page.

### Data Input (data_in)

- **Step Description:**
  Since `totalpage_step` is the first step in a Study, it usually does not require data input from a previous step. In this case, `data_in` can remain empty or contain some test data to verify the step's correctness. Test data can be static, for example, including an empty JSON object or a JSON object with test information.

### Setting Priority and Execution Frequency

- **Step Description:**
  The priority of `totalpage_step` should be set high to ensure it runs first when the Study begins. This can be achieved by assigning a high numeric value. The execution frequency (interval) can be set based on actual conditions, for example, if the data source is not frequently updated, you can set a longer interval, such as once every day or week.

### Example Configuration

- **Step Description:**
  ```json
  {
    "data_in": {
      "data_for_test": [
        {
          "Note": "This is a test note for totalpage_step"
        }
      ]
    },
    "project_name": "{STU}.totalpage",
    "url": "http://www.example.com/products.html",
    "type": "one-off",
    "priority": 10, // High priority to ensure it runs first
    "interval": "86400", // Run once every day
    "excluded_workers": "{excluded_workers}"
  }
  ```
  In this configuration, the `type` field is set to "one-off," indicating the step only needs to be executed once. The `priority` field is set to 10, a high priority value, ensuring this step runs first. The `interval` field is set to 86400 seconds (24 hours), meaning the step is executed once daily.

### Considerations

- **Considerations:**
  - Ensure the URL is correct and accurately reflects the data source's pagination structure. If the URL is incorrect, the step cannot execute properly.
  - Should the pagination structure of the data source change, promptly update the `totalpage_step` configuration to avoid extraction failures. This may include the pagination link URL pattern, the HTML structure of pagination buttons, etc.
  - It is advisable to conduct thorough testing before actual deployment to ensure `totalpage_step` correctly identifies and returns the total number of pages. During testing, check if the returned total number of pages matches expectations and if there are any errors or exceptions.

### Testing totalpage_step

- **Step Description:**
  On the DP2 platform, you can test the `totalpage_step` configuration. During testing, check if the total number of pages is correctly returned and if there are any errors or exceptions. If test results do not meet expectations, adjustments may be needed for the URL or data input configurations.

**Conclusion**
Through this section, you should understand the importance of `totalpage_step` and how to configure it. Properly configuring `totalpage_step` is the first step to ensuring the smooth execution of the entire Study.
