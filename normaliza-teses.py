# Preparação do arquivo e instruções:
# - Com auxílio do calc, filtrei por valores distintos para saber quais não correspondiam e precisavam ser substituídos.
# - Executar o script usando python3 nome_do_arquivo.py

# Importa o Panda
import pandas as pd

# Atribui para a variavel teses o csv (o arquivo tem que estar na mesma pasta que o script for executado)
teses = pd.read_csv('teses.csv')


## Seleciona o campo e faz o replace do(s) primeiro argumento(s) pelo segundo.

# Graus: Doutorado, Mestrado e Livre-docência.
teses["field_grau_arthur"] = teses["field_grau_arthur"].replace(["DOUTORADO", "doutorado", "Doutoramento", "doutoramento", "DOUTORADo", "DOUTIRADO", "Doutoradoq", "Doutor", "doutor", "DUTORADO", "DOYTORADO", "Doutorada", "DOURADO", "Doutoraado", "Doutrorado", "Doutoado", "doutora"], "Doutorado")

teses["field_grau_arthur"] = teses["field_grau_arthur"].replace(["mestrado", "MESTRADO", "MESTRADOMESTRADO", "Mestrada", "M estrado", "Mestardo", "MSTRADO",  "MESTRDO", "MESTRADo", "MESTRDO", "MestradoMestrado", "MESTARDO", "MESTRARDO", "Mestre", "MSETRADO", "METRADO", "Metrado" ], "Mestrado")

teses["field_grau_arthur"] = teses["field_grau_arthur"].replace(["Livre-Docência", "livre-docência", "Livre Docência", "Livre -docencia", "LIVRE DOCENTE", "Livre-docência", "Livre Docencia", "Livre docência", "Livre-Docênacia", "Livre-Docencia", "Livre-Docente", '"livre Docente"', "LIVRE DOCENCIA", "Livre--docência"], "Livre-docência")

teses["field_grau_arthur"] = teses["field_grau_arthur"].replace(["Cátedra", "Titular", "m", "-------------------------", "Relatorio final", "d", "FLORENZANO, Maria", "Educação", "História", "DLM", "e de seus antecedentes", "-----------", "Cadeira", "---------------------------", "Schmidt", ""], "NA")

# Departamentos: Antropologia, Sociologia, Ciência Política, Letras Clássicas e Vernáculas, Filosofia, Geografia, História, Linguística, Teoria Literária e Literatura Comparada, Letras Orientais e Letras Modernas.
teses["field_departamento_arthur"] = teses["field_departamento_arthur"].replace(["Antopologia", "ANTROPOLOGIA", "antropologia", "Antropologia Social", "Antropologiua", "DA"], "Antropologia")


teses["field_departamento_arthur"] = teses["field_departamento_arthur"].replace(["Ciências Sociais", "Ciências Sociais e Letras", "DS", "Pós garduação Socilogia", "SOCIOLOGIA", "Ciêcias Sociais"], "Sociologia")


teses["field_departamento_arthur"] = teses["field_departamento_arthur"].replace(["CIENCIA POLITICA", "Ciencia Política", "Ciência Politica", "Ciencia Politttica", "Ciências", "Ciências Política", "Ciências Políticas", "Cioencia Politica", "CP", "DCP", "DCS", "Depto. Ciência Política", "Ciencia Politica"], "Ciência Política")


teses["field_departamento_arthur"] = teses["field_departamento_arthur"].replace(["Classicas e vernaculas", "classicas Vernaculas", "Departamento de Letras Clássicas e Vernáculas", "DLC", "DLCV", "DTLCV", "Estudos Comparados de Literaturas de Língua Portuguesa", "Filologia e Língua Portuguesa", "Filologia e lingua pportuguesa", "Letras", "LETRAS", "letras", "Letras Classicas", "Letras Clássicas e Vernáculas e Vernáculas", "Letras Clássicas e Vernáculass", "Língua, Literatura e Cultura e Italianas", "Letras (clássicas e vernáculas)"], "Letras Clássicas e Vernáculas")


teses["field_departamento_arthur"] = teses["field_departamento_arthur"].replace(["D.F", "DF", "FILOSIFIA", "FIlosofia", "FILOSOFIA", "FILOZOFIA"], "Filosofia")


teses["field_departamento_arthur"] = teses["field_departamento_arthur"].replace(["D.G", "DG", "GEOGRAFIA", "geografia", "Geografia Física", "Geografia Humana", "Instituto de Geografia"], "Geografia")


