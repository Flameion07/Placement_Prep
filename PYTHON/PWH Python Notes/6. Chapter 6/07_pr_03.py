spamWords = ['buy now', 'subscribe this', 'click this']

# email = "this is a nice stock. You need to click this and buy this stock"
email = input("Enter your email: ").lower()
spam = False

if('buy now' in email):
    spam = True

if('subscribe this' in email):
    spam = True

if('click this' in email):
    spam = True

print("Spam is", spam)
