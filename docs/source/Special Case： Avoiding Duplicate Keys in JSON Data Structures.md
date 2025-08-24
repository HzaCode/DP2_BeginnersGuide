# Special Cases: Avoiding Duplicate Keys

When configuring [Jexter](Jexter%20Configuration：Extracting%20Drug%20Information%20in%20'detail_step'.md)
, correctly representing complex data relationships is crucial. This not only helps maintain data consistency and readability but also avoids potential data loss issues. This tutorial will illustrate how to avoid using duplicate key names through a specific example, demonstrating the correct method of representing data using nested structures and the `default` key.

## Common Issue: Using Duplicate Key Names

In JSON and similar data structures, key names should be unique. If an object contains duplicate key names, typically only the last key-value pair will be retained, with the previous ones being overwritten. This can lead to data loss or configuration errors.



Consider the following Jexter configuration, which attempts to specify alternative query paths by reusing the `default` key:

```json
{
  "authNumber": {
    "path": "PrimaryQueryPath",
    "default": "AlternativeQueryPath1",
    "default": "AlternativeQueryPath2"
  }
}
```

In this configuration, although the intention is to list two alternative paths, only the last one (`"AlternativeQueryPath2"`) will be recognized and retained due to the `default` key being duplicated. This method results in the first alternative path (`"AlternativeQueryPath1"`) being ignored, leading to potential configuration errors.

##  Using Nested Structures and the `default` Key

To correctly represent a main path and its alternative paths, we should use a nested structure and utilize a unique `default` key at each nested level. This approach not only avoids the issue of duplicate key names but also clearly represents the hierarchical relationship between the data.


Here is an improved configuration that correctly uses the `default` key to specify alternative paths through a nested structure:

```json
{
  "authNumber": {
    "path": "PrimaryQueryPath",
    "default": {
      "path": "AlternativeQueryPath1",
      "default": {
        "path": "AlternativeQueryPath2"
      }
    }
  }
}
```

In this configuration:

- The top-level `"authNumber"` object specifies the main query path `"PrimaryQueryPath"`.
- The first `"default"` key introduces the first alternative path `"AlternativeQueryPath1"`.
- Within the object for the first alternative path, another `"default"` key is used to specify the second alternative path `"AlternativeQueryPath2"`.

Through this method of multiple nesting, we clearly define a main path and two levels of alternative paths, with each level using a unique `default` key. This structure maintains the clarity and logic of the configuration while avoiding the problem of duplicate key names.

## Conclusion

When designing and maintaining Jexter configurations, avoiding duplicate key names is very important. By using nested structures and maintaining the uniqueness of key names at each level, we can clearly and logically represent complex data relationships, while avoiding data loss and configuration errors.
