from smartpfone import Smartpfone

catalog = []

phone1 = Smartpfone("Samsung", "Galaxy M51", "+79206070471")
phone2 = Smartpfone("Apple", "iphone 15", "+79206080761")
phone3 = Smartpfone("Honor", "20S", "+79208369230")
phone4 = Smartpfone("Xiami", "pro", "+79206070478")
phone5 = Smartpfone("Realmi", "9Pro", "+79206070865")  

catalog.append(phone1)
catalog.append(phone2)
catalog.append(phone3)
catalog.append(phone4)
catalog.append(phone5)

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")