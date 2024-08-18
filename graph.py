import networkx as nx
import matplotlib.pyplot as plt

# Criando o grafo
transporte_metropolitano_sp = nx.Graph()

corredor_a = [
    "Sônia Maria", "São Bernardo", "Ferrazópolis", "Piraporinha", "Diadema"
] 

corredor_b = [
    "Vila Galvão", "Cecap", "Taboão"
]

linha_1 = [
    "Jabaquara", "Conceição", "Saúde", "São Judas", "Praça da Árvore", "Santa Cruz", "Vila Mariana", "Ana Rosa", "Paraíso", "Vergueiro", "São Joaquim", "Sé", "São Bento", "Luz", "Tiradentes", "Armênia", "Portuguesa-Tietê", "Carandiru", "Santana", "Jardim São Paulo-Ayrton Senna", "Parada Inglesa", "Tucuruvi"
]

linha_2 = [
    "Ana Rosa", "Paraíso", "Brigadeiro", "Trianon-Masp", "Consolação", "Clínicas", "Sumaré", "Vila Madalena", "Chácara Klabin", "Santos-Imigrantes", "Alto do Ipiranga", "Sacomã", "Tamanduateí", "Vila Prudente"
]

linha_3 = [
    "Lapa", "Marechal Deodoro", "Santa Cecília", "República", "Anhangabaú", "Sé", "Pedro II", "Brás", "Bresser - Mooca", "Belém", "Tatuapé", "Carrão", "Penha", "Vila Matilde", "Guilhermina-Esperança", "Patriarca", "Artur Alvim", "Corinthians-Itaquera"
]

linha_4 = [
    "Higienópolis-Mackenzie", "Oscar Freire", "Fradique Coutinho", "Faria Lima", "Pinheiros", "Butantã", "São Paulo-Morumbi", "Vila Sônia", "Taboão da Serra"
]

linha_5 = [
    "Capão Redondo", "Campo Limpo", "Vila das Belezas", "Giovanni Gronchi", "Santo Amaro", "Largo Treze", "Adolfo Pinheiro", "Alto da Boa Vista", "Borba Gato", "Brooklin", "Campo Limpo", "Eucaliptos", "Moema", "AACD-Servidor", "Hospital São Paulo"     
]

linha_7 = [
    "Palmeiras - Barra Funda", "Água Branca", "Lapa_7", "Piqueri", "Pirituba", "Vila Clarice", "Jaraguá", "Vila Aurora", "Perus", "Caieiras", "Franco da Rocha", "Baltazar Fidélis", "Francisco Morato", "Botujuru", "Campo Limpo Paulista", "Várzea Paulista", "Jundiaí"
]

linha_8 = [
    "Júlio Prestes", "Lapa_8", "Domingos de Moraes", "Imperatriz Leopoldina", "Presidente Altino", "Osasco", "Comandante Sampaio", "Quitauna", "General Miguel Costa", "Carapicuíba", "Santa Terezinha", "Antonio João", "Barueri", "Jardim Belval", "Jardim Silveira", "Jandira", "Sagrado Coração", "Engenheiro Cardoso", "Itapevi", "Santa Rita", "Amador Bueno"
]

linha_9 = [
    "Bruno Covas", "Grajaú", "Primavera - Interlagos", "Autódromo", "Jurubatuba", "Socorro", "João Dias", "Granja Julieta", "Morumbi", "Berrini", "Vila Olímpia", "Cidade Jardim", "Hebraica-Rebouças", "Cidade Universitária", "Vila Lobos - Jaguaré", "Ceasa", "Vila Aurora"
]

linha_10 = [
    "Juventude-Mooca", "Ipiranga", "Tamanduateí", "São Caetano do Sul", "Utinga", "Prefeito Saladino", "Santo André", "Capuava", "Mauá", "Guapituba", "Ribeirão Pires", "Rio Grande da Serra"
]

linha_11 = [
    "Dom Bosco", "José Bonifácio", "Guaianases", "Antonio Gianetti Neto", "Ferraz de Vasconcelos", "Poé", "Calmon Viana", "Suzano", "Jundiapeba", "Braz Cubas", "Mogi das Cruzes", "Estudantes"
] 

linha_12 = [
    "Engenheiro Goulart", "USP Leste", "Comendador Ermelino", "São Miguel Paulista", "Jardim Helena", "Itaim Paulista", "Jardim Romano", "Engenheiro Manoel Feio", "Itaquaquecetuba", "Aracaré"
] 

linha_13 = [
    "Guarulhos-Cecap", "Aeroporto-Guarulhos"
]

