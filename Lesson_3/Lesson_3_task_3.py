from address import Address
from mailing import Mailing

to_address = Address("12345", "Москва", "Ленина", "10", "20")
from_address = Address("54321", "Санкт-Петербург", "Пушкина", "5", "10")
Mailing = Mailing(to_address, from_address, 500, "ABC123")

print(f"Отправление {Mailing.track} из {Mailing.from_address.index}, {Mailing.from_address.city},"
      f"{Mailing.from_address.street}, {Mailing.from_address.house} - {Mailing.from_address.apartment}"
      f"в {Mailing.to_address.index}, {Mailing.to_address.city}, {Mailing.to_address.street},"
      f"{Mailing.to_address.house} - {Mailing.to_address.apartment}. Стоимость {Mailing.cost} рублей.")
