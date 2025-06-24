# DETECCIÓN DE EMOCIONES DE LA RUEDA DE PLUTCHIK EN TEXTOS EN INGLÉS Y/O ESPAÑOL.

# Descripción del proyecto
Este proyecto tiene como objetivo desarrollar un sistema basado en inteligencia artificial y procesamiento del lenguaje natural (PLN) para la detección y clasificación de emociones según el modelo de la Rueda de Plutchik en textos escritos en inglés y español. La propuesta busca identificar emociones primarias (como alegría, tristeza, miedo, y sorpresa) y emociones combinadas, permitiendo un análisis profundo del contenido emocional presente en los textos. La Rueda de las Emociones, que es una representación gráfica desarrollada por el psicólogo Robert Plutchik para ilustrar las relaciones entre diferentes emociones humanas. Este modelo es ampliamente utilizado en psicología y ciencias del comportamiento para comprender y categorizar las emociones de manera más estructurada. Descripción de la Rueda de las Emociones La Rueda de Plutchik organiza las emociones en un formato circular, destacando ocho emociones primarias que son universales y básicas para los seres humanos. Estas emociones se agrupan en pares de opuestos: Alegría ↔ Tristeza Confianza ↔ Asco Miedo ↔ Ira Sorpresa ↔ Anticipación Características principales del modelo: Intensidad: Las emociones más intensas se encuentran en el centro del círculo, mientras que las menos intensas están en la periferia. Por ejemplo: Alegría (alta intensidad) → Serenidad (baja intensidad). Ira (alta intensidad) → Molestia (baja intensidad). Combinaciones: Plutchik también sugiere que las emociones se pueden combinar para formar emociones más complejas. Por ejemplo: Alegría + Confianza → Amor. Miedo + Sorpresa → Temor. Adaptación Evolutiva: Según Plutchik, las emociones tienen una función adaptativa que ha evolucionado para ayudar a la supervivencia. Por ejemplo: El miedo prepara al individuo para huir de un peligro. La ira prepara al individuo para luchar contra una amenaza.

# Dataset
Para efectos de este proyecto se uso el dataset Jsevisal/go_emotions_wheel[https://huggingface.co/datasets/Jsevisal/go_emotions_wheel]

## Dimensiones y tipos de datos
- Número de filas: 43410 entries
- Número de columnas: 3 {text, labels, id}

## Tipos de datos
| Columna | Tipo | Nulos |
|---------|------|--------|
| text    | str  | 0      |
| lables  | list  | 0      |
| id | str | 0 | 0 |