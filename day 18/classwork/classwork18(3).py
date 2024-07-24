kuknishvili_dict = {
    "name": "dati",
    "age": 23,
}

kuknishvili_dict.update({"surname": "kuknishvili"})
kuknishvili_dict["email"] = "kuknishvilidati@gmail.com"
print(kuknishvili_dict)

for key in kuknishvili_dict:
    print(kuknishvili_dict[key])
    