linha_15 = [
    "Oratório", "São Lucas", "Camilo Haddad", "Vila Tolstói", "Vila União", "Jardim Planalto", "Sapopemba", "Fazenda da Juta", "São Mateus", "Jardim Colonial"
]

transporte_metropolitano_sp.add_nodes_from(corredor_a)
transporte_metropolitano_sp.add_nodes_from(corredor_b)
transporte_metropolitano_sp.add_nodes_from(linha_1)
transporte_metropolitano_sp.add_nodes_from(linha_2)
transporte_metropolitano_sp.add_nodes_from(linha_3)
transporte_metropolitano_sp.add_nodes_from(linha_4)
transporte_metropolitano_sp.add_nodes_from(linha_5)
transporte_metropolitano_sp.add_nodes_from(linha_7)
transporte_metropolitano_sp.add_nodes_from(linha_8)
transporte_metropolitano_sp.add_nodes_from(linha_9)
transporte_metropolitano_sp.add_nodes_from(linha_10)
transporte_metropolitano_sp.add_nodes_from(linha_11)
transporte_metropolitano_sp.add_nodes_from(linha_12)
transporte_metropolitano_sp.add_nodes_from(linha_13)
transporte_metropolitano_sp.add_nodes_from(linha_15)

edges = [
    # Corredor A
    ("São Mateus", "Sônia Maria"), ("Sônia Maria", "Santo André"),
    ("Santo André", "São Bernardo"), ("São Bernardo", "Ferrazópolis"),
    ("São Bernardo", "Piraporinha"), ("Piraporinha", "Diadema"),
    ("Diadema", "Jabaquara"), ("Diadema", "Brooklin"),
    ("Brooklin", "Morumbi"), ("Morumbi", "Berrini"),

    # Corredor B
    ("Tucuruvi", "Vila Galvão"), ("Vila Galvão", "Cecap"),
    ("Cecap", "Guarulhos-Cecap"), ("Guarulhos-Cecap", "Taboão"),

    # Linha 1 - Azul
    ("Jabaquara", "Conceição"), ("Conceição", "Saúde"),
    ("Saúde", "São Judas"), ("São Judas", "Praça da Árvore"),
    ("Praça da Árvore", "Santa Cruz"), ("Santa Cruz", "Vila Mariana"),
    ("Vila Mariana", "Ana Rosa"), ("Ana Rosa", "Paraíso"),
    ("Paraíso", "Vergueiro"), ("Vergueiro", "São Joaquim"), 
    ("São Joaquim", "Sé"), ("Sé", "São Bento"),
    ("São Bento", "Luz"), ("Luz", "Tiradentes"),
    ("Tiradentes", "Armênia"), ("Armênia", "Portuguesa-Tietê"),
    ("Portuguesa-Tietê", "Carandiru"), ("Carandiru", "Santana"),
    ("Santana", "Jardim São Paulo-Ayrton Senna"), ("Jardim São Paulo-Ayrton Senna", "Parada Inglesa"),
    ("Parada Inglesa", "Tucuruvi"),

    # Linha 2 - Verde
    ("Paraíso", "Brigadeiro"),
    ("Brigadeiro", "Trianon-Masp"), ("Trianon-Masp", "Consolação"),
    ("Consolação", "Clínicas"), ("Clínicas", "Sumaré"),
    ("Sumaré", "Vila Madalena"), ("Ana Rosa", "Chácara Klabin"),
    ("Chácara Klabin", "Santos-Imigrantes"), ("Santos-Imigrantes", "Alto do Ipiranga"),
    ("Alto do Ipiranga", "Sacomã"), ("Sacomã", "Tamanduateí"),
    ("Tamanduateí", "Vila Prudente"),

    # Linha 3 - Vermelha
    ("Lapa", "Marechal Deodoro"), ("Marechal Deodoro", "Santa Cecília"),
    ("Santa Cecília", "República"), ("República", "Anhangabaú"),
    ("Anhangabaú", "Sé"), ("Sé", "Pedro II"),
    ("Pedro II", "Brás"), ("Brás", "Bresser - Mooca"),
    ("Bresser - Mooca", "Belém"), ("Belém", "Tatuapé"),
    ("Tatuapé", "Carrão"), ("Carrão", "Penha"),
    ("Penha", "Vila Matilde"), ("Vila Matilde", "Guilhermina-Esperança"),
    ("Guilhermina-Esperança", "Patriarca"), ("Patriarca", "Artur Alvim"),
    ("Artur Alvim", "Corinthians-Itaquera"),

    # Linha 4 - Amarela
    ("São Bento", "República"), ("República", "Higienópolis-Mackenzie"),
    ("Higienópolis-Mackenzie", "Consolação"), ("Consolação", "Oscar Freire"),
    ("Oscar Freire", "Fradique Coutinho"), ("Fradique Coutinho", "Faria Lima"),
    ("Faria Lima", "Pinheiros"), ("Pinheiros", "Butantã"),
    ("Butantã", "São Paulo-Morumbi"), ("São Paulo-Morumbi", "Vila Sônia"),
    ("Vila Sônia", "Taboão da Serra"),

    # Linha 5 - Lilás
    ("Capão Redondo", "Campo Limpo"), ("Campo Limpo", "Vila das Belezas"),
    ("Vila das Belezas", "Giovanni Gronchi"), ("Giovanni Gronchi", "Santo Amaro"),
    ("Santo Amaro", "Largo Treze"), ("Largo Treze", "Adolfo Pinheiro"),
    ("Adolfo Pinheiro", "Alto da Boa Vista"), ("Alto da Boa Vista", "Borba Gato"),
    ("Borba Gato", "Brooklin"), ("Brooklin", "Campo Limpo"),
    ("Campo Limpo", "Eucaliptos"), ("Eucaliptos", "Moema"),
    ("Moema", "AACD-Servidor"), ("AACD-Servidor", "Hospital São Paulo"),
    ("Hospital São Paulo", "Santa Cruz"), ("Santa Cruz", "Chácara Klabin"),

    #Linha 7 - Rubi
    ("Luz", "Palmeiras - Barra Funda"), ("Palmeiras - Barra Funda", "Água Branca"),
    ("Água Branca", "Lapa_7"), ("Lapa_7", "Piqueri"), ("Piqueri", "Pirituba"),
    ("Pirituba", "Vila Clarice"), ("Vila Clarice", "Jaraguá"), ("Jaraguá", "Vila Aurora"),
    ("Vila Aurora", "Perus"), ("Perus", "Caieiras"), ("Caieiras", "Franco da Rocha"),
    ("Franco da Rocha", "Baltazar Fidélis"), ("Baltazar Fidélis", "Francisco Morato"),
    ("Francisco Morato", "Botujuru"), ("Botujuru", "Campo Limpo Paulista"),
    ("Campo Limpo Paulista", "Várzea Paulista"), ("Várzea Paulista", "Jundiaí"),

    #Linha 8 - Diamante
    ("Júlio Prestes", "Palmeiras - Barra Funda"), ("Palmeiras - Barra Funda", "Lapa_8"),
    ("Lapa_8", "Domingos de Moraes"), ("Domingos de Moraes", "Imperatriz Leopoldina"),
    ("Imperatriz Leopoldina", "Presidente Altino"), ("Presidente Altino", "Osasco"),
    ("Osasco", "Comandante Sampaio"), ("Comandante Sampaio", "Quitauna"),
    ("Quitauna", "General Miguel Costa"), ("General Miguel Costa", "Carapicuíba"),
    ("Carapicuíba", "Santa Terezinha"), ("Santa Terezinha", "Antonio João"),
    ("Antonio João", "Barueri"), ("Barueri", "Jardim Belval"),
    ("Jardim Belval", "Jardim Silveira"), ("Jardim Silveira", "Jandira"),
    ("Jandira", "Sagrado Coração"), ("Sagrado Coração", "Engenheiro Cardoso"),
    ("Engenheiro Cardoso", "Itapevi"), ("Itapevi", "Santa Rita"),
    ("Santa Rita", "Amador Bueno"),

    #Linha 9 - Esmeralda
    ("Osasco", "Presidente Altino"), ("Presidente Altino", "Ceasa"),
    ("Ceasa", "Vila Lobos - Jaguaré"), ("Vila Lobos - Jaguaré", "Cidade Universitária"),
    ("Cidade Universitária", "Pinheiros"), ("Pinheiros", "Hebraica-Rebouças"),
    ("Hebraica-Rebouças", "Cidade Jardim"), ("Cidade Jardim", "Vila Olímpia"),
    ("Vila Olímpia", "Berrini"), ("Berrini", "Morumbi"),
    ("Morumbi", "Granja Julieta"), ("Granja Julieta", "João Dias"),
    ("João Dias", "Santo Amaro"), ("Santo Amaro", "Socorro"),
    ("Socorro", "Jurubatuba"), ("Jurubatuba", "Autódromo"),
    ("Autódromo", "Primavera - Interlagos"), ("Primavera - Interlagos", "Grajaú"),
    ("Grajaú", "Bruno Covas"),

    #Linha 10 - Turquesa
    ("Luz", "Brás"), ("Brás", "Juventude-Mooca"),
    ("Ipiranga", "Tamanduateí"), ("Tamanduateí", "São Caetano do Sul"),
    ("São Caetano do Sul", "Utinga"), ("Santo André", "Capuava"),
    ("Utinga", "Prefeito Saladino"), ("Prefeito Saladino", "Santo André"),
    ("Mauá", "Guapituba"), ("Guapituba", "Ribeirão Pires"),
    ("Capuava", "Mauá"), ("Guapituba", "Ribeirão Pires"),
    ("Ribeirão Pires", "Rio Grande da Serra"),

    #Linha 11 - Coral
    ("Luz", "Brás"), ("Tatuapé", "Corintihians-Itaquera"),
    ("Corinthians-Itaquera", "Dom Bosco"), ("Dom Bosco", "José Bonifácio"),
    ("José Bonifácio", "Guaianases"), ("Guaianases", "Antonio Gianetti Neto"),
    ("Antonio Gianetti Neto", "Ferraz de Vasconcelos"), ("Ferraz de Vasconcelos", "Poé"),
    ("Poé", "Calmon Viana"), ("Calmon Viana", "Suzano"),
    ("Suzano", "Jundiapeba"), ("Jundiapeba", "Braz Cubas"),
    ("Braz Cubas", "Mogi das Cruzes"), ("Mogi das Cruzes", "Estudantes"),

    #Linha 12 - Safira
    ("Brás", "Tatuapé"), ("Tatuapé","Engenheiro Goulart"),
    ("Engenheiro Goulart", "USP Leste"), ("USP Leste", "Comendador Ermelino"),
    ("Comendador Ermelino", "São Miguel Paulista"), ("São Miguel Paulista", "Jardim Helena"),
    ("Jardim Helena", "Itaim Paulista"), ("Itaim Paulista", "Jardim Romano"),
    ("Jardim Romano", "Engenheiro Manoel Feio"), ("Engenheiro Manoel Feio", "Itaquaquecetuba"),
    ("Itaquaquecetuba", "Aracaré"), ("Aracaré", "Calmon Viana"),

    #Linha 13 - Jade
    ("Engenheiro Goulart", "Guarulhos-Cecap"), ("Guarulhos-Cecap", "Aeroporto-Guarulhos"),

    #Linha 15 - Prata
    ("Vila Prudente", "Oratório"), ("Oratório", "São Lucas"),
    ("São Lucas", "Camilo Haddad"), ("Camilo Haddad", "Vila Tolstói"),
    ("Vila Tolstói", "Vila União"), ("Vila União", "Jardim Planalto"),
    ("Jardim Planalto", "Sapopemba"), ("Sapopemba", "Fazenda da Juta"),
    ("Fazenda da Juta", "São Mateus"), ("São Mateus", "Jardim Colonial")
]

