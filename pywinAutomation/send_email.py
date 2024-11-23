import win32com.client

def send_outlook_email(subject, body, to_email):
    #Launch Outlook
    outlook = win32com.client.Dispatch("Outlook.Application")

    mail = outlook.CreateItem(0)
    mail.Subject = subject
    mail.Body = body
    mail.To = to_email
    mail.Send()

send_outlook_email("Test email", "Test body", "arjun.sudarsanan@outlook.com")