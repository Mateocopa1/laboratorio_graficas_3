import pandas as pd
import plotly.graph_objects as go


df = pd.read_csv('datos.csv', delimiter=';')

labels = ['aprobados','Reprobados']
values = [sum(df['aprobado'] == 'Sí'), sum(df['aprobado'] == 'No')]

fig = go.Figure()  # Crear una figura vacía

# Añadir el trazado de torta a la figura
fig.add_trace(go.Pie(
    labels=labels, values=values,  # Etiquetas y valores
    hole=0.0  # Tamaño del hueco en el centro del gráfico de torta
))

# Personalizar el diseño del gráfico
fig.update_layout(
    title='Gráfico de Torta'  # Título del gráfico
)

# Mostrar el gráfico
fig.show()

fig = go.Figure()  # Crear una figura vacía
materias = df['materia'].unique().tolist()
notas_m = df[df['materia'] == materias[0]]['nota']
notas_h = df[df['materia'] == materias[1]]['nota']
notas_c = df[df['materia'] == materias[2]]['nota']
notas_l = df[df['materia'] == materias[3]]['nota']

# Añadir el trazado de cajas a la figura
fig.add_trace(go.Box(
    y=notas_m,  # Datos para el gráfico de cajas
    name=materias[0],  # Etiqueta del gráfico de cajas
    jitter=0.3,  # Controlar la dispersión horizontal de los puntos
    whiskerwidth=0.2,  # Controlar el ancho de las cajas
    fillcolor='lightgray',  # Color de relleno de las cajas
))
fig.add_trace(go.Box(
    y=notas_h,  # Datos para el gráfico de cajas
    name=materias[1],  # Etiqueta del gráfico de cajas
    jitter=0.3,  # Controlar la dispersión horizontal de los puntos
    whiskerwidth=0.2,  # Controlar el ancho de las cajas
    fillcolor='lightgray',  # Color de relleno de las cajas
))
fig.add_trace(go.Box(
    y=notas_c,  # Datos para el gráfico de cajas
    name=materias[2],  # Etiqueta del gráfico de cajas
    jitter=0.3,  # Controlar la dispersión horizontal de los puntos
    whiskerwidth=0.2,  # Controlar el ancho de las cajas
    fillcolor='lightgray',  # Color de relleno de las cajas
))
fig.add_trace(go.Box(
    y=notas_l,  # Datos para el gráfico de cajas
    name=materias[3],  # Etiqueta del gráfico de cajas
    jitter=0.3,  # Controlar la dispersión horizontal de los puntos
    whiskerwidth=0.2,  # Controlar el ancho de las cajas
    fillcolor='lightgray',  # Color de relleno de las cajas
))


# Personalizar el diseño del gráfico
fig.update_layout(
    title='Gráfico de Cajas',  # Título del gráfico
    yaxis_title='Valores'  # Etiqueta del eje y
)

# Mostrar el gráfico
fig.show()