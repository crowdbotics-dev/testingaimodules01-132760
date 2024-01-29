## Django Fleet Management Backend configuration and information

## Module description

This module implements the backend functionality for a fleet management system, including models for user and equipment and API endpoints for user authentication and equipment data retrieval.

### Features

- User authentication
- Equipment data model
- Equipment data retrieval API endpoint

## Dependencies

No new 3rd party dependencies / pip packages are used.

## API details

- `/authenticate/` (POST): Authenticate user credentials
- `/equipment/` (GET): Retrieve real-time equipment data

## Installation and configuration

To use this module, include it in your Django project by adding 'fleet_management_backend' to your `INSTALLED_APPS` setting:

```python
INSTALLED_APPS = [
    ...
    'fleet_management_backend',
]
```

Then, ensure the module's URL patterns are included in your project's `urls.py`.

## Environment variables

No environment variables are specifically required for this module.
