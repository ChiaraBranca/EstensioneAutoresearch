"""
=============================================================================
FILE: generate_figures.py
DESCRIPTION: 
This script generates the statistical charts for the Living Survey.
It is divided into two strict zones:
1. The AI Agent Zone: Dictionaries that the AI Actor dynamically updates.
2. The Untouchable Zone: The underlying Matplotlib plotting logic that 
   translates the dictionaries into .png images.
=============================================================================
"""

import os
import matplotlib.pyplot as plt

# Ensure the output directory exists
os.makedirs("figures", exist_ok=True)

# Clean style settings for scientific publications
plt.style.use('seaborn-v0_8-paper' if 'seaborn-v0_8-paper' in plt.style.available else 'default')
plt.rcParams.update({
    'font.size': 10,
    'axes.labelsize': 11,
    'axes.titlesize': 12,
    'figure.titlesize': 14
})

# ==============================================================================
# [AI AGENT ZONE] MODIFY EXCLUSIVELY THESE TWO DICTIONARIES AND THE TITLE
# ==============================================================================
SURVEY_TITLE = "Living Survey: cancer"

# Format: "Year": Number_of_Papers
TIMELINE_DATA = {
    "2024": 0,
    "2025": 0,
    "2026": 0
}

# Format: "Category / Method": Number_of_Papers
TAXONOMY_DATA = {
    "Baseline Categorization": 1
}
# ==============================================================================
# [UNTOUCHABLE ZONE] DO NOT MODIFY THE PLOTTING LOGIC BELOW
# ==============================================================================

def plot_publication_timeline():
    """Generates the timeline of the papers included in the survey."""
    years = list(TIMELINE_DATA.keys())
    counts = list(TIMELINE_DATA.values())
    
    fig, ax = plt.subplots(figsize=(10, 3.5))
    ax.bar(years, counts, color='#2b5c8f', width=0.6)
    ax.set_title(f"Publication Timeline: {SURVEY_TITLE}")
    ax.set_xlabel("Year")
    ax.set_ylabel("Number of Cited Papers")
    ax.grid(axis='y', linestyle='--', alpha=0.7)
    
    # Avoid visual errors if all values are zero
    if max(counts if counts else [0]) == 0:
        ax.set_ylim(0, 5)
        
    plt.tight_layout()
    plt.savefig("figures/timeline.png", dpi=300)
    plt.close()

def plot_taxonomy_distribution():
    """Generates the methodology distribution according to the survey's taxonomy."""
    labels = list(TAXONOMY_DATA.keys())
    values = list(TAXONOMY_DATA.values())
    
    # If all values are 0, set a dummy baseline to avoid Matplotlib crashes
    if sum(values) == 0:
        labels = ["No classified data"]
        values = [1]
        
    # Extended color palette to support adding many categories without crashing
    colors = [
        '#2b5c8f', '#d95f02', '#7570b3', '#e7298a', '#66a61e', 
        '#ff7f0e', '#4e79a7', '#f28e2b', '#76b7b2', '#59a14f', 
        '#edc948', '#b07aa1', '#ff9da7', '#9c755f', '#bab0ac'
    ]
    
    fig, ax = plt.subplots(figsize=(6, 3.5))
    ax.pie(
        values, 
        labels=labels, 
        autopct='%1.1f%%', 
        startangle=140, 
        colors=colors[:len(labels)]
    )
    ax.set_title(f"Taxonomy Distribution: {SURVEY_TITLE}")
    
    plt.tight_layout()
    plt.savefig("figures/taxonomy.png", dpi=300)
    plt.close()

if __name__ == "__main__":
    plot_publication_timeline()
    plot_taxonomy_distribution()
    print("[GENERATE_FIGURES] Charts successfully updated in figures/")