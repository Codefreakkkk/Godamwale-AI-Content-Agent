import os

from dotenv import load_dotenv
from openai import OpenAI

from config import (
    MODEL_NAME,
    MAX_TOKENS
)


# ============================================================
# ENVIRONMENT CONFIGURATION
# ============================================================

load_dotenv()

api_key = os.getenv(
    "OPENROUTER_API_KEY"
)


# ============================================================
# OPENROUTER CLIENT
# ============================================================

client = None

if api_key:

    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
        timeout=30.0
    )


# ============================================================
# AI REQUEST FUNCTION
# ============================================================

def ask_ai(prompt):
    """
    Send a prompt to the configured AI model.

    Returns generated text on success.
    Returns a safe error message on failure.
    """

    # --------------------------------------------------------
    # PROMPT VALIDATION
    # --------------------------------------------------------

    if not prompt or not prompt.strip():

        return (
            "Unable to generate AI response currently. "
            "No prompt was provided."
        )


    # --------------------------------------------------------
    # API CONFIGURATION VALIDATION
    # --------------------------------------------------------

    if not api_key:

        print(
            "AI service error: "
            "OPENROUTER_API_KEY is not configured."
        )

        return (
            "Unable to generate AI response currently. "
            "The AI service is not configured."
        )


    if client is None:

        print(
            "AI service error: "
            "OpenRouter client is unavailable."
        )

        return (
            "Unable to generate AI response currently. "
            "The AI service is not available."
        )


    # --------------------------------------------------------
    # AI REQUEST
    # --------------------------------------------------------

    try:

        response = client.chat.completions.create(

            model=MODEL_NAME,

            max_tokens=MAX_TOKENS,

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )


        # ----------------------------------------------------
        # RESPONSE VALIDATION
        # ----------------------------------------------------

        if not response.choices:

            print(
                "AI service returned no choices."
            )

            return (
                "Unable to generate AI response currently. "
                "No response was returned by the AI service."
            )


        message = response.choices[0].message


        if message is None:

            print(
                "AI service returned no message."
            )

            return (
                "Unable to generate AI response currently. "
                "No response message was returned."
            )


        result = message.content


        if not result or not result.strip():

            print(
                "AI service returned empty content."
            )

            return (
                "Unable to generate AI response currently. "
                "The AI service returned an empty response."
            )


        # ----------------------------------------------------
        # RETURN CLEAN RESPONSE
        # ----------------------------------------------------

        return result.strip()


    # --------------------------------------------------------
    # AI / NETWORK / API ERROR
    # --------------------------------------------------------

    except Exception as error:

        print(
            "AI service error occurred:",
            error
        )

        return (
            "Unable to generate AI response currently. "
            "Please try again later."
        )