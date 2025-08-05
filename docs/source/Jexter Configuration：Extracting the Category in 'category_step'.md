# Jexter Configuration - Extract Category Information
## Extracting the Category in `category_step` 


**Description:**
Within the DP2 system, `category_step` serves as a crucial step for extracting category information from web pages. In this tutorial, we will detail how to extract category links from HTML pages using Jextor. We will demonstrate the use of Jextor configuration through three examples, each targeting a specific HTML structure and extraction requirement. This will help you understand how to write and apply Jextor configurations according to your specific situations.

### Example 1: Extracting Elements with a Specific Class Name

Suppose we have the following HTML fragment, containing two `div` elements with product information, each with a `p_parentBox` class:

```html
<div class="p_parentBox">
  <a href="https://www.example.com/product/12345/">Antitumor Medication</a>
</div>
<div class="p_parentBox">
  <a href="https://www.example.com/product/67890/">Cardiovascular Drugs</a>
</div>
```

To extract the product category, link, and category ID from these elements, we can use the following Jextor configuration:

```json
{
  "total_rows": "//div[contains(@class, 'p_parentBox')]",
  "elements": {
    "category": ".//a/text()",
    "link": {
      "col": ".//a/@href",
      "callback": "absolute_url"
    },
    "category_id": {
      "col": ".//a/@href",
      "function": {
        "regexp": "/product/(\\d+)/",
        "type": "string"
      }
    }
  }
}
```

The expected extraction results are as follows:

```json
[
  {
    "category": "Antitumor Medication",
    "link": "https://www.example.com/product/12345/",
    "category_id": "12345"
  },
  {
    "category": "Cardiovascular Drugs",
    "link": "https://www.example.com/product/67890/",
    "category_id": "67890"
  }
]
```

### Example 2: Extracting Elements with a Specific Path Structure in the Link

Consider the following HTML fragment, containing a link to a specific product:

```html
<div class="formMiddleContent482">
  <a href="https://www.example.com/path/0_482_54321.html">Anti-infection Drugs</a>
</div>
```

To extract the product category, link, and category ID defined by the link path structure, we can use the following configuration:

```json
{
  "total_rows": "//div[contains(@class, 'formMiddleContent482')]//a",
  "elements": {
    "category": {
      "col": "./text()",
      "callback": "text"
    },
    "link": {
      "col": "./@href",
      "callback": "absolute_url"
    },
    "category_id": {
      "col": "./@href",
      "function": {
        "regexp": "0_482_(\\d+).html",
        "type": "string"
      }
    }
  }
}
```

This will produce the following extraction results:

```json
[
  {
    "category": "Anti-infection Drugs",
    "link": "https://www.example.com/path/0_482_54321.html",
    "category_id": "54321"
  }
]
```

### Example 3: Extracting Category ID Using Data Attributes

Finally, consider the following HTML fragment, where elements are marked with a `data-cateid` attribute identifying the category ID:

```html
<div class="w-com-menu-in">
  <ul>
    <li data-cateid="98765">
      <div><a href="https://www.example.com/product/98765/">Healthcare Products</a></div>
    </li>
    <li data-cateid="54321">
      <div><a href="https://www.example.com/product/54321/">Traditional Chinese Medicine</a></div>
    </li>
  </ul>
</div>
```

We can extract the product category, link, and category ID through the following Jextor configuration:

```json
{
  "total_rows": "//div[@class='w-com-menu-in']/ul/li",
  "elements": {
    "category": "./div/a/text()",
    "link": {
      "col": "./div/a/@href",
      "callback": "absolute_url"
    },
    "category_id": {
      "col": "./@data-cateid",
      "type": "string"
    }
  }
}
```

The expected extraction results are as follows:

```json
[
  {
    "category": "Healthcare Products",
    "link": "https://www.example.com/product/98765/",
    "category_id": "98765"
  },
  {
    "category": "Traditional Chinese Medicine",
    "link": "https://www.example.com/product/54321/",
    "category_id": "54321"
  }
]
```
In these three examples, we've shown how to use Jextor for extracting data from different HTML page structures within the `category_step` . Following the data extraction, the subsequent step is to determine the total number of pages, which is done in the [`totalpage_step` ](Study：totalpage_step.md).
