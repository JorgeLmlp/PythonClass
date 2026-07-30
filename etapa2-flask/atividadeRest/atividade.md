PS C:\Users\22400060> Invoke-RestMethod http://127.0.0.1:5000/api/livros



ano          : 1949
autor        : George Orwell
data_criacao : 2026-07-30 08:05:18.096197
id           : 3
titulo       : 1984

ano          : 1899
autor        : Machado de Assis
data_criacao : 2026-07-30 08:05:18.096197
id           : 1
titulo       : Dom Casmurro

ano          : 1890
autor        : Aluísio Azevedo
data_criacao : 2026-07-30 08:05:18.096197
id           : 2
titulo       : O Cortiço




PS C:\Users\22400060> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
  -Method POST `
  -ContentType "application/json" `
  -Body '{"titulo":"NOME DO LIVRO","autor":"NOME DO AUTOR","ano":ANO DA PUBLICAÇÃO}'
Invoke-RestMethod : 
400 Bad Request
Bad Request
Failed to decode JSON object: &#39;utf-8&#39; codec can&#39;t decode byte 0xc7 in position 70: invalid continuation byte
No linha:1 caractere:1
+ Invoke-RestMethod http://127.0.0.1:5000/api/livros `
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidOperation: (System.Net.HttpWebRequest:HttpWebRequest) [Invoke-RestMethod], WebException
    + FullyQualifiedErrorId : WebCmdletWebResponseException,Microsoft.PowerShell.Commands.InvokeRestMethodCommand

PS C:\Users\22400060> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
  -Method POST `
  -ContentType "application/json" `
  -Body '{"titulo":"nsei1","autor":"NOME_DO_AUTOR","ano":ANO_DA_PUBLICAÇÃO}'
Invoke-RestMethod : 
400 Bad Request
Bad Request
Failed to decode JSON object: &#39;utf-8&#39; codec can&#39;t decode byte 0xc7 in position 62: invalid continuation byte
No linha:1 caractere:1
+ Invoke-RestMethod http://127.0.0.1:5000/api/livros `
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidOperation: (System.Net.HttpWebRequest:HttpWebRequest) [Invoke-RestMethod], WebException
    + FullyQualifiedErrorId : WebCmdletWebResponseException,Microsoft.PowerShell.Commands.InvokeRestMethodCommand

PS C:\Users\22400060> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
  -Method POST `
  -ContentType "application/json" `
  -Body '{"titulo":"mito_de_sisifo","autor":"camus","ano":2026}'


ano          : 2026
autor        : camus
data_criacao : 2026-07-30 08:08:29.819806
id           : 4
titulo       : mito_de_sisifo




PS C:\Users\22400060> Invoke-RestMethod http://127.0.0.1:5000/api/livros



ano          : 1949
autor        : George Orwell
data_criacao : 2026-07-30 08:05:18.096197
id           : 3
titulo       : 1984

ano          : 1899
autor        : Machado de Assis
data_criacao : 2026-07-30 08:05:18.096197
id           : 1
titulo       : Dom Casmurro

ano          : 1890
autor        : Aluísio Azevedo
data_criacao : 2026-07-30 08:05:18.096197
id           : 2
titulo       : O Cortiço

ano          : 2026
autor        : camus
data_criacao : 2026-07-30 08:08:29.819806
id           : 4
titulo       : mito_de_sisifo




PS C:\Users\22400060> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
  -Method POST `
  -ContentType "application/json" `
  -Body '{"titulo":"O Pequeno Principe","autor":"Antoine de Saint-Exupery","ano":1943}'



ano          : 1943
autor        : Antoine de Saint-Exupery
data_criacao : 2026-07-30 08:10:00.617306
id           : 5
titulo       : O Pequeno Principe




PS C:\Users\22400060> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
  -Method POST `
  -ContentType "application/json" `
  -Body '{"titulo":"A Revolucao dos Bichos","autor":"George Orwell","ano":1945}'


ano          : 1945
autor        : George Orwell
data_criacao : 2026-07-30 08:10:08.954268
id           : 6
titulo       : A Revolucao dos Bichos




