# API Parking Lot

Api para gerenciar um estacionamento de veículos.

|   Como utilizar o projeto	|   Tecnologias utilizadas	|
|---	|---	|
|1º Clone o projeto em um diretório de sua preferência. | Python com _django_ e _djangorestframework_. |
|2º Instale todos a dependencias do projeto que estão listadas no arquivo _requirements.txt_. **pip install -r _requeriments.txt_** |
|3º Agora é só rodar o servidor. Estando da raiz da aplicação digite: **./manage.py runserver**



&nbsp; 
###  Base URL: http://localhost:8000/
&nbsp; 
##  Endpoints públicos
####  POST /api/accounts/
> Criar um usuário administrador.
> * Admin - terá ambos os campos is_staff e is_superuser com o valor True


Criando um administrador

Body JSON:
```json
{
  "username": "admin",
  "password": "1234",
  "is_superuser": true,
  "is_staff": true
}
```
Response - HTTP Status 201:
```json
{
  "id": 3,
  "is_superuser": true,
  "is_staff": true,
  "username": "admin"
}
```

####  POST /api/login/
> Fazer login

Body JSON:
```json
{
	"username": "admin",
	"password": "1234"
}
```
Response - HTTP Status 200:
```json
{
  "token": "dfd384673e9127213de6116ca33257ce4aa203cf"
}
```

&nbsp;
## Endpoints restritos
Os endpoints a seguir estão disponíveis apenas para usuários com um token de administador. No header, espeficar nesse formato:
```json
Authorization: Token <token admin>
```

####  POST /api/levels/
> Criando um nivel do estacionamento. Apenas um admintrador pode criar.

Header:
```json
// Authorization: Token <admin>
```

Body JSON:
```json
{
	"name": "floor 2",
	"fill_priority": 2,
	"bike_spots": 1,
	"car_spots": 2
}
```
Response - HTTP Status 201:
```json
{
  "id": 2,
  "name": "floor 2",
  "fill_priority": 2,
  "available_spots": {
    "available_bike_spots": 1,
    "available_car_spots": 2
  }
}
```

####  GET /api/levels/
> Recuperando todos os níveis do estaciomento com suas vagas disponíveis. Apenas um administrador pode acessar.
Header:
```json
// Authorization: Token <admin>
```

Response:
```json
[
  {
    "id": 1,
    "name": "floor 1",
    "fill_priority": 2,
    "available_spots": {
      "available_bike_spots": 1,
      "available_car_spots": 2
    }
  },
  {
    "id": 2,
    "name": "floor 2",
    "fill_priority": 2,
    "available_spots": {
      "available_bike_spots": 1,
      "available_car_spots": 2
    }
  }
]
```

####  POST /api/pricings/
> Criar os coeficientes da tebela de preço. Trabalhar com centavos. Apenas um admintrador pode criar.

Header:
```json
// Authorization: Token <admin>
```

Body JSON:
```json
{
	"a_coefficient": 100,
	"b_coefficient": 100
}
```
Response - HTTP Status 201:
```json
{
  "id": 4,
  "a_coefficient": 100,
  "b_coefficient": 100
}
```

&nbsp;  
#### Desenvolvedor
**[Alex Miguel](https://www.linkedin.com/in/alexmiguel95/)**

alexmiguel95@gmail.com
