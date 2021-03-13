import requests

class TesteCardapio:
    headers = {'authorization': 'Token 53d0c6931ed52a8c68c47066de2e00367697d784'}
    url_base_cardapio = 'http://localhost:8000/api/v1/cardapios/'

    def test_get_cardapio(self):
        resposta = requests.get(url=self.url_base_cardapio, headers=self.headers)

        assert resposta.status_code == 200

    def test_get_cardapio(self):
        resposta = requests.get(url=f'{self.url_base_cardapio}2/', headers=self.headers)

        assert resposta.status_code == 200

    def test_post_cardapio(self):
        novo = {
            "prato": "Filé a cubana",
            "descricao": " FILÉ À CUBANA: MAIS UM PRATO DE 'O ALEMÃO' Marque um amigo para te acompanhar neste fds ;-) Filet Mignon à milanesa, coberto com presunto e mussarela... ",
            "popularidade": "Prato da casa",
            "evento": "alemao",
            "preco": "150.98"
        }
        resposta = requests.post(url=self.url_base_cardapio, headers=self.headers, data=novo)

        assert resposta.status_code == 201
        assert resposta.json()['prato'] == novo['prato']

    def test_put_cardapio(self):
        atualizar = {
            "prato": "Filé a cubana premiun",
            "descricao": " FILÉ À CUBANA: MAIS UM PRATO DE 'O ALEMÃO' Marque um amigo para te acompanhar neste fds ;-) Filet Mignon à milanesa, coberto com presunto e mussarela... ",
            "popularidade": "Prato da casa",
            "evento": "alemao",
            "preco": "200"
        }

        resposta = requests.put(url=f'{self.url_base_cardapio}9/', headers=self.headers, data=atualizar)

        assert resposta.status_code == 200


    def test_delete_cardapio(self):
        resposta = requests.delete(url=f'{self.url_base_cardapio}9/', headers=self.headers)

        assert resposta.status_code == 204 and len(resposta.text) == 0



class TesteAvalicao:
    headers = {'authorization': 'Token 53d0c6931ed52a8c68c47066de2e00367697d784'}
    url_base_avaliacao= 'http://localhost:8000/api/v1/avaliacao/'

    def test_get_avaliacao(self):
        resposta = requests.get(url=self.url_base_avaliacao, headers=self.headers)

        assert resposta.status_code == 200

    def test_get_avaliacao(self):
        resposta = requests.get(url=f'{self.url_base_avaliacao}1/', headers=self.headers)

        assert resposta.status_code == 200

    def test_post_avaliacao(self):
        novo = {
            "prato": "1",
            "nome": "Nathalia",
            "email": "nathalia@gmail.com",
            "comentario": "falta de tempero",
            "criticas": "",
            "satisfacao": "4.0",
            "avaliacao": "2.9",
            "evento": "nenhum"

        }
        resposta = requests.post(url=self.url_base_avaliacao, headers=self.headers, data=novo)

        assert resposta.status_code == 201
        assert resposta.json()['email'] == novo['email']


    def test_delete_cardapio(self):
        resposta = requests.delete(url=f'{self.url_base_avaliacao}3/', headers=self.headers)

        assert resposta.status_code == 204 and len(resposta.text) == 0