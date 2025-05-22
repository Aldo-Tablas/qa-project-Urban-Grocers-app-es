import sender_stand_request
import data

# Crear un kit body dinámicamente con nombre
def get_kit_body(name):
    return {"name": name}

# Obtener authToken creando un nuevo usuario
def get_new_user_token():
    response = sender_stand_request.post_new_user(data.user_body)
    return response.json()["authToken"]

# Prueba positiva
def positive_assert(kit_body):
    token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, token)

    assert response.status_code == 201
    assert response.json()["name"] == kit_body["name"]

# Prueba negativa para código 400
def negative_assert_code_400(kit_body):
    token = get_new_user_token()
    response = sender_stand_request.post_new_client_kit(kit_body, token)

    assert response.status_code == 400
    assert response.json()["code"] == 400

# Prueba 1: 1 carácter permitido
def test_kit_name_one_letter():
    positive_assert(get_kit_body(data.one_letter_name))

# Prueba 2: 511 caracteres
def test_kit_name_511_characters():
    positive_assert(get_kit_body(data.characters_511_name))

# Prueba 3: 0 caracteres
def test_kit_name_empty_string():
    negative_assert_code_400(get_kit_body(data.empty_name))

# Prueba 4: 512 caracteres
def test_kit_name_512_characters():
    negative_assert_code_400(get_kit_body(data.characters_512_name))

# Prueba 5: Caracteres especiales permitidos
def test_kit_name_special_chars():
    positive_assert(get_kit_body(data.special_char_name))

# Prueba 6: Espacios permitidos
def test_kit_name_spaces():
    positive_assert(get_kit_body(data.name_with_spaces))

# Prueba 7: Números permitidos
def test_kit_name_numbers():
    positive_assert(get_kit_body(data.numeric_name))

# Prueba 8: No se pasa "name"
def test_kit_name_missing_param():
    negative_assert_code_400(data.kit_body_without_name)

# Prueba 9: Tipo incorrecto (número en vez de string)
def test_kit_name_invalid_type():
    negative_assert_code_400(get_kit_body(data.numeric_type_name))