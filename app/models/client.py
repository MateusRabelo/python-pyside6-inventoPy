class Client:
    def __init__(self, client_id, name, email, phone):
        self.client_id = client_id
        self.name = name
        self.email = email
        self.phone = phone

    def __repr__(self):
        return f"Client(id={self.client_id}, name={self.name}, email={self.email}, phone={self.phone})"

    def save(self):
        # Lógica para salvar o cliente no banco de dados
        pass

    def update(self):
        # Lógica para atualizar o cliente no banco de dados
        pass

    def delete(self):
        # Lógica para deletar o cliente no banco de dados
        pass

    @staticmethod
    def get_all():
        # Lógica para retornar todos os clientes do banco de dados
        pass
