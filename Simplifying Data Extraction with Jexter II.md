
# Simplifying Data Extraction with Jexter：`Parent`

In this tutorial, we will delve into the basic concepts of XPath and demonstrate through practical examples how to effectively use the `Parent` configuration in Jexter settings to simplify XPath expressions, improving the efficiency and accuracy of data extraction.

#### Common Forms of XPath Expressions Include:

- Absolute path: A path starting from the root element, for example, `/html/body/div`.
- Relative path: A path relative to the current element, for example, `./div/p`.
- Wildcard: Using `*` to represent any element, for example, `/html/*/div`.
- Conditional expression: Adding conditions with `[]`, for example, `//div[@class='example']`.

#### Simplifying XPath Using Parent Configuration

In Jexter settings, the parent configuration allows us to define a base XPath path, which serves as the starting point for all subsequent elements. By using parent, we can avoid repeating long paths, making the configuration more concise and easier to manage.

#### Example 1: Nested Structure of Medicine Information

**HTML Structure Example**:

```html
<div class="medicine">
  <h1>Medicine S</h1>
  <div class="details">
    <span class="category">Category: Antipyretic Analgesics</span>
    <div class="composition">
      <h2>Components</h2>
      <ul>
        <li>Component U</li>
        <li>Component V</li>
      </ul>
    </div>
    <div class="usage">
      <h2>Usage Method</h2>
      <p>Three times a day, one tablet each time</p>
    </div>
  </div>
</div>
```

**Jexter Configuration**:

```yaml
parent: "//div[@class='medicine']/div[@class='details']"
```

**Explanation**:
This structure contains nested `div` elements for different types of medicine information. The `parent` configuration helps focus on data extraction under `details`, such as components and usage methods, rather than the entire medicine information.

#### Example 2: Columnar Display of Medicine Components and Effects

**HTML Structure Example**:

```html
<div class="medicine-detail">
  <div class="left-column">
    <h3>Components</h3>
    <ul>
      <li>Component X</li>
      <li>Component Y</li>
    </ul>
  </div>
  <div class="right-column">
    <h3>Expected Effects</h3>
    <p>Relieves headache, reduces fever</p>
  </div>
</div>
```

**Jexter Configuration**:

```yaml
parent: "//div[@class='medicine-detail']/div[@class='left-column'] | //div[@class='medicine-detail']/div[@class='right-column']"
```

**Explanation**:
In this example, the components and effects of the medicine are placed in the left and right columns, respectively. The `parent` configuration allows us to locate these two different columns simultaneously for extracting the list of components and the description of expected effects.

#### Example 3: Medicine Reviews and User Ratings Combination

**HTML Structure Example**:

```html
<div class="reviews-section">
  <div class="review">
    <span class="user-name">User M</span>
    <span class="rating">Rating: 5 stars</span>
    <p class="comment">Very effective, minor side effects.</p>
  </div>
  <!-- More reviews -->
</div>
```

**Jexter Configuration**:

```yaml
parent: "//div[@class='reviews-section']/div[@class='review']"
```

**Explanation**:
In this example, each review includes the user name, rating, and comment text. The `parent` configuration targets each independent review, allowing for granular extraction and analysis of user feedback.

#### Example 4: Medicine Instructions and Warning Information

**HTML Structure Example**:

```html
<div class="instruction-section">
  <div class="usage-instructions">
    <h4>Usage Instructions</h4>
    <p>Dosage instructions...</p>
  </div>
  <div class="warnings">
    <h4>Warnings</h4>
    <ul>
      <li>Not for pregnant women</li>
      <li>Use with caution if allergic</li>
    </ul>
  </div>
</div>
```

**Jexter Configuration**:

```yaml
parent: "//div[@class='instruction-section']/div[@class='usage-instructions'] | //div[@class='instruction-section']/div[@class='warnings']"
```

**Explanation**:
This structure separates usage instructions and warning information, but both are part of the larger `instruction-section`. The `parent` configuration allows focusing on extracting information about usage instructions and warnings simultaneously.

#### Example 5: Multi-Functional Medicine Page

**HTML Structure Example**:

