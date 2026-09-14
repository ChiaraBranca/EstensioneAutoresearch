import os
import matplotlib.pyplot as plt

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FIG_DIR = os.path.join(BASE_DIR, "figures")
os.makedirs(FIG_DIR, exist_ok=True)

plt.style.use('seaborn-v0_8-paper' if 'seaborn-v0_8-paper' in plt.style.available else 'default')
plt.rcParams.update({'font.size': 10, 'axes.labelsize': 11, 'axes.titlesize': 12, 'figure.titlesize': 14})

SURVEY_TITLE = "rag_architecture"
# [AI AGENT ZONE] Edit only these dictionaries
TIMELINE_DATA = {"2024": 11, "2025": 8, "2026": 7}
TAXONOMY_DATA = {"GraphRAG & Knowledge Graphs": 3, "Multi-Agent & Dynamic Filtering": 2, "Dynamic Chunking & Vector Search": 1, "Instruction Tuning & Data Synthesis": 1, "Chunk-Distilled Generation": 1, "Human-Centered AI & Optimization": 1, "Document Classification": 1, "Hallucination & Faithfulness Evaluation": 2, "Governance & Privacy in RAG": 3, "Domain-Specific & Adaptive RAG": 3, "Low-Resource & Specialized Language RAG": 1, "Pedagogical & Provenance-Aware RAG": 2, "Semantic Retrieval & Sentiment Analysis": 1, "Multimodal & Document Intelligence RAG": 1, "Enterprise & Serving RAG Architectures": 1, "Safety-Gated & Resource-Aware RAG": 1, "Verification & Gated RAG Architectures": 1}

def plot_publication_timeline():
    years, counts = list(TIMELINE_DATA.keys()), list(TIMELINE_DATA.values())
    fig, ax = plt.subplots(figsize=(10, 3.5))
    ax.bar(years, counts, color='#2b5c8f', width=0.6)
    ax.set_title(f"Publication Timeline: {SURVEY_TITLE}")
    ax.set_xlabel("Year")
    ax.set_ylabel("Number of Cited Papers")
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    if max(counts if counts else [0]) == 0: ax.set_ylim(0, 5)
    plt.tight_layout()
    plt.savefig(os.path.join(FIG_DIR, "timeline.png"), dpi=300)
    plt.close()

def plot_taxonomy_distribution():
    labels, values = list(TAXONOMY_DATA.keys()), list(TAXONOMY_DATA.values())
    if sum(values) == 0: labels, values = ["No data"], [1]
    colors = ['#2b5c8f', '#d95f02', '#7570b3', '#e7298a', '#66a61e', '#ff7f0e', '#4e79a7', '#f28e2b', '#76b7b2', '#59a14f']
    fig, ax = plt.subplots(figsize=(6, 3.5))
    ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=140, colors=colors[:len(labels)])
    ax.set_title(f"Taxonomy Distribution: {SURVEY_TITLE}")
    plt.tight_layout()
    plt.savefig(os.path.join(FIG_DIR, "taxonomy.png"), dpi=300)
    plt.close()

if __name__ == "__main__":
    plot_publication_timeline()
    plot_taxonomy_distribution()
    print(f"[GENERATE_FIGURES] Charts updated in {FIG_DIR}")
