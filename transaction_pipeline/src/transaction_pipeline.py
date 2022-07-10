from src import reporting_db
from src.store_revenue import StoreRevenue


def run() -> int:
    reporting_db.save_records(StoreRevenue())
    return 0
