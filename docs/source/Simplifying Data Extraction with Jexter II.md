
# Simplifying Data Extraction with Jexter：`Parent`

In this tutorial, we will delve into the basic concepts of XPath and demonstrate through practical examples how to effectively use the `Parent` configuration in Jexter settings to simplify XPath expressions, improving the efficiency and accuracy of data extraction.

#### Common Forms of [XPath](XPath%20for%20DP2.md) Expressions Include:

- Absolute path: A path starting from the root element, for example, `/html/body/div`.
- Relative path: A path relative to the current element, for example, `./div/p`.
- Wildcard: Using `*` to represent any element, for example, `/html/*/div`.
- Conditional expression: Adding conditions with `[]`, for example, `//div[@class='example']`.

#### Simplifying XPath Using `Parent` Configuration

In Jexter settings, the `parent` configuration allows us to define a base XPath path, which serves as the starting point for all subsequent elements. By using `parent`, we can avoid repeating long paths, making the configuration more concise and easier to manage.

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
  <div class="overview">
    <h2>Overview</h2>
    <p>General information about the medicine</p>
  </div>
  <div class="details">
    <h2>Details</h2>
    <!-- Sub-sections for components, effects, etc. -->
  </div>
</div>
```

**Jexter Configuration**:

```yaml
parent: "//div[@class='medicine-page']/div[@class='overview'] | //div[@class='medicine-page']/div[@class='details']"
```

**Explanation**:
In this final example, the page is divided into an overview section and a detailed information section. The `parent` configuration enables the extraction of both general and detailed information about the medicine without redundant path specifications.

#### Conclusion

Using the `parent` configuration in Jexter settings not only simplifies XPath expressions but also enhances the structure and readability of your data extraction setup. By effectively leveraging this feature, you can streamline the extraction process, making it more efficient and adaptable to complex HTML structures.
