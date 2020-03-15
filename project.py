import plaid
import datetime
import json

access_token = "access-sandbox-f02d70ea-6a72-44d4-ad8f-e8520f45656a"

client = plaid.Client(client_id = "5e650dd550b89700137a3213", secret="b2a5b5db117f84ee3940bb89b3b74a",
                      public_key="8fb15895563ab1e7f8add4c0453212", environment="sandbox", api_version='2019-05-29')


start_date = '{:%Y-%m-%d}'.format(datetime.datetime.now() + datetime.timedelta(-30))
end_date = '{:%Y-%m-%d}'.format(datetime.datetime.now())

transactions = client.Transactions.get(access_token, start_date, end_date)
print(transactions)

#### Plot bar char payment channels
