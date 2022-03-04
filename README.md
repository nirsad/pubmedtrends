
# Table of Contents 
1. [Introduction and Project Description](README.md#Introduction%20and%20Project%20Description)
2. [Example Visualization](README.md#Example%20Visualization)
3. [Data Pipeline and Tools Used](README.md#Data%20Pipeline%20and%20Tools%20Used)
# Introduction and Project Description
- pubmedtrends.com succinctly describes the trends in medical literature. 
- A word cloud on the website ranks the most frequently used words in the top 1000 trending articles on PubMed. 
- A new cloud is automatically generated and posted to the website every week.
- Users can look through past clouds to view how the trends have shifted over time. 
- This project incorporates various aspects of the data lifecycle including data ETL, analysis, visualization, and project deployment.
# Example Visualization:
![Example cloud](static/Mar-03-2022.png)
# Data Pipeline and Tools Used
**General Overview**

This project 

1. HTML is taken from PubMed's trending webpages using the Python requests library
2. Titles from the trending articles are scraped from the HTML using Beautifulsoup 
3. Titles are cleaned using regular expressions and converted into a list of words
4. A word cloud is generated from the list of words and is rendered on the website

**Below is a Mermaid diagram of the pipeline**
``` mermaid
graph LR
    A{<a style='color:blue' href='https://pubmedtrends.com/'>pubmedtrends.com <br> server </br></a>} -->|Run Weekly| B>Airflow Scheduler]
    style B stroke:#f90,stroke-width:2px
    B --> |Task 1|D[getTitles.py]
    style D stroke:#f66,stroke-width:2px,stroke-dasharray: 5 5
    D --> E{<a style='color:blue' href='https://pubmed.ncbi.nlm.nih.gov/trending/'>pubmed.ncbi.nlm.nih.gov/<br>trending/</br></a>}
    E --> F[\Article Data<br>.CSV</br>/]
    F --> G
    B --> |Task 2|G[dataCleaning.py]
    B --> |Task 3|H
    style G stroke:#f66,stroke-width:2px,stroke-dasharray: 5 5
    G --> H[generateCloud.py]
    style H stroke:#f66,stroke-width:2px,stroke-dasharray: 5 5
    H --> |Return Cloud to Frontend|A
    B --> |Task 4|I[mongoingest.py]
    style I stroke:#f66,stroke-width:2px,stroke-dasharray: 5 5
    F --> I
    I --> J[(MongoDB <br>Data</br>Grows<br>Weekly</br.)]
```
