import redis
import random
import string

# Redis connection URL
redis_url = "redis://default:z3KzwXWhAsKqQWwiK6BZTBRPAxCMKRz61brbrEwsFmjmqZDO1XoMAUNB9BcJaTUm@15.204.46.122:6969/0"

def random_string(length=10):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for i in range(length))

def set_and_get_keys():
    try:
        # Connect to Redis
        client = redis.StrictRedis.from_url(redis_url)

        # Set a thousand key-value pairs
        for i in range(1000):
            key = f"test_key_{i}"
            value = random_string()
            client.set(key, value)

        print("Successfully set 1000 key-value pairs in Redis.")

        # Retrieve the key-value pairs
        key_value_pairs = {}
        for i in range(1000):
            key = f"test_key_{i}"
            value = client.get(key).decode('utf-8')
            key_value_pairs[key] = value

        return key_value_pairs

    except Exception as e:
        print(f"Error connecting to Redis: {e}")
        return None

# Call the function and store the result
result = set_and_get_keys()
if result:
    print(result)