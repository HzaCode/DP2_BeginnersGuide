# Locating Data in DP2 Using XPath

XPath, short for XML Path Language, is a language designed for locating information within XML and HTML documents. It facilitates the navigation through elements and attributes, proving indispensable for precise data retrieval in data extraction tasks.

### Basics of XPath

XPath expressions allow for the selection of nodes, including elements, attributes, text, and more. Below are basic XPath expressions and their functions:

- `//element`: Selects all nodes named `element` within the document.
- `/element`: Targets all `element` nodes directly under the root node.
- `element[@attribute]`: Finds all `element` nodes with a specific attribute.
- `element[@attribute='value']`: Chooses all `element` nodes where the attribute equals `value`.
- `element/text()`: Retrieves the text content of `element` nodes.
- `element/child::node()`: Selects the child nodes of `element`.

### Advanced Usage

XPath's capabilities extend to using logical operators (`and`, `or`), axes (`ancestor`, `descendant`, `following-sibling`), and functions (`contains()`, `starts-with()`, `not()`) for crafting complex queries.

1. **Logical Operators:**
   ```xpath
   //input[@type='submit' or @type='button']
   ```
   This selects all `input` elements with a `type` attribute of either 'submit' or 'button'.

2. **Using Axes:**
   ```xpath
   //div/ancestor::form
   ```
   This expression finds `form` ancestors of `div` elements.

3. **Applying Functions:**
   ```xpath
   //h2[contains(text(),'News')]
   ```
   It selects `h2` elements containing the text 'News'.

### Applying XPath in DP2

In DP2, XPath expressions are specified as data selectors for precise data extraction. For instance:

```json
{
  "elements": {
    "postTitle": {
      "col": "//div[contains(@class, 'post-title')]/text()",
      "type": "string"
    },
    "link": {
      "col": "//a/@href",
      "type": "string"
    }
  }
}
```

Here, `postTitle` is configured to extract text from `div` elements with 'post-title' class, and `link` extracts the `href` attribute from all links.

Here are some additional practical examples of using XPath to extract specific types of information:

### [Extracting Drug Information in ` detail_step `：](Jexter%20Configuration：Extracting%20Drug%20Information%20in%20'detail_step'.md)

- **Select `<td>` elements with the class 'drug-name':**
  ```xpath
  //td[@class='drug-name']
  ```
- **Select `<td>` elements with the class 'approval-number':**
  ```xpath
  //td[@class='approval-number']
  ```
- **Select `<td>` elements with the class 'company-name':**
  ```xpath
  //td[@class='company-name']
  ```
- **Select `<a>` elements within `<div>` elements with the class 'attachments':**
  ```xpath
  //div[@class='attachments']/a
  ```
- **Select `<p>` elements within `<div>` elements with the class 'reference':**
  ```xpath
  //div[@class='reference']/p
  ```

### [Extract the Total Number of Pages in `totalpage_step`：](Jexter%20Configuration：Extract%20the%20Total%20Number%20of%20Pages%20in%20`totalpage_step`.md)

- **Locate the last link in pagination (excluding "Next" and "Last"):**
  ```xpath
  //div[@class='pagination']//a[5]
  ```
- **Extract total page count from `<span>` within pagination info:**
  ```xpath
  //div[@class='pagination']/span[@class='page-info']
  ```
- **Extract total page count from pagination script in static pages:**
  ```xpath
  //div[@class='pagination']/script
  ```

### [Extracting the Category in `category_step`：](Jexter%20Configuration：Extracting%20the%20Category%20in%20'category_step'.md)


- **Extracting Category Name from Parent Box Element:**
   ```xpath
   //div[contains(@class, 'p_parentBox')]/a/text()
   ```

- **Extracting Category Name from Form Middle Content:**
   ```xpath
   //div[contains(@class, 'formMiddleContent482')]//a/text()
   ```


- **Extracting Category Name from Web Component Menu:**
   ```xpath
   //div[@class='w-com-menu-in']/ul/li/div/a/text()
   ```

### [Extract Page Information in `list_step`：](Jexter%20Configuration：Extract%20Page%20Information%20in%20the%20list_step%20.md)

- **Select `<li>` elements within `<ul>` elements with the class 'category-list':**
  ```xpath
  //ul[@class='category-list']/li
  ```

- **Select `<div>` elements within `<div>` elements with the class 'category-grid':**
  ```xpath
  //div[@class='category-grid']/div[@class='category-cell']
  ```

- **Select `<a>` elements within `<div>` elements with the class 'category-sidebar':**
  ```xpath
  //div[@class='category-sidebar']//a
  ```

- **Select `<a>` elements within `<div>` elements with the class 'category-tags':**
  ```xpath
  //div[@class='category-tags']//a
  ```

- **Select `<div>` elements within `<div>` elements with the class 'category-waterfall':**
  ```xpath
  //div[@class='category-waterfall']/div[@class='category-item']
  ```

### Resource Link

Explore XPath further with this handy resource:

- [XPath Cheatsheet](https://devhints.io/xpath)

This cheat sheet offers a quick reference for XPath syntax and functions, ideal for quick consultations during practical applications.

### Summary

XPath serves as a robust tool for data location and extraction in DP2, enabling precise targeting of document elements. When setting up DP2 configurations, thorough testing of XPath expressions is crucial to ensure they precisely target the intended elements.
