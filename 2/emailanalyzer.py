# Core email analyzer without sending capabilities (read-only safety)
class EmailAnalyzer:
    def __init__(self):
        self.patterns = {
            "urgent_keywords": ["deadline", "blocker", "urgent", "asap"],
            "delegate_keywords": ["help", "question about", "can you look"],
            "ignore_keywords": ["newsletter", "update", "reminder"],
        }

    def score_urgency(self, email):
        score = 50  # Base score

        # Sender history weight
        if email.from_address in self.sender_trust_scores:
            score += self.sender_trust_scores[email.from_address] * 20

        # Content analysis (runs locally)
        if any(kw in email.subject.lower() for kw in self.patterns["urgent_keywords"]):
            score += 30

        # Thread analysis
        if email.is_in_thread and email.is_latest_in_thread:
            score += 15

        # Response time pattern (learned)
        avg_response_days = self.get_avg_response_time(email.from_address)
        if avg_response_days < 2:
            score += 20

        return min(score, 100)  # Cap at 100

    def suggest_action(self, email):
        score = self.score_urgency(email)

        if score > 75:
            return "RESPOND_NOW"
        elif score > 50:
            return "RESPOND_TODAY"
        elif score > 30:
            return "DEFER_1_WEEK"
        else:
            return "IGNORE_OR_NEWSLETTER"


# UI shows suggestions, user approves with one click
suggestions = {
    "respond_now@client.com": {
        "action": "draft_reply",
        "template": "Acknowledge receipt, commit to timeline",
        "text": "Hi [Name], got it—I'll have this to you by EOD Friday.",
    },
    "delegate@teammate.com": {
        "action": "forward_with_context",
        "delegate_to": "sarah@company.com",
        "reason": "Sarah handled 3 similar requests last month",
    },
    "ignore@newsletter.com": {
        "action": "archive",
        "reason": "You've opened 0/12 of their emails",
    },
}


# OAuth scopes (read-only, no send access)
SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",  # Gmail
    "https://outlook.office.com/Mail.Read",  # Outlook
]


# Process emails locally (never send content to cloud)
class LocalEmailProcessor:
    def __init__(self):
        self.model = load_local_model("distilbert-base-uncased")

    def process_email(self, email):
        # All processing happens on user's machine
        features = self.extract_features(email)
        # Only send anonymous statistics (if user opts in)
        return self.model.predict(features)


# Enterprise version
class EnterpriseEmailAnalyzer:
    def __init__(self, company_policies):
        self.policies = company_policies  # Inherits company rules

        # Example policies:
        # - "Never auto-ignore emails from C-suite"
        # - "Always defer external client emails to legal"
        # - "Delegate vendor questions to procurement@company.com"

    def is_compliant(self, suggested_action):
        # Check against company compliance rules
        return self.policy_engine.validate(suggested_action)

