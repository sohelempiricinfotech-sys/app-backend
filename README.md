# app-backend

Mock production API backend used for OpenAPI contract drift validation.

The repository contains:

- `openapi/openapi.yaml` - public API contract, OpenAPI 3.1.0
- `openapi/admin-swagger.json` - admin API contract, Swagger 2.0
- `src/app/main.py` - representative FastAPI/Pydantic route source
- `api-version.json` and `VERSION` - release metadata

Production API request and response logs for the validation window are stored in the Supabase project named `app-backend`.
