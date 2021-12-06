from core import app, Configuration

def main():
    app.run(host='0.0.0.0', port=Configuration.PORT, threaded=True)

if __name__ == '__main__':
    main()
