import requests

from bs4 import BeautifulSoup

from urllib.parse import (
    urljoin,
    urlparse
)

from config import (
    MAX_WEBSITE_PAGES,
    WEBSITE_CONTENT_LIMIT
)


# ============================================================
# HTTP REQUEST
# ============================================================

def fetch_page(url):

    try:

        headers = {
            "User-Agent": (
                "Mozilla/5.0 "
                "(Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 "
                "(KHTML, like Gecko) "
                "Chrome/151.0 Safari/537.36"
            )
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        response.raise_for_status()

        return response

    except Exception as error:

        print(
            "Website request error:",
            url,
            error
        )

        return None


# ============================================================
# PAGE CONTENT EXTRACTION
# ============================================================

def extract_page_content(
    url,
    response=None
):

    try:

        if response is None:

            response = fetch_page(
                url
            )

        if response is None:

            return ""

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        # ----------------------------------------------------
        # Remove non-content elements
        # ----------------------------------------------------

        for tag in soup(
            [
                "script",
                "style",
                "nav",
                "footer",
                "header",
                "noscript",
                "svg"
            ]
        ):

            tag.decompose()

        # ----------------------------------------------------
        # Extract visible text
        # ----------------------------------------------------

        text = soup.get_text(
            separator="\n"
        )

        cleaned_text = "\n".join(
            line.strip()
            for line in text.splitlines()
            if line.strip()
        )

        return cleaned_text

    except Exception as error:

        print(
            "Page extraction error:",
            url,
            error
        )

        return ""


# ============================================================
# TOKEN ESTIMATION
# ============================================================

def estimate_tokens(text):

    if not text:

        return 0

    return max(
        1,
        len(text) // 4
    )


# ============================================================
# URL NORMALIZATION
# ============================================================

def normalize_url(url):

    url = url.strip()

    if not url:

        return ""

    if not url.startswith(
        (
            "http://",
            "https://"
        )
    ):

        url = (
            "https://"
            + url
        )

    return url.rstrip("/")


# ============================================================
# INTERNAL LINK DISCOVERY
# ============================================================

def find_internal_links(
    base_url,
    response
):

    links = []

    try:

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        base_domain = urlparse(
            base_url
        ).netloc.lower()

        for link in soup.find_all(
            "a",
            href=True
        ):

            href = link.get(
                "href"
            )

            if not href:

                continue

            full_url = urljoin(
                base_url,
                href
            )

            parsed_url = urlparse(
                full_url
            )

            domain = (
                parsed_url.netloc
                .lower()
            )

            # ------------------------------------------------
            # Same-domain pages only
            # ------------------------------------------------

            if domain != base_domain:

                continue

            # ------------------------------------------------
            # HTTP/HTTPS only
            # ------------------------------------------------

            if parsed_url.scheme not in [
                "http",
                "https"
            ]:

                continue

            # ------------------------------------------------
            # Remove fragments
            # ------------------------------------------------

            clean_url = full_url.split(
                "#"
            )[0].rstrip("/")

            if not clean_url:

                continue

            # ------------------------------------------------
            # Avoid duplicate URLs
            # ------------------------------------------------

            if clean_url in links:

                continue

            # ------------------------------------------------
            # Prefer useful business pages
            # ------------------------------------------------

            useful_keywords = [
                "service",
                "services",
                "solution",
                "solutions",
                "about",
                "warehouse",
                "warehousing",
                "location",
                "locations",
                "contact",
                "fulfillment",
                "logistics",
                "3pl"
            ]

            url_lower = (
                clean_url.lower()
            )

            link_text = (
                link.get_text(
                    " ",
                    strip=True
                ).lower()
            )

            if (
                any(
                    keyword in url_lower
                    for keyword in useful_keywords
                )
                or
                any(
                    keyword in link_text
                    for keyword in useful_keywords
                )
            ):

                links.append(
                    clean_url
                )

    except Exception as error:

        print(
            "Internal link discovery error:",
            error
        )

    return links


# ============================================================
# WEBSITE CONTENT EXTRACTION
# ============================================================

def extract_website_content(url):

    try:

        # ----------------------------------------------------
        # Normalize URL
        # ----------------------------------------------------

        url = normalize_url(
            url
        )

        if not url:

            return (
                "",
                {
                    "pages": [],
                    "total_pages": 0,
                    "total_characters": 0,
                    "total_estimated_tokens": 0,
                    "error": "Invalid URL"
                }
            )

        # ----------------------------------------------------
        # Storage
        # ----------------------------------------------------

        website_content = ""

        visited_pages = set()

        page_statistics = []

        # ----------------------------------------------------
        # Load main page
        # ----------------------------------------------------

        main_response = fetch_page(
            url
        )

        if main_response is None:

            return (
                "",
                {
                    "pages": [],
                    "total_pages": 0,
                    "total_characters": 0,
                    "total_estimated_tokens": 0,
                    "error": (
                        "Unable to load website"
                    )
                }
            )

        main_page_content = (
            extract_page_content(
                url,
                main_response
            )
        )

        visited_pages.add(
            url
        )

        # ----------------------------------------------------
        # Store main page
        # ----------------------------------------------------

        if main_page_content:

            page_statistics.append(
                {
                    "url": url,
                    "characters": len(
                        main_page_content
                    ),
                    "estimated_tokens": (
                        estimate_tokens(
                            main_page_content
                        )
                    )
                }
            )

            website_content += (
                "\n\n"
                "========================================\n"
                f"PAGE: {url}\n"
                "========================================\n\n"
                + main_page_content
            )

        # ----------------------------------------------------
        # Find internal pages
        # ----------------------------------------------------

        important_links = (
            find_internal_links(
                url,
                main_response
            )
        )

        # ----------------------------------------------------
        # Respect configured page limit
        # ----------------------------------------------------

        remaining_pages = max(
            0,
            MAX_WEBSITE_PAGES - 1
        )

        selected_links = (
            important_links[
                :remaining_pages
            ]
        )

        # ----------------------------------------------------
        # Extract internal pages
        # ----------------------------------------------------

        for page in selected_links:

            if page in visited_pages:

                continue

            page_response = fetch_page(
                page
            )

            visited_pages.add(
                page
            )

            if page_response is None:

                continue

            page_content = (
                extract_page_content(
                    page,
                    page_response
                )
            )

            if not page_content:

                continue

            page_statistics.append(
                {
                    "url": page,
                    "characters": len(
                        page_content
                    ),
                    "estimated_tokens": (
                        estimate_tokens(
                            page_content
                        )
                    )
                }
            )

            website_content += (
                "\n\n"
                "========================================\n"
                f"PAGE: {page}\n"
                "========================================\n\n"
                + page_content
            )

        # ----------------------------------------------------
        # Website statistics
        # ----------------------------------------------------

        total_characters = sum(
            page["characters"]
            for page in page_statistics
        )

        total_estimated_tokens = sum(
            page["estimated_tokens"]
            for page in page_statistics
        )

        statistics = {

            "pages": page_statistics,

            "total_pages": len(
                page_statistics
            ),

            "total_characters": (
                total_characters
            ),

            "total_estimated_tokens": (
                total_estimated_tokens
            )
        }

        # ----------------------------------------------------
        # Controlled AI input
        # ----------------------------------------------------

        controlled_content = (
            website_content[
                :WEBSITE_CONTENT_LIMIT
            ]
        )

        return (
            controlled_content,
            statistics
        )

    except Exception as error:

        print(
            "Website extraction error:",
            error
        )

        return (
            "",
            {
                "pages": [],
                "total_pages": 0,
                "total_characters": 0,
                "total_estimated_tokens": 0,
                "error": str(error)
            }
        )