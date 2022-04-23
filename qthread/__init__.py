
import threading
import queue
import logging
import time

#logging.basicConfig(format="%(asctime)s [%(levelname)s] %(threadName)s: %(message)s", level=logging.INFO)

class QThread(threading.Thread):
    def __init__(self):
        logging.debug("Starting up")
        super().__init__()
        self._q = queue.Queue()
        self._shutdown = False
        self.timeout = 3
        self.alive = lambda: not self.shutdown

    @property
    def q(self):
        return self._q

    @q.setter
    def q(self, q):
        self._q = q

    @property
    def shutdown(self):
        return self._shutdown

    def wait(self):
        while self.alive():
            time.sleep(1)

    @shutdown.setter
    def shutdown(self, shutdown):
        self._shutdown = shutdown

    def put(self, obj):
        return self.q.put(obj)

    def stop(self):
        self.shutdown = True
        self.join()

    def run(self):
        logging.info("Running")
        while self.alive():
            try:
                obj = self.q.get(timeout=self.timeout)
            except:
                obj = None
            if obj:
                logging.debug("Found obj")
                self.process(obj)
            else:
                logging.debug("No obj found")
        logging.info("Shutting Down.")

    def process(self, obj):
        logging.info(obj)
