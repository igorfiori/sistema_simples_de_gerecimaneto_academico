import json
# LISTAS ===============================================================================================================
estudantes = []
professores = []
disciplinas = []
turmas = []
matriculas = []
codigo = []

def menu_principal():
    print("Bem-vindo ao menu!")
    print("1. Estudantes")
    print("2. Professores")
    print("3. Disciplinas")
    print("4. Turmas")
    print("5. Matrículas")
    print("0. Sair")

    return input("Digite uma opção válida: ")
def menu_secundario():
    print(f"Menu de operações")
    print("1. Incluir")
    print("2. Listar")
    print("3. Atualizar")
    print("4. Excluir")
    print("0. Voltar ao menu anterior.")

    return input("Digite uma opção válida: ")
# ESTUDANTES ===========================================================================================================
def estudantes_inclusao(lista_etudantes):
    print("====== INCLUSÃO ======")

    codigo = int(input("Digite seu codigo de estudante: "))
    nome = input("Digite o nome: ")
    cpf = input("Digite seu CPF: ")

    dados_estudantes = {
        "codigo": codigo,
        "nome": nome,
        "cpf": cpf
    }
    lista_estudantes = leitura_arquivo("estudantes.json")
    lista_estudantes.append(dados_estudantes)
    salvar_arquivo(lista_estudantes, "estudantes.json")

    return input("Pressione ENTER para continuar.")
def estudantes_listar(lista_estudantes):
    lista_estudantes = leitura_arquivo("estudantes.json")
    if len(lista_estudantes) == 0:
        print("Não há estudantes cadastrados")
        enter = input("Pressione ENTER para continuar.")
    else:
        print("======= LISTAGEM ======")
        for nome in lista_estudantes:
            print(f"Estudante: {nome}")

        return input("Pressione ENTER para continuar.")
def estudantes_atualizar(codigo, lista_etudantes):
    lista_estudantes = leitura_arquivo("estudantes.json")
    codigo_para_editar = int(input("Qual é codigo que deseja editar? "))

    codigo_para_ser_editado = None
    for estudantes in lista_estudantes:
        if estudantes["codigo"] == codigo_para_editar:
            estudantes["nome"] = input("Digite o novo nome: ")
            estudantes["cpf"] = input("Digite o novo CPF: ")
            salvar_arquivo(lista_estudantes, "estudantes.json")
            return input("Pressione ENTER para continuar.")

    print(f"Olha não encontrei o estudante de código {codigo_para_editar} na lista.")
def estudantes_excluir(codigo, lista_etudantes):
    lista_estudantes = leitura_arquivo("estudantes.json")
    codigo_para_remover = int(input("Qual é codigo que deseja remover: "))

    codigo_para_ser_removido = None
    for dados_estudantes in lista_estudantes:
        if dados_estudantes["codigo"] == codigo_para_remover:
            codigo_para_ser_removido = dados_estudantes
            break

    if codigo_para_ser_removido is None:
        print(f"Olha não encontrei o estudante de código {codigo_para_remover} na lista.")
    else:
        lista_estudantes.remove(codigo_para_ser_removido)
        salvar_arquivo(lista_estudantes, "estudantes.json")
        print("Estudante removido.")

    print(dados_estudantes)

    return input("Pressione ENTER para continuar.")
