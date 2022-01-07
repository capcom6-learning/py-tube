from core import app, Configuration
from core.rabbit import RabbitClient
from threading import Thread

def main():
    rabbit = RabbitClient(Configuration.RABBIT)

    Thread(target=rabbit.start_consuming).start()
    
    app.run(host='0.0.0.0', port=Configuration.PORT, threaded=True)

    rabbit.stop_consuming()
    rabbit.close()


if __name__ == '__main__':
    main()
