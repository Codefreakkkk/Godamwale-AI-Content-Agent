from ai_agent import ask_ai

from config import (
    MODULE_CONTEXT_LIMIT,
    WEBSITE_CONTENT_LIMIT
)


# ============================================================
# WEBSITE CONTENT OPTIMIZATION
# ============================================================

def optimize_content(
    website_content,
    company_information
):
    """
    Improve existing website content while preserving its
    original meaning and keeping company-specific claims
    grounded in approved information.
    """

    # --------------------------------------------------------
    # INPUT VALIDATION
    # --------------------------------------------------------

    if not website_content or not website_content.strip():

        return (
            "Unable to optimize website content. "
            "No website content was provided."
        )

    if not company_information or not company_information.strip():

        company_information = (
            "No approved company information is available."
        )

    # --------------------------------------------------------
    # LIMIT INPUT CONTEXT
    # --------------------------------------------------------

    approved_information = company_information[
        :MODULE_CONTEXT_LIMIT
    ]

    existing_content = website_content[
        :WEBSITE_CONTENT_LIMIT
    ]

    # --------------------------------------------------------
    # OPTIMIZATION PROMPT
    # --------------------------------------------------------

    prompt = f"""
You are the Website Content Optimization Module
of the Godamwale AI Content Agent.

Your task is to improve the existing website content while
preserving its original meaning, important information, and
business purpose.

The result should be a clearer and more professional version
of the existing content, NOT a completely different article.

============================================================
APPROVED COMPANY INFORMATION
============================================================

{approved_information}

============================================================
EXISTING WEBSITE CONTENT
============================================================

{existing_content}

============================================================
OPTIMIZATION OBJECTIVES
============================================================

Improve the content by:

- Improving readability.
- Improving clarity.
- Improving sentence quality.
- Improving structure and organization.
- Adding clear headings where appropriate.
- Breaking up overly long sections.
- Making important information easier to understand.
- Making the content more customer-friendly.
- Maintaining a professional business tone.
- Improving logical flow.
- Removing unnecessary repetition and filler.
- Preserving useful factual information.
- Preserving the original topic and purpose.

============================================================
FACTUAL ACCURACY RULES
============================================================

The approved company information is the reference for
company-specific facts.

NEVER invent or assume:

- Services
- Locations
- Pricing
- Certifications
- Statistics
- Customers
- Partnerships
- Warehouse counts
- Technology capabilities
- Performance claims
- Guarantees
- Other company-specific information

Do not exaggerate company achievements.

Do not turn general industry information into a
Godamwale-specific claim.

If the existing content contains a company-specific claim that
cannot be supported by the approved information, do not silently
invent supporting details.

Instead, either:

1. Preserve the claim if it is clearly presented as existing
   website information, and flag it for verification, or

2. Rewrite it more cautiously when appropriate.

============================================================
CONTENT PRESERVATION RULES
============================================================

- Do not change the main subject.
- Do not remove important services or offerings from the
  original content merely to shorten it.
- Do not remove important customer-facing information without
  a clear reason.
- Do not introduce unrelated topics.
- Do not turn the content into a blog unless the original
  content is already structured as one.
- Do not add unsupported calls to action.
- Keep the final content coherent as a complete website section.

============================================================
SEO GUIDELINES
============================================================

If the existing content or request contains a target keyword:

- Use it naturally.
- Improve keyword relevance where appropriate.
- Place it in relevant headings or sections when natural.
- Avoid keyword stuffing.
- Do not sacrifice readability for keyword placement.

SEO improvements must remain useful to actual customers.

Do not guarantee search rankings, traffic, or visibility.

============================================================
REQUIRED RESPONSE FORMAT
============================================================

Optimized Website Content:

(Provide the complete improved website content here.)


Summary of Improvements:

- [Major improvement]
- [Major improvement]
- [Major improvement]


Information Requiring Verification:

(List company-specific claims that should be human-verified
before publishing.)

Write:

None

if no verification is required.

============================================================
FINAL QUALITY CHECK
============================================================

Before returning the response:

- Confirm the original topic is preserved.
- Confirm the original meaning is preserved.
- Confirm important information has not been unnecessarily removed.
- Confirm company-specific claims are grounded.
- Remove unsupported additions.
- Avoid keyword stuffing.
- Ensure the final content is readable and professional.
- Follow the required output format.
"""

    # --------------------------------------------------------
    # AI OPTIMIZATION
    # --------------------------------------------------------

    try:

        result = ask_ai(
            prompt
        )

        return result

    except Exception as error:

        print(
            "Website content optimization error:",
            error
        )

        return (
            "Unable to optimize website content "
            "at this time."
        )