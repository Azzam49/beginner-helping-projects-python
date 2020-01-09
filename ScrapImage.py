
import bs4,requests,os

imageUrl = "https://upload.wikimedia.org/wikipedia/commons/thumb/e/eb/Ash_Tree_-_geograph.org.uk_-_590710.jpg/220px-Ash_Tree_-_geograph.org.uk_-_590710.jpg"

os.makedirs("ImageFolder", exist_ok=True)

res = requests.get(imageUrl)

res.raise_for_status()

imageFile = open("ImageFolder//Tree.jpg","wb")

for chunk in res.iter_content():
    imageFile.write(chunk)

imageFile.close()
