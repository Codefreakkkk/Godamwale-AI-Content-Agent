from ai_agent import ask_ai


VALID_MODULES = {
    "optimization",
    "outdated",
    "blog",
    "seo",
    "social_media",
    "email",
    "competitor_analysis"
}


DEFAULT_MODULE = "optimization"


def decide_module(user_request):
    """
    Decide which content module should handle the user's request.

    The AI is used only as a classifier. The returned value is
    validated against the known module list before being accepted.
    """

    # ------------------------------------------------------------
    # INPUT VALIDATION
    # ------------------------------------------------------------

    if not user_request or not user_request.strip():

        return DEFAULT_MODULE

    prompt = f"""
You are the routing engine for the Godamwale AI Content Agent.

Classify the user's request into EXACTLY ONE of these modules:

optimization
outdated
blog
seo
social_media
email
competitor_analysis

Return ONLY the exact module name.

Do not explain.
Do not use punctuation.
Do not return multiple modules.
Do not return markdown.
Do not return any other text.

============================================================
ROUTING PRIORITY
============================================================

If multiple intents are present, use this priority:

1. competitor_analysis
2. blog
3. optimization
4. seo
5. outdated
6. social_media
7. email

============================================================
COMPETITOR ANALYSIS
============================================================

Choose competitor_analysis when the request involves:

- Comparing Godamwale with a competitor
- Competitor website analysis
- Competitor content analysis
- Comparing website content
- Competitor keyword analysis
- Competitor content gaps
- Identifying topics competitors cover better
- Recommendations based on competitor content

Explicit competitor comparison ALWAYS takes priority over SEO.

============================================================
BLOG
============================================================

Choose blog when the user wants:

- A new blog
- A blog article
- A new article
- Content around a target keyword
- A customer-facing article
- A blog that should then be optimized

A NEW article always goes to blog, even if SEO is mentioned.

============================================================
OPTIMIZATION
============================================================

Choose optimization when the user wants to improve EXISTING
website content.

Examples:

- Rewrite existing content
- Improve readability
- Improve clarity
- Improve structure
- Improve wording
- Make existing content more customer-friendly

============================================================
SEO
============================================================

Choose seo when the PRIMARY task is SEO or AIO analysis.

Examples:

- SEO analysis
- Keyword recommendations
- Meta title
- Meta description
- Search intent
- AIO analysis
- AI search optimization
- FAQ opportunities
- Search optimization recommendations

Do not choose seo when the primary task is rewriting the
entire existing content.

============================================================
OUTDATED
============================================================

Choose outdated when the user wants to identify:

- Outdated information
- Old website information
- Information that may need updating
- Information requiring freshness review

============================================================
SOCIAL MEDIA
============================================================

Choose social_media for:

- Social media posts
- Social media captions
- LinkedIn content
- Instagram content
- Facebook content
- Promotional social content

============================================================
EMAIL
============================================================

Choose email for:

- Email generation
- Customer emails
- Marketing emails
- Business emails
- Email content

============================================================
USER REQUEST
============================================================

{user_request}
"""

    try:

        decision = ask_ai(prompt)

        if not decision:

            return DEFAULT_MODULE

        # --------------------------------------------------------
        # NORMALIZE AI RESPONSE
        # --------------------------------------------------------

        decision = decision.strip().lower()

        decision = decision.replace("`", "")
        decision = decision.replace(".", "")
        decision = decision.replace("\n", "")
        decision = decision.strip()

        # --------------------------------------------------------
        # VALIDATE RESPONSE
        # --------------------------------------------------------

        if decision in VALID_MODULES:

            return decision

        # --------------------------------------------------------
        # SAFE FALLBACK
        # --------------------------------------------------------

        print(
            "Invalid decision-engine response:",
            decision
        )

        return DEFAULT_MODULE

    except Exception as error:

        print(
            "Decision engine error:",
            error
        )

        return DEFAULT_MODULE