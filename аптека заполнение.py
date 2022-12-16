query = """insert INTO supplier (number, address, company_name)
VALUES (89034566793, 'Санкт-Петербург', 'Bracco');
insert INTO supplier (number, address)
VALUES (89456341238, 'Москва', 'Глафарм');
insert INTO supplier (number, address)
VALUES (89456345908, 'Москва', 'Медторг');
insert INTO supplier (number, address)
VALUES (89075679367, 'Краснодар', 'Русская тройка');
insert INTO supplier (number, address)
VALUES (89098765096, 'Владивосток', 'Инфодиагностика');

insert INTO client (name, number)
VALUES ('Никита', 89783452683);
insert INTO client (name, number)
VALUES ('Паша', 89564309781);
insert INTO client (name, number)
VALUES ('Света', 89180987653);
insert INTO client (name, number)
VALUES ('Милана', 89236137964);
insert INTO client (name, number)
VALUES ('Кристина', 89093585678);

insert INTO pharmacy (address, number)
VALUES ('Москва', 89783452683);
insert INTO pharmacy (address, number)
VALUES ('Тюмень', 89567894230);
insert INTO pharmacy (address, number)
VALUES ('Пермь', 89097345671);
insert INTO pharmacy (address, number)
VALUES ('Кемерово', 89087653456);
insert INTO pharmacy (address, number)
VALUES ('Краснодар', 89783452683);


insert INTO pharmacy (name, category, price_medicines)
VALUES ('Атенолол', 'Адреноблокатор', 55 руб);
insert INTO pharmacy (name, category, price_medicines)
VALUES ('Нурофен', 'Нестероидные противоспалительные средства', 100 руб);
insert INTO pharmacy (name, category, price_medicines)
VALUES ('Мирамистин', 'Четвертичные аммонивые соединения', 300 руб);
insert INTO pharmacy (name, category, price_medicines)
VALUES ('Кагоцел', 'Индукторов интерферона', 250 руб);
insert INTO pharmacy (name, category, price_medicines)
VALUES ('Кардиомагнил', 'Антитромботические', 200 руб);
"""