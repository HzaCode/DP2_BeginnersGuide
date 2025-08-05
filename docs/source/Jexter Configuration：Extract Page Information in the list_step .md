# Jexter Configuration - Extract List Page Information

## Extract Page Information in the `list_step` 

In the `list_step` step of a Study, Jexter serves as a potent instrument for gleaning key data from list pages, such as names and links of products. Below, we detail examples showcasing Jexter's application across varied HTML structures encountered on numerous informational categorization sites.

### Example 1: Standard List Layout

**HTML Structure:**
```html
<ul class="category-list">
  <li>
    <span class="category-name">Cold Medicines</span>
    <a href="http://example.com/cold-medicines">View More</a> 
  </li>
  <!-- Additional categories -->
</ul>
```

**Jexter Configuration:**
```json
{
  "total_rows": "//ul[@class='category-list']/li",
  "elements": {
    "dp2_id": "TASK_id",
    "drug_name": "./span[@class='category-name']/text()",
    "link": {
      "col": ".//a/@href",
      "callback": "absolute_url"
    }
  }
}
```

**Explanation:**
This configuration targets each `<li>` element under `<ul class='category-list'>`, extracting both the category name and its link.

### Example 2: Grid Layout

**HTML Structure:**
```html
<div class="category-grid">
  <div class="category-cell">
    <div class="category-title">Vitamins</div>
    <a href="http://example.com/vitamins">Learn More</a>
  </div>
  <!-- Additional categories -->
</div>
```

**Jexter Configuration:**
```json
{
  "total_rows": "//div[@class='category-grid']/div[@class='category-cell']",
  "elements": {
    "dp2_id": "TASK_id",
    "drug_name": "./div[@class='category-title']/text()",
    "link": {
      "col": ".//a/@href",
      "callback": "absolute_url"
    }
  }
}
```

**Explanation:**
This configuration locates each `<div class='category-cell'>` within `<div class='category-grid'>`, to extract the category title and link.

### Example 3: Sidebar Menu Layout

**HTML Structure:**
```html
<div class="category-sidebar">
  <a href="http://example.com/antibiotics">Antibiotics</a>
  <a href="http://example.com/pain-relievers">Pain Relievers</a>
  <!-- More categories -->
</div>
```

**Jexter Configuration:**
```json
{
  "total_rows": "//div[@class='category-sidebar']//a",
  "elements": {
    "dp2_id": "TASK_id",
    "drug_name": "./text()",
    "link": {
      "col": "./@href",
      "callback": "absolute_url"
    }
  }
}
```

**Explanation:**
This setup directly targets each `<a>` link under `<div class='category-sidebar'>`, extracting the category name and link.

### Example 4: Tag Cloud Layout

**HTML Structure:**
```html
<div class="category-tags">
  <a href="http://example.com/antioxidants">Antioxidants</a>
  <a href="http://example.com/weight-loss">Weight Loss Products</a>
  <!-- More categories -->
</div>
```

**Jexter Configuration:**
```json
{
  "total_rows": "//div[@class='category-tags']//a",
  "elements": {
    "dp2_id": "TASK_id",
    "drug_name": "./text()",
    "link": {
      "col": "./@href",
      "callback": "absolute_url"
    }
  }
}
```

**Explanation:**
This configuration aims at each `<a>` element within `<div class='category-tags'>`, for extracting both the category name and link.

### Example 5: Waterfall Layout

**HTML Structure:**
```html
<div class="category-waterfall">
  <div class="category-item">
    <div class="category-title">Blood Pressure Medication</div>
    <a href="http://example.com/blood-pressure">View Details</a>
  </div>
  <!-- More categories -->
</div>
```

**Jexter Configuration:**
```json
{
  "total_rows": "//div[@class='category-waterfall']/div[@class='category-item']",
  "elements": {
    "dp2_id": "TASK_id",
    "drug_name": "./div[@class='category-title']/text()",
    "link": {
      "col": ".//a/@href",
      "callback": "absolute_url"
    }
  }
}
```

**Explanation:**
This setup specifically targets each `<div class='category-item'>` under `<div class='category-waterfall'>`, to extract the category title and link.

These examples showcase Jexter's adaptability in processing various HTML structures for category list pages. Choosing the right configuration to match the specific layout of the target website is crucial for effective category information extraction. Additionally, practical implementation may need to consider the dynamic loading characteristics of websites to guarantee precise data retrieval.The drug links extracted at this stage are vital for the crucial task of gathering drug information in the [next step](https://github.com/HzaCode/DP2-for-Beginners/blob/main/Study%EF%BC%9Adetail_step.md).
