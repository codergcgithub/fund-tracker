
# Fund Portfolio Tracker

## How to test locally
Install uv locally if not installed as it is faster
preferably using the install script 

`curl -LsSf https://astral.sh/uv/install.sh | sh` 

Alternatively using =>
`pip install uv`

Build =>
`make install`

Activate the virtual environment 

`cd <Project folder>` 

`source .venv/bin/activate`

Copy the example env file as .env and change settings as needed

`cp .env.example .env`

Run the local server interactively

`uvicorn app.main:app --reload`

open the swagger UI at http://127.0.0.1:8000/docs



## Functional Requirements
Create a simple fund portfolio to track investments and calculate fund performance.

## User Operations

### 1. Create Fund
- **Fund Name**
- **Initial Cash Balance**

### 2. Add Assets to the Fund
- **Symbol**
- **Purchase price per unit**
- **Number of units**
- **Purchase Date**

### 3. Fetch a List of All Funds Managed
- Returns a list of all Funds entered by the user with their **name** and **total net asset value**  
  _(Sum of Cash Balance and total market value of each position)_

### 4. Fetch Fund Details for a Specific Fund
- **Current holdings** (Asset information from what the user entered above) and their **current market value**, **Percent Change**
- **Total Net Asset Value** of the fund

## Technical Requirements
- Can use **any programming language**, but **C# or Python** is preferred.
- Having a **UI** would be preferred; otherwise, provide examples of how to run these APIs.
- Project must be **uploaded to GitHub** and shared.
- The application **must run**.

## Assumptions & Simplifications
- No need to worry about **Authentication or Authorization**.
- For current market value, you can use a **stubbed-out API** or call one of the **free API tiers**.
