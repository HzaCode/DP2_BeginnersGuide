# Creating a Study

## Configuring `totalpage_step`

### Step Description

`totalpage_step` is a critical initial step in a study, responsible for determining the total number of pages in the data source. This step is crucial for planning the entire data extraction task as it dictates the number of pages to be processed in subsequent steps. Knowing the total number of pages aids in efficiently allocating resources, optimizing extraction strategies, and ensuring data integrity.

### Configuring the URL

When configuring the URL for `totalpage_step` on the DP2 platform, ensure that the URL points to a page containing pagination navigation. This page should display all pagination links or at least contain an element indicating the total number of pages. For example, if pagination links are presented in numerical form (e.g., page=1, page=2, ..., page=N), the URL might be the homepage of a list page.

### Data Input (`data_in`)

`totalpage_step` might not require data input from a previous step, especially when it is the first step in the study flow. In such cases, `data_in` can be empty for testing. Here are some examples:

**Example 1: No Previous Step Output**

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

**Example 2: Based on Previous Step Output**

```json

{
  "data_in": {
    "data_for_test": [
      {
        "categoryLink": "example-category-list" // Placeholder for a category link from a previous step
      }
    ]
  },
  "project_name": "{STU}.totalpage",
  "url": "https://www.example.com/news/{categoryLink}-0.htm", // Dynamic URL construction using categoryLink
  "type": "one-off",
  "priority": 2,
  "fetch_method": "direct",
  "method": "GET",
  "extra_data": {
    "linKey": "{categoryLink}" // Passing the categoryLink for further processing
  },
  "status": 1,
  "charset": "UTF-8",
  "charact_string_start": "",
  "charact_string_end": "",
  "pf_id": 1502,
  "data_out": [
    {
      "jpath": "" // JSON Path for extracting specific data from the response, left empty as an example
    }
  ],
  "interval": "86400", // Execution interval set to once every day
  "excluded_workers": "{excluded_workers}" // Workers to exclude from executing this task
}
```


In the examples above, the `extra_data` field is utilized to transmit output from this step (e.g., `categoryLink`) to the `list_step`, facilitating the construction of a dynamic URL.

### Setting Priority and Execution Frequency

Ensure the priority of `totalpage_step` is set high to run first at the beginning of the study. The execution frequency (interval) should be set based on the update frequency of the data source. For instance, if the data source is not frequently updated, a longer execution interval, such as once every day or once a week, can be set.

### Testing `totalpage_step`

On the DP2 platform, you can test the configuration of `totalpage_step`. During the testing process, ensure that the total number of pages is correctly returned and there are no errors or exceptions. If the test results do not meet expectations, adjustments to the URL or data input configurations may be necessary.

Through these detailed tutorial contents and examples, you will gain a deeper understanding of how to configure and test the `totalpage_step` in a study. Properly setting up this step is crucial for the seamless progression of the entire data extraction task.
