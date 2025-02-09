import pandas as pd
data = {"number": [i for i in range(1,11)],
        "letter": [i for i in 'abcdefghij']}

df = pd.DataFrame(data)

df.to_csv('dumb.csv')