PS C:\Users\22400060> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
  -Method POST `
  -ContentType "application/json" `
  -Body '{"titulo":"O Senhor dos Aneis","autor":"J. R. R. Tolkien","ano":1954}'


ano          : 1954
autor        : J. R. R. Tolkien
data_criacao : 2026-07-30 08:10:14.022595
id           : 7
titulo       : O Senhor dos Aneis




PS C:\Users\22400060> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
  -Method POST `
  -ContentType "application/json" `
  -Body '{"titulo":"Harry Potter e a Pedra Filosofal","autor":"J. K. Rowling","ano":1997}'


ano          : 1997
autor        : J. K. Rowling
data_criacao : 2026-07-30 08:10:18.382379
id           : 8
titulo       : Harry Potter e a Pedra Filosofal




PS C:\Users\22400060> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
  -Method POST `
  -ContentType "application/json" `
  -Body '{"titulo":"Crime e Castigo","autor":"Fiodor Dostoievski","ano":1866}'


ano          : 1866
autor        : Fiodor Dostoievski
data_criacao : 2026-07-30 08:10:24.163707
id           : 9
titulo       : Crime e Castigo




PS C:\Users\22400060> Invoke-RestMethod http://127.0.0.1:5000/api/livros



ano          : 1949
autor        : George Orwell
data_criacao : 2026-07-30 08:05:18.096197
id           : 3
titulo       : 1984

ano          : 1945
autor        : George Orwell
data_criacao : 2026-07-30 08:10:08.954268
id           : 6
titulo       : A Revolucao dos Bichos

ano          : 1866
autor        : Fiodor Dostoievski
data_criacao : 2026-07-30 08:10:24.163707
id           : 9
titulo       : Crime e Castigo

ano          : 1899
autor        : Machado de Assis
data_criacao : 2026-07-30 08:05:18.096197
id           : 1
titulo       : Dom Casmurro

ano          : 1997
autor        : J. K. Rowling
data_criacao : 2026-07-30 08:10:18.382379
id           : 8
titulo       : Harry Potter e a Pedra Filosofal

ano          : 1890
autor        : Aluísio Azevedo
data_criacao : 2026-07-30 08:05:18.096197
id           : 2
titulo       : O Cortiço

ano          : 1943
autor        : Antoine de Saint-Exupery
data_criacao : 2026-07-30 08:10:00.617306
id           : 5
titulo       : O Pequeno Principe

ano          : 1954
autor        : J. R. R. Tolkien
data_criacao : 2026-07-30 08:10:14.022595
id           : 7
titulo       : O Senhor dos Aneis

ano          : 2026
autor        : camus
data_criacao : 2026-07-30 08:08:29.819806
id           : 4
titulo       : mito_de_sisifo




PS C:\Users\22400060> Invoke-RestMethod http://127.0.0.1:5000/api/livros `
  -Method POST `
  -ContentType "application/json" `
  -Body '{"titulo":"Cem Anos de Solidao","autor":"Gabriel Garcia Marquez","ano":1967}'


ano          : 1967
autor        : Gabriel Garcia Marquez
data_criacao : 2026-07-30 08:11:04.336312
id           : 10
titulo       : Cem Anos de Solidao




PS C:\Users\22400060> 
PS C:\Users\22400060> Invoke-RestMethod http://127.0.0.1:5000/api/livros/COLOCAR/4 `
  -Method PUT `
  -ContentType "application/json" `
  -Body '{"titulo":"O Senhor dos Anéis","autor":"J. R. R. Tolkien","ano":1954}'
Invoke-RestMethod : 
404 Not Found
Not Found
The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.
No linha:1 caractere:1
+ Invoke-RestMethod http://127.0.0.1:5000/api/livros/COLOCAR/4 `
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidOperation: (System.Net.HttpWebRequest:HttpWebRequest) [Invoke-RestMethod], WebException
    + FullyQualifiedErrorId : WebCmdletWebResponseException,Microsoft.PowerShell.Commands.InvokeRestMethodCommand

