from ai_agent import ask_ai


# ============================================================
# COMPETITOR CONTENT ANALYSIS
# ============================================================

def analyze_competitor(
    target_keyword,
    company_content,
    competitor_content
):
    """
    Compare Godamwale website content with competitor content
    around a specific target keyword.

    The analysis is based only on the supplied content and does
    not make claims about actual search-engine rankings.
    """

    # --------------------------------------------------------
    # INPUT VALIDATION
    # --------------------------------------------------------

    if not target_keyword or not target_keyword.strip():

        target_keyword = "Not specified"

    if not company_content or not company_content.strip():

        return (
            "Unable to perform competitor analysis. "
            "Godamwale website content was not provided."
        )

    if not competitor_content or not competitor_content.strip():

        return (
            "Unable to perform competitor analysis. "
            "Competitor website content was not provided."
        )

    # --------------------------------------------------------
    # LIMIT WEBSITE CONTENT
    # --------------------------------------------------------

    company_information = company_content[:6000]

    competitor_information = competitor_content[:6000]

    # --------------------------------------------------------
    # COMPETITOR ANALYSIS PROMPT
    # --------------------------------------------------------

    prompt = f"""
You are the Competitor Analysis and Content Optimization Module
of the Godamwale AI Content Agent.

Your task is to compare Godamwale's website content with a
competitor's website content around a specific target keyword.

The goal is to identify practical content opportunities that
Godamwale could consider based ONLY on the supplied content.

============================================================
TARGET KEYWORD
============================================================

{target_keyword}

============================================================
GODAMWALE WEBSITE CONTENT
============================================================

{company_information}

============================================================
COMPETITOR WEBSITE CONTENT
============================================================

{competitor_information}

============================================================
IMPORTANT ANALYSIS RULES
============================================================

Analyze both websites specifically around the target keyword.

Base every observation ONLY on the supplied content.

Do not use outside knowledge.

Do not claim actual Google rankings.

Do not claim that the competitor ranks higher.

Do not claim that a content change guarantees higher rankings
or better visibility.

Do not invent:

- Services
- Locations
- Pricing
- Statistics
- Certifications
- Customers
- Partnerships
- Awards
- Business claims
- Operational capabilities

Clearly distinguish observable content differences from
interpretations.

Use cautious language such as:

- appears
- may
- could
- potentially
- based on the supplied content

============================================================
1. KEYWORD CONTENT COMPARISON
============================================================

Compare how Godamwale and the competitor address the target
keyword.

Consider:

- Direct keyword coverage
- Related topics
- Service information
- Explanations
- Use cases
- Locations
- Customer questions
- FAQs
- Supporting information

Explain which topics are actually covered by each website.

============================================================
2. COMPETITOR CONTENT STRENGTHS
============================================================

Identify areas where the competitor appears stronger based ONLY
on the supplied content.

Consider:

- More complete information
- More detailed explanations
- Wider topic coverage
- Better content organization
- Clearer service explanations
- Better customer-question coverage
- Better supporting information
- Clearer keyword relevance

For each strength explain what is actually present in the
competitor content.

Do not assume that a content strength directly causes higher
search rankings.

============================================================
3. GODAMWALE CONTENT STRENGTHS
============================================================

Identify useful or strong content already present on Godamwale's
website.

Consider:

- Services
- Locations
- Explanations
- Customer information
- Calls to action
- Supporting information
- Keyword relevance

Do not recommend changing content simply because it differs from
the competitor.

============================================================
4. GODAMWALE CONTENT GAPS
============================================================

Identify specific content differences.

Classify each gap as:

- Missing
- Briefly Covered
- Unclear
- Could Be Expanded
- Could Be Better Structured

For every important gap provide:

Gap:
Competitor Coverage:
Godamwale Coverage:
Recommended Action:

Only identify gaps supported by the supplied content.

============================================================
5. SEARCH INTENT AND TOPIC COVERAGE
============================================================

Analyze the likely customer intent behind the target keyword.

Explain:

- What a potential customer may want to know
- Whether Godamwale addresses that intent
- Whether the competitor addresses that intent
- Related topics visible in the competitor content
- Topics Godamwale could explain more clearly

Use cautious language.

Do not claim actual search-engine behavior.

============================================================
6. KEYWORD AND RELATED TOPIC ANALYSIS
============================================================

Analyze how naturally the target keyword and related concepts
appear in both websites.

Identify:

- Main keyword usage
- Related terminology
- Supporting topics
- Missing related concepts
- Potential opportunities for natural topical coverage

Do NOT recommend keyword stuffing.

Focus on useful and relevant coverage.

============================================================
7. CONTENT STRUCTURE COMPARISON
============================================================

Compare the observable organization of the two websites.

Consider:

- Headings
- Sections
- Service explanations
- Location information
- FAQs
- Customer questions
- Definitions
- Use cases
- Calls to action
- Supporting information

Only mention elements that are actually observable.

============================================================
8. GODAMWALE CONTENT OPTIMIZATION ACTION PLAN
============================================================

Create a practical action plan.

HIGH PRIORITY:

List the most important improvements.

MEDIUM PRIORITY:

List useful secondary improvements.

LOW PRIORITY:

List optional improvements.

For each recommendation provide:

Action:
Reason:
Expected Content Improvement:

Do not promise ranking improvements.

============================================================
9. SUGGESTED NEW CONTENT SECTIONS
============================================================

Suggest useful sections that Godamwale could consider adding.

For each section provide:

Section:
What to Include:
Why It Is Useful:

Only suggest sections supported by the supplied competitor
content or reasonable customer intent around the target keyword.

Do not invent company-specific facts.

============================================================
10. CONTENT THAT COULD BE REWRITTEN OR EXPANDED
============================================================

Identify important existing Godamwale content that could
potentially be improved.

For each item provide:

Current Content:
Current Weakness:
Recommended Improvement:

Do not rewrite the entire website.

Focus on the most important opportunities.

============================================================
11. QUICK COMPETITIVE SUMMARY
============================================================

Use this structure:

Godamwale Currently Does Well:
-

Competitor Appears Stronger In:
-

Biggest Content Opportunity:
-

Most Important Recommended Action:
-

============================================================
12. INFORMATION REQUIRING VERIFICATION
============================================================

List company-specific information that should be checked by
a human before publishing changes.

Write:

None

if no verification is required.

============================================================
FINAL SAFETY RULES
============================================================

- Do NOT claim actual Google rankings.
- Do NOT claim the competitor ranks higher.
- Do NOT guarantee SEO results.
- Do NOT guarantee AI-search visibility.
- Do NOT invent Godamwale services.
- Do NOT invent competitor services.
- Do NOT invent locations.
- Do NOT invent statistics.
- Do NOT invent pricing.
- Do NOT invent certifications.
- Do NOT invent business claims.
- Base the analysis ONLY on supplied website content.
- Focus specifically on the target keyword.
- Avoid keyword stuffing.
- Give practical recommendations.
- Clearly distinguish observations from assumptions.
"""

    # --------------------------------------------------------
    # AI ANALYSIS
    # --------------------------------------------------------

    try:

        result = ask_ai(
            prompt
        )

        return result

    except Exception as error:

        print(
            "Competitor analysis error:",
            error
        )

        return (
            "Unable to perform competitor analysis "
            "at this time."
        )