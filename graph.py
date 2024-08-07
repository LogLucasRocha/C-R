import networkx as nx
import matplotlib.pyplot as plt

transporte_metropolitano_sp = nx.Graph()

corredor_sao_mateus_jabaquara = [
    "São Mateus", "Sônia Maria", "Santo André", "São Bernardo", "Ferrazópolis", "Piraporinha", "Diadema", "Jabaquara", "Brooklin", "Morumbi", "Berrini"
] 

linha_1_azul = [
    "Jabaquara", "Conceição", "Saúde", "São Judas", "Praça da Árvore", "Santa Cruz", "Vila Mariana", "Ana Rosa", "Paraíso", "Vergueiro", "São Joaquim", "Se", "São Bento", "Luz", "Tiradentes", "Armênia", "Portuguesa-Tietê", "Carandiru", "Santana", "Jardim São Paulo-Ayrton Senna", "Parada Inglesa", "Tucuruvi"
]

transporte_metropolitano_sp.add_nodes_from(corredor_sao_mateus_jabaquara)
transporte_metropolitano_sp.add_nodes_from(linha_1_azul)

edges = [
    # Linha 1 - Azul
    ("Jabaquara", "Conceição"), ("Conceição", "Saúde"),
    ("Saúde", "São Judas"), ("São Judas", "Praça da Árvore"),
    ("Praça da Árvore", "Santa Cruz"), ("Santa Cruz", "Vila Mariana"),
    ("Vila Mariana", "Ana Rosa"), ("Ana Rosa", "Paraíso"),
    ("Paraíso", "Vergueiro"), ("Vergueiro", "São Joaquim"),
    ("São Joaquim", "Se"), ("Se", "São Bento"),
    ("São Bento", "Luz"), ("Luz", "Tiradentes"),
    ("Tiradentes", "Armênia"), ("Armênia", "Portuguesa-Tietê"),
    ("Portuguesa-Tietê", "Carandiru"), ("Carandiru", "Santana"),
    ("Santana", "Jardim São Paulo-Ayrton Senna"), ("Jardim São Paulo-Ayrton Senna", "Parada Inglesa"),
    ("Parada Inglesa", "Tucuruvi"),

    # Corredor São Mateus - Jabaquara
    ("São Mateus", "Sônia Maria"), ("Sônia Maria", "Santo André"),
    ("Santo André", "São Bernardo"), ("São Bernardo", "Ferrazópolis"),
    ("São Bernardo", "Piraporinha"), ("Piraporinha", "Diadema"),
    ("Diadema", "Jabaquara"), ("Diadema", "Brooklin"),
    ("Brooklin", "Morumbi"), ("Morumbi", "Berrini")
]
transporte_metropolitano_sp.add_edges_from(edges)

pos = {
    "Jabaquara": (0, 0), "Conceição": (0, -1),
    "Saúde": (0, -2), "São Judas": (0, -3),
    "Praça da Árvore": (0, -4), "Santa Cruz": (0, -5),
    "Vila Mariana": (0, -6), "Ana Rosa": (0, -7),
    "Paraíso": (0, -8), "Vergueiro": (0, -9),
    "São Joaquim": (0, -10), "Se": (0, -11),
    "São Bento": (0, -12), "Luz": (0, -13),
    "Tiradentes": (0, -14), "Armênia": (0, -15),
    "Portuguesa-Tietê": (0, -16), "Carandiru": (0, -17),
    "Santana": (0, -18), "Jardim São Paulo-Ayrton Senna": (0, -19),
    "Parada Inglesa": (0, -20), "Tucuruvi": (0, -21),
    "São Mateus": (1, 0), "Sônia Maria": (1, -1),
    "Santo André": (1, -2), "São Bernardo": (4, 2),
    "Ferrazópolis": (4, 4), "Piraporinha": (2, 2),
    "Diadema": (0, 2), "Brooklin": (1, -7),
    "Morumbi": (1, -8), "Berrini": (1, -9)
}


fig, ax = plt.subplots(figsize=(14, 12))

nx.draw(
    transporte_metropolitano_sp, pos,
    with_labels=False,
    node_size=0,
    edge_color='gray',
    ax=ax,
)

for node, (x, y) in pos.items():
    ax.text(x, y, node, fontsize=8, ha='center', va='center', fontweight='bold', color='black')

ax.axis('off')

plt.title('Rede Metropolitana de SP', fontsize=16)
plt.show()
