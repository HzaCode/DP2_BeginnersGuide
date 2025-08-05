 # Step Configuration ① - Category Step
## Configuring `category_step`
### Step Description
Configuring the `category_step` in the DP2 system is the initial phase in the data extraction process, aimed at gathering category information from a website's category page. This step is crucial for laying the groundwork for subsequent extraction phases, such as retrieving data from list pages. Typically, this configuration requires only a single URL because the category page is often a static webpage that houses links to all categories. This process ensures a structured approach to data extraction by systematically categorizing and accessing the website's content through its category structure.


### Data Input (`data_in`)
In the `data_in` section, you need to provide test data to verify the effectiveness of your configuration. This might include example URLs or other relevant information to ensure the accuracy of your configuration.

### Defining Global Variables
Define global variables, such as `"STU"`, for reference throughout the configuration to ensure consistency and reusability of your configuration.

### Setting Project Name
The project name should clearly reflect its purpose and content. For example, using `{STU}.category` as the name helps differentiate between different extraction steps.

### Specifying the URL
Specify the `url` of the category page, ensuring it directly links to the page containing all category links.

### Configuring Data Output (`data_out`)
In the `data_out` field, define how the extracted data will be formatted and passed to the next step. Common processing methods include JMESPath or jq expressions.

### Example Configuration
Below is a typical example of a `category_step` configuration, demonstrating how to use the aforementioned parameters:

```json
{
  "STU": "company.example.drugs",
  "excluded_workers": [],
  "steps": [
    {
      "data_in": {
        "note": "",
        "data_for_test": {
          "note": ""
        }
      },
     "project_name": "{STU}.category",
      "url": "https://www.example.com/categories",
      "type": "one-off",
      "priority": 2,
      "fetch_method": "direct",
      "method": "GET",
      "status": 1,
      "charset": "UTF-8",
      "charact_string_start": "",
      "charact_string_end": "",
      "pf_id": 1765,
      "data_out": "",
      "interval": 86400,
      "excluded_workers": "{excluded_workers}"
    }
  ]
}

```

### Considerations

- **Unique Global Variables**: Ensure the value of "STU" is unique to avoid confusion with other studies in the system. This helps maintain clarity and ease of management for your project.

- **Testing Configuration Before Running**: Prior to initiating your data extraction process, it's crucial to ensure the accuracy of your setup with the DP2 platform's test feature. This can be done via the "Test Configuration Parameters" section within the interface. A successful check, confirming your setup is correct and free from errors, results in the creation of a new project. Within this **test project**, you have the opportunity to fine-tune the extraction parameters by setting up the [Jexctor configuration for 'category_step'](Jexter%20Configuration：Extracting%20the%20Category%20in%20'category_step'.md).



