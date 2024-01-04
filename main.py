import uvicorn
from fastapi import FastAPI
import logging
import sys

from models.transactions import Transaction
from hendlers import handle_raw_message


logging.basicConfig(level=logging.INFO, stream=sys.stdout)
logger = logging.getLogger(__name__)

app = FastAPI()


@app.post('/api/v1/budget/raw/', status_code=201)
async def create_budget_transaction(transaction: Transaction):
    logger.info(f'Received text message: {transaction.text}, '
                f'from {transaction.user}')
    handle_raw_message(transaction.text, transaction.user)
    return transaction


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
