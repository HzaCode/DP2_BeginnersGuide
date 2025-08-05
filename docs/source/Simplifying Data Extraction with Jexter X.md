
### Comprehensive Example

Suppose you need to extract drug names, batch numbers, production and expiration dates, manufacturer links, availability, and additional information from a webpage that contains a list of multiple drugs, each with detailed descriptions and images：

```html
<div class="drugs-container">
    <div class="drug-item">
        <h1>Drug Name 1</h1>
        <span class="batch-number">BN-1234</span>
        <span class="production-date">01/01/2023</span>
        <span class="expiration-date">01/01/2024</span>
        <a class="manufacturer-link" href="http://example.com/manufacturer1">Manufacturer 1 - Pharma Inc</a>
        <img src="http://example.com/drugs/images/drug1.jpg" />
        <div class="description">This is a description of Drug Name 1.</div>
        <span class="availability">In Stock</span>
        <div class="additional-info">Contains active ingredients A, B, C.</div>
    </div>
    <div class="drug-item">
        <h1>Drug Name 2</h1>
        <span class="batch-number">BN-5678</span>
        <span class="production-date">02/02/2023</span>
        <span class="expiration-date">02/02/2024</span>
        <a class="manufacturer-link" href="http://example.com/manufacturer2">Manufacturer 2 - BioHealth</a>
        <img src="http://example.com/drugs/images/drug2.jpg" />
        <div class="description">This is a description of Drug Name 2, with more details.</div>
        <span class="availability">Out of Stock</span>
        <div class="additional-info">Recommended for condition X, Y.</div>
    </div>
</div>
```
We will use all the core functions of Jexter to accomplish this task：

```json
{
  "parent": "//div[@class='drugs-container']",
  "total_rows": "//div[@class='drug-item']",
  "elements": {
    "drugs": [
      {
        "name": {
          "col": "./h1/text()",
          "callback": "trim"
        },
        "batch_number": {
          "col": "./span[@class='batch-number']/text()",
          "regexp": "\\w+-\\w+",
          "type": "string",
          "default": "N/A"
        },
        "production_date": {
          "col": "./span[@class='production-date']/text()",
          "callback": "trim|parse_date",
          "type": "string"
        },
        "expiration_date": {
          "col": "./span[@class='expiration-date']/text()",
          "callback": "trim|parse_date",
          "type": "string"
        },
        "manufacturer_link": {
          "col": "./a[@class='manufacturer-link']/@href",
          "type": "string"
        },
        "manufacturer_name": {
          "function": {
            "regexp": "(.+)\\s-\\s(.+)",
            "return": ["manufacturer_name", 1],
            "type": "string"
          }
        },
        "image": {
          "col": "./img/@src",
          "prefix": "http://example.com/drugs/images/",
          "type": "string"
        },
        "description": {
          "col": "./div[@class='description']/innerHtml()",
          "callback": "trim|extract_text",
          "type": "string"
        },
        "availability": {
          "col": "./span[@class='availability']/text()",
          "text": "Check Stock",
          "must_match": "In Stock",
          "default": "Out of Stock"
        },
        "additional_info": {
          "col": "./div[@class='additional-info']/text()",
          "postfix": " - More details available on request.",
          "type": "string"
        }
      }
    ]
  },
  "data_out": {
    "jq": ".drugs | map({name: .name, batch_number: .batch_number, production_date: .production_date, expiration_date: .expiration_date, manufacturer_link: .manufacturer_link, manufacturer_name: .manufacturer_name, image: .image, description: .description, availability: .availability, additional_info: .additional_info})"
  }
}
```

- `parent`: This function sets the absolute path for elements, allowing the relative paths in `elements` to be correctly resolved. In this example, it points to the container that holds all the drug information.
- `total_rows`: This function specifies the XPath path for all drug items. Jexter will traverse these paths to extract information for each drug.
- `elements`: This function defines the elements to extract and their structure. In this example, we define the drug's name, batch number, production date, expiration date, manufacturer link, image, description, availability, and additional information.
- `callback`: This function is used to further process the data after extraction. For example, `"trim"` is used to remove spaces at the beginning and end of a string, `"parse_date"` is used to convert a date string to a standard format, and `"extract_text"` is used to extract plain text.
- `regexp`: This function uses regular expressions to match and extract specific text patterns. For example, `"\\w+-\\w+"` is used to match batch numbers composed of letters and digits.
- `innerHtml`: This function is used to extract the full content of an HTML element, including all child elements. In this example, it is used to extract the drug description.
- `text`: This function directly returns a fixed string. In this example, it is used to set the default availability text.
- `function`: This function allows us to define a custom data processing function. In this example, we use it to extract the manufacturer's name from the text of the manufacturer link. The regular expression `"(.+)\\s-\\s(.+)"` matches two parts separated by spaces, and the `return` array specifies the second part (index 1) we want to extract, which is the manufacturer's name.
- `default`: This function provides a default value to use when `col` does not find data. In this example, it is used to set default values for the batch number and manufacturer's name.
- `must_match`: This function ensures that the extracted text matches a specified pattern. If not, the `default` value is used. In this example, it is used to ensure the drug is "In Stock".
- `prefix` and `postfix`: These functions add a specified string before and after the extracted text, respectively. In this example, `prefix` is used to build the full image link, and `postfix` is used to add extra text after the additional information.
- `data_out`: This function uses JMESPath syntax to format the final output. It maps the extracted data to a new JSON object and arranges it according to the specified structure.

### Conclusion

We have detailed all the core functions of Jexter and demonstrated how to combine these functions through a comprehensive example. This tutorial aims to help you better understand and utilize Jexter for efficient webpage data extraction.
