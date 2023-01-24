import kanboard, os

kban = {'USER':os.environ["user_kanboard"],
            'TOKEN':os.environ["token_kanboard"],
            'URL': os.environ["url_kanboard"]} 

USER = kban['USER']
TOKEN = kban['TOKEN']
URL = kban['URL']
KB = kanboard.Client(url=URL, username=USER, password=TOKEN)


def pegaIdProjetos():
    """Retorna uma lista de dicionários onde a chave é o projeto e o ID é o valor"""
    projetos = []
    resultado = KB.getAllProjects()

    for projeto in resultado:
        temp = {}
        temp[projeto["name"]] = projeto["id"]
        projetos.append(temp)
    return projetos


def adcionaUsuario():
    projetos = pegaIdProjetos()
    for projeto in projetos:
        for chave in projeto.keys():
            resutado = KB.addProjectUser(project_id=projeto[chave], user_id=441, role="project-viewer")
            if resutado:
                print(f"Usuário adicionado no projeto {chave} que tem o ID {projeto[chave]}")
            else:
                print(f"Usuário não adicionado no projeto {chave} Favor verificar")


def removeUsuario():
    projetos = pegaIdProjetos()
    for projeto in projetos:
        for chave in projeto.keys():
            resutado = KB.removeProjectUser(project_id=projeto[chave], user_id=92)
            if resutado:
                print(f"Usuário removido do projeto {chave} que tem o ID {projeto[chave]}")
            else:
                print(f"Usuário não foi removido do projeto {chave} Favor verificar")


# print(KB.removeProjectUser(project_id=143, user_id=92))
print(pegaIdProjetos())
#adcionaUsuario()
#removeUsuario()
