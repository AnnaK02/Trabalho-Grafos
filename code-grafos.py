import networkx as nx
import matplotlib.pyplot as plt

# Leitura da base de dados

G = nx.read_edgelist('/Users/admin/Desktop/trabGrafos/terrorists/terrorists.net')

# Renomeação dos nós

mapping = {
    '0': "Mohamed Atta",
    '1': "Abdul Aziz Al-Omari",
    '2': "Ziad Jarrah",
    '3': "Ramzi Omar",
    '4': "Said Bahaji",
    '5': "Zacariya Essabar",
    '6': "Marwan Al-Shehhi",
    '7': "Shaykh Saiid",
    '8': "Mamoun Darkazanli",
    '9': "Mamduh MahMud Salim",
    '10': "Waleed Alshehri",
    '11': "Wail Alshehri",
    '12': "Satam Suqami",
    '13': "Fayez Banihammad",
    '14': "Mohand Alshehri",
    '15': "Raed Hijazi",
    '16': "Nabil al-Marabh",
    '17': "Saeed Alghamdi",
    '18': "Ahmed Al Haznawi",
    '19': "Hamza Alghamdi",
    '20': "Ahmed Alghamdi",
    '21': "Salem Alhazmi",
    '22': "Nawaf Alhazmi",
    '23': "Ahmed Alnami",
    '24': "Mohamed Abdi",
    '25': "Osama Awadallah",
    '26': "Abdussattar Shaikh",
    '27': "Khalid Almihdhar",
    '28': "Majed Moqed",
    '29': "Hani Hanjour",
    '30': "Rayed Mohammed Abdullah",
    '31': "Faisal Al Salmi",
    '32': "Lofti Raissi",
    '33': "Habib Zacarias Moussaoui"
}

G = nx.relabel_nodes(G, mapping)


# Aparência do grafo

options = {
    "font_size": 3,
    "node_size": 1300,
    "node_color": "white",
    "edgecolors": "black",
    "linewidths": 0.5,
    "width": 1,
}

# Impressão

nx.draw_networkx(G, **options)
plt.show()
