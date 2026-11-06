from flask import Flask, jsonify, render_template_string, request

app = Flask(__name__)

# Nöron için özel koyu tema sohbet arayüzü
HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="tr">
<head>
    <meta charset="UTF-8">
    <title>Nöron AI Asistanı</title>
    <style>
        body { background-color: #0f172a; color: #f8fafc; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; display: flex; flex-direction: column; align-items: center; justify-content: center; height: 100vh; margin: 0; }
        .chat-container { width: 100%; max-width: 600px; background: #1e293b; border-radius: 12px; box-shadow: 0 4px 20px rgba(0,0,0,0.5); display: flex; flex-direction: column; height: 80vh; overflow: hidden; border: 1px solid #334155; }
        .chat-header { background: #0f172a; padding: 20px; text-align: center; border-bottom: 1px solid #334155; font-size: 1.2rem; font-weight: bold; color: #38bdf8; }
        .chat-messages { flex: 1; padding: 20px; overflow-y: auto; display: flex; flex-direction: column; gap: 15px; }
        .message { padding: 12px 16px; border-radius: 8px; max-width: 80%; line-height: 1.4; }
        .user { background: #2563eb; color: white; align-self: flex-end; }
        .bot { background: #334155; color: #f1f5f9; align-self: flex-start; }
        .chat-input { display: flex; padding: 15px; background: #0f172a; border-top: 1px solid #334155; gap: 10px; }
        input { flex: 1; padding: 12px; border-radius: 6px; border: 1px solid #475569; background: #1e293b; color: white; outline: none; }
        button { background: #38bdf8; color: #0f172a; border: none; padding: 0 20px; border-radius: 6px; font-weight: bold; cursor: pointer; }
        button:hover { background: #0ea5e9; }
    </style>
</head>
<body>
    <div class="chat-container">
        <div class="chat-header">🧠 Nöron - 7/24 Aktif Yapay Zeka Asistanı</div>
        <div class="chat-messages" id="chatMessages">
            <div class="message bot">Merhaba! Ben Nöron. Sana nasıl yardımcı olabilirim?</div>
        </div>
        <div class="chat-input">
            <input type="text" id="userInput" placeholder="Nöron'a bir şeyler yaz..." onkeypress="handleKeyPress(event)">
            <button onclick="sendMessage()">Gönder</button>
        </div>
    </div>

    <script>
        async function sendMessage() {
            const input = document.getElementById('userInput');
            const messages = document.getElementById('chatMessages');
            const text = input.value.trim();
            if (!text) return;

            messages.innerHTML += `<div class="message user">${text}</div>`;
            input.value = '';
            messages.scrollTop = messages.scrollHeight;

            const response = await fetch('/chat', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ message: text })
            });
            const data = await response.json();

            messages.innerHTML += `<div class="message bot">${data.reply}</div>`;
            messages.scrollTop = messages.scrollHeight;
        }

        function handleKeyPress(e) {
            if (e.key === 'Enter') sendMessage();
        }
    </script>
</body>
</html>
"""


@app.route("/")
def home():
  return render_template_string(HTML_TEMPLATE)


@app.route("/chat", methods=["POST"])
def chat():
  data = request.get_json()
  user_msg = data.get("message", "").lower()

  # Nöron'un akıllı yanıt mantığı
  if "merhaba" in user_msg or "selam" in user_msg:
    reply = "Selam! Nöron aktif ve komutlarını bekliyor."
  elif "nasılsın" in user_msg:
    reply = "Harikayım! Render bulut sunucusunda 7/24 kesintisiz çalışıyorum."
  elif "sen kimsin" in user_msg:
    reply = (
        "Ben Nöron, senin bulut tabanlı kişisel yapay zeka asistanınım."
    )
  else:
    reply = f"Şunu söyledin: '{user_msg}'. Bu komutu öğrenmek için sabırsızlanıyorum!"

  return jsonify({"reply": reply})


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=10000)
