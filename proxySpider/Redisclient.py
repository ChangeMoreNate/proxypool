from redis import StrictRedis
from config.conf import REDIS_HOST, REDIS_PORT, REDIS_PASSWORD


class Redis(object):

    def __init__(self):
        if REDIS_PASSWORD:
            self.__db = StrictRedis(host=REDIS_HOST, port=REDIS_PORT, password=REDIS_PASSWORD)
        else:
            self.__db = StrictRedis(host=REDIS_HOST, port=REDIS_PORT, db=3)

    def lpush(self, Listname, item):
        self.__db.lpush(Listname, item)

    def rpush(self, Listname, item):
        self.__db.rpush(Listname, item)

    def rpop(self, Listname):
        try:
            return self.__db.rpop(Listname).decode('utf-8')
        except:
            return 0

    def lpop(self, Listname):
        try:
            return self.__db.lpop(Listname).decode('utf-8')
        except:
            return 0

    def lrange(self, Listname, p1=0, p2=-1):
        return self.__db.lrange(Listname, p1, p2)

    def lrem(self, Listname, len, item):
        self.lrem(Listname, len, item)


    def sadd(self, Setname, item):
        self.__db.sadd(Setname, item)

    def smember(self, Setname):
        return self.__db.smembers(Setname)

    def srem(self, Setname, item):
        self.__db.srem(Setname, item)


if __name__ == '__main__':
    redis = Redis()
    print(redis.lrange('no_start_match_info', 0, -1))
