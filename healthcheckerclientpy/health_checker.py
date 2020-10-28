import time
import logging
import sys
import grpc
from health_pb2_grpc import HealthStub
from health_pb2 import HealthCheckRequest


log = logging.getLogger(__name__)


def main(address: str):
    log.info("Starting health check pinger with frequency of once per 5 seconds...")

    while True:
        start_time = time.perf_counter()
        log.info("Establishing channel to %s...", address)
        with grpc.insecure_channel(address) as channel:
            log.info("Channel establishment took %f seconds", time.perf_counter() - start_time)
            client = HealthStub(channel)
            request = HealthCheckRequest()
            invoke_time = time.perf_counter()
            log.info("Invoking health check point on %s...", address)
            response = client.Check(request)
            log.info("Invocation took %f seconds", time.perf_counter() - invoke_time)
            log.info("Response from %s is %s", address, response)
        log.info("Whole operation took %f seconds", time.perf_counter() - start_time)
        log.info("=== waiting for 5 seconds... ===")

        time.sleep(5.0)



if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    main(address=sys.argv[1])
