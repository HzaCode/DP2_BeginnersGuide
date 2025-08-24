#  Execution Order of Extraction with the Jexter in DP2

When exploring the use of Jexter within DP2, it becomes especially important to deeply understand how they function, their key concepts, and their execution order. These tools are designed to simplify and automate the process of extracting information from HTML or similarly structured documents. Let's revisit and familiarize ourselves with these key functions and steps to be able to configure data extraction rules efficiently and accurately, ensuring the capture of the desired data.

### Data Location

- **parent**: Sets a starting node, providing context for subsequent queries. This helps to limit the scope of data extraction to a specific area of the HTML, enhancing the efficiency and accuracy of the query.
- **total_rows**: Pre-defines the number of data rows to be extracted, aiding in verifying data integrity in advance or adjusting extraction logic to ensure the data meets expectations.

### Specific Extraction Rules

- **elements**: Defines a series of extraction rules for specific elements or attributes within the HTML, which is central to the configuration process. The precision of these rules will directly impact the quality of the final data.

### Execution Order of Extraction Logic

Within the defined **elements**, data extraction and processing follow this order:

1. **col**: First, select data columns. This typically involves specifying an XPath path to locate HTML elements or extract their attribute values.
2. **regexp**: Then, execute regular expression matching on the data selected by col, mainly used for data cleaning or extracting text in a specific format.
3. **innerHtml**: This step aims to extract the full HTML content of the selected element, suitable for scenarios where maintaining HTML tag structure or extracting rich text content is necessary.
4. **text**: Insert direct text values, often used to add static information or as a supplement to the data.

### Data Processing Functions

- **callback**: Allows the use of custom processing functions to format or transform the extracted data in complex ways.
- **function**: Process data through predefined functions, executing operations.
- **default**: Specify default values for data that could not be successfully extracted, ensuring the completeness of the final data structure.

### Other Key Concepts

- **must_match**: Ensures only data that meets specific criteria is included in the final results during the data row extraction phase.
- **prefix** and **postfix**: Used to add formatting content before or after the final extracted text, such as adding a domain prefix to links or appending parameter suffixes.

Below, we will demonstrate how to employ Jexter's various functions in a sequential and layered manner to achieve precise and clean data extraction results.

#### HTML Source Example

```html
<div id="drug-details">
  <h1>Acetaminophen</h1>
  <p>Active ingredient: Paracetamol</p>
  <p>Dosage: 500mg, twice daily</p>
  <p>Manufacturer: Pharma Inc., since 1992</p>
  <p>Certification: <strong>Approved</strong> by Health Authority</p>
  <img src="acetaminophen.png" alt="Acetaminophen image">
  <a href="/more-info" class="external">More Info</a>
</div>
```

####  Jexter Configuration and Execution Order

1. **Parent Selection**

   To focus our extraction on the relevant section, we define a parent node that encompasses all the drug information:

   ```json
   "parent": "//*[@id='drug-details']"
   ```

2. **Element Extraction and Processing Order**

   Within this context, we outline a series of specific extraction rules. These rules not only identify what data to extract but also how to clean, transform, and format it to meet our requirements:

   ```json
   "elements": {
     "drug_name": {
       "col": "./h1"
     },
     "active_ingredient": {
       "col": "./p[contains(text(), 'Active ingredient')]",
       "regexp": "Active ingredient: (.+)"
     },
     "dosage": {
       "col": "./p[contains(text(), 'Dosage')]",
       "function": {
         "regexp": "Dosage: ([\\dmg]+), ([a-zA-Z ]+)",
         "return": ["$1 taken $2"],
         "type": "string"
       }
     },
     "manufacturer": {
       "col": "./p[contains(text(), 'Manufacturer')]",
       "regexp": "Manufacturer: (.+), since [\\d]+",
       "callback": "trim"
     },
     "certification": {
       "col": "./p/strong",
       "callback": "extract_text"
     },
     "image_url": {
       "col": "./img/@src",
       "prefix": "https://example.com/images/",
       "default": {
         "text": "https://example.com/images/default.png"
       }
     }
   
   }
   ```

3. **Data Out Manipulation**


 ```json
  "data_out": {
  "jq": "map_values(if . == null then \"N/A\" else . end)"
}
```

#### Expected JSON Output

The application of the specified Jexter configuration to our HTML source should yield a JSON object like this:

```json
{
  "drug_name": "Acetaminophen",
  "active_ingredient": "Paracetamol",
  "dosage": "500mg taken twice daily",
  "manufacturer": "Pharma Inc.",
  "certification": "Approved",
  "image_url": "https://example.com/images/acetaminophen.png",
}

```



This section integrates and emphasizes the sequential application of Jexter's extraction and processing functions, providing a structured approach to handling complex data extraction needs. Through the comprehensive scenario, we've demonstrated the utility of `parent` for scope limitation, `elements` for data selection and extraction, and `data_out` for final data manipulation. This approach allows for the efficient and precise capture of structured data from HTML sources, showcasing the depth of customization and control offered by Jexter within DP2.