teses["field_departamento_arthur"] = teses["field_departamento_arthur"].replace(["DH","HISTORIA", "Historia", "história", "Hístoria", "História e Cultura", "Hístoria Econômica", "Historia Social", "Hístoria Social", "Núcleo de Estudos das Diversidades, Intolerâncias e Conflitos"], "História")


teses["field_departamento_arthur"] = teses["field_departamento_arthur"].replace(["D.Linguística", "DL","dl", "inguística", "Linguistica", "LINGUISTICA", "Lingüística", "Linguística e Literários em Inglês", "Linguistica Geral", "Semiótica e Linguística Geral", "Semiotica Linguistica"], "Linguística")


teses["field_departamento_arthur"] = teses["field_departamento_arthur"].replace(["DTLL", "DTLLC", "Teoria Literaria", "Teoria Literária", "Teoria Literaria e Literatura Comparada", "Teoria Litéraria e Literatura Comparada", "Teoria Literária e Literaura Comparada", "TLLC"], "Teoria Literária e Literatura Comparada")


teses["field_departamento_arthur"] = teses["field_departamento_arthur"].replace(["DLO", "FLO", "LETRAS ORIENTAIS", "Lingua Orientais", "Línguas Orientais", "Literatura e cultura Russa", "Letras (Orientais)"], "Letras Orientais")


teses["field_departamento_arthur"] = teses["field_departamento_arthur"].replace(["DLM", "Francês", "Letras Moderna", "Letras Modernass", "Lingua Espanhola", "Línguas Modernas", "Línguas modernas", "LM", "Letras (Modernas)"], "Letras Modernas")


