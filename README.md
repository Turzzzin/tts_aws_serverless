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

## Documentações úteis:
1. [Serverless Framework](https://www.serverless.com/framework/docs)
2. [Amazon Polly](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/polly.html)
3. [Amazon S3](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html)
4. [Amazon DynamoDB](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/dynamodb.html)
