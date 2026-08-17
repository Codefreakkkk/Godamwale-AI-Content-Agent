from ai_agent import ask_ai

from config import MODULE_CONTEXT_LIMIT


# ============================================================
# SOCIAL MEDIA CONTENT GENERATION
# ============================================================

def generate_social_media(
    company_information
):
    """
    Generate professional social media content using only
    approved company information.
    """

    # --------------------------------------------------------
    # INPUT VALIDATION
    # --------------------------------------------------------

    if not company_information or not company_information.strip():

        return (
            "Unable to generate social media content. "
            "No approved company information was provided."
        )

    # --------------------------------------------------------
    # LIMIT COMPANY CONTEXT
    # --------------------------------------------------------

    approved_information = company_information[
        :MODULE_CONTEXT_LIMIT
    ]

    # --------------------------------------------------------
    # SOCIAL MEDIA PROMPT
    # --------------------------------------------------------

    prompt = f"""
You are the Social Media Content Generation Module
of the Godamwale AI Content Agent.

Create professional, customer-facing social media content
using ONLY the approved company information provided below.

============================================================
APPROVED COMPANY INFORMATION
============================================================

{approved_information}

============================================================
CONTENT OBJECTIVE
============================================================

Create one professional social media post suitable for:

- LinkedIn
- A company social media page
- A business audience

The post should communicate a useful and relevant message
about the company, its services, or its business value based
only on the supplied information.

============================================================
CONTENT RULES
============================================================

- Keep the post professional.
- Keep the message clear and customer-focused.
- Make the opening sentence engaging but factual.
- Use natural business language.
- Keep the post concise and readable.
- Use short paragraphs where appropriate.
- Include a practical call to action only if it can be made
  without inventing information.
- Do not create unsupported claims.
- Do not make guarantees.
- Do not exaggerate achievements.
- Do not use misleading promotional language.

============================================================
FACTUAL ACCURACY RULES
============================================================

NEVER invent:

- Services
- Locations
- Pricing
- Discounts
- Certifications
- Statistics
- Customers
- Partnerships
- Awards
- Achievements
- Warehouse counts
- Operational capabilities
- Performance claims
- Guarantees

Do not assume information that is not present in the
approved company information.

If there is not enough company-specific information to make
a specific claim, keep the statement general.

============================================================
HASHTAG RULES
============================================================

Provide relevant hashtags based on the actual topic.

- Use relevant industry hashtags.
- Use relevant business/logistics hashtags where supported.
- Avoid excessive hashtags.
- Do not create hashtags containing unsupported company claims.
- Prefer approximately 5-8 useful hashtags.

============================================================
RETURN FORMAT
============================================================

Social Media Post:

(Write the complete social media post here.)


Suggested Hashtags:

(List approximately 5-8 relevant hashtags.)


Information Requiring Verification:

(List any company-specific information that should be
human-verified before publishing.)

Write:

None

if no verification is required.
"""

    # --------------------------------------------------------
    # AI GENERATION
    # --------------------------------------------------------

    try:

        result = ask_ai(
            prompt
        )

        return result

    except Exception as error:

        print(
            "Social media generation error:",
            error
        )

        return (
            "Unable to generate social media content "
            "at this time."
        )