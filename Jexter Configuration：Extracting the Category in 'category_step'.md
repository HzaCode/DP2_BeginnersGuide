# Creating a Study
## Extracting the Category in `category_step` 


**Description:**
Within the DP2 system, `category_step` serves as a crucial step for extracting category information from web pages. This tutorial provides four examples to demonstrate how to use XPath expressions to extract category IDs across various HTML structures.

### Example 1: Extracting Category ID from Pagination Links

**HTML Structure:**
```html
<div class="w-pages">
  <a href="category-1-1.html">1</a>
  <a href="category-1-2.html">2</a>
  <a href="category-1-3.html">3</a>
  <!-- ... -->
  <a href="category-1-10.html" class="w-page-last">Last</a>
</div>
```

**Jexter Configuration:**
```json
{
  "elements": {
    "TotalPageNum": {
      "col": "//div[@class='w-pages']/a[not(contains(@class, 'w-page-next')) and not(contains(@class, 'w-page-last'))][last()]",
      "function": {
        "regexp": "(\\d+)",
        "type": "string"
      },
      "default": "1"
    },
    "category_id": {
      "col": "TASK_extra_data",
      "callback": "json_extract##category_id"
    }
  }
}
```

**Explanation:**
In this example, we utilize XPath to locate the last link in the pagination list (excluding "Next" and "Last" classes) and extract the number within as the total number of pages. The category ID is extracted from `TASK_extra_data`.

### Example 2: Extracting Category ID from Product Links

**HTML Structure:**
```html
<div class="w-prd-infobox">
  <h2><a href="product-123-1-456.html">Product Name</a></h2>
</div>
```

**Jexter Configuration:**
```json
{
  "elements": {
    "TotalPageNum": {
      "col": "//div[@class='w-pages']/a[not(contains(@class, 'w-page-next')) and not(contains(@class, 'w-page-last'))][last()]",
      "function": {
        "regexp": "(\\d+)",
        "type": "string"
      },
      "default": "1"
    },
    "category_id": {
      "col": "//div[contains(@class, 'w-prd-infobox')]/h2/a/@href",
      "function": {
        "regexp": "product-(\\d+)-(\\d+)-\\d+.html",
        "type": "string"
      }
    }
  }
}
```

**Explanation:**
In this example, we extract the category ID by parsing product links, assuming the link format is `product-<category_id>-<other_id>.html`.

### Example 3: Extracting Category ID from Pagination Text

**HTML Structure:**
```html
<div class="pageNum active">1</div>
<!-- ... -->
<div class="pageNum">10</div>
```

**Jexter Configuration:**
```json
{
  "elements": {
    "TotalPageNum": {
      "col": "//div[contains(@class, 'pageNum active')]/text()",
      "default": {
        "text": "0"
      }
    },
    "category_id": {
      "col": "TASK_extra_data",
      "callback": "json_extract##category_id"
    }
  }
}
```

**Explanation:**
In this example, we directly extract the total number of pages from pagination text. The method of extracting the category ID is the same as in Example 1.

### Example 4: Extracting Category ID from Data Attributes

**HTML Structure:**
```html
<div data-key="total">10</div>
<div data-key="category_id">123</div>
```

**Jexter Configuration:**
```json
{
  "elements": {
    "TotalPageNum": {
      "col": "//div[@data-key='total']",
      "function": {
        "regexp": "(\\d+)",
        "type": "string"
      }
    },
    "category_id": {
      "col": "//div[@data-key='category_id']",
      "function": {
        "regexp": "(\\d+)",
        "type": "string"
      }
    }
  }
}
```

**Explanation:**
In this example, we directly extract the total number of pages and the category ID from data attributes.

### Conclusion

Through these examples, we have showcased methods for extracting category information across different HTML structures.  In practice, you may need to adjust the XPath expressions based on the specific structure of the web pages.
