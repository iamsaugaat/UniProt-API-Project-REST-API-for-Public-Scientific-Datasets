# UniProt API Project – REST API for Public Scientific Datasets

## Overview
This project showcases the use of **REST APIs to integrate live scientific data into bioinformatics workflows**, focusing on **protein data retrieval, analysis, and visualization**.  
Using the UniProt public API, the project builds a **pipeline that automates querying, processing, and visualizing human proteins related to a given biological keyword (default: COVID).**

---

## Key Objectives
- **Integrate live external datasets:** Demonstrates how to connect and pull data from a large-scale biological REST API (UniProt).
- **Transform unstructured JSON into structured data:** Automated data cleaning and parsing into Pandas DataFrames.
- **Enable data-driven insights:** Using exploratory data analysis and dashboards to reveal trends in protein properties.
- **Create a scalable and reusable platform:** Streamlit app for interactive exploration, adaptable for any keyword or organism.

---

## Methodology

### 1. Data Acquisition (REST API)
- Queried UniProt using:
  - Filters: `organism_id:9606` (Homo sapiens)  
  - Keywords: default **COVID**, but user-defined in the dashboard.
- Retrieved fields:
  - Accession, Entry Name, Protein Name, Organism, and Length.

### 2. Data Wrangling
- Parsed raw JSON to clean structured tables.
- Stored protein metadata in Pandas DataFrames.

### 3. Exploratory Data Analysis
- Calculated descriptive statistics:
  - Number of retrieved proteins
  - Protein length distribution
  - Top proteins by sequence size
- Created visualizations:
  - Histograms showing protein size variability
  - Tabular views for detailed exploration

### 4. Interactive Dashboard (Streamlit)
- Filter by keyword and dynamically fetch fresh UniProt data.
- Live plots of protein properties.
- Top 10 longest proteins displayed in ranked tables.

<img width="1653" height="825" alt="Dashboard" src="https://github.com/user-attachments/assets/7d7703e2-3a97-4f6a-ae3f-7dafbb2fde0f" />

---

## Insights & Findings
From a sample query of **COVID-related human proteins**:
- **Number of proteins:** 35 (sample run)
- **Average protein length:** ~593 amino acids
- **Length variability:** Ranges from small regulatory proteins to large receptors (~1500 aa).
- **Notable long proteins:** NLRP1, TLR7, and ACE2, all of which are relevant in immune pathways.

These patterns confirm that protein length and associated domains are highly variable, which could be critical in **drug targeting and pathway analysis**.

---

## Recommendations
1. **Extendable Pipeline:** Can be scaled to include other public APIs (PDB for 3D structures, NCBI for gene expression).
2. **Integration in R&D:** Use this as an exploratory tool for research teams to quickly filter and explore protein families in therapeutic pipelines.
3. **Next Steps:**
   - Add gene names, functional annotations, and cross-references.
   - Implement local caching to improve speed for repeated queries.
   - Include download/export functionality (CSV/Excel).

---

## Value Delivered
- **Demonstrates ability to integrate live APIs** into a scientific workflow.
- Builds **reproducible and interactive tools** for research teams.
- Bridges **data engineering and biological insights**, making it a powerful asset for bioinformatics-driven organizations.

https://uniprot-api-project-rest-api-for-public-scientific-datasets-5q.streamlit.app/
---

## Tech Stack
- **Python** (requests, pandas)
- **Visualization:** Matplotlib, Seaborn
- **Web App:** Streamlit
- **Data Source:** UniProt REST API

---

## Run Locally
Clone the repository, install requirements, and run the Streamlit app:

```bash
pip install -r requirements.txt
streamlit run app.py
