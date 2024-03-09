#  Execution Order of Extraction with the Jextor in DP2

When exploring the use of Jextor within DP2, it becomes especially important to deeply understand how they function, their key concepts, and their execution order. These tools are designed to simplify and automate the process of extracting information from HTML or similarly structured documents. Let's revisit and familiarize ourselves with these key functions and steps to be able to configure data extraction rules efficiently and accurately, ensuring the capture of the desired data.

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

Below, we will illustrate these concepts of order with specific examples.
