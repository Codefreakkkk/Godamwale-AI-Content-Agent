import re


def calculate_content_quality(content):

    if not content or len(content.strip()) == 0:

        return {
            "score": 0,
            "details": {},
            "suggestions": [
                "No content available for analysis."
            ]
        }


    content = content.strip()


    words = content.split()


    sentences = re.split(
        r'[.!?]+',
        content
    )


    sentences = [
        s.strip()
        for s in sentences
        if s.strip()
    ]


    paragraphs = [
        p.strip()
        for p in content.split("\n\n")
        if p.strip()
    ]


    word_count = len(words)


    sentence_count = max(
        len(sentences),
        1
    )


    average_sentence_length = (
        word_count / sentence_count
    )



    suggestions = []



    # -------------------------
    # Readability
    # -------------------------

    readability_score = 20


    if average_sentence_length > 20:

        readability_score -= 3


    if average_sentence_length > 30:

        readability_score -= 5


    if average_sentence_length > 40:

        readability_score -= 5



    readability_score = max(
        readability_score,
        5
    )



    # -------------------------
    # Structure
    # -------------------------

    structure_score = 20


    if word_count < 80:

        structure_score -= 5

        suggestions.append(
            "Content is short and may require more detail."
        )


    if len(paragraphs) < 2:

        structure_score -= 5

        suggestions.append(
            "Add clearer sections or paragraphs."
        )


    if not re.search(
        r'(^|\n)([A-Z][A-Za-z ]+):',
        content
    ):

        structure_score -= 3

        suggestions.append(
            "Consider adding headings for better structure."
        )



    structure_score = max(
        structure_score,
        5
    )



    # -------------------------
    # Paragraph Quality
    # -------------------------

    paragraph_score = 20


    long_paragraphs = [

        p for p in paragraphs

        if len(p.split()) > 120

    ]


    if long_paragraphs:

        paragraph_score -= 5

        suggestions.append(
            "Break large paragraphs into smaller sections."
        )



    paragraph_score = max(
        paragraph_score,
        5
    )



    # -------------------------
    # Business Keyword Usage
    # -------------------------

    keyword_score = 20


    logistics_keywords = [

        "warehouse",
        "warehousing",
        "logistics",
        "storage",
        "supply chain",
        "inventory",
        "customer",
        "business",
        "service",
        "solution"

    ]


    lower_content = content.lower()


    keyword_found = 0


    for keyword in logistics_keywords:

        if keyword in lower_content:

            keyword_found += 1



    if keyword_found < 3:

        keyword_score -= 5

        suggestions.append(
            "Include more relevant logistics and business keywords."
        )


    if keyword_found < 1:

        keyword_score -= 5



    keyword_score = max(
        keyword_score,
        5
    )



    # -------------------------
    # Sentence Quality
    # -------------------------

    sentence_score = 20


    if average_sentence_length > 30:

        sentence_score -= 5


    if average_sentence_length < 5:

        sentence_score -= 5



    repeated_sentences = (

        len(sentences)

        -

        len(set(sentences))

    )


    if repeated_sentences > 0:

        sentence_score -= 5

        suggestions.append(
            "Avoid repeating similar sentences."
        )



    sentence_score = max(
        sentence_score,
        5
    )



    total_score = (

        readability_score

        +

        structure_score

        +

        paragraph_score

        +

        keyword_score

        +

        sentence_score

    )



    if not suggestions:

        suggestions.append(
            "Content structure and quality look good."
        )



    return {

        "score": total_score,

        "details": {

            "Readability":
                f"{readability_score}/20",

            "Structure":
                f"{structure_score}/20",

            "Paragraph Quality":
                f"{paragraph_score}/20",

            "Keyword Usage":
                f"{keyword_score}/20",

            "Sentence Quality":
                f"{sentence_score}/20"

        },

        "suggestions": suggestions

    }