
import asyncio
import websockets
import aioconsole
import json
import os
import time


# global aa
aa=0



connected = set()


def handle(websocket, path):
    connected.add(websocket)
    print('서버구동중')


def hi(매개변수):
    print(매개변수)
    # aioconsole.aprint(매개변수)



async def hi2():
    global aa
    await asyncio.sleep(1)
    # asyncio.sleep(1.0)
    print(aa)
    aa=aa+1
    return aa
    # aioconsole.aprint('hi2')


while False:

    hi('hihi')
    hi2()



매개변수 ='매개변수내용'

hi(매개변수)

# .run_utill_complete(hi2())

# loop = asyncio.get_event_loop()
# loop.run_until_complete(hi2())
# loop.run_forever()
#


#
# loop =aasyncio.get_event_loop()
# loop.run_utill_complete(hi2())
# loop.close
#
print("서버 구동 시작")
# start_server = websockets.serve(handle, 'localhost', 8060)

# asyncio.get_event_loop().run_until_complete(start_server)
# asyncio.get_event_loop().run_forever()







async def good_night():
    await asyncio.sleep(1)
    print('잘자요')


async def main():
    await asyncio.gather(
        good_night(),
        good_night()

    )


async def hi3():
    await asyncio.gather(
        hi2(),
        hi2(),
        hi2()
    )


print(f"start : {time.strftime('%X')}")
asyncio.run(main())
print(f"end : {time.strftime('%X')}")

# for a in range(0,15):
#
#     asyncio.run(hi2())
#     print('ll')

print('hi')
asyncio.run(hi3())




asyncio.get_event_loop()
asyncio.get_event_loop().close()
# asyncio.get_event_loop().run_forever()











