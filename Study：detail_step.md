# Creating a Study

## Configuring Detail Steps (`detail_step`) 

In the `detail_step` of a Study, you focus on obtaining more in-depth information from the detailed pages corresponding to each link extracted from the list page. Correctly configuring the `detail_step` is crucial for building a complete dataset and analysis.

### Step Description

The `detail_step` phase typically follows the `list_step` phase closely, where it is responsible for extracting specific data from the detailed page of each list item. This data may include, but is not limited to:

- Product ID (`dp2_id`)
- Company name (`company`)
- Product name (`drug_name`)
- Approval number (`auth_num`)
- Product specifications (`specification`)
- Product description (`drug_reference`)
- Attachments (`attachments`)

When configuring the `detail_step`, consider the structure of the target website to ensure that the Jexter configuration can accurately locate the required data elements.

### Example Configuration

Below is a typical example of a `detail_step` configuration, showing how to extract key information from a product page:

```json
{
  "data_in": {
    "data_for_test": [
      {
        "dp2_id": 12345678,
        "product_name": "Example Medication Name",
        "product_link": "https://www.examplepharm.com/product-detail?id=12345"   
      }
    ]
  },
  "project_name": "examplepharm.drugs.detail",
  "url": "{product_link}",
  "type": "one-off",
  "priority": 2,
  "fetch_method": "direct",
  "method": "GET",
  "status": 1,
  "charset": "UTF-8",
  "charact_string_start": "",
  "charact_string_end": "",
  "add_only": 1,
  "excluded_workers": "{excluded_workers}",
  "interval": 5184000,
  "data_out": {
    "jpath": "",
    "api": {
      "url": "http://api2.example.cn/dp2/mongo/save",   
      "table": "company.examplepharm.drugs",
      "type": "merge",
      "where": {
        "uniqueId": "{dp2_id}"
      }
    }
  }
}
```

In this configuration:

- `data_in` contains the product information passed from the `list_step` phase, including `dp2_id`, `product_name`, and `product_link`. Here, `12345678` is used as an example `dp2_id`, "Example Medication Name" as the product name, and `https://www.examplepharm.com/product-detail?id=12345` as the product link.
- `project_name` defines the name of the current Study, here using `examplepharm.drugs.detail` as an example.
- The `url` field uses the `{product_link}` placeholder, representing the URL of the detailed page.
- Fields such as `type`, `priority`, `fetch_method`, `method`, etc., define the type and priority of the request.
- The `data_out` field contains the details of the API call for saving the extracted data to the database. Here, the `merge` type is used, indicating that new data is merged into existing records.
- The `add_only` field is set to 1, meaning that if a record already exists, it will not be updated.

### Considerations

- Ensure that the links in `data_in` are valid and correctly point to the detailed pages.
- In `data_out`, use placeholders (e.g., `{dp2_id}`) to represent the data extracted from the detailed page, which will be replaced by the actual data during the extraction process.
- If the detailed page contains dynamically loaded content, you may need to adjust the `interval` field to give the page enough time to load all content.
- Perform thorough testing before actual deployment to ensure the configuration is correct and error-free.

By accurately configuring the detail_step, you can ensure that in the [next phase of extraction](https://github.com/HzaCode/DP2-for-Beginners/blob/main/Jexter%20Configuration%EF%BC%9AExtracting%20Drug%20Information%20in%20'detail_step'.md), the correct drug links are obtained, and the details of the information are [properly captured and saved](https://github.com/HzaCode/DP2-for-Beginners/blob/main/API%20Configuration%20Guide%20in%20DP2.md).
