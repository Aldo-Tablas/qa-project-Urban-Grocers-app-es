import sender_stand_request
import data

# Obtener token de un nuevo usuario
def get_new_user_token():
    response = sender_stand_request.post_new_user(data.user_body.copy())
    return response.json()["authToken"]

# Generar cuerpo del kit con nombre personalizado
def get_kit_body(name):
    kit_body = data.kit_body.copy()
    kit_body["name"] = name
    return kit_body

# Afirmación positiva (espera código 201 y validación de nombre)
def positive_assert(kit_body):
    auth_token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

# Afirmación negativa (espera código 400)
def negative_assert_code_400(kit_body):
    auth_token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, auth_token)

    assert response.status_code == 400

# Test 1: Nombre con 1 carácter
def test_kit_name_min_length():
    kit_body = get_kit_body("a")
    positive_assert(kit_body)

# Test 2: Nombre con 511 caracteres
def test_kit_name_511_characters():
    kit_body = {
        "name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC"
    }
    positive_assert(kit_body)

# Test 3: Nombre vacío
def test_kit_name_zero_length():
    kit_body = get_kit_body("")
    negative_assert_code_400(kit_body)

# Test 4: Nombre con más de 512 caracteres
def test_kit_name_512_characters():
    kit_body = {
        "name": "AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD"
    }
    negative_assert_code_400(kit_body)

# Test 5: Nombre con caracteres especiales
def test_kit_name_with_special_characters():
    kit_body = get_kit_body("№%@")
    positive_assert(kit_body)

# Test 6: Nombre con espacios
def test_kit_name_with_spaces():
    kit_body = get_kit_body(" A Aaa ")
    positive_assert(kit_body)

# Test 7: Nombre con números
def test_kit_name_with_numbers():
    kit_body = get_kit_body("123")
    positive_assert(kit_body)

# Test 8: Falta el parámetro name
def test_kit_name_missing():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert_code_400(kit_body)

# Test 9: Tipo incorrecto - número en lugar de string
def test_kit_name_number_type():
    kit_body = get_kit_body(123)
    negative_assert_code_400(kit_body)