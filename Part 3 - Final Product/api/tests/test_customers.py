from fastapi.testclient import TestClient
from ..controllers import customers as controller
from ..main import app
import pytest
from ..models import customers as model

# Create a test client for the app
client = TestClient(app)


@pytest.fixture
def db_session(mocker):
    return mocker.Mock()


def test_create_customer(db_session):
    # Create a sample customer
    customer_data = {
        "customer_name": "John Doe",
        "customer_email": "JDoe@gmail.com",
        "customer_phone_number": "123-456-7890",
        "customer_address": "4335 Main Street",
        "customer_rating": 5,
        "customer_review": "Pretty Good"
    }

    customer_object = model.Customer(**customer_data)

    # Call the create function
    created_customer = controller.create(db_session, customer_object)

    # Assertions
    assert created_customer is not None
    assert created_customer.customer_name == "John Doe"
    assert created_customer.customer_email == "JDoe@gmail.com"
    assert created_customer.customer_phone_number == "123-456-7890"
    assert created_customer.customer_address == "4335 Main Street"
    assert created_customer.customer_rating == 5
    assert created_customer.customer_review == "Pretty Good"
