# Project Description
pubmedtrends.com succinctly describes the trends in medical literature. A simple word cloud appears on the website that shows the most frequently used words in the top trending articles on PubMed. A user may generate an updated word cloud at any time.
# Instructions to emulate website on local server
1. Clone this repository
2. Install and update any dependencies outlined in "server.py"
3. Run "server.py"
4. Go to any browser and type in 127.0.0.1:5000 as the url (This is the default location of the python flask local server)
# Process
1. HTML is taken from PubMed's trending webpages using the Python requests library
2. Titles from the trending articles are scraped from the HTML using Beautifulsoup 
3. Titles are cleaned using regular expressions and converted into a list of words
4. A word cloud is generated from the list of words and is rendered on the website

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

# Example of a wordcloud:
![Example cloud](static/Mar-03-2022.png)
