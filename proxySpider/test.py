from Redisclient import Redis
import dis



# redis = Redis()
#
# t = redis.lrange('proxies')
# print(len(t))

# import asyncio
# import requests
# async def get(url):
#
#     r = requests.get(url)
#     # print(r.text)
#     return r.status_code
#
# # 1 直接尝试
# coroutine = get('http://www.baidu.com')
# print('coroutine', coroutine)
# print('After calling get')
# loop = asyncio.get_event_loop()
# loop.run_until_complete(coroutine)
# print('after calling loop')
#
#
#
#
# # 2 显示定义task
# coroutine = get('http://www.baidu.com')
# print('coroutine', coroutine)
# print('After calling get')
# loop = asyncio.get_event_loop()
# task = loop.create_task(coroutine)
# print('task', task)
# loop.run_until_complete(task)
# print('task', task)
# print('after calling loop')
#
#
# # 3 使用 ensure_future() 来定义task
# coroutine = get('http://www.baidu.com')
# print('coroutine', coroutine)
# print('After calling get')
# task = asyncio.ensure_future(coroutine)
# print('task', task)
# loop = asyncio.get_event_loop()
# loop.run_until_complete(task)
# print('task', task)
# print('after calling loop')
#
#
#
# # 4 绑定回调函数
# def callback(task):
#     print('status', task.result())
#
# coroutine = get('http://www.baidu.com')
# print('coroutine', coroutine)
# print('After calling get')
# task = asyncio.ensure_future(coroutine)
# task.add_done_callback(callback)
# print('task', task)
# loop = asyncio.get_event_loop()
# loop.run_until_complete(task)
# print('task', task)
# print('after calling loop')
#
#
# # 5 也可以在task 完成之后 直接调用task.result() 获取task的结果回调
# coroutine = get('http://www.baidu.com')
# print('coroutine', coroutine)
# print('After calling get')
# task = asyncio.ensure_future(coroutine)
# print('task', task)
# loop = asyncio.get_event_loop()
# loop.run_until_complete(task)
# print('task', task)
# print('status', task.result())
# print('after calling loop')
#
#
#
#
# # 6 多任务 先将将任务组成tasks列表，然后用到asyncio的wait()方法来将任务注册到时间循环当中
# print('After calling get')
# tasks = [asyncio.ensure_future(get('http://www.baidu.com')) for i in range(5)]
# print('tasks', tasks)
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))
# for task in tasks:
#     print('status', task.result())
# print('after calling loop')
#
#
#
#
# # 7 要实现异步http请求，需要用到aiohttp
# import aiohttp
# import time
#
# start = time.time()
#
#
# async def getpage(url):
#     async with aiohttp.ClientSession() as session:
#         async with session.get(url) as response:
#             result = await response.text()
#     return result
#
#
# async def rq():
#     url = 'http://httpbin.org/get'
#     print('Waiting for', url)
#     result = await getpage(url)
#     print('Get response from', url, 'Result', result)
#
#
# tasks = [asyncio.ensure_future(rq()) for i in range(3)]
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.wait(tasks))
#
# end = time.time()
#
# print('Cost time:', end - start)


#
# def test():
#     a = 1.231
#     b = int(a)
#     return a + b



# dis.dis(test)

# import json
# import requests
# from Redisclient import Redis
#
#
# myredis = Redis()
#
# proxy = myredis.rpop('goodproxies')
# proxies = {
#     'https': 'https://' + proxy,
#     'http': 'http://' + proxy
# }
#
# r = requests.get(url='http://httpbin.org/get', proxies=proxies)
#
# print(r.text)
# print(json.loads(r.text)['origin'].split(','))


from pymongo import MongoClient


client = MongoClient(host='127.0.0.1', port=27017)
db = client['thisdb']
clc = db['thisclc']

# clc.insert({'name':'123'})
data = clc.find_one({'name': '123'})
# data = clc.update_one({'name': '123'}, {'$set': {'play_list': { 'a' :'3', 'b': '2', 'c': '3'}, 'age': 32}})
print(data)
