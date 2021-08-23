# surfs_up

## Purpose of This Analysis
This analysis was done as part of a project to see if an ice cream business should be built in Oahu would be sustainable year-round. This project has me use data from the [hawaii.sqlite](https://github.com/bazinga183/surfs_up/blob/main/hawaii.sqlite) file. 

For this, I used Jupyter Notebook and used dependencies such as numpy, pandas, and sqlalchemy:
```
# Dependencies
import numpy as np
import pandas as pd

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
```

Then, I utilized SQLAlchemy's ```create_engine``` function to prepare SQLite queries for the dataset. I set up the foundation of the code using ```Base = automap_base()``` so that I could build upon SQLAlchemy and make sure the code functions correctly. Next, I prepared the data so that I could reflect tables and saved references to different sets of data within these tables:
```
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station
```

Last, I set up the ability to query the data with ```session = Session(engine)``` and I could begin my analysis of the data from that point.

## Results 

### June
To begin, I imported extract from SQLAlchemy to make filtering certain months from the year easier. The query used to get the data from the month of July was:
```
session.query(Measurement.date, Measurement.tobs).filter(extract('month', Measurement.date) == 6).all()
```

To convert this code into a list, I set ```results``` equal to the above query and then was able to translate this list into a DataFrame with the code:
```
df = pd.DataFrame(results, columns = ['date', 'temperature'])
```

The resulting DataFrame looked as such:

![june_results](https://user-images.githubusercontent.com/46951897/130465707-77c64934-ad9f-4c3b-8208-50a6731873fb.PNG)

I then gathered the summary statistics of June temperatures:

![june_summary_stats](https://user-images.githubusercontent.com/46951897/130466128-f1b0275d-9a56-4a3b-9472-9474d70a4abe.PNG)

### December
I used much of the same code for December as I did for June, I only had to replace the 6 with a 12 in ```filter(extract('month', Measurement.date) == 6)``` so that only December would show up.

The resulting DataFrame looked as such:

![december_results](https://user-images.githubusercontent.com/46951897/130466397-fc8f3ab5-9a9e-4c7f-898e-ce5fa323e836.PNG)

The summary statistics for the month of December:

![december_summary_stats](https://user-images.githubusercontent.com/46951897/130466523-9cb9a349-d80b-4663-b4ee-a86c3c9b3563.PNG)

### Conclusion
If we compare the summary statistics between June and December, we will notice:
  - June tends to be hotter than December where the means for the months are 74.9 degrees Fahrenheit versus 71.0 degrees Fahrenheit, respectively. This is only a difference of approximately 4 degrees.
  - The lowest temperature ever reached during the month of June was 64 degrees versus December's 56 degrees where the difference here is 8 degrees.
  - The median temperature for June was 75 degrees versus December's 71 degrees.

Looking at these comparisons, it seems that on its face it would be safe to build an ice cream shop that would be year-round since the temperatures between the summer and winter months do not differ drastically.

## Summary
In summary, the two months do not differ in temperature too much in Oahu. In fact, the median temperatures are very close in magnitude when considering how colder the winter months can be in other states. 
Another good metric to gather would be the amount of rainy, cloudy, windy, etc. kind of weather days where the ability or desire to eat ice cream may be affected. If these deterrents are strong enough, it may waver the sales of ice cream and force an early bankruptcy. Querying for days that were not sunny and grouping by these other weather conditions by month or year would allow for a richer analysis.
Also, while the data does suggest that the temperature would not differ, it may help to acquire the opinion of consumers to see how much their marginal propensity to consume drops off with each incremental decrease in temperature. This can be done by getting polls or sales data on days where the temperature was between December's lowest temperature, 56, and June's highest temperature, 85.
