import yagmail
yag = yagmail.SMTP('stinakallesson@gmail.com', oauth2_file="~/oauth2_creds.json")
contents = ['This is the body, and here is just text']
yag.send(subject="hello")