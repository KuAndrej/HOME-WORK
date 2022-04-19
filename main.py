from flask import Flask

from utils import get_candidates, format_candidates, get_candidate_id, get_candidates_skills

app = Flask(__name__)


@app.route('/')
def main():
    candidat_raw = get_candidates('candidates.json')

    return format_candidates(candidat_raw)


@app.route('/candidates/<int:candidate_id>')
def candidate_page(candidate_id):
    candidat_raw = get_candidates('candidates.json')
    candidate = get_candidate_id(candidat_raw, candidate_id)

    result = f'<img src="{candidate["picture"]}">'
    return result + format_candidates([candidate])


@app.route('/skills/<skill>')
def skills(skill):
    candidat_raw = get_candidates('candidates.json')

    return format_candidates(get_candidates_skills(candidat_raw, skill))


app.run()