```html
<div class="medicine-page">
  <section class="overview">
    <h2>Overview</h2>
    <p>Medicine N is used for treating...</p>
  </section>
  <section class="details">
    <div class="composition">
      <h2>Components</h2>
      <ul>
        <li>Component A</li>
        <li>Component B</li>
      </ul>
    </div>
    <div class="effects">
      <h2>Effects</h2>
      <p>Description of treatment effects...</p>
    </div>
  </section>
  <section class="reviews">
    <h2>User Reviews</h2>
    <div class="review">...</div>
    <!-- More reviews -->
  </section>
</div>
```

**Jexter Configuration**:

```yaml
parent: "//div[@class='medicine-page']/section"
```

**Explanation**:
In this complex medicine page structure, the `parent` configuration is used to target each major `section`, including medicine overview, detailed components, effects, and user reviews. This method allows for segment-wise information extraction, suitable for content-rich pages.

#### Example 6: Medicine Purchase Options and Price Comparison

**HTML Structure Example**:

```html
<div class="purchase-options">
  <table>
    <thead>
      <tr>
        <th>Packaging Specification</th>
        <th>Price</th>
        <th>Supplier</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>10 tablets/box</td>
        <td>¥50</td>
        <td>Supplier A</td>
      </tr>
      <!-- More options -->
    </tbody>
  </table>
</div>
```

**Jexter Configuration**:

```yaml
parent: "//div[@class='purchase-options']/table/tbody"
```

**Explanation**:
This example uses the `parent` configuration to target different purchase options for the medicine, particularly suitable for extracting data from tables, such as price comparisons, packaging specifications, etc.

#### Example 7: Medicine Storage Conditions and Shelf Life

**HTML Structure Example**:

```html
<div class="storage-info">
  <h3>Storage Conditions</h3>
  <p>Store in a cool, dry place, away from direct sunlight.</p>
  <h3>Shelf Life</h3>
  <p>24 months</p>
</div>
```



**Jexter Configuration**:

```yaml
parent: "//div[@class='storage-info']"
```

**Explanation**:
Using the `parent` configuration for medicine storage conditions and shelf life information helps extract key storage requirements and expiration date information, crucial for ensuring safe use of the medicine.

#### Example 8: Medicine Indications and Contraindications

**HTML Structure Example**:

```html
<div class="indication-contra">
  <section class="indication">
    <h4>Indications</h4>
    <p>Used for treating...</p>
  </section>
  <section class="contraindications">
    <h4>Contraindications</h4>
    <ul>
      <li>Not for pregnant women</li>
      <li>Not for patients with heart disease</li>
    </ul>
  </section>
</div>
```

**Jexter Configuration**:

```yaml
parent: "//div[@class='indication-contra']/section"
```

**Explanation**:
This example shows how to separately locate and extract information on medicine indications and contraindications, important for medical professionals and consumers to understand the significance and restrictions of medicine use.

#### Example 9: Medicine Ratings and Institutional Certification

**HTML Structure Example**:

```html
<div class="ratings-certifications">
  <div class="ratings">
    <h5>User Ratings</h5>
    <p>4.5/5 stars</p>
  </div>
  <div class="certifications">
    <h5>Certifications</h5>
    <img src="certified.png" alt="Institutional Certification">
  </div>
</div>
```

**Jexter Configuration**:

```yaml
parent: "//div[@class='ratings-certifications']/div"
```

**Explanation**:
In this example, the `parent` configuration is used to extract information on medicine user ratings and institutional certifications obtained, crucial for establishing consumer trust and assurance of medicine quality.

#### Example 10: Medicine-Related Research and Literature References

**HTML Structure Example**:

```html
<div class="research-literature">
  <h6>Related Research</h6>
  <ul>
    <li>
      <a href="study1.pdf">Research Report 1</a>
    </li>
    <li>
      <a href="study2.pdf">Research Report 2</a>
    </li>
  </ul>
</div>
```

**Jexter Configuration**:

```yaml
parent: "//div[@class='research-literature']/ul"
```

**Explanation**:
This example leverages the `parent` configuration to extract links to medicine-related research and literature, providing important resources for users conducting academic research or seeking in-depth understanding of the medicine background.

Through these examples, we've shown how the parent configuration simplifies and improves data extraction for various webpage structures. By setting a base XPath, it reduces redundancy and increases extraction accuracy, making the data collection process more efficient and manageable, especially for complex or extensive webpages.
