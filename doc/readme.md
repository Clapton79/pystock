## Description of JSON database

### Data file type
#### Type 1
Holds daily stock stats
File naming convention:
TICKER_STARTDATE_ENDDATE_01.json

Column|Data type|Description
:---|:---:|:---
Date|Date|Datetime of rate
Open|Decimal(5,2)|Opening rate
High|Decimal(5,2)|Highest within interval
Low|Decimal(5,2)|Lowest within interval
Close|Decimal(5,2)|Closing within interval
Volume|Decimal(5,2)|Quantity

#### Type 2
Holds metrics to daily stock stats
TICKER_STARTDATE_ENDDATE_02.json

Column|Data type|Description
:---|:---:|:---
Date|Date|Datetime of metric
Metric|Text |Descriptor of metric (RSI, MACD, etc)
Value|Float|Value of the metric
