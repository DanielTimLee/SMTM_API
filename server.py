from app import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001, debug=True, use_debugger=True, threaded=True)
