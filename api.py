from flask import Flask, request, Response
import spacy
import json

app = Flask(__name__)
nlp = spacy.load("es_core_news_sm")

@app.route('/ner', methods=['POST'])
def ner():
    data = request.get_json()
    oraciones = data.get('oraciones', [])
    
    result = []
    for oracion in oraciones:
        doc = nlp(oracion)
        entidades = {ent.text: ent.label_ for ent in doc.ents}
        result.append({
            "oración": oracion,
            "entidades": entidades
        })
    
    # Interpreté que se espera que la oración esté en español, por eso
    # Uso ensure_ascii=False para que no haya problemas con caracteres en español
    response_body = json.dumps({"resultado": result}, ensure_ascii=False)
    return Response(response_body, content_type="application/json; charset=utf-8")


if __name__ == '__main__':
    app.run(debug=True)
