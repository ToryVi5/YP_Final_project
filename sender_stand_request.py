# Импортируем библиотеку requests, файл с телом запроса, 
# и конфигурацию файла с URL и путями к API-методам.
import requests
import data
import configuration

# Выполненяем POST-запрос с использованием URL из конфигурационного файла и тела запроса
# для создания заказа
# json=body используем для отправки данных о создании заказа в формате JSON
def post_new_orders(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDERS_PATH,
                         json=body)

# Выполняем GET запрос на получение заказа по номеру трека
# Вызов функции requests.get с телом запроса для создания нового заказа из модуля data
def get_order_by_track(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH,
                        params={"t": track_number})