teses["field_departamento_arthur"] = teses["field_departamento_arthur"].replace(["________", "_________", "-", "-----", "-----------", "-------------", "----------------", "-----------------", "---------------------", "------------------------------", "-----------------------------------", "Univ. de Paris", "USP-Rio Preto", "FE-USP", "Instituto de Geociências", "UFMG", "Instituto Caro y Cuervo", "Campus de Assis", "Faculdades Candido Mendes", "Universidade de Brasília", "UNESP-Marília", "Instituto de Geografia Uberlândia", "Université de Paris-Sorbonne", "Iniversité Provence", "Univ. Federal do Pará", "FLH", "faculté des lettres et Sciences Humaines", "Não Consta", "UFBA", "Universidade Federal Pernambuco", "Univ. federal de Uberlândia", "UFGRS", "PUC/SP", "Universitat Autònoma de Barcelona", "FFCL-Assis", "UFRJ/UFJF", "FFLCH-Franca", "Economia", "Faculdade Saúde Pública", "Univ. Fed. do Pará", "Univ. Federal de Mato Grosso", "Instituto Caetano de Campos", "Fundação Universidade de Brasília", "Centro de Ciências Jurídicas e Econômicas", "Universidade de Lisboa", "ECA", "Universidade Estadual Paulista", "L'Ecole des Hautes Etudes em Sciences Sociales", "Univ. Federal de Uberlândia", "University of Chicago", "Universidade de Toulouse le Mirail", "Univ. Federal Paulista", "IP -USP", "Unesp", "Universidade do Vale di Rio do Sinos", "Direito Internacional", "Universidad Nacional Autonoma de Honduras", "FFCL/Araraquara", "Universidade Federal do Paraná", "Universidade Federal de Minas Gerais", "Faculdade de Teologia Nossa Senhora da Assunção", "Uinversidade de Brasilia", "Universidade Federal de Santa Catarina", "UFCE", "Universidade Católica de Goiás", "UF de Santa Maria", "UFPE", "FFCL- Araraquara", "ECA-USP", "FFCL-Araraquara", "IP-USP", "LUIZ DE QUEIROZ-USP", "Universidade Federal paulista Júlio de Mesquita", "Universite de Paris", "Instituto de Estudos da Linguagem", "Univ. de Brasília", "Univ. federal de Santa catarina", "Comunicação Social", "Univ.de Brasília", "Universidade do Brasil-RJ", "Univ. Federal de Pernambuco", "Escola de Sociologia e Política-SP", "Psicologia", "FAUUSP", "UFRJ", "Universidade Federal do Espírito Santo", "Universidade Estadual Júlio de Mesquita F.", "Universidade Estadual de Maringá", "Zoologia", "UFSM", "PUC/RGS", "UNESP", "Universidade Federal de Pernambuco", "Universite de Paris X", "Universidade Federal de Santa Maria", "Universidade Federal Paulista Júlio de Mesquita", "Katholieke Universiteit te Leuven", "universidade Federal do Rio Grande do Norte", "Universidade do Estado do Rio de Janeiro", "Univ. Federal do Rio Grande do Sul", "FFCL-Presidente Prudente", "Instituto Sedes Sapientiae", "FFCLC-USP", "PUCSP", "FFLCH-Araraquara", "Univ. Federal da Paraíba", "Universidade Federal Paulista", "Universdidade Federal Fluminense", "FALE/UFMG", "Universidade Federal da Bahia", "USP-IP", "PUC/RS", "UFSM/SC", "USP-IP", "PUC/RS", "UFSM/SC","Universidade Federal de Pernanbuco", "Universidade Est. Do Rio de Janeiro", "Universidade de Presidente Prudente", "Museu de Arquiologia", "Universidade Federal de Brasília", "FFCL-ASSIS","Univ. Federal de São Carlos", "DO", "FFCL-Franca", "PUC-SP", "Universidade de Barsília", "ECA -USP", "Univ. de Chicago", "Doutorado", "Univ. Federal do Ceará", "MAE - Arqueologia", "Universidade estadual Paulista", "Universidade Federal de Viçosa", "UNESP-ASSIS", "UFSC", "Universidade Esatdual Paulista Júlio de Mesquita", "Universidade Vale dos Sinos", "UFRGS", "UFRS", "História- UNESP", "Universidade Estadual Paulista Júlio de Mesquita", "FM-USP", "UNESP/ASSIS", "USP", "Univ. Estadual Paulista", "Universidade Federal Rural do Rio de Janeiro", "Universidade Federal do Rio de Janeiro", "UFPB", "UFMGrosso", "Universite De L'etat a Anvers", "FAU-USP", "Universidade São Marcos", "Univ. Federal do Paraná", "Depto. Educação", "PUC-RS", "PUC", "CAMPUS FRANCA", "FFCL-Rio Claro", "ECA/USP", "UNESP- Marília", "Mackenzie", "Universidade Federal Fluminense", "PUC/Minas", "UNICAMP", "FEA-USP", "Institut des Hautes Etudes deI'Amérique Latine", "Fundação Getúlio Vargas", "DLS", "DP", "Escola Superior Luiz de Queiroz", "Comunicação e Letras", "FAU/USP", "Universidade Federal do Ceará", "FFCL-USP", "USP-ECA","FFCL - SJRP", "UFF", "UFB", "Unicamp", "USP-Assis", "Universidade Federal do Rio Grande do Sul", "Universidade Federal de Goiás", "PUC/RJ", "PUS-RS", "Geociências-USP", "UMESP", "URJ", "Universidade de Minas Gerais", "MAE", "PUS-RS", "Geociências-USP", "UMESP", "URJ", "Universidade de Minas Gerais", "MAE", "PUS-RS", "Geociências-USP", "UMESP", "URJ", "Universidade de Minas Gerais", "MAE", "PUS-RS", "Geociências-USP", "UMESP", "URJ", "Universidade de Minas Gerais", "MAE", "DGF", "Centro de Ciências Sociais e Humanas", "DGF", "Filosofia,Letras e ciências Humanas", "Univ. Est. Paulista Júlio de Mesquita Filho","Instituto de Ciências Humanas e Filosofia", "LCV", "LLP", "DEL", "Universidade Federal da Paraíba", "FE", "Universidade Metodista de Piracicaba", "Artes/ECA/USP", "IPEN", "Artes/ECA/USP", "IPEN", "Artes/ECA/USP", "IPEN", "UFP", "UFP", "Universidade Estadual Paulista Rio Claro", "Instituto Universitário Europeu", "Instituto Universitário Europeu", "Instituto Universitário Europeu", "IUPERJ", "UERJ", "Educação", "Fundação Escola de Sociologia e Política", "DH/UNESP", "Filosofia,Letras  e ciências Humanas", "Física", "Fundação Escola Sociologia e Política", "Fundação Escola Sociologia e Política", "Fundação Escola Sociologia e Política", "Geologia", "Fundação Escola de Sociologia e Política de SP", "UFPe", "FFCL", "Universidade Federal do Pará", "Comunicação e Semiótica", "Universidade de Brasilia", "Centro de Ciências Humanas", "DCV"], "NA")

# Caso queira, retire o comentário para a impressão dos valores únicos após as substituições.
# print(set(teses['grau']))
# print(set(teses['departamento']))

# Arquivo gerado após as substituições.
teses.to_csv('teses-normalizado.csv')
			
			
