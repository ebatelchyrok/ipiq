from flask import Flask, request, jsonify, redirect

app = Flask(__name__)

@app.route('/')
def index():
    # Получение IP-адреса клиента
    client_ip = request.remote_addr

    # Получение User-Agent
    user_agent = request.headers.get('User-Agent')

    # Получение всех заголовков запроса
    headers = dict(request.headers)

    # Получение метода запроса
    request_method = request.method

    # Получение URL запроса
    request_url = request.url

    # Получение всех параметров запроса (query string)
    query_params = request.args

    # Получение данных, отправленных с POST запросом (если есть)
    post_data = request.form if request.method == 'POST' else None

    # Собираем всю информацию в словарь
    request_info = {
        "client_ip": client_ip,
        "user_agent": user_agent,
        "headers": headers,
        "request_method": request_method,
        "request_url": request_url,
        "query_params": query_params,
        "post_data": post_data
    }

    # Выводим информацию в консоль
    print("Request Information:")
    print(jsonify(request_info).get_data(as_text=True))

    # Перенаправляем пользователя на другой URL
    return redirect('https://vk.com/1mi_musulmane_s_nami_bog')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)