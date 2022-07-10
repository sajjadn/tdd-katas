from src import reporting_db, transaction_api_client
from src.store_revenue import StoreRevenue


def run() -> int:
    transactions: list = transaction_api_client.fetch_transactions()["transactions"]
    store_revenues = []
    for transaction in transactions:
        store_revenues.append(StoreRevenue(transaction["storeId"]))
    reporting_db.save_records(store_revenues)
    return 0
