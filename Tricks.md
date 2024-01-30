# Tricks (Continuously Updated)

1. **Save MainPage Last**: Ensure to save the main page at the end to avoid incorporating data from other websites.
2. **Reparse Instead of Download**: Opt for reparsing rather than downloading; refresh data and wait for **`HasNew1`** to indicate new content.
3. **Post-Modification Steps**: After modifications, conduct a batch reparse, execute `HasNew1`, and then push the study.
4. **Data Structure Integrity**:
    - Include the **`dp2_id`** field by default in the **`detail`** structure to avoid reference errors in **`data_out`**.
5. **Data Processing Workflow Update**:
    - Simply altering **`study`** isn't enough for updating data; it requires **`HasNew1`**, followed by a **`push study`**.
6. **Using `dp2_id`**:
    - The **`dp2_id`** is a unique identifier for each detail page, different from **`category_id`** which might repeat across multiple pages.
    - In MongoDB, use **`dp2_id`** as the unique identifier for data entry.
7. **Managing Multi-Step Task Parameters**:
    - In tasks with multiple steps, pass necessary parameters through **`extra_data`**.
8. **Understanding Fields in `TASK`**:
    - Extract diverse fields like **`TASK_url`** and **`TASK_extra_data`** from **`TASK`**.
    - Employ **`TASK_extra_data`** for extracting information such as **`category_id`**.
9. **Project Names and Task Correlation**:
    - One **`project_name`** may include many **`tasks`**, each with its unique **`id`**.
10. **Using `TASK_extra_data` in Jextor**:
    - In Jextor, use **`TASK_extra_data`** to extract specific details like **`category_id`**.
