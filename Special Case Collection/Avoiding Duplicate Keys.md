## Avoiding Duplicate Keys and Correctly Using Nesting

When dealing with JSON data, we often encounter scenarios that require the expression of complex data structures. These scenarios may include data with multiple levels of hierarchy or the need to represent multiple similar data points at the same level. Properly constructing and maintaining these structures is crucial for ensuring data consistency and readability. This tutorial will demonstrate how to avoid duplicate keys and correctly use nesting to address common JSON structure issues through a specific example.

### The Issue with Duplicate Keys

In a JSON object, keys serve as unique identifiers for accessing their corresponding values. If an object contains two identical keys, it leads to a structural error because, typically, only the last key-value pair will be retained upon parsing. This can result in data loss or incorrect data representation.

### Solving Complex Data Relationships with Nesting

Nesting objects and arrays within JSON is a powerful tool for representing complex data relationships. By nesting, we can create multiple levels within a larger object, each with its unique set of key-value pairs, allowing for precise representation of data structures.

### Example: Correctly Constructing a Complex JSON Structure

Consider a scenario where we need to represent an auth_num object in JSON that contains information related to an approval number. We want to include a primary query path and an alternative query path for use when the primary path is unavailable.

The incorrect approach would be trying to include two default keys at the same level, as shown below:

```json
{
"auth_num": {
"col": "Primary query path",
"default": "Alternative query path 1",
"default": "Alternative query path 2"
}
}
```

The correct structure should use nesting to avoid duplicate keys and clearly express the alternative query paths, as follows:

```json
{
"auth_num": {
"col": "//p[contains(., '【批准文号】')]/text()",
"default": {
"col": "substring-after(//p[contains(., '【批准文号】国药准字')], '【批准文号】')",
"default": {
"col": "//p[contains(., '【批准文号】')]/text()"

}
}
}

}
```

In this improved structure, `auth_num` is an object containing a `col` and a `default` key. The `default` key itself is another object, containing a `col` and a `default` key again, forming a clear, non-duplicate key nested structure. This not only resolves the issue of duplicate keys but also makes the data structure's intentions more clear, understandable, and maintainable.

### Conclusion

Ensuring the uniqueness of each key at its level of hierarchy is vital when designing and maintaining JSON structures. Using nested objects and arrays helps us represent complex data structures while keeping the data clear and consistent. Avoiding duplicate keys and correctly utilizing nesting are key steps in ensuring the validity and usability of JSON data.
