# Flask NER API

Una sencilla API REST construida con Flask y Spacy para el reconocimiento de entidades nombradas en oraciones en español.

## 🚀 Instalación

**1.** Asegúrate de tener Python y pip instalados.

**2.** Clona este repositorio:

```bash
git clone https://github.com/Mcruz-G/flask-ner-api.git
cd flask-ner-api
```

**3.** Instala las dependencias (tip: instala las dependencias en un ```virtualenv``` con ```sudo apt-get install virtualenv``` ):

```bash
pip install flask spacy
python -m spacy download es_core_news_sm
```

## 📖 Uso
1. Ejecuta el servidor con:
``` bash
python api.py
```

2. Para probar la API, usa la siguiente solicitud CURL:

``` bash
curl -X POST -H "Content-Type: application/json" -d '{
  "oraciones": [
    "Apple está buscando comprar una startup del Reino Unido por mil millones de dólares.",
    "San Francisco considera prohibir los robots de entrega en la acera."
  ]
}' http://127.0.0.1:5000/ner
``` 

El servidor debería responder con:
``` bash
{
 "resultado": [
   {
     "oración": "Apple está buscando comprar una startup del Reino Unido por mil millones de dólares.",
     "entidades": {
       "Apple": "ORG",
       "Reino Unido": "LOC",
     }
   },
   {
     "oración": "San Francisco considera prohibir los robots de entrega en la acera.",
     "entidades": {
       "San Francisco": "LOC"
     }
   }
 ]
}
``` 
📚 Referencias
Flask
Spacy