# JSON SALVAR ESTUDANTES ===============================================================================================
def salvar_arquivo(lista_estudantes, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo_aberto:
        json.dump(lista_estudantes, arquivo_aberto)
# JSON LEITURA ESTUDANTES ==============================================================================================
def leitura_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo_aberto:
            lista_estudantes = json.load(arquivo_aberto)

        return lista_estudantes
    except:
        return []
# PROFESSOR ============================================================================================================
def professores_inclusao(lista_professores):
    print("====== INCLUSÃO ======")

    codigo = int(input("Digite seu codigo: "))
    nome = input("Digite o nome: ")
    cpf = input("Digite seu CPF: ")

    dados_professores = {
        "codigo": codigo,
        "nome": nome,
        "cpf": cpf
    }
    lista_professores = leitura_arquivo("professores.json")
    lista_professores.append(dados_professores)
    salvar_arquivo(lista_professores, "professores.json")

    return input("Pressione ENTER para continuar.")
def professores_listar(lista_professores):
    lista_professores = leitura_arquivo("professores.json")
    if len(lista_professores) == 0:
        print("Não há professores cadastrados")
        enter = input("Pressione ENTER para continuar.")
    else:
        print("======= LISTAGEM ======")
        for nome_professor in lista_professores:
            print(f"Professor(a): {nome_professor}")

        return input("Pressione ENTER para continuar.")
def professores_atualizar(codigo, lista_professores):
    lista_professores = leitura_arquivo("professores.json")
    codigo_para_editar_professores = int(input("Qual é codigo que deseja editar? "))

    codigo_para_ser_editado_professores = None
    for professores in lista_professores:
        if professores["codigo"] == codigo_para_editar_professores:
            professores["nome"] = input("Digite o novo nome: ")
            professores["cpf"] = input("Digite o novo CPF: ")
            salvar_arquivo(lista_professores, "professores.json")
            return input("Pressione ENTER para continuar.")

    print(f"Olha não encontrei o professor de código {codigo_para_editar_professores} na lista.")
def professores_excluir(codigo, lista_professores):
    lista_professores = leitura_arquivo("professores.json")
    codigo_para_remover_professores = int(input("Qual é codigo que deseja remover: "))

    codigo_para_ser_removido_professores = None
    for dados_professores in lista_professores:
        if dados_professores["codigo"] == codigo_para_remover_professores:
            codigo_para_ser_removido_professores = dados_professores
            break

    if codigo_para_ser_removido_professores is None:
        print(f"Olha não encontrei o estudante de código {codigo_para_remover_professores} na lista.")
    else:
        lista_professores.remove(codigo_para_ser_removido_professores)
        salvar_arquivo(lista_professores, "professores.json")
        print("Professor(a) removido.")

    print(dados_professores)

    return input("Pressione ENTER para continuar.")
# JSON SALVAR DISCIPLINAS ==============================================================================================
def salvar_arquivo(lista_professores, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo_aberto:
        json.dump(lista_professores, arquivo_aberto)
# JSON LEITURA PROFESSORES =============================================================================================
def leitura_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo_aberto:
            lista_professores = json.load(arquivo_aberto)

        return lista_professores
    except:
        return []

# DISCIPLINAS ==========================================================================================================
def disciplinas_inclusao(lista_disciplinas):
    print("====== INCLUSÃO ======")

    codigo_disciplina = int(input("Digite seu codigo da disciplina: "))
    nome_disciplina = input("Digite o nome da disciplina: ")

    dados_disciplinas = {
        "codigo": codigo_disciplina,
        "nome": nome_disciplina
    }
    lista_disciplinas = leitura_arquivo("disciplinas.json")
    lista_disciplinas.append(dados_disciplinas)
    salvar_arquivo(lista_disciplinas, "disciplinas.json")

    return input("Pressione ENTER para continuar.")

def disciplinas_listar(lista_disciplinas):
    lista_disciplinas = leitura_arquivo("disciplinas.json")
    if len(lista_disciplinas) == 0:
        print("Não há disciplinas cadastradas")
        enter = input("Pressione ENTER para continuar.")
    else:
        print("======= LISTAGEM ======")
        for nome_disciplinas in lista_disciplinas:
            print(f"Professor(a): {nome_disciplinas}")

        return input("Pressione ENTER para continuar.")

def disciplinas_atualizar(codigo, lista_disciplinas):
    lista_disciplinas = leitura_arquivo("disciplinas.json")
    codigo_para_editar_disciplinas = int(input("Qual é codigo que deseja editar? "))

    codigo_para_ser_editado_disciplinas = None
    for disciplinas in lista_disciplinas:
        if disciplinas["codigo"] == codigo_para_editar_disciplinas:
            disciplinas["nome"] = input("Digite o novo nome da disciplina: ")
            salvar_arquivo(lista_disciplinas, "disciplinas.json")
            return input("Pressione ENTER para continuar.")

    print(f"Olha não encontrei a disciplina de código {codigo_para_editar_disciplinas} na lista.")

def disciplinas_excluir(codigo, lista_disciplinas):
    lista_disciplinas = leitura_arquivo("disciplinas.json")
    codigo_para_remover_disciplinas = int(input("Qual é codigo que deseja remover: "))

    codigo_para_ser_removido_disciplinas = None
    for dados_disciplinas in lista_disciplinas:
        if dados_disciplinas["codigo"] == codigo_para_remover_disciplinas:
            codigo_para_ser_removido_disciplinas = dados_disciplinas
            break

    if codigo_para_ser_removido_disciplinas is None:
        print(f"Olha não encontrei a disciplina de código {codigo_para_remover_disciplinas} na lista.")
    else:
        lista_disciplinas.remove(codigo_para_ser_removido_disciplinas)
        salvar_arquivo(lista_disciplinas, "disciplinas.json")
        print("Disciplina removida.")

    print(dados_disciplinas)

    return input("Pressione ENTER para continuar.")
# JSON SALVAR DISCIPLINAS ==============================================================================================
def salvar_arquivo(lista_disciplinas, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo_aberto:
        json.dump(lista_disciplinas, arquivo_aberto)
# JSON LEITURA DISCIPLINAS =============================================================================================
def leitura_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo_aberto:
            lista_disciplinas = json.load(arquivo_aberto)

        return lista_disciplinas
    except:
        return []
# TURMAS ===============================================================================================================
def turmas_inclusao(lista_turmas):
    print("====== INCLUSÃO ======")

    codigo_turma = int(input("Digite seu codigo de turma: "))
    codigo_professor = int(input("Digite seu codigo do professor(a) : "))
    codigo_disciplina = int(input("Digite seu codigo da disciplina: "))

    dados_turmas = {
        "codigo turma": codigo_turma,
        "codigo professor(a)": codigo_professor,
        "codigo disciplina": codigo_disciplina
    }
    lista_turmas = leitura_arquivo("turmas.json")
    lista_turmas.append(dados_turmas)
    salvar_arquivo(lista_turmas, "turmas.json")

    return input("Pressione ENTER para continuar.")
def turmas_listar(lista_turmas):
    lista_turmas = leitura_arquivo("turmas.json")
    if len(lista_turmas) == 0:
        print("Não há turmas cadastradas")
        enter = input("Pressione ENTER para continuar.")
    else:
        print("======= LISTAGEM ======")
        for codigo_turmas in lista_turmas:
            print(f"Turmas: {codigo_turmas}")

        return input("Pressione ENTER para continuar.")
def turmas_atualizar(codigo, lista_turmas):
    lista_turmas = leitura_arquivo("turmas.json")
    codigo_para_editar_turmas = int(input("Qual é codigo de turmas que deseja editar? "))

    codigo_para_ser_editado_turmas = None
    for turmas in lista_turmas:
        if turmas["codigo turma"] == codigo_para_editar_turmas:
            turmas["codigo turma"] = int(input("Digite o novo codigo da turma: "))
            salvar_arquivo(lista_turmas, "turmas.json")
            return input("Pressione ENTER para continuar.")

    print(f"Olha não encontrei a turma de código {codigo_para_editar_turmas} na lista.")
def turmas_excluir(codigo, lista_turmas):
    lista_turmas = leitura_arquivo("turmas.json")
    codigo_para_remover_turmas = int(input("Qual é codigo que deseja remover: "))

    codigo_para_ser_removido_turmas = None
    for dados_turmas in lista_turmas:
        if dados_turmas["codigo turma"] == codigo_para_remover_turmas:
            codigo_para_ser_removido_turmas = dados_turmas
            break

    if codigo_para_ser_removido_turmas is None:
        print(f"Olha não encontrei a turma de código {codigo_para_remover_turmas} na lista.")
    else:
        lista_turmas.remove(codigo_para_ser_removido_turmas)
        salvar_arquivo(lista_turmas, "turmas.json")
        print("Turma removida.")

    print(dados_turmas)

    return input("Pressione ENTER para continuar.")
# JSON SALVAR TURMAS ===================================================================================================
def salvar_arquivo(lista_turmas, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo_aberto:
        json.dump(lista_turmas, arquivo_aberto)
# JSON LEITURA TURMAS ==================================================================================================
def leitura_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo_aberto:
            lista_turmas = json.load(arquivo_aberto)

        return lista_turmas
    except:
        return []
# MATRICULAS ===========================================================================================================
def matriculas_inclusao(lista_matriculas):
    print("====== INCLUSÃO ======")

    codigo_matriculas = int(input("Digite seu codigo de turma: "))
    codigo_disciplina = int(input("Digite seu codigo da disciplina: "))

    dados_matriculas = {
        "codigo": codigo_matriculas,
        "codigo disciplina": codigo_disciplina
    }
    lista_matriculas = leitura_arquivo("matriculas.json")
    lista_matriculas.append(dados_matriculas)
    salvar_arquivo(lista_matriculas, "matriculas.json")

    return input("Pressione ENTER para continuar.")
def matriculas_listar(lista_matriculas):
    lista_matriculas = leitura_arquivo("matriculas.json")
    if len(lista_matriculas) == 0:
        print("Não há matriculas cadastradas")
        enter = input("Pressione ENTER para continuar.")
    else:
        print("======= LISTAGEM ======")
        for codigo_matriculas in lista_matriculas:
            print(f"Matrícula: {codigo_matriculas}")

        return input("Pressione ENTER para continuar.")
def matriculas_atualizar(codigo, lista_matriculas):
    lista_matriculas = leitura_arquivo("matriculas.json")
    codigo_para_editar_matriculas = int(input("Qual é codigo de matrícula que deseja editar? "))

    codigo_para_ser_editado_matriculas = None
    for matriculas in lista_matriculas:
        if matriculas["codigo"] == codigo_para_editar_matriculas:
            matriculas["codigo"] = int(input("Digite o novo codigo de matrícula: "))
            salvar_arquivo(lista_matriculas, "matriculas.json")
            return input("Pressione ENTER para continuar.")

    print(f"Olha não encontrei matrícula de código {codigo_para_editar_matriculas} na lista.")
def matriculas_excluir(codigo, lista_matriculas):
    lista_matriculas = leitura_arquivo("matriculas.json")
    codigo_para_remover_matriculas = int(input("Qual é codigo de matrícula que deseja remover: "))

    codigo_para_ser_removido_matriculas = None
    for dados_matriculas in lista_matriculas:
        if dados_matriculas["codigo"] == codigo_para_remover_matriculas:
            codigo_para_ser_removido_matriculas = dados_matriculas
            break

    if codigo_para_ser_removido_matriculas is None:
        print(f"Olha não encontrei a matrícula de código {codigo_para_remover_matriculas} na lista.")
    else:
        lista_matriculas.remove(codigo_para_ser_removido_matriculas)
        salvar_arquivo(lista_matriculas, "matriculas.json")
        print("Matrícula removida.")

    print(dados_matriculas)

    return input("Pressione ENTER para continuar.")

# JSON SALVAR MATRICULAS ===============================================================================================
def salvar_arquivo(lista_matriculas, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo_aberto:
        json.dump(lista_matriculas, arquivo_aberto)
# JSON LEITURA MATRICULA ===============================================================================================
def leitura_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r') as arquivo_aberto:
            lista_matriculas = json.load(arquivo_aberto)

        return lista_matriculas
    except:
        return []
# MENU PRINCIPAL =======================================================================================================
while True:

    opcao = menu_principal()

    print(f"Você escolheu a opção {opcao}. ")

    if opcao == "1" or opcao == "2" or opcao == "3" or opcao == "4" or opcao == "5":

# MENU SECUNDARIO OPÇÕES & CUMPRIMENTOS ================================================================================

        if opcao == "1":
            print("Olá Estudante!")

            while True:
                opcao_secundaria = menu_secundario()
                print(f"Você escolheu a opção {opcao_secundaria}. ")

                if opcao_secundaria == "1":
                    estudantes_inclusao(estudantes)
                elif opcao_secundaria == "2":
                    estudantes_listar(estudantes)
                elif opcao_secundaria == "3":
                    estudantes_atualizar(codigo, estudantes)
                elif opcao_secundaria == "4":
                    estudantes_excluir(codigo, estudantes)
                elif opcao_secundaria == "0":
                    break

        elif opcao == "2":
            print("Olá Professor!")

            while True:
                opcao_secundaria = menu_secundario()
                print(f"Você escolheu a opção {opcao_secundaria}. ")

                if opcao_secundaria == "1":
                    professores_inclusao(professores)
                elif opcao_secundaria == "2":
                    professores_listar(professores)
                elif opcao_secundaria == "3":
                    professores_atualizar(codigo, professores)
                elif opcao_secundaria == "4":
                    professores_excluir(codigo, professores)
                elif opcao_secundaria == "0":
                    break

        elif opcao == "3":
            print("Bem-vindo a Disciplinas")

            while True:
                opcao_secundaria = menu_secundario()
                print(f"Você escolheu a opção {opcao_secundaria}. ")

                if opcao_secundaria == "1":
                    disciplinas_inclusao(disciplinas)
                elif opcao_secundaria == "2":
                    disciplinas_listar(disciplinas)
                elif opcao_secundaria == "3":
                    disciplinas_atualizar(codigo, disciplinas)
                elif opcao_secundaria == "4":
                    disciplinas_excluir(codigo, disciplinas)
                elif opcao_secundaria == "0":
                    break

        elif opcao == "4":
            print("Bem- vindo a turmas")

            while True:
                opcao_secundaria = menu_secundario()
                print(f"Você escolheu a opção {opcao_secundaria}. ")

                if opcao_secundaria == "1":
                    turmas_inclusao(turmas)
                elif opcao_secundaria == "2":
                    turmas_listar(turmas)
                elif opcao_secundaria == "3":
                    turmas_atualizar(codigo, turmas)
                elif opcao_secundaria == "4":
                    turmas_excluir(codigo, turmas)
                elif opcao_secundaria == "0":
                    break

        elif opcao == "5":
            print("Bem-vindo a matriculas")
            while True:
                opcao_secundaria = menu_secundario()
                print(f"Você escolheu a opção {opcao_secundaria}. ")

                if opcao_secundaria == "1":
                    matriculas_inclusao(matriculas)
                elif opcao_secundaria == "2":
                    matriculas_listar(matriculas)
                elif opcao_secundaria == "3":
                    matriculas_atualizar(codigo, matriculas)
                elif opcao_secundaria == "4":
                    matriculas_excluir(codigo, matriculas)
                elif opcao_secundaria == "0":
                    break

    elif opcao == "0":
        print("Desconectado.")
        break
    else:
        print("Essa opção é INVÁLIDA.")
