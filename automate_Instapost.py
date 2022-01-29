from instabot import Bot
bot=Bot()
username=""
bot.login(username=username,password="")
print("Login Successful")
img="demo.jpg"
bot.upload_photo(img,caption="This is a demo image")
bot.logout() 

