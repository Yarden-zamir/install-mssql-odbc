from os import getenv

from requests import get

remove_exits = getenv('REMOVE_EXITS', "True")
docs_url = getenv('DOCS_URL',
                  "https://raw.githubusercontent.com/MicrosoftDocs/sql-docs/live/docs/connect/odbc/linux-mac"
                  "/installing-the-microsoft-odbc-driver-for-sql-server.md")
distro = getenv("DISTRO", "Ubuntu")
ODBC_version = getenv("ODBC_VERSION", "18")

ODBC_section = get(docs_url).text.split(f"Microsoft ODBC {ODBC_version}")[1].split("---")[0]
platforms = ODBC_section.split("### [")[1:]
per_platform_instructions = {}
for platform in platforms:
    name = platform.split("]")[0]
    code = platform.split("```bash")[1].split("```")[0]
    per_platform_instructions[name] = code.replace("exit\n", "") if remove_exits else code

print(per_platform_instructions[distro])
