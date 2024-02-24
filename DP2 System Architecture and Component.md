# DP2 System Architecture and Component

## Study

In the DP2 platform, the **Study** function allows users to plan and execute data processing activities in a project-oriented manner. Each study instance is designed as an integrated project container, consisting of a series of well-defined steps. Each step targets a specific segment of the data processing workflow. The global variables defined in a [study](https://github.com/HzaCode/DP2-for-Beginners/blob/main/Study%EF%BC%9Acatogery_step.md) can be shared among steps, aiming to reduce repetitive configuration work, thereby improving the efficiency and flexibility of project execution. This design enables users to quickly adjust and optimize processing strategies for different data processing needs.

## Jexter

**Jexter** serves as the parsing engine within the DP2 platform, designed for structured data extraction from web pages. It utilizes [XPath](XPath%20for%20DP2.md), [jq](jq%20and%20JMESPath%20in%20DP2.md), and [JMESPath](jq%20and%20JMESPath%20in%20DP2.md), enabling a broad spectrum of data extraction techniques alongside tools for efficient web content retrieval. Jexter supports extensive data transformation capabilities and various output formats, providing a robust foundation for the data processing activities planned and executed in [Study](Study:list_step.md), ensuring its compatibility and integration within the DP2 system.

## Step

Within the framework of the DP2 system, a **Step** is the fundamental unit that constitutes the skeleton of a study, responsible for achieving specific objectives in the data processing flow. Each step contains a series of detailed configuration information, covering key aspects such as target URLs, HTTP request methods (GET or POST), data to be submitted, and cookies configuration. In addition, steps offer highly configurable solutions for data input ([Data In](Understanding%20Data%20Flow%20and%20Task%20Management.md)) and output ([Data Out](Understanding%20Data%20Flow%20and%20Task%20Management.md)), supporting advanced data querying and transformation operations using [JMESPath](jq%20and%20JMESPath%20in%20DP2.md) to accommodate complex data processing scenarios.

## Task

In the DP2 platform, a **Task** refers to an operational instance defined by steps, automatically assigned to designated worker nodes for execution. The types of tasks are extremely diverse, covering a range of operations from precise extraction of web content, deep parsing of data structures, to effective extraction of specific information. Upon completion, the output data from tasks can provide necessary input for subsequent steps or be directly stored in databases, supporting the continuous accumulation and [flow of data](Understanding%20Data%20Flow%20and%20Task%20Management.md).

## Elements

Within the framework of the DP2 system, a **Step** is the fundamental unit that constitutes the skeleton of a study, responsible for achieving specific objectives in the data processing flow. Each step contains a series of detailed configuration information, covering key aspects such as target URLs, HTTP request methods (GET or POST), data to be submitted, and cookies configuration. In addition, steps offer highly configurable solutions for data input ([Data In](Understanding%20Data%20Flow%20and%20Task%20Management.md)) and output ([Data Out](Understanding%20Data%20Flow%20and%20Task%20Management.md)), supporting advanced data querying and transformation operations using [JMESPath](jq%20and%20JMESPath%20in%20DP2.md) to accommodate complex data processing scenarios.
In the Jexter system, **[Elements](https://github.com/HzaCode/DP2-for-Beginners/blob/main/Simplifying%20Data%20Extraction%20with%20Jexter%20III%20.md)** refer to the configuration section that specifies which data to extract from web pages and how to extract it. Each element defines a data field, including its name and the rules or paths required to extract that data. These rules often utilize [XPath](XPath%20for%20DP2.md) expressions to precisely locate specific content on a web page, but can also include other processing instructions such as regular expression matching, text processing functions, etc., to accommodate complex data extraction needs.


## Worker Node

Worker nodes are the execution units within the DP2 data processing architecture, which can be built on physical servers or cloud-based virtual machines. By adopting a distributed technological architecture, DP2 efficiently distributes tasks across multiple worker nodes, significantly enhancing the speed and overall efficiency of data processing. This design ensures the system can handle large-scale data requests, guaranteeing high parallelism and quick response in [task processing](https://github.com/HzaCode/DP2-for-Beginners/blob/main/Understanding%20Data%20Flow%20and%20Task%20Management.md)
.

## Data Input (Data In) & Data Output (Data Out)

In the step configurations of DP2, the data input and output functions provide a flexible data flow scheme for the entire data processing workflow. The data input specifies the data foundation required before executing a task, which may include a fixed data set or data dynamically generated by a previous step. The data output defines the results produced after executing a step, which not only can support the execution of subsequent steps but can also be pushed to external databases through [API interfaces](API%20Configuration%20Guide%20in%20DP2.md) for storage. This flexible configuration option for data input and output enables the DP2 platform to effectively support complex data processing tasks and meet diverse business needs.

## XPath

**[XPath](XPath%20for%20DP2.md)** is a language used for locating information in XML and HTML documents. In Jexter, XPath expressions are extensively utilized for pinpointing and extracting elements from web pages. It enables users to precisely target nodes, attributes, or text within the document structure by defining specific paths. The power of XPath lies in its flexibility and expressive capability, capable of handling complex document structures. This includes selecting elements with specific attributes, traversing sibling or child elements, and applying conditional filtering, among others.

## JMESPath

**[JMESPath](jq%20and%20JMESPath%20in%20DP2.md)** is a language specifically designed for querying and transforming JSON data. It enables users to effectively filter, sort, and map data within complex JSON structures through a series of query expressions. By leveraging JMESPath, users can simplify the data extraction and transformation process, significantly improving the efficiency and accuracy of data processing.

## API (Application Programming Interface)

The DP2 platform provides strong [API interfaces](API%20Configuration%20Guide%20in%20DP2.md) support, allowing users to seamlessly integrate and push the results of data processing to external systems, such as various types of database systems. Moreover, DP2 also offers direct support for popular database systems (such as MySQL and MongoDB), further facilitating users' management and analysis work after data processing, enhancing the flexibility and breadth of data applications.



## Special Table Data Processing

Faced with specially formatted or constantly changing table data, the DP2 platform offers a flexible and powerful processing mechanism. By configuring precise XPath and JMESPath query rules, users can effectively extract key information from these changing tables, meeting specific data processing needs. This special data processing functionality allows the DP2 platform to handle various complex data scenarios, ensuring the accuracy and effectiveness of data extraction.

## Attachment Handling and Storage

Considering the need to process attachments in data processing tasks, the DP2 platform specifically provides functionality for downloading and storing attachments. The system supports securely processing and storing attachments as Object Storage Service (OSS) keys, ensuring data integrity and security. This feature offers convenience in handling data tasks that include attachments, enhancing the platform's data processing capabilities.

## Data Updates and Notifications

To keep users informed of the latest developments in data processing, the DP2 platform supports configuring real-time data update notification mechanisms. With simple settings, users can receive email or WeChat message notifications of data updates, allowing real-time monitoring of the status and results of data processing. This mechanism provides an efficient project management and monitoring tool for users, ensuring transparency and traceability in data processing activities.


