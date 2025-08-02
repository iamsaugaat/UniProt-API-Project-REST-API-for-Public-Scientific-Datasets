import streamlit as st
import pandas as pd
import requests
import seaborn as sns
import matplotlib.pyplot as plt

# --- Function to fetch data from UniProt API ---
def fetch_uniprot_data(keyword="covid", size=50):
    base_url = "https://rest.uniprot.org/uniprotkb/search"
    query = f"reviewed:true AND organism_id:9606 AND {keyword}"
    params = {
        "query": query,
        "format": "json",
        "size": size
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        results = response.json().get("results", [])
        records = []
        for r in results:
            accession = r.get('primaryAccession', '')
            entry_name = r.get('uniProtkbId', '')
            protein_name = (
                r.get('proteinDescription', {})
                 .get('recommendedName', {})
                 .get('fullName', {})
                 .get('value', '')
            )
            organism = r.get('organism', {}).get('scientificName', '')
            length = r.get('sequence', {}).get('length', None)

            records.append({
                "Accession": accession,
                "Entry Name": entry_name,
                "Protein Name": protein_name,
                "Organism": organism,
                "Length": length
            })
        return pd.DataFrame(records)
    else:
        return pd.DataFrame()

# --- Streamlit UI ---
st.title("Protein Data Explorer (UniProt API)")

# Sidebar inputs
st.sidebar.header("Fetch Options")
keyword = st.sidebar.text_input("Keyword", value="covid")
size = st.sidebar.slider("Number of proteins", 10, 100, 50)
fetch_button = st.sidebar.button("Fetch Data")

# --- Fetch data on first load (default behavior) ---
if "df" not in st.session_state:
    st.session_state.df = fetch_uniprot_data(keyword, size)

# --- Fetch again if button clicked ---
if fetch_button:
    st.session_state.df = fetch_uniprot_data(keyword, size)

df = st.session_state.df

# --- Show results ---
if not df.empty:
    st.subheader(f"Retrieved {len(df)} proteins")
    st.dataframe(df)

    # Distribution of protein lengths
    st.subheader("Distribution of Protein Lengths")
    fig, ax = plt.subplots()
    sns.histplot(df["Length"], kde=True, bins=15, ax=ax)
    ax.set_xlabel("Protein Length (aa)")
    ax.set_ylabel("Count")
    st.pyplot(fig)

    # Top 10 proteins by length
    st.subheader("Top 10 Proteins by Length")
    st.dataframe(df.sort_values(by="Length", ascending=False).head(10))
else:
    st.warning("No data retrieved. Try a different keyword or increase the size.")
