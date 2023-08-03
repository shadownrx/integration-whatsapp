
import os
from twilio.rest import Client


account_sid = os.environ['Api_key']
auth_token = os.environ['Api_token']
client = Client(account_sid, auth_token)

message = client.messages.create(
                              body='Hello there!',
                              from_='whatsapp:+14155238886',
                              to='whatsapp:+543816375805'
                          )

print(message.sid)


