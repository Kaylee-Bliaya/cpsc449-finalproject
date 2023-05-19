# CPSC 449-02 Final Project: Online Bookstore API

## Team Members:
* Kaylee Bliaya
* ALan Blandon
* Andrew Lau


## Running the API:
### 1. Open a Command Prompt Terminal and run the following command to start MongoDB:
"C:\Program Files\MongoDB\Server\6.0\bin\mongod.exe" --dbpath="c:\data\db"

### 2. Open another Command Prompt Terminal and run the following command to connect to MongoDB:
mongosh.exe

### 3. Open another Command Prompt Terminal and run the following command to run the API:
uvicorn main:app --reload

### 4. Copy the link given when running uvicorn main:app --reload and paste it in your browser.

### 5. Add */docs* to the link to get to the endpoints.