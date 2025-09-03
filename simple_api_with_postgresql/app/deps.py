from .db import pool  


async def get_db():
	print(pool)
	# if pool is None:
	# 	raise RuntimeError("Database pool is not initialized!")
	# async with pool.connection() as conn:
	# 	yield conn