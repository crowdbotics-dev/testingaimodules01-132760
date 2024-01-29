## Django PayPal API Integration Module configuration and information

## Module description

This module provides a proxy to interact with PayPal's API, enabling easy integration within Django projects. It simplifies the process of making PayPal API requests, handling payments, and processing responses.

## Features

- [ ] This module includes migrations.
- [x] This module requires manual configurations.
- [x] This module includes environment variables.
- [ ] This module can be configured with module options.

## Environment variables

```dotenv
PAYPAL_CLIENT_ID="Your PayPal Client ID"
PAYPAL_CLIENT_SECRET="Your PayPal Client Secret"
PAYPAL_MODE="sandbox" # or 'live' for production
```

## 3rd party setup

To use PayPal API, you need to setup a PayPal developer account and create an app to obtain the Client ID and Client Secret. Use these credentials in the environment variables.

## Dependencies

Ensure the `paypalrestsdk` package is installed: `pip install paypalrestsdk`.

## API details

Implemented PayPal API proxy functionalities include:
- Processing payments
- Managing invoices
- Viewing transaction details

Further API endpoint implementations can easily be added to the module as needed.