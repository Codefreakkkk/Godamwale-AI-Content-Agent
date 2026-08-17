from ai_agent import ask_ai

from config import MODULE_CONTEXT_LIMIT


# ============================================================
# EMAIL CONTENT GENERATION
# ============================================================

def generate_email(
    company_information
):
    """
    Generate a professional business email using only
    approved company information.
    """

    # --------------------------------------------------------
    # INPUT VALIDATION
    # --------------------------------------------------------

    if not company_information or not company_information.strip():

        return (
            "Unable to generate email content. "
            "No approved company information was provided."
        )

    # --------------------------------------------------------
    # LIMIT COMPANY CONTEXT
    # --------------------------------------------------------

    approved_information = company_information[
        :MODULE_CONTEXT_LIMIT
    ]

    # --------------------------------------------------------
    # EMAIL GENERATION PROMPT
    # --------------------------------------------------------

    prompt = f"""
You are the Email Generation Module
of the Godamwale AI Content Agent.

Create a professional business email using ONLY the
approved company information provided below.

============================================================
APPROVED COMPANY INFORMATION
============================================================

{approved_information}

============================================================
EMAIL OBJECTIVE
============================================================

Create an email suitable for:

- Customer communication
- Business communication
- Professional outreach

The email should be clear, useful, concise, and
customer-focused.

============================================================
CONTENT RULES
============================================================

- Use a professional and polite tone.
- Keep the email easy to read.
- Clearly communicate the main purpose.
- Use short paragraphs where appropriate.
- Include a clear call to action only when appropriate.
- Do not use unnecessary marketing language.
- Do not exaggerate company capabilities.
- Do not make unsupported promises or guarantees.

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

If company-specific information is unavailable,
keep the statement general rather than inventing details.

============================================================
EMAIL STRUCTURE
============================================================

Use:

1. Subject
2. Greeting
3. Main message
4. Relevant call to action, if appropriate
5. Professional closing

============================================================
RETURN FORMAT
============================================================

Subject:

(Write a concise professional subject line.)


Email Body:

(Write the complete email.)


Information Requiring Verification:

(List any company-specific information that should be
human-verified before sending.)

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
            "Email generation error:",
            error
        )

        return (
            "Unable to generate email content "
            "at this time."
        )