# Adicionando as arestas
transporte_metropolitano_sp.add_edges_from(edges)

# Mapeando a cor dos nós de acordo com a linha/corredor
node_colors = []

for node in transporte_metropolitano_sp.nodes():
    if node in corredor_a:
        node_colors.append("skyblue")
    elif node in corredor_b:
        node_colors.append("purple")
    elif node in linha_1:
        node_colors.append("blue")
    elif node in linha_2:
        node_colors.append("green")
    elif node in linha_3:
        node_colors.append("red")
    elif node in linha_4: 
        node_colors.append("yellow")
    elif node in linha_5:
        node_colors.append("plum")
    elif node in linha_7:
        node_colors.append("purple")
    elif node in linha_8:
        node_colors.append("silver")
    elif node in linha_9:
        node_colors.append("lime")
    elif node in linha_10:
        node_colors.append("turquoise")
    elif node in linha_11:
        node_colors.append("coral")
    elif node in linha_12:
        node_colors.append("navy")
    elif node in linha_13:
        node_colors.append("darkgreen")
    elif node in linha_15:
        node_colors.append("grey")
    else:
        node_colors.append("black")

# Usando um layout automático com espaçamento maior (k maior) e mais iterações
pos = nx.spring_layout(transporte_metropolitano_sp, k=0.5, iterations=200)

# Criando a figura
fig, ax = plt.subplots(figsize=(16, 14))

# Desenhando os nós
nx.draw_networkx_nodes(
    transporte_metropolitano_sp, pos,
    node_color=node_colors,
    node_size=50,
    ax=ax
)

# Desenhando as arestas
nx.draw_networkx_edges(
    transporte_metropolitano_sp, pos,
    edge_color="black",
    ax=ax
)

# Desenhando os rótulos dos nós (posicionando-os acima dos nós)
pos_labels = {node: (x, y + 0.02) for node, (x, y) in pos.items()}
nx.draw_networkx_labels(
    transporte_metropolitano_sp, pos_labels,
    font_size=5,
    font_weight='bold',
    ax=ax
)

plt.title('Rede Metropolitana de SP - Nós Coloridos', fontsize=18)
plt.show()
