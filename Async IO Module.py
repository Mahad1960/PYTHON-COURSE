import asyncio
async def task(name,sec):
   print(f"Let's Start {name}!")
   await asyncio.sleep(sec)
   print(f"Let's Finish {name}!")
async def main():
   await asyncio.gather(
      task("Mahad",2),
      task("Mahad",3)
   )
asyncio.run(main())
# OUTPUT:
# main() is called with "asyncio.run(main())".
# Inside main, task("Mahad",2) and task("Mahad",3) are both started immediately because of "gather".
# Now "Let's Finish!" will print after 2 secs and again "Let's Finish!" will print after 1 more sec.