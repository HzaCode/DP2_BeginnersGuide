#  Select Drug Category Links
This tutorial will demonstrate how to use Jextor configurations to handle specific HTML structures, with a particular emphasis on selecting links. This process is basically introduced in our [DP2 for Beginners](Jexter%20Configuration：Extracting%20the%20Category%20in%20'category_step'.md) guide, while in this tutorial, we will explore a special case, namely how to filter links.





#### Sample Web Page Structure

Assume the target webpage's HTML structure is as follows:

```html
<div class="com_main bg3">
  <div>
    <div>
      <ul>
        <li>All Categories</li>
        <li>
          <a href="https://www.examplepharma.com/categories/list.html?catid=123">Antiviral Drugs</a>
        </li>
        <li>
          <a href="https://www.examplepharma.com/categories/list.html?catid=456">Cardiac Protection Drugs</a>
        </li>
        <li>Other Categories</li> <!-- This is the last element we don't need -->
      </ul>
    </div>
  </div>
</div>
```

#### XPath Expression

To extract the category names and links in the middle (excluding the first and last `li` elements), we use the following XPath expression:

```
//div[@class='com_main bg3']/div[1]/div[1]/ul/li[position()>1 and position()<last()]
```

#### Data Extraction Configuration

Based on the provided structure, we define the following  configuration for data extraction:

```json
{
  "total_rows": "//div[@class='com_main bg3']/div[1]/div[1]/ul/li[position()>1 and position()<last()]",
  "elements": {
    "category": "./a/text()",
    "link": {
      "col": "./a/@href",
      "callback": "absolute_url"
    },
    "category_id": {
      "col": "./a/@href",
      "function": {
        "regexp": "catid=(\\d+)",
        "type": "string"
      },
      "post_process": "return data.match(/catid=(\\d+)/)[1]"
    }
  }
}
```

#### Example Extraction Results

With the above configuration and HTML structure, we expect the following extraction results:

```json
[
  {
    "category": "Antiviral Drugs",
    "link": "https://www.examplepharma.com/categories/list.html?catid=123",
    "category_id": "123"
  },
  {
    "category": "Cardiac Protection Drugs",
    "link": "https://www.examplepharma.com/categories/list.html?catid=456",
    "category_id": "456"
  }
]
```

#### Result Explanation

This result is a JSON array, where each object represents a drug category. For each category, we provide three key pieces of information:

- `category`: The name of the drug category, such as "Antiviral Drugs" or "Cardiac Protection Drugs".
- `link`: A link to the list of drugs in that category.
- `category_id`: The category ID extracted from the link, represented as the value of the query parameter `catid`.

Through this tutorial, we demonstrated how to extract drug category information from webpages with specific HTML structures,  with a particular emphasis on link selection.
