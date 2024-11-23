import win32com.client

def get_inbox_emails(namespace):
    #Launch Outlook
    inbox = namespace.GetDefaultFolder(6)
    messages = inbox.items
    print(f"Total messages in Inbox: {len(messages)}")
    
    #Print subject of the first 5 emails
    for i in range (min(5, len(messages))):
        message = messages[i]
        print(f"Subject: {message.Subject}")
        print(f"Sender: {message.SenderName}")
        print(f"Received: {message.ReceivedTime}")

#Example usage
outlook = win32com.client.Dispatch("Outlook.Application")
namespace = outlook.GetNamespace("MAPI")
get_inbox_emails(namespace)