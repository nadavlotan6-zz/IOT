class setInterval():
    def __init__(self, myMQTTClient, topic, sec):
        def func_wrapper():
            self.t = threading.Timer(sec, func_wrapper)
            self.t.start()
            payload = {}
            myMQTTClient.publish(topic, json.dumps(payload), 1)
        self.t = threading.Timer(sec, func_wrapper)
        self.t.start()

    def cancel(self):
        self.t.cancel()