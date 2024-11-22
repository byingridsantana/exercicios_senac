# import bibliotecario.crud_bibliotecario as bi

# bi.cadastrar("Paola Oliveira", "paola@gmail.com", "11-2635-5263")
# bi.atualizar_biblioteario(1,"Elena Moraes Dias", "elena@gmail.com", "11-2635-8596")
# bi.apagar_bibliotecario(2)

# Para verificar:
# bi.listar_bibliotecario()

# Importar Aluno

# import aluno.crud_aluno as al

# Cadastrar Aluno: 
# al.cadastrar("Joana Soares", "11243","Psicologia","joana@gmail.com.br","11-8865-6523")

# Atualizar Aluno:
# al.atualizar_aluno("Joana Soares", "11243","Artes Plasticas","joana@gmail.com.br","11-8865-6523",2)

# Apagar Aluno
# al.apagar_aluno(2)
# al.listar_aluno()

# Importar Publicação

# import publicacao.crud_publicacao as pl 

# Cadastrar Publicação:

# pl.cadastrar ("A Biblioteca da Meia-Noite", " Matt Haig", "Bertrand Brasil", "2021-09-27", "6558380544", " Ficção Científica Humorística", "Livro", "ficção, romance, ", "2", "Setor de Ficção")
# pl.cadastrar ("Outlive: A arte e a ciência de viver mais e melhor", "Bill Gifford,  Peter Attia", "Intrínseca", "2023-09-1", "6555606150", "Saúde", "Livro", "Saúde, Bem-Estar, Medicina", "3", "Setor de Medicina")
# pl.cadastrar ("Outlive 2: A arte e a ciência de viver mais e melhor", "Bill Gifford,  Peter Attia", "Intrínseca", "2023-09-1", "6555606152", "Saúde", "Livro", "Saúde, Bem-Estar, Medicina", "3", "Setor de Medicina")

# Atualizacao Publicação:
# pl.atualizar_publicacao("A Biblioteca da Meia-Noite", " Matt Haig", "Bertrand Brasil", "2021-09-27", "6558380544", " Ficção Científica Humorística", "Livro", "ficção, romance, ", "5", "Setor de Ficção", 1)

# Apagar Publicação:
# bi.apagar_bibliotecario(2)

# pl.apagar_publicacao(5)

# Importar Emprestimo
import Biblioteca.emprestimo.crud_emprestimo as em

# Para Cadastrar: 
em.cadastrar("2024-11-25","",1,1,1)

# Para Atualizar: 
# em.atualizar_emprestimo("2024-11-28",1)
# em.listar_emprestimo()

# Para Apagar
# em.apagar_emprestimo(2)