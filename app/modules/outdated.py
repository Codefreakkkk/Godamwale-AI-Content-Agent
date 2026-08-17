from ai_agent import ask_ai

from config import MODULE_CONTEXT_LIMIT


# ============================================================
# OUTDATED CONTENT DETECTION
# ============================================================

def detect_outdated_content(
    existing_content,
    approved_information
):
    """
    Compare existing website content with approved company
    information and identify possible outdated or unsupported
    information.

    The module does not assume that missing information is
    outdated or incorrect.
    """

    # --------------------------------------------------------
    # INPUT VALIDATION
    # --------------------------------------------------------

    if not existing_content or not existing_content.strip():

        return (
            "Unable to analyze outdated content. "
            "No website content was provided."
        )

    if not approved_information or not approved_information.strip():

        return (
            "Unable to analyze outdated content. "
            "No approved company information was provided."
        )

    # --------------------------------------------------------
    # LIMIT CONTEXT
    # --------------------------------------------------------

    website_content = existing_content[
        :MODULE_CONTEXT_LIMIT
    ]

    company_information = approved_information[
        :MODULE_CONTEXT_LIMIT
    ]

    # --------------------------------------------------------
    # OUTDATED CONTENT ANALYSIS PROMPT
    # --------------------------------------------------------

    prompt = f"""
You are the Outdated Content Detection Module of the
Godamwale AI Content Agent.

Your task is to compare existing website content against
approved company information and identify information that
may be outdated, inconsistent, incorrect, or require review.

============================================================
EXISTING WEBSITE CONTENT
============================================================

{website_content}

============================================================
APPROVED COMPANY INFORMATION
============================================================

{company_information}

============================================================
ANALYSIS RULES
============================================================

Compare ONLY the information provided.

Do not use outside knowledge.

Do not invent facts.

Do not assume that missing information is incorrect.

Do not assume that a difference automatically means that
the website information is outdated.

Pay particular attention to:

- Company services
- Locations
- Business offerings
- Company descriptions
- Capabilities
- Contact-related information
- Operational information
- Statistics
- Certifications
- Other company-specific claims

============================================================
CLASSIFICATION RULES
============================================================

Classify findings into these categories:

CONFIRMED DIFFERENCE:

Use this only when the supplied approved information clearly
contradicts the existing website content.

POSSIBLE OUTDATED INFORMATION:

Use this when the information appears potentially outdated
based on the supplied information, but the available evidence
is not sufficient to confirm it.

MISSING FROM WEBSITE:

Use this when important information exists in the approved
company information but is not clearly represented in the
website content.

INFORMATION REQUIRING VERIFICATION:

Use this when the available information is insufficient to
determine whether something is correct or outdated.

============================================================
IMPORTANT SAFETY RULES
============================================================

- Do not say information is outdated unless there is evidence.
- Do not say a service has stopped unless the supplied
  information confirms this.
- Do not say a location has closed unless the supplied
  information confirms this.
- Do not treat missing information as incorrect.
- Do not create replacement facts.
- Do not recommend removing information solely because it is
  absent from the approved information.
- Clearly distinguish facts from possibilities.
- If there are no confirmed differences, explicitly say so.

============================================================
RETURN FORMAT
============================================================

Outdated Content Review:


1. Confirmed Differences

(List only clear contradictions between the website and
approved company information.)

Write:

None found.

if there are no confirmed differences.


2. Possible Outdated Information

(List information that may be outdated but cannot be
confirmed from the supplied information.)

Write:

None identified.

if there are no possible issues.


3. Missing Information

(List important information from the approved company
information that is not clearly represented on the website.)

Write:

None identified.

if there is no important missing information.


4. Recommended Updates

(Provide practical updates based only on the supplied
information.)


5. Information Requiring Verification

(List information that requires human checking before
making changes.)

Write:

None

if no verification is required.


6. Overall Assessment

(Summarize whether the supplied information indicates:

- Confirmed outdated information
- Possible outdated information
- Mostly consistent information
- Insufficient information for a reliable comparison
)
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
            "Outdated content detection error:",
            error
        )

        return (
            "Unable to analyze outdated website content "
            "at this time."
        )