# Text to Speech (AWS / Serverless)
Este é um projeto de estudo. Nele, aprimorarei minhas habilidades em alguns serviços da AWS (Polly, S3 e DynamoDB) e no framework Serverless

## Como utilizar?
Os endpoints da aplicação que eu criei, estarão offline por conta de cobranças da Amazon Web Services. Porém, para utilizar em sua máquina, é necessário seguir alguns passos.
1. Baixar os arquivos deste repositório
2. Abrir com um editor de texto a pasta `/tts_aws_serverless`
3. Criar, dentro da pasta `src` um arquivo `.env`
4. Configurar as credenciais e nomes de acordo com o arquivo `.env.example`
5. Baixar o framework *serverless* e configurar as credenciais de acordo com o que foi configurado no .env
6. Abrir o terminal no diretório da aplicação e rodar o seguinte comando: `serverless deploy`
7. Depois do deploy terminar, 4 rotas serão disponibilizadas
8. As rotas POST serão indicadas no terminal
9. Sendo assim, basta utilizar uma ferramenta de requisições (como o POSTMAN por exemplo) para utilizar a aplicação


## Exemplos de retornos:

### Rota /v1/tts

```json
{
    "received_phrase": "Isso eh um teste",
    "url_to_audio": "https://sprint06-project.s3.amazonaws.com/d9a7aae31fe65abadbbdae54956bad17?AWSAccessKeyId=AKIAWIELUULDJGHMPSQT&Signature=tXfwJ5w49wNrX9FwzZZxnVZqSrM%3D&Expires=1696363246",
    "created_audio": "03-10-2023 16:00:45"
}
```

### Rota /v2/tts

```json
{
    "received_phrase": "Isso NAO eh um teste",
    "url_to_audio": "https://sprint06-project.s3.amazonaws.com/688dd2ead9c9427fd0338d7c463f9f37?AWSAccessKeyId=AKIAWIELUULDJGHMPSQT&Signature=WPywy3VTB%2BYtTBHpW4m%2F6IzqPN4%3D&Expires=1696363216",
    "created_audio": "03-10-2023 16:00:16",
    "unique_id": "688dd2ead9c9427fd0338d7c463f9f37"
}
```

### Rota /v3/tts

```json
{
    "received_phrase": "Isso NAO eh um teste",
    "url_to_audio": "https://sprint06-project.s3.amazonaws.com/688dd2ead9c9427fd0338d7c463f9f37?AWSAccessKeyId=AKIAWIELUULDJGHMPSQT&Signature=cx7THrO6pBRceHJrTSJqYxqEdbA%3D&Expires=1696362217",
    "created_audio": "03-10-2023 15:43:36",
    "unique_id": "688dd2ead9c9427fd0338d7c463f9f37"
}
```

## Documentações úteis:
1. [Serverless Framework](https://www.serverless.com/framework/docs)
2. [Amazon Polly](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/polly.html)
3. [Amazon S3](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html)
4. [Amazon DynamoDB](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html)
