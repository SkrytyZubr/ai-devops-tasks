  +--------+         +-------------+         +--------+
  |        |  HTTP   |             |  SQL    |        |
  | Client | ------> | App Server  | ------> | Database|
  |        |  REST   |             |  Query  |        |
  +--------+         +-------------+         +--------+

                    HTTP/REST                       SQL Queries
  +--------+     ----------->     +-------------+     ----------->     +--------+
  |        |    Request/Response  |             |    CRUD Operations   |        |
  | Client |                      | App Server  |                      | Database|
  | Browser|     <-----------     | Node.js/API |     <-----------     | MySQL  |
  | Mobile |     JSON Data        |             |     Result Sets      | MongoDB|
  +--------+                      +-------------+                      +--------+
              Authentication         Business Logic           Data Persistence
              User Interface         Data Processing          Transactions