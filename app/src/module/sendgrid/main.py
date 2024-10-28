import sendgrid
from sendgrid.helpers.mail import Mail, Email, To, Content
import os
from secret import get_token
from dotenv import load_dotenv

load_dotenv()

prj_id = os.environ['PROJECT_ID']
api_key = os.environ['API_KEY']
# api_key = get_token(prj_id)
from_email = os.environ['FROM_EMAIL']

sg = sendgrid.SendGridAPIClient(api_key=api_key)
from_email = Email(from_email)   # 送信者のメールアドレス(Gmailの送信者名になる。認証なくても設定可能で任意のものが付けれる。その場合、受信側のセキュリティではじかれる可能性がある。)
to_emails = [
    To("test@test.com"),
    # To("")
]

subject = "SendGrid テストメール"
content = Content("text/plain", "テストメールです。SendGridとPythonを使用して送信されました。")
mail = Mail(from_email, to_emails, subject, content)

response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)
