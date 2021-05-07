import pandas as pd

risk_free = pd.read_csv('.\\Data\\risk_free_return.csv')
risk_free.Date = pd.to_datetime(risk_free.Date)
risk_free = risk_free.set_index('Date')
