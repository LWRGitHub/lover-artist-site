import json

products = [
    {
        "src": "data:image/gif;base64,R0lGODdhFQAXAPAAANba3wAAACwAAAAAFQAXAAACFISPqcvtD6OctNqLs968+w+GolUAADs=",
        "alt": "#",
        "title": "Example Product",
        "_id": 123456789
    },
    {
        "src": "https://ih1.redbubble.net/image.1751903044.6537/fp,840x830,black,off_white,box20,s,f8f8f8-pad,1000x1000,f8f8f8.jpg",
        "alt": "#",
        "title": "Example Product",
        "_id": 7653413
    }
]
data = json.dumps(products)

f = open("data.txt", "a")
f.write(data)
f.close()

#open and read the file after the appending:
f = open("data.txt", "r")
print(f.read())