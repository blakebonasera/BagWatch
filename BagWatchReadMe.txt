Hey, hope you are doing alright my name is Blake Bonasera this is a passion project of mine Utilizing the jup.ag API to get Solana SPL token prices from the API so you can save them and get a rough estimate on what your P&L could be or would have been if you had invested in a coin at that time!

-ToDo

-set up MySQL 
-Figure out JUP API -Get request to pull and store all SPL on the Token List API at load of app to use the mintSymbol to find the correct mintSymbol for the Price API. 
-Create DB tables and SP for User, Token, FavToken, Wallet potentially if I can connect RUST to django easily but will need to be done on my laptop with rust set up.
-Create Models , Views and Controllers
-Create Templates with bootstrap 5
-Create Login/Registration page



tables

User: User_ID int PK, Username Varchar(25),Email varchar(25), Password varchar(25)
Token: id varchar(max) pk, mintSymbol varchar(10), vsToken varchar(max), price decimal
Watchlist: Watchlist_ID int PK, Username User_ID FK, id, mintSymbol, price Token_ID FK