PS C:\Users\22400060> Invoke-RestMethod http://127.0.0.1:5000/api/livros/COLOCAR/4 `
  -Method PUT `
  -ContentType "application/json" `
  -Body '{"titulo":"O Senhor dos Anéis","autor":"J. R. R. Tolkien","ano":1954}'
Invoke-RestMethod : 
404 Not Found
Not Found
The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.
No linha:1 caractere:1
+ Invoke-RestMethod http://127.0.0.1:5000/api/livros/COLOCAR/4 `
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidOperation: (System.Net.HttpWebRequest:HttpWebRequest) [Invoke-RestMethod], WebException
    + FullyQualifiedErrorId : WebCmdletWebResponseException,Microsoft.PowerShell.Commands.InvokeRestMethodCommand

PS C:\Users\22400060> Invoke-RestMethod http://127.0.0.1:5000/api/livros/COLOCAR/4 `
  -Method PUT `
  -ContentType "application/json" `
  -Body '{"titulo":"OSenhor dos Anéis","autor":"J. R. R. Tolkien","ano":1954}'
Invoke-RestMethod : 
404 Not Found
Not Found
The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.
No linha:1 caractere:1
+ Invoke-RestMethod http://127.0.0.1:5000/api/livros/COLOCAR/4 `
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidOperation: (System.Net.HttpWebRequest:HttpWebRequest) [Invoke-RestMethod], WebException
    + FullyQualifiedErrorId : WebCmdletWebResponseException,Microsoft.PowerShell.Commands.InvokeRestMethodCommand

PS C:\Users\22400060> Invoke-RestMethod http://127.0.0.1:5000/api/livros/COLOCAR/4 `
  -Method PUT `
  -ContentType "application/json" `
  -Body '{"titulo":"OSenhor-dos-Anéis","autor":"J. R. R. Tolkien","ano":1954}'
Invoke-RestMethod : 
404 Not Found
Not Found
The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.
No linha:1 caractere:1
+ Invoke-RestMethod http://127.0.0.1:5000/api/livros/COLOCAR/4 `
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidOperation: (System.Net.HttpWebRequest:HttpWebRequest) [Invoke-RestMethod], WebException
    + FullyQualifiedErrorId : WebCmdletWebResponseException,Microsoft.PowerShell.Commands.InvokeRestMethodCommand

PS C:\Users\22400060> Invoke-RestMethod http://127.0.0.1:5000/api/livros/COLOCAR/4 `
  -Method PUT `
  -ContentType "application/json" `
  -Body '{"titulo":"OSenhor-dos-Anéis","autor":"J. R.R.Tolkien","ano":1954}'
Invoke-RestMethod : 
404 Not Found
Not Found
The requested URL was not found on the server. If you entered the URL manually please check your spelling and try again.
No linha:1 caractere:1
+ Invoke-RestMethod http://127.0.0.1:5000/api/livros/COLOCAR/4 `
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidOperation: (System.Net.HttpWebRequest:HttpWebRequest) [Invoke-RestMethod], WebException
    + FullyQualifiedErrorId : WebCmdletWebResponseException,Microsoft.PowerShell.Commands.InvokeRestMethodCommand

PS C:\Users\22400060> Invoke-RestMethod http://127.0.0.1:5000/api/livros/4 `
  -Method PUT `
  -ContentType "application/json" `
  -Body '{"titulo":"OSenhor-dos-Anéis","autor":"J. R.R.Tolkien","ano":1954}'
Invoke-RestMethod : 
400 Bad Request
Bad Request
Failed to decode JSON object: &#39;utf-8&#39; codec can&#39;t decode byte 0xe9 in position 25: invalid continuation byte
No linha:1 caractere:1
+ Invoke-RestMethod http://127.0.0.1:5000/api/livros/4 `
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidOperation: (System.Net.HttpWebRequest:HttpWebRequest) [Invoke-RestMethod], WebException
    + FullyQualifiedErrorId : WebCmdletWebResponseException,Microsoft.PowerShell.Commands.InvokeRestMethodCommand

