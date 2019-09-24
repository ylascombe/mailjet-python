from mailjet_rest import Client
import os

api_key = os.environ['API_KEY']
api_secret = os.environ['API_SECRET']
recipient = os.environ['TO']
from_mail = os.environ['FROM']

mailjet = Client(auth=(api_key, api_secret), version='v3.1')
data = {
  'Messages': [
    {
      "From": {
        "Email": from_mail,
        "Name": "Pod mailjet test on kubernetes"
      },
      "To": [
        {
          "Email": recipient,
          "Name": "Pod mailjet test on kubernetes"
        }
      ],
      "Subject": "Greetings from Mailjet.",
      "TextPart": "My first Mailjet email",
      "HTMLPart": "<h3>Dear passenger 1, welcome to <a href='https://www.mailjet.com/'>Mailjet</a>!</h3><br />May the delivery force be with you!",
      "CustomID": "AppGettingStartedTest"
    }
  ]
}
result = mailjet.send.create(data=data)
print(result.status_code)
print(result.json())

