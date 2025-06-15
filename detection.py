import re

# Malicious patterns common in SQL injection
INJECTION_PATTERNS = [
    r"(--|\#|\/\*)",                      # SQL comments
    r"(\bOR\b\s+1=1|\bAND\b\s+1=1)",      # Boolean-based bypass
    r"UNION\s+SELECT",                   # UNION injections
    r"'.*?'",                             # Suspicious quoted strings
    r"EXEC(\s+|\()",                      # Executing procedures
    r"INSERT\s+INTO\s+\w+\s+VALUES.*--",  # Insert with comment end
    r"(DROP\s+TABLE|DROP\s+DATABASE)",    # Dangerous drop
    r";.*(SELECT|DROP|INSERT|DELETE)",    # Stacked queries
    r"UPDATE\s+\w+\s+SET\s+.*=.*--",      # Update with bypass
]

def normalize_input(text):
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)
    return text

def detect_sql_injection(sql_command):
    """
    Detects if the SQL command is likely an injection attempt.
    """
    if not sql_command:
        return False

    normalized = normalize_input(sql_command)
    for pattern in INJECTION_PATTERNS:
        if re.search(pattern, normalized):
            return True  # Likely SQL injection

    return False  # Considered a normal SQL command
