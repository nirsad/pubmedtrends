# pubmedtrends
A website succinctly describing the trends in medical literature.
# Instructions to emulate website on local server
1. Install and update any dependencies outlined in "server.py"
2. Run "server.py"
3. Go to any browser and type in 127.0.0.1:5000 as the url (This is the default location of the python flask local server)
# Description

'''mermaid
graph LR
    A{<a style='color:blue' href='https://pubmed.ncbi.nlm.nih.gov/trending/'>pubmed.ncbi.nlm.nih.gov/<br>trending/</br></a>} -->|HTML| B[getTitles.py]
    style B stroke:#f66,stroke-width:2px,stroke-dasharray: 5 5
    B --> |Titles|C[(Article Data<br>.CSV</br>)]
    C -->D[dataCleaning.py]
    style D stroke:#f66,stroke-width:2px,stroke-dasharray: 5 5
    D -->|Words| E[generateCloud.py]
    style E stroke:#f66,stroke-width:2px,stroke-dasharray: 5 5
    E -->|Cloud|F{<a style='color:blue' href='https://pubmedtrends.com/'>pubmedtrends</a>}
    G[User Feedback] -->F
    %%H[User Generates Cloud] -->F-->A
    F -->|User Clicks to Generate Cloud|A
    '''
