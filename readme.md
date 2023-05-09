[![Pylint](https://github.com/Yarden-zamir/install-mssql-odbc/actions/workflows/pylint.yml/badge.svg)](https://github.com/Yarden-zamir/install-mssql-odbc/actions/workflows/pylint.yml)
# install-mssql-odbc
Action for installing ODBC drivers for mssql exactly according to [Microsoft's instructions](https://learn.microsoft.com/en-us/sql/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server?view=sql-server-ver16&tabs=redhat18-install%2Calpine17-install%2Cdebian8-install%2Credhat7-13-install%2Crhel7-offline#18).

This action runs a python script that scrapes Microsoft's official instructions per the requested distribution and executes them.
By default we remove "exit\n" cases that are found in the instructions.
```yaml
inputs:
  ODBC_VERSION:
    description: 'ODBC version to install (18 or 17 validated)'
    default: "18"
  DISTRO:
    description: 'Distribution (Alpine, Debian, RHEL and Oracle Linux, SLES, Ubuntu)'
    default: Ubuntu
  DOCS_URL:
    description: 'URL to the docs page to scrape instructions from'
    default: "https://raw.githubusercontent.com/MicrosoftDocs/sql-docs/live/docs/connect/odbc/linux-mac/installing-the-microsoft-odbc-driver-for-sql-server.md"
  REMOVE_EXITS:
    default: 'true'
    description: 'Remove exit statements from the script (they break the workflow)'
```
Usage examples
```yaml
# minimal
      - uses: Yarden-zamir/install-mssql-odbc@main
```

```yaml
# all inputs
      - uses: Yarden-zamir/install-mssql-odbc@main
        with:
          ODBC_VERSION: 17
          DISTRO: Alpine
          DOCS_URL: https://yarden-zamir.com/alternate-docs-path.md
          REMOVE_EXITS: false
```