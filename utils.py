import json


def get_candidates(path):
    """Загружает вопросы из файла JSON"""
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def format_candidates(candidat_raw):
    result = '<pre>'
    for i in candidat_raw:
        result += (
            f'Имя кандидата - {i["name"]}\n'
            f'Позиция кандидата {i["id"]}\n'
            f'Позиция кандидата {i["skills"]}\n\n'
        )
    result += '<pre>'
    return result


def get_candidate_id(candidat_raw, candidate_id):
    for i in candidat_raw:
        if i['id'] == candidate_id:
            return i


def get_candidates_skills(candidat_raw, candidate_skill):
    result = []
    for i in candidat_raw:
        candidat_skill = i['skills'].lower().split(', ')
        if candidate_skill.lower() in candidat_skill:
            result.append(i)
    return result
