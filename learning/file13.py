phone_book={"Batman":486675,"Cersei":445566,"Ghostbusters":44778}
print(phone_book["Cersei"])
print(phone_book.get("Ghostbusters"))

phone_book["Batman"]=9211
phone_book["Godzilla"]=420
phone_book["abcd"]=4545
print(phone_book)

cersei=phone_book.pop("Cersei")
print(cersei)

lastAdded=phone_book.popitem()
print(lastAdded)

second_phone_book={"Jaime":237734,"Godzilla":37623,"Catwoman":67423}
phone_book.update(second_phone_book)
print(phone_book)

