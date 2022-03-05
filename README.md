
# Table of Contents 
1. [Introduction and Project Description](#Introduction%20and%20Project%20Description)
2. [Example Visualization](#Example%20Visualization)
3. [Data Pipeline and Tools Used](#Data%20Pipeline%20and%20Tools%20Used)
4. [Development Process](
# Introduction and Project Description
- [pubmedtrends.com](https://pubmedtrends.com/) succinctly describes the trends in medical literature. 
- A word cloud on the website ranks the most frequently used words in the top 1000 trending articles on [PubMed.gov](pubmed.ncbi.nlm.nih.gov/trending/). 
- A new cloud is automatically generated and posted to the website every week.
- Users can look through past clouds to view how the trends have shifted over time. 
- This project incorporates various aspects of the data lifecycle including data ETL, analysis, visualization, and project deployment.
# Example Visualization:
![Example cloud](static/Mar-03-2022.png)
# Data Pipeline and Tools Used
**Overview**
This project's data pipeline involves several steps:

1. An Apache Airflow DAG is set to run weekly with each individial task being a single-threaded python script.
2. Task 1 is a webscraper that returns HTML from [PubMed's](pubmed.ncbi.nlm.nih.gov/trending/) first 100 trending webpages using the Python requests library. The HTML files are parsed using beatifulsoup and information about each trending article's title, authors, and journal citations are written to a csv file.

**Example Scraped Data**
| Title                  | Authors                  | Journal/Citation            |
|:-----------------------|:-------------------------|:----------------------------|
|Ribosome accumulation during early phase resistance training in humans.|Hammarström D, Øfsteng SJ, Jacobsen NB, Flobergseter KB, Rønnestad BR, Ellefsen S.|Acta Physiol (Oxf). 2022 Feb 25:e13806. doi: 10.1111/apha.13806. Online ahead of print.|
|Phosphate, pyrophosphate, and vascular calcification: a question of balance.|Villa-Bellosta R, Egido J.|Eur Heart J. 2017 Jun 14;38(23):1801-1804. doi: 10.1093/eurheartj/ehv605.|     
|Mucosal fungi promote gut barrier function and social behavior via Type 17 immunity.|Leonardi I, Gao IH, Lin WY, Allen M, Li XV, Fiers WD, De Celie MB, Putzel GG, Yantiss RK, Johncilla M, Colak D, Iliev ID.|Cell. 2022 Feb 16:S0092-8674(22)00075-7. doi: 10.1016/j.cell.2022.01.017. Online ahead of print.|
| Continued...                    |Continued...                       |Continued...                         |

4. Task 2 takes the scraped titles and 
5. Titles are cleaned using regular expressions and converted into a list of words
6. A word cloud is generated from the list of words and is rendered on the website

**A Mermaid diagram of the pipeline is shown below:**
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
# Development Process

