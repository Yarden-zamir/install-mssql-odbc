# install-mssql-odbc
Action for installing odbc drivers for mssql exactly according to microsofts instrucitons.

This action runs a python script that scrapes microsofts official instructions per the requested distribution and executes them.
By default we remove "exit\n" cases that are found in the instructions.
```yaml
inputs:
  ODBC_VERSION:
    description: 'ODBC version to install (18 or 17 validated)'
    default: "18"
  DISTRO:
    description: 'Distribution'
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