
 # Extracting Drug Information in `detail_step `

## Description

In this tutorial,  we will guide you through a detailed example, showing you how to configure Jexter to extract drug names, approval numbers, company names, attachment links, and drug reference information.

## Detailed Case Explanation

Let's assume you have a web page with the following structure, which contains drug information:

```html
<!-- Example HTML structure -->
<table>
    <tr>
        <td class="drug-name">Drug A</td>
        <td class="approval-number">[Batch 123456]</td>
        <td class="company-name">Company X</td>
    </tr>
    <tr>
        <td class="drug-name">Drug B</td>
        <td class="approval-number">[Batch 789012]</td>
        <td class="company-name">Company Y</td>
    </tr>
</table>
<div class="attachments">
    <a href="attachment1.pdf">Attachment 1</a>
    <a href="attachment2.pdf">Attachment 2</a>
</div>
<div class="reference">
    <p class="reference-cell">This is a detailed reference for Drug A.</p>
    <p class="reference-cell">This is a detailed reference for Drug B.</p>
</div>
```

We will extract the following details:

- Drug Name (drug_name)
- Approval Number (auth_num)
- Company Name (company)
- Attachment Links (attachments)
- Drug Reference Information (drug_reference)

## Jexter Configuration：

Here's a Jexter configuration file that targets the example HTML structure:

```json
{
  "elements": {
    "drug_name": {
      "col": "//td[@class='drug-name']"
    },
    "auth_num": {
      "col": "//td[@class='approval-number']",
      "function": {
        "regexp": "\\[Batch (\\d+)\\]",
        "type": "string",
        "return": [1]
      }
    },
    "company": {
      "col": "//td[@class='company-name']"
    },
    "attachments": {
      "innerHtml": "//div[@class='attachments']/a",
      "extract_attachments": {}
    },
    "drug_reference": {
      "innerHtml": "//div[@class='reference']/p"
    }
  }
}
```

## Explanation of Configuration

- `drug_name`: Uses XPath to select the `<td>` element with the class `drug-name` to extract the drug name.

- `auth_num`: Uses XPath to select the `<td>` element with the class `approval-number` and applies a regular expression to extract the approval number. The `return` array specifies the first capturing group, which is the number after "Batch".

- `company`: Uses XPath to select the `<td>` element with the class `company-name` to extract the company name.

- `attachments`: Uses `innerHtml` to select the `<a>` elements within the `<div>` with the class `attachments`. The `extract_attachments` field is used to process the extracted links.

- `drug_reference`: Uses `innerHtml` to select the `<p>` elements within the `<div>` with the class `reference` to extract the drug reference information.





This tutorial has provided guidance on using Jexter to extract drug information from web pages. After configuring your extraction rules, it's critical to review the output to ensure it aligns with your expectations. If discrepancies are identified,  fine-tune the XPath expressions and regular expressions to more accurately mirror the structure of the target web page before saving your settings. This step is pivotal before proceeding to the [last study step](Study：%20attachment_step.md), ensuring the integrity and accuracy of the data collection process.
