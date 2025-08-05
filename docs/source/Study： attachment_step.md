# Step Configuration ⑤ - Attachment Step
## Configuring the Attachment Handling Step (`attachment_step`)

**Description:**
In the DP2 system, `attachment_step` is designed for processing and saving attachments extracted from the detail page (`detail_step`). These attachments often include images, PDF files, or other multimedia content. The following tutorial will guide you on how to configure `attachment_step` to properly process and save these attachments.

### Prepare Attachment Data

In the `data_in` field, you need to provide relevant information about the attachments. This typically includes the task's unique identifier (`task_fp`), the DP2 ID (`dp2_id`), title (`title`), link (`link`), and file type (`type`).

###  Set the Project Name

Use `{STU}.attachments` as the project name in the `project_name` field, where `{STU}` is your study template's unique identifier.

###  Specify the Attachment Link

Use `{link}` as a placeholder in the `url` field, which will be replaced with the attachment's link during runtime.

###  Configure the API Request

Set `type` to `one-off`, indicating this is a single-use task. Set `fetch_method` to `direct`, indicating direct data fetching. Set `method` to `GET`, as attachments are typically downloaded via GET requests.

###  Handle Attachment Download

In the `data_out` field, use `jpath` `{key:key}` to extract the attachment's OSS key. This will be used for subsequent database updates.

###  Update Database Records

Specify the database URL, table name, unique identifier (`where`), and the data to be updated in the `api` field. Here, we use `data.oss_keys.{row_idx}.key` to update the attachment OSS key in the database.

### Sample Configuration

Below is a sample attachment_step configuration for reference:

```json
{
  "data_in": {
    "jpath": "attachments",
    "data_for_test": {
      "attachments": [
        {
          "task_fp": "b23166330ad46c070a293085a2b340b6",
          "dp2_id": 123456,
          "title": "Example Product",
          "link": "https://example.com/upload/2021-09-06/example.JPG",
          "type": "jpg"
        }
      ]
    }
  },
  "project_name": "{STU}.attachments",
  "url": "{link}",
  "type": "one-off",
  "priority": 2,
  "fetch_method": "direct",
  "method": "GET",
  "status": 1,
  "charset": "UTF-8",
  "add_only": 1,
  "excluded_workers": "{excluded_workers}",
  "interval": 5184000,
  "data_out": {
    "note": "jpath only extracts key, masks the attachment task's own dp2_id",
    "note2": "Writes the corresponding oss address into oss_keys, separated from the attachments field",
    "jpath": "{key:key}",
    "api": {
      "url": "http://api2.example.com/save/v2",
      "table": "company.example.drugs",
      "where": {
        "uniqueId": "{dp2_id}"
      },
      "data": {
        "data.oss_keys.{row_idx}.key": "{key}"
      }
    }
  },
  "pf_id": 1792
}
```
With this configuration, you can ensure that attachment data is correctly downloaded and saved to the database. Configuring the attachment_step requires [precise mapping](API%20Configuration%20Guide%20in%20DP2.md) of attachment information and ensuring they are correctly associated with records in the database. Before running live, do not forget to **conduct testing** to verify the setup works as intended and to catch any issues before they affect your data collection process.
