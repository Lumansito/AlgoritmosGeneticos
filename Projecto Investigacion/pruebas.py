import pandas as pd

# Ejemplo de datos
data = {
    'text': [
        "El rápido gato marrón salta sobre el perro perezoso",
        "Nunca saltes sobre el perro perezoso rápidamente",
        "La economía global está en crisis",
        "Las acciones suben y bajan en el mercado",
        "Los nuevos avances en inteligencia artificial son asombrosos",
        "La red neuronal ha aprendido a jugar al ajedrez",
        "La pelota ha empezado a rodar en el campo de futbol",
        "El equipo azul y amarillo vencio a su par de Buenos Aires"
    ],
    'category': [
        'animal', 'animal', 'economía', 'economía', 'tecnología', 'tecnología', 'deportes','deportes'
    ]
}

df = pd.DataFrame(data)

from sklearn.feature_extraction.text import CountVectorizer

# Lista de stop words en español
stop_words_spanish = [
    'de', 'la', 'que', 'el', 'en', 'y', 'a', 'los', 'del', 'se', 'las', 'por', 'un', 
    'para', 'con', 'no', 'una', 'su', 'al', 'lo', 'como', 'más', 'pero', 'sus', 'le', 
    'ya', 'o', 'fue', 'este', 'ha', 'sí', 'porque', 'esta', 'son', 'entre', 'cuando', 
    'muy', 'sin', 'sobre', 'también', 'me', 'hasta', 'hay', 'donde', 'quien', 'desde', 
    'todo', 'nos', 'durante', 'todos', 'uno', 'les', 'ni', 'contra', 'otros', 'ese', 
    'eso', 'ante', 'ellos', 'e', 'esto', 'mí', 'antes', 'algunos', 'qué', 'unos', 'yo', 
    'otro', 'otras', 'otra', 'él', 'tanto', 'esa', 'estos', 'mucho', 'quienes', 'nada', 
    'muchos', 'cual', 'poco', 'ella', 'estar', 'estas', 'algunas', 'algo', 'nosotros', 
    'mi', 'mis', 'tú', 'te', 'ti', 'tu', 'tus', 'ellas', 'nosotras', 'vosotros', 
    'vosotras', 'os', 'mío', 'mía', 'míos', 'mías', 'tuyo', 'tuya', 'tuyos', 'tuyas', 
    'suyo', 'suya', 'suyos', 'suyas', 'nuestro', 'nuestra', 'nuestros', 'nuestras', 
    'vuestro', 'vuestra', 'vuestros', 'vuestras', 'esos', 'esas', 'estoy', 'estás', 
    'está', 'estamos', 'estáis', 'están', 'esté', 'estés', 'estemos', 'estéis', 'estén', 
    'estaré', 'estarás', 'estará', 'estaremos', 'estaréis', 'estarán', 'estaría', 
    'estarías', 'estaríamos', 'estaríais', 'estarían', 'estaba', 'estabas', 'estábamos', 
    'estabais', 'estaban', 'estuve', 'estuviste', 'estuvo', 'estuvimos', 'estuvisteis', 
    'estuvieron', 'estuviera', 'estuvieras', 'estuviéramos', 'estuvierais', 'estuvieran', 
    'estuviese', 'estuvieses', 'estuviésemos', 'estuvieseis', 'estuviesen', 'estando', 
    'estado', 'estada', 'estados', 'estadas', 'estad'
]

# Crear el vectorizador con la lista de stop words en español
vectorizer = CountVectorizer(stop_words=stop_words_spanish)


X = vectorizer.fit_transform(df['text']) # Ajustar y transformar los documentos


print(vectorizer.get_feature_names_out())
print(X.toarray())  

from sklearn.model_selection import train_test_split


# Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, df['category'], test_size=0.3, random_state=42)


from sklearn.naive_bayes import MultinomialNB

# Crear y entrenar el clasificador Naive Bayes
clf = MultinomialNB()
clf.fit(X_train, y_train)



# Nuevos textos a clasificar en las categorías existentes
new_texts = [
    "El mercado bursátil ha caído drásticamente",
    "Los avances en robótica son impresionantes",
    "El equipo de futbol argentino ha ganado el campeonato",
    "El perro y el gato son amigos inseparables",
    "La inteligencia artificial es el futuro",
]

# Transformar los nuevos textos utilizando el mismo vectorizador
X_new = vectorizer.transform(new_texts)

# Predecir las categorías de los nuevos textos
new_predictions = clf.predict(X_new)
print(new_predictions)