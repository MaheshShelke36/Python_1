# demo-1 of Asynchormous

import asyncio

async def greet():
    print("Hello")
    await asyncio.sleep(4)
    print("Welcome to Asyncio")

asyncio.run(greet())  

#demo 2 of Asynchorous

import asyncio

async def fun():
      print("This is ")
      await asyncio.sleep(3)
      print("Mahesh")

asyncio.run(fun())

#using gather asynchronous

import asyncio

async def square(n):
      await asyncio.sleep(2)
      return n*n

async def main():
      result=await asyncio.gather(
            square(2),
            square(3),
            square(4)
      )
      print(result)
asyncio.run(main())   

#simple program of Synchronous

import time

def task(name):
    print(f"{name} started")
    time.sleep(3)
    print(f"{name} completed")

task("task1")
task("task2")    
task("task3")
