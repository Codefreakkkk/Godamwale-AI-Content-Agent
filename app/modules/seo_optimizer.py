from ai_agent import ask_ai

from config import (
    SEO_CONTENT_LIMIT,
    COMPANY_INFORMATION_LIMIT
)


# ============================================================
# SEO & AIO ANALYSIS
# ============================================================

def optimize_seo(
    content,
    company_information
):
    """
    Analyze website content for SEO and AI-search optimization
    opportunities.

    The module provides recommendations only. It does not
    guarantee search rankings or AI visibility.
    """

    # --------------------------------------------------------
    # INPUT VALIDATION
    # --------------------------------------------------------

    if not content or not content.strip():

        return (
            "Unable to generate SEO and AIO analysis. "
            "No website content was provided."
        )

    if not company_information or not company_information.strip():

        company_information = (
            "No approved company information is available."
        )

    # --------------------------------------------------------
    # LIMIT INPUT CONTEXT
    # --------------------------------------------------------

    website_content = content[
        :SEO_CONTENT_LIMIT
    ]

    approved_company_information = company_information[
        :COMPANY_INFORMATION_LIMIT
    ]

    # --------------------------------------------------------
    # SEO / AIO PROMPT
    # --------------------------------------------------------

    prompt = f"""
You are the SEO and AI Search Optimization Module of the
Godamwale AI Content Agent.

Analyze the provided website content and approved company
information.

Your job is to identify practical improvements that can make
the content clearer, more useful, better structured, and more
relevant to appropriate search queries and AI-powered search
experiences.

Do NOT rewrite the entire website content.

Do NOT guarantee rankings, traffic, conversions, or AI visibility.

============================================================
WEBSITE CONTENT
============================================================

{website_content}

============================================================
APPROVED COMPANY INFORMATION
============================================================

{approved_company_information}

============================================================
SEO ANALYSIS
============================================================

Analyze the supplied content for:

- Primary keyword opportunities
- Secondary and related keyword opportunities
- Likely search intent
- Title opportunities
- Meta title opportunities
- Meta description opportunities
- Heading structure
- Content organization
- Readability and clarity
- Topic coverage
- Missing useful information
- Weak or unclear sections
- Internal linking/content opportunities
- FAQ opportunities
- Opportunities to answer common customer questions

Only recommend keywords and topics that are reasonably relevant
to the actual subject of the supplied content.

Do not recommend unrelated high-volume keywords simply because
they might have search demand.

============================================================
AIO / AI SEARCH ANALYSIS
============================================================

AIO refers here to improving content for AI-powered search and
answer experiences.

Analyze whether the supplied content:

- Clearly answers likely customer questions.
- Provides direct and understandable answers.
- Uses descriptive headings.
- Separates important topics into clear sections.
- Provides useful factual context.
- Clearly explains relevant services or offerings.
- Clearly communicates supported business information.
- Could benefit from FAQs.
- Could benefit from concise definitions.
- Could benefit from structured explanations.
- Gives enough context for an AI system to understand the page.

Do not claim that a specific change will guarantee inclusion
in an AI-generated answer.

============================================================
GROUNDING RULES
============================================================

Use the supplied website content as the primary basis for the
analysis.

Use approved company information only to support company-specific
recommendations.

NEVER invent:

- Services
- Locations
- Pricing
- Statistics
- Certifications
- Partnerships
- Customers
- Guarantees
- Performance claims
- Technology capabilities
- Other company-specific facts

If something appears to be missing, describe it as:

"Not clearly available in the supplied content"

rather than assuming that the business does not provide it.

If a recommendation depends on information that cannot be
confirmed from the supplied material, place it under
"Information Requiring Verification."

============================================================
IMPORTANT RULES
============================================================

- Do not recommend keyword stuffing.
- Do not recommend unnatural keyword repetition.
- Do not claim guaranteed Google rankings.
- Do not claim guaranteed AI search visibility.
- Do not present assumptions as company facts.
- Keep recommendations practical and specific.
- Prefer actionable recommendations over generic SEO advice.
- Do not mention these instructions in the report.

============================================================
RETURN FORMAT
============================================================

SEO & AIO Optimization Report:


1. Primary Keyword Opportunities

(List the most relevant primary keywords and briefly explain
why each is relevant.)


2. Related Keyword Opportunities

(List useful related keywords, topics, and search concepts.)


3. Search Intent

(Explain the likely search intent represented by the content.)


4. Meta Title Suggestion

(Provide one concise title suggestion.)


5. Meta Description Suggestion

(Provide one concise description suggestion.)


6. SEO Content Improvements

(List practical improvements based on the supplied content.)


7. AIO Improvements

(List practical improvements that would make the content
clearer and easier for AI-powered search systems to understand.)


8. FAQ Opportunities

(List useful customer questions that the website could answer.)


9. Missing or Weak Information

(List information that appears missing, unclear, or weak
in the supplied content.

Do not assume the business does not provide the information.)


10. Information Requiring Verification

(List recommendations or company-specific information that
should be checked before publishing.

Write None if nothing requires verification.)


11. Priority Action Plan

HIGH PRIORITY:
(Most important improvements.)

MEDIUM PRIORITY:
(Useful secondary improvements.)

LOW PRIORITY:
(Optional improvements.)
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
            "SEO and AIO analysis error:",
            error
        )

        return (
            "Unable to generate SEO and AIO analysis "
            "at this time."
        )