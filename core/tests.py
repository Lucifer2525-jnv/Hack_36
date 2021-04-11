import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC5c02098e2b8867fc74d77cceaecd55af'
auth_token = '34a3711d0d07754a176ddd1680767244'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hello there!',
                              from_='+15085254297',
                              to='+917999776136'
                          )

print(message.sid)