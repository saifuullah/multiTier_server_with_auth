This is multi tier servers architicture code

It has 4 parts

1--The main server
2--Three service providers servers
3--Authenticator server
4--Client


Client first communicate with mainServer and validate itself. Main server pass user creditional
to the Authenticator and if the user is valid it returns 2 things. 

1- Client demanded service provider server PORT
2- Token

Client then use this Token and PORT number to communicate with its required service providers
server.

service provider server then check weather the Token is valid or not (It communicate with main server)
