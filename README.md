# Тестовое задание

## Что сделано
### 1 задание: 
Flask приложение и postgresql собраны с помощью docker-compose`a, 
данные в БД прописываются в миграции вместе с созданием таблиц

### 2 задание: 
Выборки со всеми полями из каждой таблицы:
  - ```/api/racks```
  - ```/api/rooms```
  - ```/api/customers```
 
 Составная выборка всех occupied стоек с заданными полями: ```/api/racks/occupied```
 
 Выборка клиентов по комнате в необходимом виде не получилась, максимальный результат, 
 к которому получилось приблизиься - записи вида ```(Room.id, Room.name, Customer.id) ``` для каждой occupied стойки клиента, в итоговое приложение не включил
 
 Стойки с максимальной высотой для каждой серверной: максимально близкий полученный результат ```(Room.id, Rack.size)``` с помощью функций max и group_by, не понял как вытащить Rack.id
 
 ### 3 задание
 Четыре функции, принимающие произвольное количество аргументов созданы и доступны по:
  - ```/api/addition```
  - ```/api/subtraction```
  - ```/api/multiplication```
  - ```/api/division```
 Для всех четырех фукнций доступен аргумент reverse, '''/reverse'''
 
 Как подменить аргументы с тем условием что я получаю их из request, я не нашел
