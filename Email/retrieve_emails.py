"""
This program will explain how to get the emails from out inbox using python
IMAP: Internet message access protocal -- interacts with service providers to get the mails
python module: imaplib

Third party modules" pip install imapclinet
                        pip install pyzmail
"""

import imapclient

conn = imapclient.IMAPClient("imap.gmail.com",ssl=True)
conn.login("mail_id","password")

conn.select_folder('INBOX', readonly=True)

UIDs = conn.search(['SINCE 20-Aug-2019'])

raw_message = conn.fetch([uid],['BODY[]','FLAGS'])

import pyzmail

message = pyzmail.PyzMessage.factory(raw_message[uid][b'BODY[]'])
message.get_subject()
message.get_addresses('from')
message.get_addresses('to')
message.get_addresses('bcc')

message.text_part
message.html_part
message.text_part.get_payload().decode('UTF-8')

conn.delete_messages([uids])
