# APPLICATION ARCHITECTURE

## LAYERS

Layer name | Role | Typical activities
:---|:---|:---
file engine| manages data files | Read, write files
query engine|put together queries|read from data files
data service engine|Run API requests to extract web data|Run API, pass data to file engine
logger engine|create log entries|write to log files, rotates log files
statistics engine|execute stats on a query|passes a query to the query engine then executes statistical methods on the data, forwards statistics data to file engine to save metrics
visualization engine|display data on charts|pass queries to the query engine, draw charts
portfolio manager|manages portfolios|reads and writes portfolio data files
service manager|manages services|read and write service descriptors, execute them
stream manager|creates and manages streams|create and start data streams
UI| user interface|
