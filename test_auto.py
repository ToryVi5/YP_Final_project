import pytest
import sender_stand_request
import data

# Тоноян Виктория, 43-я кагорта — Финальный проект. Инженер по тестированию плюс
def test_order_creation_and_tracking():
    # Создание заказа
    create_response = sender_stand_request.post_new_orders(data.order_body)
    assert create_response.status_code == 201
    assert "track" in create_response.json(), "Не удалось создать заказ"

def test_order_by_track():   
    create_response = sender_stand_request.post_new_orders(data.order_body)
    
    track_number = create_response.json()["track"]
    print("Заказ создан. Номер трека:", track_number)
    assert track_number, "Трек-номер не получен"
    
    # Получение заказа по трек-номеру
    get_response = sender_stand_request.get_order_by_track(track_number)
    assert get_response.status_code == 200, "Заказ не найден"
    print("Тест успешно пройден. Код 200.")