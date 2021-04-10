import os
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'AC5c02098e2b8867fc74d77cceaecd55af'
auth_token = 'ba78dd79b097140995725d3844a31de5'
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hello there!',
                              from_='+15085254297',
                              to='+917999776136'
                          )

print(message.sid)