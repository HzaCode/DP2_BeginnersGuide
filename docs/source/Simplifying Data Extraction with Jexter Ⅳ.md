

In this tutorial, we'll summarize the usage of three key aspects in Jexter: `total_row`, `parent`, and `elements`. These concepts work together to simplify the configuration process and enhance the efficiency and accuracy of drug data extraction from web pages.

### Total Row: Defining the Total Number of Drugs to Extract

`total_row` is utilized to specify the total number of drugs to extract from a list. This is especially useful for pages containing extensive lists of drugs. By setting `total_row`, you can control the scope of data extraction, ensuring that only the necessary information is retrieved, thus avoiding redundancy.

**HTML Example:**
```html
<table class="drug-list">
  <tr>
    <td>Aspirin</td>
    <td>100mg</td>
  </tr>
  <tr>
    <td>Ibuprofen</td>
    <td>200mg</td>
  </tr>
  <!-- More drugs -->
</table>
```

**Jexter Configuration:**
```json
{
  "total_row": "//table[@class='drug-list']/tr[position()<=20]",
  "elements": {
    "name": "./td[1]/text()",
    "dosage": "./td[2]/text()"
  }
}
```

**Extraction Result:**
```json
[
  {
    "name": "Aspirin",
    "dosage": "100mg"
  },
  {
    "name": "Ibuprofen",
    "dosage": "200mg"
  }
  // Up to 20 records
]
```

In this example, `total_row` effectively limits the extraction process to the first 20 drugs in the list.

### Parent: Streamlining the XPath Configuration

`parent` defines a base XPath, setting a common starting point for extracting all related drug information. This approach streamlines the configuration by eliminating the need to repeat the base path for each data element, thus making your configuration more concise and manageable.

**HTML Example:**
```html
<div class="drug-info">
  <h2>Amoxicillin</h2>
  <p class="desc">Amoxicillin is an antibiotic used to treat various infections.</p>
  <span class="indication">Commonly prescribed for infections of the respiratory tract and skin.</span>
</div>
```

**Jexter Configuration:**
```json
{
  "parent": "//div[@class='drug-info']",
  "elements": {
    "name": "./h2/text()",
    "description": "./p[@class='desc']/text()",
    "indication": "./span[@class='indication']/text()"
  }
}
```

**Extraction Result:**
```json
{
  "name": "Amoxicillin",
  "description": "Amoxicillin is an antibiotic used to treat various infections.",
  "indication": "Commonly prescribed for infections of the respiratory tract and skin."
}
```

Using `parent` simplifies specifying the XPaths for each element by setting a common reference point.

### Elements: Specifying Drug Information to Extract

Within the `elements` section of the Jexter configuration, you define what specific information to extract. This setup uses XPath expressions, which can be relative to the `parent` XPath if defined, to identify the exact data points within the webpage.

**HTML Example:**
```html
<div class="drug-detail">
  <p class="name">Lisinopril</p>
  <p class="ingredient">Active Ingredient: Lisinopril Dihydrate</p>
  <p class="warning">Warning: May cause dizziness or fainting.</p>
</div>
```

**Jexter Configuration:**
```json
{
  "parent": "//div[@class='drug-detail']",
  "elements": {
    "name": "./p[@class='name']/text()",
    "ingredient": "./p[@class='ingredient']/text()",
    "warning": "./p[@class='warning']/text()"
  }
}
```

**Extraction Result:**
```json
{
  "name": "Lisinopril",
  "ingredient": "Active Ingredient: Lisinopril Dihydrate",
  "warning": "Warning: May cause dizziness or fainting."
}
```

In this setup, `elements` are defined relative to the `parent` to efficiently extract the desired information.

### Combining the Three Aspects for Efficient Drug Data Extraction

When `total_row`, `parent`, and `elements` are used together, they form a robust configuration for drug data extraction.

**HTML Example:**
```html
<div class="drug-catalog">
  <div class="drug-item">
    <h3>Metformin</h3>
    <p class="dosage">500mg, 850mg, 1000mg</p>
    <div class="indication">Used to treat type 2 diabetes.</div>
  </div>
  <!-- More drug items -->
</div>
```

**Jexter Configuration:**
```json
{
  "total_row": "//div[@class='drug-catalog']/div[@class='drug-item']",
  "parent": "//div[@class='drug-item']",
  "elements": {
    "name": "./h3/text()",
    "dosage": "./p[@class='dosage']/text()",
    "indication": "./div[@class='indication']/text()"
  }
}
```

**Extraction Result:**
```json
[
  {
    "name": "Metformin",
    "dosage": "500mg, 850mg, 1000mg",
    "indication": "Used to treat type 2 diabetes."
  }
  // Additional drugs as per configuration
]
```
