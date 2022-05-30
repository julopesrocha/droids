# Projeto 01 | Relatório
A empresa foi contratada pela Federação de Comércio para desenvolver uma pequena aplicação que possibilite a publicação de cotações de peças específicas de droids.


## Índice
* [Informações sobre o hardware](#informações-sobre-o-hardware)
* [Requisitos MVP](#requisitos-mvp)
* [Entrega](#entrega)

## Informações sobre o hardware
- Distro: Ubuntu 20.04.4 LTS
- Nome do Modelo: Intel(R) Core(TM) i3-8145U CPU @ 2.10GHz
- Arquitetura: x86_64

## Requisitos MVP
:exclamation: Criação de uma API REST utilizando Django e Django Rest Framework como Backend.Não foi necessária a criação de um Client para consumir estes endpoints. A validação será feita através de uma coleção de chamadas do Postman.

Uma Demanda de Peças é composta por:
- Descrição da peça solicitada
- Endereço de Entrega
- Informações de Contato
- Anunciante (Usuário Dono)
- Status de Finalização

Devem existir dois tipos de usuários: um Administrador e um Anunciante. O Administrador tem acesso a todas as demandas criadas no sistema, enquanto o Anunciante possui apenas permissão para a visualização e manipulação de suas próprias demandas.

As seguintes ações devem ser disponíveis para um usuário do tipo Anunciante, através de uma API REST:
- Cração de uma Demanda
- Listagem de Demandas
- Edição de Demanda
- Exclusão de Demanda
- Finalização de uma Demanda

O Administrador, através do admin do Django, deve ser capaz de visualizar as Demandas cadastradas na plataforma com todas as suas inforamações presentes na listagem

## Entrega
- Container Docker
- Collection exportada do Postman