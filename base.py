from fastapi import FastAPI

DATABASE = 'sqlite:///cars.db'

app = FastAPI(title="REST API using electric cars")