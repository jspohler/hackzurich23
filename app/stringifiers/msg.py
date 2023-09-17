import os
import glob
import extract_msg

def extract_data(msg_file):
    content = ''
    try:
        msg = extract_msg.Message(msg_file)
        sender = msg.sender if hasattr(msg, 'sender') else "N/A"
        recipients = msg.to if hasattr(msg, 'to') else "N/A"
        subject = msg.subject if hasattr(msg, 'subject') else "N/A"
        email_text = msg.body if hasattr(msg, 'body') else "N/A"
    except (UnicodeEncodeError, AttributeError, TypeError):
        pass
    content += f"Sender: {sender}\n"
    content += f"Recipients: {recipients}\n"
    content += f"Subject: {subject}\n"
    content += "Email Text:\n"
    content += email_text
    return content