PS C:\Users\22400060> Invoke-RestMethod http://127.0.0.1:5000/api/livros/4 `
  -Method PUT `
  -ContentType "application/json" `
  -Body '{"titulo":"OSenhor-dos-Anéis","autor":"J. R.R.Tolkien","ano":1954}'
Invoke-RestMethod : 
400 Bad Request
Bad Request
Failed to decode JSON object: &#39;utf-8&#39; codec can&#39;t decode byte 0xe9 in position 25: invalid continuation byte
No linha:1 caractere:1
+ Invoke-RestMethod http://127.0.0.1:5000/api/livros/4 `
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidOperation: (System.Net.HttpWebRequest:HttpWebRequest) [Invoke-RestMethod], WebException
    + FullyQualifiedErrorId : WebCmdletWebResponseException,Microsoft.PowerShell.Commands.InvokeRestMethodCommand

PS C:\Users\22400060> Invoke-RestMethod http://127.0.0.1:5000/api/livros/4 `
  -Method PUT `
  -ContentType "application/json" `
  -Body '{"titulo":"OSenhor-dos-Anéis","autor":". R.R.Tolkien","ano":1954}'
Invoke-RestMethod : 
400 Bad Request
Bad Request
Failed to decode JSON object: &#39;utf-8&#39; codec can&#39;t decode byte 0xe9 in position 25: invalid continuation byte
No linha:1 caractere:1
+ Invoke-RestMethod http://127.0.0.1:5000/api/livros/4 `
+ ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    + CategoryInfo          : InvalidOperation: (System.Net.HttpWebRequest:HttpWebRequest) [Invoke-RestMethod], WebException
    + FullyQualifiedErrorId : WebCmdletWebResponseException,Microsoft.PowerShell.Commands.InvokeRestMethodCommand

PS C:\Users\22400060> Invoke-RestMethod http://127.0.0.1:5000/api/livros/4 `
  -Method PUT `
  -ContentType "application/json" `
  -Body '{"titulo":"O Senhor dos Aneis","autor":"J. R. R. Tolkien","ano":1954}'


ano          : 1954
autor        : J. R. R. Tolkien
data_criacao : 2026-07-30 08:08:29.819806
id           : 4
titulo       : O Senhor dos Aneis




PS C:\Users\22400060> Invoke-RestMethod http://127.0.0.1:5000/api/livros/5 -Method DELETE


PS C:\Users\22400060> Invoke-RestMethod http://127.0.0.1:5000/api/livros/6 -Method DELETE


PS C:\Users\22400060> Invoke-RestMethod http://127.0.0.1:5000/api/livros/7 -Method DELETE


PS C:\Users\22400060> Invoke-RestMethod http://127.0.0.1:5000/api/livros



ano          : 1949
autor        : George Orwell
data_criacao : 2026-07-30 08:05:18.096197
id           : 3
titulo       : 1984

ano          : 1967
autor        : Gabriel Garcia Marquez
data_criacao : 2026-07-30 08:11:04.336312
id           : 10
titulo       : Cem Anos de Solidao

ano          : 1866
autor        : Fiodor Dostoievski
data_criacao : 2026-07-30 08:10:24.163707
id           : 9
titulo       : Crime e Castigo

ano          : 1899
autor        : Machado de Assis
data_criacao : 2026-07-30 08:05:18.096197
id           : 1
titulo       : Dom Casmurro

ano          : 1997
autor        : J. K. Rowling
data_criacao : 2026-07-30 08:10:18.382379
id           : 8
titulo       : Harry Potter e a Pedra Filosofal

ano          : 1890
autor        : Aluísio Azevedo
data_criacao : 2026-07-30 08:05:18.096197
id           : 2
titulo       : O Cortiço

ano          : 1954
autor        : J. R. R. Tolkien
data_criacao : 2026-07-30 08:08:29.819806
id           : 4
titulo       : O Senhor dos Aneis




PS C:\Users\22400060> 