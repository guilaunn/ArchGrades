# ArchGrades

# Instalação
Clone o repositório e dentro dele crie um ambiente virtual

Utilize o pip para baixar as dependências do projeto:
```
pip install -r requirements.txt
```
Para iniciar, pausar e gerar os logs dos containers no docker use:
iniciar:
```
docker-compose up --build -d
```
Ver logs:
```
docker-compose logs -f
```
Pausar:
```
docker-compose down -v
```

Para iniciar o servidor da api:
```
uvicorn app.main:app --reload --workers 1 --host 0.0.0.0 --port 8000
```
Para consultar a documentação da API e testar as rotas, acesse http://127.0.0.1:8000/docs e para interomper a execução pressione «Ctrl»+«C».
