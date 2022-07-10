from src import reporting_db, transaction_api_client
from src.store_revenue import StoreRevenue


def run() -> int:
    transaction_response: list = transaction_api_client.fetch_transactions()
    if transaction_response and "transactions" in transaction_response:
        transactions = transaction_response["transactions"]
        store_revenues = []
        for transaction in transactions:
            store_revenues.append(StoreRevenue(transaction["storeId"]))
        reporting_db.save_records(store_revenues)
    return 0
