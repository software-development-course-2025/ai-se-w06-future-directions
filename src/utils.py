"""
utils.py - small helpers for demo and prototyping
"""

def mock_data():
    # Placeholder dataset: suggested directions with minimal metadata
    return [
        {'theme': 'Code-centric LLM agents', 'impact': 0.9, 'feasibility': 0.6},
        {'theme': 'Automated testing generation', 'impact': 0.8, 'feasibility': 0.85},
        {'theme': 'Self-healing CI pipelines', 'impact': 0.75, 'feasibility': 0.5},
        {'theme': 'AI-assisted requirements mining', 'impact': 0.7, 'feasibility': 0.7},
    ]

def simple_score(record):
    # Simple scoring heuristic: weighted impact * feasibility
    return record['impact'] * record['feasibility']
