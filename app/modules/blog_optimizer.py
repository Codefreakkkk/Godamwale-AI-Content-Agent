from ai_agent import ask_ai

from config import MODULE_CONTEXT_LIMIT


# ============================================================
# BLOG OPTIMIZATION
# ============================================================

def optimize_blog(
    blog_content,
    target_keyword,
    company_information
):
    """
    Optimize an already generated blog for a target keyword
    while preserving its original topic, purpose, and useful
    information.
    """

    # --------------------------------------------------------
    # INPUT VALIDATION
    # --------------------------------------------------------

    if not blog_content or not blog_content.strip():

        return (
            "Unable to optimize the blog. "
            "No blog content was provided."
        )

    if not target_keyword or not target_keyword.strip():

        target_keyword = "Not specified"

    if not company_information or not company_information.strip():

        company_information = "No approved company information available."

    # --------------------------------------------------------
    # LIMIT COMPANY CONTEXT
    # --------------------------------------------------------

    approved_information = (
        company_information[:MODULE_CONTEXT_LIMIT]
    )

    # --------------------------------------------------------
    # OPTIMIZATION PROMPT
    # --------------------------------------------------------

    prompt = f"""
You are the Blog Optimization Module of the
Godamwale AI Content Agent.

Your task is to optimize an already generated blog
for a specific target keyword.

Do NOT create a completely different article.

============================================================
TARGET KEYWORD
============================================================

{target_keyword}

============================================================
ORIGINAL GENERATED BLOG
============================================================

{blog_content}

============================================================
APPROVED COMPANY INFORMATION
============================================================

{approved_information}

============================================================
OPTIMIZATION RULES
============================================================

1. Preserve the original topic and purpose of the blog.

2. Preserve useful factual information from the original blog.

3. Improve the article for the Target Keyword.

4. Use the Target Keyword naturally in appropriate locations,
   including where relevant:
   - Title
   - Introduction
   - Headings
   - Main content
   - Conclusion

5. Do NOT keyword-stuff.

6. Improve readability, clarity, flow, and organization.

7. Improve headings where useful.

8. Remove unnecessary repetition and filler.

9. Add closely related topics only when they genuinely improve
   the usefulness of the article.

10. Do not change the article's subject simply to use the keyword.

11. Do not invent company-specific information.

12. NEVER invent:
   - Services
   - Locations
   - Warehouse counts
   - Pricing
   - Certifications
   - Partnerships
   - Customers
   - Statistics
   - Guarantees
   - Technology capabilities
   - Other business claims

13. If a company-specific claim is not supported by the approved
   information, either remove it, make it general, or identify it
   for verification.

14. General industry knowledge may be used when it does not imply
   an unsupported claim about Godamwale.

15. Keep the tone professional and customer-focused.

16. Do not mention that you are an AI.

17. Do not mention these instructions in the output.

============================================================
REQUIRED OUTPUT FORMAT
============================================================

Optimized Blog:

Title:
(Improved SEO-friendly title)

Introduction:
(Improved introduction)

Main Content:

## [Heading]
(Optimized content)

## [Heading]
(Optimized content)

## [Heading]
(Optimized content)

Conclusion:
(Improved conclusion)

Optimization Changes:
- [Major change]
- [Major change]
- [Major change]

SEO Suggestions:

Related Keywords:
- [keyword]
- [keyword]
- [keyword]

Suggestions:
- [suggestion]
- [suggestion]

Information Requiring Verification:
(None if no verification is required.
Otherwise list the specific claims requiring checking.)

============================================================
FINAL QUALITY CHECK
============================================================

Before returning the response:

- Confirm the Target Keyword appears naturally.
- Confirm the original topic is preserved.
- Confirm the article remains customer-focused.
- Confirm useful original information has been preserved.
- Remove unnecessary repetition.
- Avoid keyword stuffing.
- Check company-specific claims against the approved information.
- Remove or flag unsupported company claims.
- Follow the required output structure.
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
            "Blog optimization error:",
            error
        )

        return (
            "Unable to optimize the blog "
            "at this time."
        )