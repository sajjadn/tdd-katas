from unittest import mock

from src import transaction_pipeline
from src.store_revenue import StoreRevenue


@mock.patch("src.reporting_db.save_records")
@mock.patch("src.transaction_api_client.fetch_transactions")
def test_should_save_store_revenue_for_single_transaction(mock_api_client,
	mock_db_gateway) -> None:

	expected_store_id = 1
	mock_api_client.return_value = {
		"transactions": [
			{
				"storeId": expected_store_id
			}
		]
	}

	transaction_pipeline.run()

	mock_db_gateway.assert_called_once()
	actual_args = mock_db_gateway.call_args[0][0]

	assert isinstance(actual_args[0], StoreRevenue)
	assert actual_args[0].store_id == expected_store_id


@mock.patch("src.reporting_db.save_records")
@mock.patch("src.transaction_api_client.fetch_transactions")
def test_should_save_store_revenue_for_two_different_stores(mock_api_client,
	mock_db_gateway) -> None:
	mock_api_client.return_value = {
		"transactions": [
			{
				"storeId": 2
			},
			{
				"storeId": 3
			}
		]
	}

	transaction_pipeline.run()

	mock_db_gateway.assert_called_once()
	actual_args = mock_db_gateway.call_args[0][0]
	assert actual_args[0].store_id == 2
	assert actual_args[1].store_id == 3

