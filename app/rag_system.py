from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

from config import (
    CHUNK_SIZE,
    TOP_K_RESULTS
)


# ============================================================
# TEXT CHUNKING
# ============================================================

def create_chunks(
    text,
    chunk_size=CHUNK_SIZE
):
    """
    Split text into approximately equal-sized chunks.

    Chunk size is measured approximately in characters.
    """

    if not text or not text.strip():

        return []

    try:

        chunk_size = int(
            chunk_size
        )

    except (TypeError, ValueError):

        chunk_size = CHUNK_SIZE

    if chunk_size <= 0:

        chunk_size = CHUNK_SIZE

    chunks = []

    words = text.split()

    current_chunk = []

    current_length = 0

    for word in words:

        word_length = len(word) + 1

        # ----------------------------------------------------
        # Prevent a single extremely long word from creating
        # an oversized chunk.
        # ----------------------------------------------------

        if (
            current_chunk
            and
            current_length + word_length > chunk_size
        ):

            chunks.append(
                " ".join(
                    current_chunk
                )
            )

            current_chunk = []

            current_length = 0

        current_chunk.append(
            word
        )

        current_length += word_length


    # --------------------------------------------------------
    # Store remaining text
    # --------------------------------------------------------

    if current_chunk:

        chunks.append(
            " ".join(
                current_chunk
            )
        )


    return chunks


# ============================================================
# CREATE TF-IDF VECTOR DATABASE
# ============================================================

def create_vector_database(
    text
):
    """
    Create a TF-IDF representation of the supplied text.
    """

    chunks = create_chunks(
        text
    )

    if not chunks:

        return (
            None,
            None,
            []
        )


    try:

        vectorizer = TfidfVectorizer(
            ngram_range=(1, 2),
            lowercase=True,
            strip_accents="unicode"
        )


        vectors = vectorizer.fit_transform(
            chunks
        )


        return (
            vectorizer,
            vectors,
            chunks
        )


    except Exception as error:

        print(
            "Vector database creation error:",
            error
        )

        return (
            None,
            None,
            []
        )


# ============================================================
# RETRIEVE RELEVANT INFORMATION
# ============================================================

def retrieve_information(
    query,
    vectorizer,
    vectors,
    chunks,
    number_of_results=TOP_K_RESULTS
):
    """
    Retrieve the most relevant text chunks for a query
    using TF-IDF similarity.
    """

    if (
        not query
        or not query.strip()
        or vectorizer is None
        or vectors is None
        or not chunks
    ):

        return ""


    try:

        # ----------------------------------------------------
        # Validate number of results
        # ----------------------------------------------------

        try:

            number_of_results = int(
                number_of_results
            )

        except (TypeError, ValueError):

            number_of_results = TOP_K_RESULTS


        number_of_results = max(
            1,
            min(
                number_of_results,
                len(chunks)
            )
        )


        # ----------------------------------------------------
        # Convert query to TF-IDF vector
        # ----------------------------------------------------

        query_vector = vectorizer.transform(
            [query]
        )


        # ----------------------------------------------------
        # Calculate similarity
        # ----------------------------------------------------

        similarity_scores = (
            vectors @ query_vector.T
        ).toarray().flatten()


        # ----------------------------------------------------
        # Rank chunks by similarity
        # ----------------------------------------------------

        best_indices = np.argsort(
            similarity_scores
        )[::-1][:number_of_results]


        results = []

        seen_chunks = set()


        for index in best_indices:

            score = similarity_scores[
                index
            ]


            # ------------------------------------------------
            # Ignore completely unrelated chunks.
            # ------------------------------------------------

            if score <= 0:

                continue


            chunk = chunks[
                index
            ].strip()


            if not chunk:

                continue


            # ------------------------------------------------
            # Prevent duplicate chunks.
            # ------------------------------------------------

            normalized_chunk = (
                " ".join(
                    chunk.lower().split()
                )
            )


            if normalized_chunk in seen_chunks:

                continue


            seen_chunks.add(
                normalized_chunk
            )


            results.append(
                chunk
            )


        # ----------------------------------------------------
        # No relevant information found
        # ----------------------------------------------------

        if not results:

            return ""


        return "\n\n".join(
            results
        )


    except Exception as error:

        print(
            "Information retrieval error:",
            error
        )

        return ""   