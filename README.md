# Test Suite

## 🏗 Project Structure

```
.
├── core/                      # Core settings, env vars, constants, and HTTP dispatch
├── request_builders/         # Centralized request builders per API domain
├── helpers/                  # Logic grouped per API entity (auth, orders, esims, packages)
├── tests/                    # Test cases and pytest configuration
├── test_data.py              # Parametrized input data for scenarios
├── Makefile                  # CLI shortcuts for testing, linting, and setup
├── requirements.txt          # Dependencies list
```

## 🧪 Test Architecture

- **Pytest** is used for organizing and running test cases.
- **Modular request builders** (like `OrderController`, `EsimController`) define and dispatch API calls via a clean controller pattern.
- **Helper classes** encapsulate logic to interact with each API domain.
- **Parametrized data** in `test_data.py` drives flexible and scalable test input.
- **Validation helpers** ensure consistent assertions and reusable business logic for test evaluation.
- **Environment variables** are managed via `.env` and loaded automatically.

### Frontend Test Setup

- **Playwright** is used for browser automation and UI validations.
- **Page Object Model (POM)** is implemented using `BasePage` and specialized pages like `HomePage`, `SearchPackagePage`, and `CartPage`.
- **Selectors and interaction methods** are centralized to reduce duplication and improve maintainability.
- **Assertions** are handled using `assert_fields_match` to ensure consistency between UI pages (e.g., search → cart).
- **Logging** is integrated to provide detailed step-by-step execution trace in test output.

To run frontend tests:

```bash
pytest tests/frontend
```

Make sure Playwright browsers are installed:

```bash
playwright install
```


---

## ⚙️ Setup & Installation

1. Clone this repo:
```bash
git clone https://github.com/your-username/airalo-api-tests.git
cd airalo-api-tests
```

2. Install dependencies:
```bash
make install
```

3. Create a `.env` file and configure:
```env
API_VERSION=v2
BASE_URL=https://{URL}
CLIENT_ID=your-client-id
CLIENT_SECRET=your-client-secret
```

---

## ✅ Run Tests

```bash
make test
```
Or
```bash
pytest -v -n "auto"
```
