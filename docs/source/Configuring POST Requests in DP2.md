
When handling specific automation tasks, configuring the correct request parameters is crucial. These `steps` may involve extracting data from specific web pages, or sending data to services to retrieve the necessary information. This tutorial will guide you through configuring a `step` to perform a POST request with a concrete example for better understanding and application.

## Example Overview

In this example, we will configure a task aimed at sending a POST request to a specific URL to search for the keyword "Cyanamide". This task will be accomplished through specified request parameters, including the request type, priority, data, cookies, etc.

## Configuring Basic Information

Firstly, we need to define the basic properties of the task, including the project name, request type, priority, and the request's URL. This information informs the `dp2` system of the task's basic structure and objectives.

```json
{
  "project_name": "YOUR_PROJECT.list",
  "type": "one-off",
  "priority": 2,
  "url": "https://www.target-website.org/protocol/IProtocol/search"
}
```

Replace `YOUR_PROJECT` with your actual project name, and `url` with the actual URL of the target website.

## Setting Request Method and Data

For a POST request, we need to specify the `method` as `POST` and provide the data to be sent. In this example, the data is the keyword "Cyanamide".

```json
{
  "method": "POST",
  "data": [
    "{keyword}"
  ]
}
```

## Defining Cookies and Headers

To ensure the request is correctly processed by the target website, it may be necessary to simulate a real browser request. This includes setting appropriate cookies and request headers.

```json
{
  "cookies": {
    "headers": {
      "Content-Type": "application/json; charset=UTF-8",
      "referer": "https://www.target-website.org/",
      "user-agent": "A_SPECIFIC_USER_AGENT_STRING"
    }
  }
}
```

Replace the values for `referer` and `user-agent` as needed. The `Content-Type` is usually `application/json` but may vary according to the requirements of the target website.

## Additional Configurations

Furthermore, you can configure other options such as character set, execution interval, as well as special identifiers for specific tasks (e.g., `pf_id`).

```json
{
  "status": 1,
  "charset": "UTF-8",
  "interval": "86400",
  "pf_id": 1985
}
```



## Complete Configuration Example 

Below is a complete configuration example based on the steps above:

```json
{
  "data_in": {
    "data_for_test": [
      {
        "keyword": "Cyanamide"
      }
    ]
  },
  "project_name": "YOUR_PROJECT.list",
  "url": "https://www.target-website.org/protocol/IProtocol/search",
  "type": "one-off",
  "priority": 2,
  "fetch_method": "direct",
  "method": "POST",
  "cookies": {
    "headers": {
      "Content-Type": "application/json; charset=UTF-8",
      "referer": "https://www.target-website.org/",
      "user-agent": "A_SPECIFIC_USER_AGENT_STRING"
    }
  },
  "data": [
    "{keyword}"
  ],
  "status": 1,
  "charset": "UTF-8",
  "interval": "86400",
  "pf_id": 1985
}
```

Note that the actual application's `project_name`, `url`, `user-agent`, and other specific values need to be adjusted according to your specific requirements.

By following the steps above, you can configure the correct POST request task for the `dp2` system to automatically obtain or submit the required data.
