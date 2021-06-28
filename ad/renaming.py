import os

names = ["\\ ".join(name.split(".")[0].split()) for name in os.listdir("./bears")]
for num, name in enumerate(names):
    os.system(f"mv ./bears/{name}.xml ./bears/image_{num}.xml")
    os.system(f"mv ./withBears/{name}.JPG ./withBears/image_{num}.JPG")

