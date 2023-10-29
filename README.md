# PostgreSQL Python: Connect To PostgreSQL Database Server

## Steps
- Install the psycopg2 module
- Connect to the PostgreSQL database using the psycopg2
- Database Connection Parameters #fetches environment variables for the database connection.
- fetches environment variables for the database connection
- attempts to establish a connection to the PostgreSQL database using the psycopg2.connect()
- Fetching the SQL Query from Command Line

Following Queries are excuted:
- `SELECT COUNT(*) FROM projects`
- `SELECT COUNT(*) FROM projects WHERE "qb_mcnNumber" != '9572338';`
- `SELECT COUNT(*) FROM projects WHERE type = 'Installation - New System' AND "qb_mcnNumber" != '9572338';`
- `SELECT COUNT(*) FROM projects WHERE type = 'System Refresh' AND "qb_mcnNumber" != '9572338' ;`
- `SELECT COUNT(*) FROM projects WHERE type = 'Software Essentials' AND "qb_mcnNumber" != '9572338';`


