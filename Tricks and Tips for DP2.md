# Tricks and Tips for DP2 (Continuously Updated)



- **Save MainPage Last**: Always prioritize saving the main page last to prevent the inclusion of data from external sources.
- **Reparse Instead of Download**: Opt for reparsing over downloading to refresh data; wait for the **`HasNew1`** signal to confirm new content before proceeding.
- **Post-Modification Workflow**: After making changes, initiate a batch reparse, run **`HasNew1`**, and then push the study to apply updates.
- **Maintaining Data Structure Integrity**:
  - Incorporate the **`dp2_id`** field into the **`detail`** structure by default to prevent reference errors in **`data_out`**.
- **Updating Data Processing Workflow**:
  - Merely updating the **`study`** is insufficient for data refresh; execute **`HasNew1`** and then **`push study`** to ensure updates are applied.
- **Utilizing `dp2_id`**:
  - The **`dp2_id`** serves as a unique identifier for each detail page, unlike the **`category_id`** which can be repeated across pages.
  - In MongoDB, employ **`dp2_id`** as the primary unique identifier for data entries.
- **Managing Multi-Step Task Parameters**:
  - For tasks involving multiple steps, transmit essential parameters via **`extra_data`**.
- **Extracting Information from `TASK`**:
  - Extract various fields such as **`TASK_url`** and **`TASK_extra_data`** from the **`TASK`** object.
  - Use **`TASK_extra_data`** to retrieve specific details, including **`category_id`**.
- **Project and Task Correlation**:
  - A single **`project_name`** may encompass numerous **`tasks`**, each with a unique **`id`**.
- **Extracting Details with Jextor**:
  - In Jextor, leverage **`TASK_extra_data`** to extract detailed information like **`category_id`**.

- **Focus on NMPA Approved Drugs**:
  Prioritize drugs approved by the NMPA, especially those with a "National Medicine Permission" number. Exclude veterinary drugs and supplements. Use the NMPA website for verification if needed to ensure data accuracy and efficiency.

