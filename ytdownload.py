import pytube

url = input("Enter video url")

path="C:/Users/ASUS/Downloads"

pytube.YouTube(url).streams.get_highest_resolution().download(path)