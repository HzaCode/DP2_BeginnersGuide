
# `prefix`, `postfix`, and `default`
When extracting data from web pages, it's often necessary to format the extracted data or ensure the flexibility and robustness of the data extraction process. Jextor offers several practical features such as `prefix`, `postfix`, and `default` to meet these needs. 

Imagine we aim to extract the name of a drug, the link to the drug's instruction manual, and the manufacturer information from a web page containing drug information. The web page's structure might slightly vary, for example, the drug name might be located within different HTML tags. Therefore, it's important to be able to flexibly extract the drug name from potentially multiple locations and format the extracted drug name appropriately.

## HTML Example

```html
<html>
<head>
    <title>Drug Information</title>
</head>
<body>
    <div class="drug-info">
        <h1>Aspirin</h1>
        <p>Manufacturer: <span>XX Pharma</span></p>
        <a href="instructions.pdf">Instruction Manual</a>
    </div>
    <!-- Alternative structure -->
    <div class="alternative-info">
        <span class="drug-name">Aspirin</span>
    </div>
</body>
</html>

```

## `prefix` and `postfix`

The `prefix` and `postfix` features allow the addition of custom text before and after the extracted data, respectively. This is especially useful for scenarios where the extracted data needs to be formatted, such as adding a clear identifier and additional information to the extracted drug name.

## Application Example

Our goal is to add the prefix "Drug Name:" and the postfix "[Details]" to the extracted drug name.

## Jextor Configuration

```json
{
    "elements": {
        "drugName": {
            "col": "//div[@class='drug-info']/h1/text()",
            "prefix": "Drug Name:",
            "postfix": " [Details]"
        }
    }
}

```

## Expected Result

```json
{
    "drugName": "Drug Name: Aspirin [Details]"
}

```

## `default`

The `default` feature provides an alternative extraction path. When the primary extraction path fails, it attempts to retrieve data from alternative paths, increasing the flexibility and success rate of data extraction.

## Application Example

Given possible variations in HTML structure, we incorporate the `default` feature to extract the drug name from an alternative structure if the primary path is unsuccessful.

## Jextor Configuration Adjustment

```json
{
    "elements": {
        "drugName": {
            "col": "//div[@class='drug-info']/h1/text()",
            "prefix": "Drug Name:",
            "postfix": " [Details]",
            "default": {
                "col": "//div[@class='alternative-info']/span[@class='drug-name']/text()"
            }
        }
    }
}

```

## Expected Result

If the primary path fails to extract data, the expected result from the alternative path would also be:

```json
{
    "drugName": "Drug Name: Aspirin [Details]"
}

```

To enhance the data extraction process's flexibility and robustness, especially for web pages with variable structures, utilizing these features is highly beneficial. It is critically important to ensure that  `default` configurations are [free from duplicate keys](Special%20Case：%20Avoiding%20Duplicate%20Keys%20in%20JSON%20Data%20Structures.md).
