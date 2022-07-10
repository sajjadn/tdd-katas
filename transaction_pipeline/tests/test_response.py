
from src import transaction_pipeline


def test_transaction_pipeline_should_0_after_successfully_completing() -> None:
    response_code = transaction_pipeline.run()
    assert response_code == 0
