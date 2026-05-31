# Импортируем библиотеку requests, файл с телом запроса, 
# и конфигурацию файла с URL и путями к API-методам.
import requests
import data
import configuration
import pytest

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

# Тоноян Виктория, 43-я кагорта — Финальный проект. Инженер по тестированию плюс
def test_order_creation_and_tracking():
    # Создание заказа
    create_response = post_new_orders(data.order_body)
    assert create_response.status_code == 201, "Не удалось создать заказ"

    # Сохранение трек-номера
    track_number = create_response.json().get("track")
    print("Заказ создан. Номер трека:", track_number)
    assert track_number, "Трек-номер не получен"

    # Получение заказа по трек-номеру
    get_response = get_order_by_track(track_number)
    assert get_response.status_code == 200, "Заказ не найден"
    print("Тест успешно пройден. Код 200.")