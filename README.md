# CPSC 449-02 Final Project: Online Bookstore API 📚

## Team Members:
* Kaylee Bliaya
* Alan Blandon
* Andrew Lau

## Running the API:
1. Open a Command Prompt Terminal and run the following command to start MongoDB:
`"C:\Program Files\MongoDB\Server\6.0\bin\mongod.exe" --dbpath="c:\data\db"`
2. Open another Command Prompt Terminal and run the following command to connect to MongoDB:
`mongosh.exe`
3. Open another Command Prompt Terminal and run the following command to run the API:
`uvicorn main:app --reload`
4. Copy the link given when running uvicorn main:app --reload and paste it in your browser.
5. Add /docs to the link to get to the endpoints.

### Project Overview:
```
├── app
│   ├── .gitignore
│   ├── README.md
│   ├── books.csv
|   ├── database.py (MongoDB Connection and Indexing)
|   ├── main.py (Aggregation)
|   ├── models.py (Book Model and Data Validation)
│   └── routes
│       ├── purchase_route.py
│       ├── routes.py (API Endpoints)
│       ├── search_author_route.py (Operators)
│       ├── search_price_route.py (Operators)
│       └── search_title_route.py (Operators)
└── requirements.txt
```
