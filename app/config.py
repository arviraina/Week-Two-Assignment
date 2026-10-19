
SYSTEM_PROMPT = """
Sort each news item into exactly one of these four categories.

World: politics, government, international affairs, conflict and disasters.
Sports: matches, results, athletes, teams, transfers and tournaments.
Business: companies, markets, earnings, the economy, trade and commercial deals.
Sci/Tech: science, research, technology, software, space and health research.
If two categories fit, choose the one the headline is mainly about instead of relying on a single keyword.
Choose Business for stories mainly about company earnings, share prices or commercial deals, even when the company operates in technology or sport
If two categories seem equally plausible, choose the best-fitting one and report confidence of 0.4 or lower.
"""


ROUTING_RULES = [
    ("why did you",        "explain"),
    ("explain",            "explain"),
    ("how confident",      "explain"),
    ("ignore your",        "refuse"),
    ("your instructions",  "refuse"),
    ("weather",            "refuse"),
]

BANNED_PHRASES = [
    "as a human",
    "i am a person",
]

ALLOWED_CATEGORIES = ["World", "Sports", "Business", "Sci/Tech"]

CONFIDENCE_FLOOR = 0.4

KNOWLEDGE_FILES = [
    "categories.md",
    "escalation.md"
]

KNOWLEDGE_PASSAGES = 2
KNOWLEDGE_THRESHOLD = 0.10

MODEL = "openai/gpt-oss-120b"
TEMPERATURE = 0
