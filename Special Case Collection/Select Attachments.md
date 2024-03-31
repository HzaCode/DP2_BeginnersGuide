#   Select Attachments

In this tutorial, we'll  demonstrate how to effectively use Jextor for HTML attachments data extraction. This process is briefly introduced in our [DP2 for Beginners](https://github.com/HzaCode/DP2-for-Beginners/blob/main/Jexter%20Configuration%EF%BC%9AExtracting%20Drug%20Information%20in%20'detail_step'.md) guide, especially for extracting detailed information from HTML. 

Here is a simplified HTML page example containing the product details section, which includes images, contact information, the official website link, and the company logo.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Product Details Page</title>
</head>
<body>
    <div>
        <h1>Product Details</h1>
        <dl class="pro_detail_op">
            <dt>Product Images</dt>
            <dd>
                <img src="http://www.example.com/image1.jpg" alt="Product Image 1">
                <img src="http://www.example.com/image2.jpg" alt="Product Image 2">
            </dd>
            <dt>Special Image</dt>
        
            <dd><img src="http://www.example.com/special_image.jpg" alt="Special Image"></dd>
            <dt>Contact Information</dt>
            <dd>
                <a href="tencent://message/?uin=328836088&Site=Songlu&Menu=yes">Contact Us</a>
            </dd>
            <dt>Official Website Link</dt>
            <dd>
                <a href="https://www.example.net">Visit Official Website</a>
            </dd>
            <dt>Company Logo</dt>
            <dd>
                <img src="http://www.example.com/logo.svg" alt="Company Logo">
            </dd>
        </dl>
    </div>
</body>
</html>

```

### Jextor Configuration and Extraction Results
 Below are three different Jextor configurations and their corresponding extraction results.

#### Basic Extraction Configuration
This configuration will extract all content within `<dl class="pro_detail_op">`.

```json
{
  "attachments": {
    "innerHtml": "//dl[@class='pro_detail_op']",
    "extract_attachments": {}
  }
}
```

#### Extraction Results (Basic Extraction)
```json
{
  "attachments": [
    {
      "task_fp": "...",
      "dp2_id": 32866965,
      "title": "Product Image 1",
      "link": "http://www.example.com/image1.jpg",
      "type": "jpg"
    },
    {
      "task_fp": "...",
      "dp2_id": 32866966,
      "title": "Product Image 2",
      "link": "http://www.example.com/image2.jpg",
      "type": "jpg"
    },
    {
      "task_fp": "...",
      "dp2_id": 32866967,
      "title": "Special Image",
      "link": "http://www.example.com/special_image.jpg",
      "type": "jpg"
    },
    {
      "task_fp": "...",
      "dp2_id": 32866968,
      "title": "Company Logo",
      "link": "http://www.example.com/logo.svg",
      "type": "svg"
    }
  ]
}
```

#### Configuration to Exclude Specific Type Attachments
This configuration will exclude SVG type attachments, extracting only JPG images.

```json
{
  "attachments": {
    "innerHtml": "//dl[@class='pro_detail_op']",
    "extract_attachments": {
      "types_excluded": ["svg"]
    }
  }
}
```

#### Extraction Results (Exclude SVG)
```json
{
  "attachments": [
    {
      "task_fp": "...",
      "dp2_id": 32866965,
      "title": "Product Image 1",
      "link": "http://www.example.com/image1.jpg",
      "type": "jpg"
    },
    {
      "task_fp": "...",
      "dp2_id": 32866966,
      "title": "Product Image 2",
      "link": "http://www.example.com/image2.jpg",
      "type": "jpg"
    },
    {
      "task_fp": "...",
      "dp2_id": 32866967,
      "title": "Special Image",
      "link": "http://www.example.com/special_image.jpg",
      "type": "jpg"
    }
  ]
}
```

#### Configuration for Extracting Image Links Within Specific Sub-elements
This configuration will only extract image links within `<dt>` tags.

```json
{
  "attachments": {
    "innerHtml": "//dl[@class='pro_detail_op']/dt/img",
    "extract_attachments": {}
  }
}
```

#### Extraction Results (Specific Sub-elements)
```json
{
  "attachments": [
    {
      "task_fp": "...",
      "dp2_id": 32866967,
      "title": "Special Image",
      "link": "http://www.example.com/special_image.jpg",
      "type": "jpg"
    }
  ]
}
```

### Conclusion
Through these configuration examples, you can see how to use Jextor to customize data extraction strategies. You can choose the appropriate configuration based on the actual HTML structure and requirements to extract the needed data.
