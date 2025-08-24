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
- **Extracting Details with Jexter**:
  - In Jexter, leverage **`TASK_extra_data`** to extract detailed information like **`category_id`**.

- **Focus on NMPA Approved Drugs**:
  - Prioritize drugs approved by the NMPA, especially those with a "National Medicine Permission" number. Exclude veterinary drugs and supplements. Use the NMPA website for verification if needed to ensure data accuracy and efficiency.
- **Data Association**:
  - When the project name (**`project_name`**) and URL remain the same, updates to new projects will automatically be associated with the original task (**`task`**) location.
- **Save JSON In Jexter**:
  - In Jexter, when you click on the configuration window, the content you see will be **`push`** ed to the next **`step`** and displayed in **`dataout`**. If needed, remember to **`Save the JSON`**. The test **`parse`** of each **`step`** is very important, so that the **`default`** parsing mechanism of Jexter is not used during the **`push`**.
- **Handling Pharmaceutical Product Information Leaflets**:
  - In the case of pharmaceutical product information leaflets, please ensure to directly extract and append them to the **`attachment`** field.
- **Multiple Link Handling for Data Input**:
  - When faced with the need to process multiple links, structure them as an array in the **`data_in`** field. This approach facilitates the generation of multiple next steps, each corresponding to a unique link in the array. 
