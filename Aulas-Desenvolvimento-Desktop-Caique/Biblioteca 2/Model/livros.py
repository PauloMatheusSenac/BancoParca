class Livros:
    def __init__(self, titulo, autor, genero, cod_livro):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.cod_livro = cod_livro
        self.status = "Disponivel"
        self.usuario = None

    def create(self):
        return f'INSERT into livro(titulo, autor, genero, status, codigo) values("{self.titulo}", "{self.autor}", "{self.genero}", "{self.status}", "{self.cod_livro}");'

    def delete(self):
        return f'DELETE FROM livro WHERE codigo = {self.cod_livro};'
    
    def update(self, novo_titulo=None, novo_autor=None, novo_genero=None, novo_status=None):
        set_clause = []
        
        if novo_titulo:
            set_clause.append(f'titulo = "{novo_titulo}"')
        if novo_autor:
            set_clause.append(f'autor = "{novo_autor}"')
        if novo_genero:
            set_clause.append(f'genero = "{novo_genero}"')
        if novo_status:
            set_clause.append(f'status = "{novo_status}"')
        
        set_clause_str = ", ".join(set_clause)
        return f'UPDATE livro SET {set_clause_str} WHERE codigo = {self.cod_livro};'

    def select(self):
        return f'SELECT * FROM livro WHERE codigo = {self.cod_livro};'



    
