 # Jexter Configuration - Get Total Pages

## Using Jexter to Extract the Total Number of Pages in `totalpage_step`
**Description:**
In the `totalpage_step`, Jexter is utilized to extract the total number of pages from a webpage, which is essential for planning the entire data extraction task. Here are several examples of using Jexter to extract this information, each tailored to different HTML structures.
### Example 1: Directly Locating Pagination Links

**HTML Structure:**
```html
<div class="pagination">
  <a href="?page=1">1</a>
  <a href="?page=2">2</a>
  <a href="?page=3">3</a>
  <a href="?page=4">4</a>
  <a href="?page=5">5</a>
  <a href="?page=6">Next</a>
</div>
```
**Jexter Configuration:**
```json
{
  "elements": {
    "TotalPageNum": "//div[@class='pagination']//a[5]"
  }
}
```
**Explanation:**
This configuration directly targets the last link in the pagination navigation, which usually points to the last page. By using the XPath expression `//div[@class='pagination']//a[5]`, we can directly obtain the text content of this link, which typically contains information about the total number of pages.

### Example 2: Extracting from Pagination Button Text

**HTML Structure:**
```html
<div class="pagination">
  <span class="page-info">Page 1 of 10</span>
</div>
```
**Jexter Configuration:**
```json
{
  "elements": {
    "TotalPageNum": "//div[@class='pagination']/span[@class='page-info']"
  }
}
```
**Explanation:**
In this configuration, we locate the `<span>` tag containing pagination information through an XPath selector. This tag usually contains the current page number and the total number of pages. Through this configuration, we can directly extract the total number of pages.

### Example 3: Extracting from Pagination Script in Static Examples

**HTML Structure:**
```html
<div class="pagination">
  <script>
    document.write("Total Pages: " + totalPages);
  </script>
</div>
```
**Jexter Configuration:**
```json
{
  "elements": {
    "TotalPageNum": "//div[@class='pagination']/script"
  }
}
```
**Explanation:**
In this static example, the pagination information is dynamically generated through a JavaScript script. The Jexter configuration obtains this information by selecting the `<script>` tag. This method is applicable in cases where pagination information is dynamically inserted into the page through JavaScript.

### Example 4: Extracting from Pagination URL Parameters

**HTML Structure:**
```html
<div class="pagination">
  <a href="?page=1">1</a>
  <a href="?page=2">2</a>
  <a href="?page=3">3</a>
  <a href="?page=4">4</a>
  <a href="?page=5">5</a>
  <a href="?page=6">Next</a>
</div>
```
**Jexter Configuration:**
```json
{
  "elements": {
    "TotalPageNum": "//div[@class='pagination']/a[last()]/@href"
  }
}
```
**Explanation:**
This configuration uses an XPath selector to find the last link in the list of pagination links, then retrieves its `href` attribute. In some cases, this attribute may contain information about the total number of pages, e.g., `href="?page=6"` might mean there are a total of 6 pages.

### Example 5: Handling Dynamically Loaded Pagination Information

**HTML Structure:**
```html
<div class="pagination">
  Total Pages: <span id="totalPages">10</span>
</div>
```
**Jexter Configuration:**
```json
{
  "elements": {
    "TotalPageNum": "//div[@class='pagination']/span[@id='totalPages']"
  }
}
```
**Explanation:**
In this example, the total number of pages is displayed directly on the page in text form, with a specific `id`. The Jexter configuration locates and extracts the total number of pages through this `id`.

### Example 6: Extracting Pagination Information from a Title

**HTML Structure:**
```html
<h2>Page 3 of 15</h2>
```
**Jexter Configuration:**
```json
{
  "elements": {
    "TotalPageNum": {
      "col": "//h2/text()",
      "function": {
        "regexp": "of (\\d+)",
        "type": "string"
      }
    }
  }
}
```
**Explanation:**
This configuration uses a regular expression to extract the total number of pages from the text of the title. The regular expression `"of (\\d+)"` matches the number that follows "of" in the title, which represents the total number of pages.

### Example 7: Leveraging the Link Parameter of the Last Page

**HTML Structure:**
```html
<div class="pagination">
  <a href="?page=1">1</a>
  <a href="?page=2">2</a>
  <a href="?page=last">Last</a>
</div>
```
**Jexter Configuration:**
```json
{
  "elements": {
    "TotalPageNum": "//div[@class='pagination']/a[@href='?page=last']/preceding-sibling::a[1]/text()"
  }
}
```
**Explanation:**
This configuration finds the link to the "Last" page using an XPath selector, then gets the text content of its previous sibling element (i.e., the second-to-last link), which usually contains the total number of pages.

### Example 8: Identifying the Last Page by the Disabled State of a Button

**HTML Structure:**
```html
<div class="pagination">
  <button>1</button>
  <button>2</button>
  <button disabled>Last</button>
</div>
```
**Jexter Configuration:**
```json
{
  "elements": {
    "TotalPageNum": "//div[@class='pagination']/button[@disabled]/preceding-sibling::button[1]/text()"
  }
}
```
**Explanation:**
In this configuration, we determine the total number of pages by locating the disabled button (usually the button for the last page). By obtaining the text content of this button's previous sibling element, we can find out the total number of pages.

### Example 9: Extracting from the Last Pagination Link with a Specific Class Name

**HTML Structure:**
```html
<div class="pagination">
  <a href="?page=1" class="page-link">1</a>
  <a href="?page=2" class="page-link">2</a>
  <a href="?page=3" class="page-link last">Last</a>
</div>
```
**Jexter Configuration:**
```json
{
  "elements": {
    "TotalPageNum": "//div[@class='pagination']/a[contains(@class, 'last')]/@href"
  }
}
```
**Explanation:**
This configuration locates the pagination link with the `last` class through an XPath selector. This class is typically used to indicate the last page. Then, we extract the total number of pages by obtaining the `href` attribute of this link.

### Example 10: Extracting from the Pagination Control's Data Attribute

**HTML Structure:**
```html
<div class="pagination" data-total-pages="20"></div>
```
**Jexter Configuration:**
```json
{
  "elements": {
    "TotalPageNum": "//div[@class='pagination']/@data-total-pages"
  }
}
```
**Explanation:**
In this configuration, we directly extract the total number of pages from the `data-total-pages` attribute of the pagination control.

These examples showcase methods to extract pagination information from diverse HTML structures, encompassing techniques like direct positioning, text extraction, script parsing, URL analysis, dynamic content management, and leveraging specific attributes and states. Adjustments might be necessary to accurately extract the total page number before constructing the dynamic URL in the  [`list_step` ](Study：list_step.md) , depending on the webpage's unique structure and content.
