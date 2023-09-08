from simple_image_download import simple_image_download as simp

response = simp.simple_image_download

keyWords = ["orange ping pong ball"]

for kw in keyWords:
    response().download(kw, 1000) 