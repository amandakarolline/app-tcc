from app.services.api import Discente, Matricula, Turma, Docente, Componente, GradeComponente


nivelados = []
formandos = []
outros = []


def lista_turmas(matricula):
    id_turmas = []
    componentes = {}
    id_discente = Discente().unico('matricula', matricula)[0]['id']
    for i in Matricula().unico('discente.id', id_discente):
        id_turmas.append(i['turma']['id'])
    for j in id_turmas:
        for k in Turma().unico('id', j):
            componentes[k['componente_curricular']['id']] = [k['componente_curricular']['codigo'],
                                                             k['componente_curricular']['nome'],
                                                             k['docentes'][0]['nome']]
    return componentes


def discentes_turma(id_turma):
    discentes = []
    for i in Matricula().unico('turma.id', id_turma):
        discentes.append(i['discente']['id'])
    return discentes


def cr_discente_id(id_discente):
    indice = Discente().unico('id', id_discente)[0]['indice_academico']
    return indice


def cr_discente_matricula(matricula):
    indice = Discente().unico('matricula', matricula)[0]['indice_academico']
    return indice


def discentes_classificacao(id_discente):
    discente = Discente().unico('id', id_discente)
    discente_dicionario = {'matricula': discente[0]['matricula'],
                           'indice_academico': discente[0]['indice_academico'],
                           'ano_ingresso': discente[0]['ano_ingresso'],
                           'semestre_ingresso': discente[0]['semestre_ingresso'],
                           'status': discente[0]['status'],
                           'id_grade': discente[0]['grade_curricular']['id']}
    return discente_dicionario


def periodo_componente(id_grade, id_componente):
    periodo = GradeComponente().dois_atributos('componente_curricular.id', id_componente,
                                               'grade_curricular.id', id_grade)[0]['periodo']
    return periodo


def classificacao(id_turma):
    id_discentes = discentes_turma(id_turma)
    ano_atual = Turma().unico('id', id_turma)[0]['ano']
    periodo_atual = Turma().unico('id', id_turma)[0]['semestre']
    turma = Turma().unico('id', id_turma)[0]
    for id in id_discentes:
        discente = discentes_classificacao(id)
        periodo_discente = (ano_atual-discente['ano_ingresso']) * 2 + periodo_atual - discente['semestre_ingresso'] + 1
        semestre_turma = periodo_componente(discente['id_grade'], turma['componente_curricular']['id'])
        if discente['status'] == 'FORMANDO':
            formandos.append(discente)
        elif periodo_discente == semestre_turma:
            nivelados.append(discente)
        else:
            outros.append(discente)

    nivelados.sort(key=lambda x: x['indice_academico'], reverse=True)
    formandos.sort(key=lambda x: x['indice_academico'], reverse=True)
    outros.sort(key=lambda x: x['indice_academico'], reverse=True)
    classificados = nivelados + formandos + outros

    return classificados


def posicao(id_turma, matricula):
    id_discentes = discentes_turma(id_turma)
    ano_atual = Turma().unico('id', id_turma)[0]['ano']
    periodo_atual = Turma().unico('id', id_turma)[0]['semestre']
    turma = Turma().unico('id', id_turma)[0]
    for id in id_discentes:
        discente = discentes_classificacao(id)
        periodo_discente = (ano_atual - discente['ano_ingresso']) * 2 + periodo_atual - discente[
            'semestre_ingresso'] + 1
        semestre_turma = periodo_componente(discente['id_grade'], turma['componente_curricular']['id'])
        if discente['status'] == 'FORMANDO':
            if discente['matricula'] == matricula:
                grupo = 'formandos'
            formandos.append(discente)
        elif periodo_discente == semestre_turma:
            if discente['matricula'] == matricula:
                grupo = 'nivelados'
            nivelados.append(discente)
        else:
            if discente['matricula'] == matricula:
                grupo = 'outros'
            outros.append(discente)

    if grupo == 'nivelados':
        nivelados.sort(key=lambda x: x['indice_academico'], reverse=True)
        for i in range(len(nivelados)):
            if nivelados[i]['matricula'] == matricula:
                posicao = i+1
                return posicao
    elif grupo == 'formandos':
        formandos.sort(key=lambda x: x['indice_academico'], reverse=True)
        posicao = len(nivelados)
        for i in range(len(formandos)):
            if formandos[i]['matricula'] == matricula:
                posicao += i+1
                return posicao
    else:
        outros.sort(key=lambda x: x['indice_academico'], reverse=True)
        posicao = len(nivelados) + len(formandos)
        for i in range(len(outros)):
            if outros[i]['matricula'] == matricula:
                posicao += i + 1
                return posicao
