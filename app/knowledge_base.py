import os


# ============================================================
# DOCUMENT FOLDERS
# ============================================================

def get_documents_folder():

    project_folder = os.path.join(
        os.path.dirname(__file__),
        ".."
    )

    return os.path.join(
        project_folder,
        "documents"
    )


def get_company_folder():

    documents_folder = get_documents_folder()

    return os.path.join(
        documents_folder,
        "company"
    )


# ============================================================
# TEXT FILE READER
# ============================================================

def read_text_file(
    file_path
):

    try:

        with open(
            file_path,
            "r",
            encoding="utf-8"
        ) as file:

            return file.read()

    except Exception as error:

        print(
            "Knowledge base reading error:",
            file_path,
            error
        )

        return ""


# ============================================================
# READ TEXT FILES FROM FOLDER
# ============================================================

def read_text_files_from_folder(
    folder_path
):

    combined_information = ""

    if not os.path.exists(
        folder_path
    ):

        return ""


    for file_name in os.listdir(
        folder_path
    ):

        file_path = os.path.join(
            folder_path,
            file_name
        )


        if not os.path.isfile(
            file_path
        ):

            continue


        extension = os.path.splitext(
            file_name
        )[1].lower()


        if extension != ".txt":

            continue


        content = read_text_file(
            file_path
        )


        if content:

            combined_information += (
                "\n\n"
                "========================================\n"
                f"FILE: {file_name}\n"
                "========================================\n\n"
                + content
            )


    return combined_information


# ============================================================
# COMPANY INFORMATION
# ============================================================

def load_company_information():

    company_folder = get_company_folder()

    return read_text_files_from_folder(
        company_folder
    )