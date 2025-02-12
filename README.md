# Ledger Service API

## Overview

The Ledger Service API provides endpoints to manage user credits through a shared ledger system.

## Endpoints

### GET /ledger/{owner_id}

Fetches the current balance of a user.

**Response:**
```json
{
  "owner_id": "owner1",
  "balance": 10
}