"""
ai_insights.py
Lightweight prototype demonstrating an "AI insight" pipeline:
- loads sample data (placeholder)
- performs a tiny feature extraction
- outputs prioritized future directions (mocked scoring)

This script is intentionally small, reproducible, and easy to expand into notebooks.
"""

from utils import mock_data, simple_score

def main():
    data = mock_data()
    print("Loaded examples:", data)
    scored = [(d['theme'], simple_score(d)) for d in data]
    scored_sorted = sorted(scored, key=lambda x: x[1], reverse=True)
    print("\nPrioritized future directions (mock scores):")
    for theme, score in scored_sorted:
        print(f" - {theme}: {score:.2f}")

if __name__ == "__main__":
    main()
