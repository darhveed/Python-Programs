capitals =  {"USA": "Washington D.C.",
             "Nigeria": "Abuja",
             "Ghana": "Accra",
             "Russia": "Moscow"}
State = {"Ondo": "Akure",
         "Lagos": "Ikeja",
         "F.C.T": "Abuja",
         "Ogun": "Abeokuta"}

#print(State.get("Ogun"))
#if capitals.get("Russia"):
 #   print("That Capital exist.")
#else:
#     print("That Capital doesn't exist.")

#capitals.update({"Germany": "Berlin"})
#capitals.pop("Nigeria")
#capitals.popitem()
#capitals.clear()
#keys = capitals.keys()
#for key in capitals.keys():
    #print(key)

#values = capitals.values()
#for value in capitals.values():
    #print(value)

items = capitals.items()
for key, value in capitals.items():
    print(f'{key}: {value}')