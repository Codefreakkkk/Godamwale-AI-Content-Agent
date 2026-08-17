from modules.optimization import optimize_content
from modules.outdated import detect_outdated_content
from modules.blog_generator import generate_blog
from modules.blog_optimizer import optimize_blog
from modules.seo_optimizer import optimize_seo
from modules.social_media_generator import generate_social_media
from modules.email_generator import generate_email
from modules.competitor_analysis import analyze_competitor

from knowledge_base import (
    load_company_information
)

from rag_system import (
    create_vector_database,
    retrieve_information
)


# ============================================================
# VALID MODULES
# ============================================================

VALID_MODULES = {
    "optimization",
    "outdated",
    "blog",
    "seo",
    "social_media",
    "email",
    "competitor_analysis"
}


# ============================================================
# MAIN AGENT CONTROLLER
# ============================================================

def run_agent(
    user_request,
    website_content=None,
    competitor_content=None,
    selected_module=None
):
    """
    Main controller for the Godamwale AI Content Agent.

    Responsibilities:
    - Validate the request
    - Validate the selected module
    - Load approved company information
    - Add dynamically extracted website information
    - Create the RAG context
    - Retrieve relevant information
    - Execute the selected module
    - Return the selected module and result

    The UI provides the selected module directly.
    """

    # --------------------------------------------------------
    # INPUT VALIDATION
    # --------------------------------------------------------

    if not user_request or not user_request.strip():

        return (
            "optimization",
            "Please provide a request for the AI Content Agent."
        )


    # --------------------------------------------------------
    # MODULE VALIDATION
    # --------------------------------------------------------

    if selected_module not in VALID_MODULES:

        return (
            "optimization",
            "Invalid content task selected."
        )


    # --------------------------------------------------------
    # LOAD APPROVED COMPANY INFORMATION
    # --------------------------------------------------------

    company_data = load_company_information()


    # --------------------------------------------------------
    # ADD DYNAMIC WEBSITE INFORMATION
    # --------------------------------------------------------

    combined_information = company_data


    if website_content and website_content.strip():

        combined_information += (
            "\n\n"
            "Website Information:\n"
            + website_content
        )


    # --------------------------------------------------------
    # CREATE RAG DATABASE
    # --------------------------------------------------------

    vectorizer, vectors, chunks = create_vector_database(
        combined_information
    )


    # --------------------------------------------------------
    # RETRIEVE RELEVANT INFORMATION
    # --------------------------------------------------------

    company_information = retrieve_information(
        user_request,
        vectorizer,
        vectors,
        chunks
    )


    # --------------------------------------------------------
    # FALLBACK CONTEXT
    # --------------------------------------------------------

    if not company_information:

        company_information = company_data


    # --------------------------------------------------------
    # EXISTING WEBSITE CONTENT
    # --------------------------------------------------------

    existing_content = (
        website_content
        if website_content and website_content.strip()
        else ""
    )


    # --------------------------------------------------------
    # EXECUTE SELECTED MODULE
    # --------------------------------------------------------

    try:

        # ====================================================
        # WEBSITE CONTENT OPTIMIZATION
        # ====================================================

        if selected_module == "optimization":

            if not existing_content:

                return (
                    selected_module,
                    "Website content is required for optimization."
                )


            result = optimize_content(
                existing_content,
                company_information
            )


            return selected_module, result


        # ====================================================
        # OUTDATED CONTENT DETECTION
        # ====================================================

        elif selected_module == "outdated":

            if not existing_content:

                return (
                    selected_module,
                    "Website content is required for outdated-content detection."
                )


            result = detect_outdated_content(
                existing_content,
                company_information
            )


            return selected_module, result


        # ====================================================
        # BLOG GENERATION + OPTIMIZATION
        # ====================================================

        elif selected_module == "blog":

            generated_blog = generate_blog(
                user_request,
                company_information
            )


            target_keyword = _extract_target_keyword(
                user_request
            )


            optimized_blog = optimize_blog(
                blog_content=generated_blog,
                target_keyword=target_keyword,
                company_information=company_information
            )


            return (
                selected_module,
                {
                    "generated_blog": generated_blog,
                    "optimized_blog": optimized_blog
                }
            )


        # ====================================================
        # SEO & AIO ANALYSIS
        # ====================================================

        elif selected_module == "seo":

            if not existing_content:

                return (
                    selected_module,
                    "Website content is required for SEO analysis."
                )


            result = optimize_seo(
                existing_content,
                company_information
            )


            return selected_module, result


        # ====================================================
        # SOCIAL MEDIA
        # ====================================================

        elif selected_module == "social_media":

            result = generate_social_media(
                company_information
            )


            return selected_module, result


        # ====================================================
        # EMAIL
        # ====================================================

        elif selected_module == "email":

            result = generate_email(
                company_information
            )


            return selected_module, result


        # ====================================================
        # COMPETITOR ANALYSIS
        # ====================================================

        elif selected_module == "competitor_analysis":

            if not existing_content:

                return (
                    selected_module,
                    "Godamwale website content is required for competitor analysis."
                )


            if not competitor_content or not competitor_content.strip():

                return (
                    selected_module,
                    "Competitor website content is required for competitor analysis."
                )


            target_keyword = _extract_target_keyword(
                user_request
            )


            result = analyze_competitor(
                target_keyword=target_keyword,
                company_content=existing_content,
                competitor_content=competitor_content
            )


            return selected_module, result


        # ====================================================
        # UNKNOWN MODULE
        # ====================================================

        else:

            return (
                selected_module,
                "Could not identify the correct module."
            )


    except Exception as error:

        print(
            "Agent execution error:",
            error
        )


        return (
            selected_module,
            "Unable to complete the requested operation at this time."
        )


# ============================================================
# TARGET KEYWORD EXTRACTION
# ============================================================

def _extract_target_keyword(
    user_request
):
    """
    Extracts a target keyword from requests formatted like:

    Target Keyword:
    warehouse in Kolkata
    """

    if not user_request:

        return "Not specified"


    lines = user_request.splitlines()


    for index, line in enumerate(lines):

        if line.strip().lower() == "target keyword:":

            if index + 1 < len(lines):

                keyword = lines[
                    index + 1
                ].strip()


                if keyword:

                    return keyword


    return "Not specified"