import sys
import json
import redis


if __name__ == '__main__':
    redis_client = redis.Redis(host='localhost', port=6379)
    message = json.dumps({'hyperparameter': sys.argv[1]})
    redis_client.publish(channel='hyperparameter', message=message)
