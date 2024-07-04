# import pyduinocli
# import json
# def arduino_upload():
#     arduino = pyduinocli.Arduino("./arduino-cli")
#     try:
#         a = arduino.compile(r"code/code.ino", fqbn = "arduino:avr:micro")
#     except:
#         pass
#     with open("demo.json", "w") as f:
#         json.dump(a, f, indent=4)
#     # print("Success" if "Global variables use" in a else "Error")
#     return a["result"]["success"]

# # arduino.upload(r"demo/demo.ino", fqbn="arduino:avr:mega", port="COM6")

books={'Hands on data science':1160,
'Python and R':7215,
'Handbook Statistics':18000,
'Data science Python projects':300,
'Machine Learning':4000
}
i=1
# You are using Python
updated = {}
while(i):
    name = input()
    cost = int(input())
    i = int(input())
    books[name] = cost
print(sorted(books.items()))
for book in books:
    if 1000 < books[book] < 2999:
        updated[book] = books[book] - books[book] * 0.05
        print(updated[book])
    if 3000 < books[book] < 5000:
        updated[book] = books[book] - books[book] * 0.03
    if books[book] > 5000:
        updated[book] = books[book] - books[book] * 0.02
    else:
        updated[book] = books[book]
print(sorted(updated.items()))