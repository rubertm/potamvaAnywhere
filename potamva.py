import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output, State #a
#from dash import no_update #a
#import dash_auth

import plotly.graph_objects as go
import pandas as pd
import json
import plotly.express as px
import geopandas as gpd
import requests

#--------------------------
geo_df = gpd.read_file("https://github.com/rubertm/potamva/blob/main/pot/amvacombinadoColab2.zip?raw=true").to_crs("EPSG:4686")
resp = requests.get('https://raw.githubusercontent.com/rubertm/potamva/main/pot/js_PP_AMVA_dash.json')
js_pp_AMVA_dash0 = json.loads(resp.content)

# ------------------------------------------------------------------
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
# ------------------------------------------------------------------
app = dash.Dash(__name__)
server = app.server

# auth = dash_auth.BasicAuth(app,
#  {'rmopython': 'rmopython.2021',
#   'pot': 'pot2021'})
# ------------------------------------------------------------------
app.layout = html.Div([

    html.H3("Información Geográfica de los POT de los municipios del AMVA", style={'text-align': 'center'}),

    dcc.Markdown('''
    #### Este aplicativo web muestra los subpolígonos resultado del cruce geográfico de los usos del suelo, tratamientos, clase de suelo, densidades, amenanzas y zonas de inundación, agrupadas por el área de servicio de acueducto "circuito", y los planes parciales.
    ''', style={'text-align': 'left', 'padding': '0px 0px 0px 0px'}),

    html.Div([

        html.Div(
            [
                dcc.Markdown('''
                ##### Componente Geográfico por Circuito
                ''', style={'text-align': 'left', 'padding': '0px 0px 0px 0px'}),

                dcc.Dropdown(id="slct_circuito",
                             options=[
                                 {"label": "AGUAS FRIAS", "value": 'AGUAS FRIAS'},
                                 {"label": "AJIZAL", "value": 'AJIZAL'},
                                 {"label": "ALTAVISTA CENTRO", "value": 'ALTAVISTA CENTRO'},
                                 {"label": "ALTAVISTA SUR", "value": 'ALTAVISTA SUR'},
                                 {"label": "ALTOS DE NIQUIA", "value": 'ALTOS DE NIQUIA'},
                                 {"label": "AMERICA", "value": 'AMERICA'},
                                 {"label": "ANA DIAZ", "value": 'ANA DIAZ'},
                                 {"label": "ASOMADERA", "value": 'ASOMADERA'},
                                 {"label": "AURES", "value": 'AURES'}, {"label": "AURES 2", "value": 'AURES 2'},
                                 {"label": "AYURA", "value": 'AYURA'}, {"label": "BARBOSA", "value": 'BARBOSA'},
                                 {"label": "BATALLON", "value": 'BATALLON'},
                                 {"label": "BELENCITO", "value": 'BELENCITO'},
                                 {"label": "BELLO", "value": 'BELLO'}, {"label": "BERLIN", "value": 'BERLIN'},
                                 {"label": "CALDAS", "value": 'CALDAS'}, {"label": "CAMPESTRE", "value": 'CAMPESTRE'},
                                 {"label": "CAMPO VALDES", "value": 'CAMPO VALDES'},
                                 {"label": "CASTILLA", "value": 'CASTILLA'},
                                 {"label": "CASTILLA-BELLO", "value": 'CASTILLA-BELLO'},
                                 {"label": "COPACABANA", "value": 'COPACABANA'},
                                 {"label": "CORAZON", "value": 'CORAZON'},
                                 {"label": "CORAZON ALTO", "value": 'CORAZON ALTO'},
                                 {"label": "CORAZON ALTO2", "value": 'CORAZON ALTO2'},
                                 {"label": "CUCARACHO", "value": 'CUCARACHO'},
                                 {"label": "CUMBRES", "value": 'CUMBRES'},
                                 {"label": "DOCE DE OCTUBRE", "value": 'DOCE DE OCTUBRE'},
                                 {"label": "EL CAPIRO", "value": 'EL CAPIRO'},
                                 {"label": "EL CHOCHO", "value": 'EL CHOCHO'},
                                 {"label": "EL DORADO", "value": 'EL DORADO'},
                                 {"label": "EL NORAL", "value": 'EL NORAL'},
                                 {"label": "EL RINCON", "value": 'EL RINCON'},
                                 {"label": "EL RODEO", "value": 'EL RODEO'},
                                 {"label": "EL TESORO", "value": 'EL TESORO'},
                                 {"label": "EL TOTUMO", "value": 'EL TOTUMO'},
                                 {"label": "ENCENILLOS", "value": 'ENCENILLOS'},
                                 {"label": "EXPANSION OCCIDENTE 1", "value": 'EXPANSION OCCIDENTE 1'},
                                 {"label": "EXPANSION OCCIDENTE 2", "value": 'EXPANSION OCCIDENTE 2'},
                                 {"label": "EXPANSION PARAISO", "value": 'EXPANSION PARAISO'},
                                 {"label": "GERONA", "value": 'GERONA'}, {"label": "GIRARDOTA", "value": 'GIRARDOTA'},
                                 {"label": "GUASIMALITO", "value": 'GUASIMALITO'},
                                 {"label": "HAMACAS", "value": 'HAMACAS'},
                                 {"label": "ITAGUI", "value": 'ITAGUI'}, {"label": "LA BARRACA", "value": 'LA BARRACA'},
                                 {"label": "LA CASCADA", "value": 'LA CASCADA'},
                                 {"label": "LA ESMERALDA", "value": 'LA ESMERALDA'},
                                 {"label": "LA ESPERANZA", "value": 'LA ESPERANZA'},
                                 {"label": "LA ESTRELLA", "value": 'LA ESTRELLA'},
                                 {"label": "LA LADERA", "value": 'LA LADERA'}, {"label": "LA MINA", "value": 'LA MINA'},
                                 {"label": "LA MONTANA", "value": 'LA MONTANA'},
                                 {"label": "LA PASTORA", "value": 'LA PASTORA'},
                                 {"label": "LA TABLAZA", "value": 'LA TABLAZA'},
                                 {"label": "LA TOLDA", "value": 'LA TOLDA'},
                                 {"label": "LA YE", "value": 'LA YE'}, {"label": "LAS BRISAS", "value": 'LAS BRISAS'},
                                 {"label": "LAS BRUJAS", "value": 'LAS BRUJAS'},
                                 {"label": "LAS FLORES", "value": 'LAS FLORES'},
                                 {"label": "LIMONCITO", "value": 'LIMONCITO'},
                                 {"label": "LLANADITAS", "value": 'LLANADITAS'},
                                 {"label": "LOS MANGOS", "value": 'LOS MANGOS'},
                                 {"label": "LOS PARRAS", "value": 'LOS PARRAS'},
                                 {"label": "MACHADO", "value": 'MACHADO'}, {"label": "MANDALAI", "value": 'MANDALAI'},
                                 {"label": "MANZANILLO", "value": 'MANZANILLO'},
                                 {"label": "MIRAFLORES", "value": 'MIRAFLORES'},
                                 {"label": "MOSCU", "value": 'MOSCU'}, {"label": "NARANJITOS", "value": 'NARANJITOS'},
                                 {"label": "NIQUIA", "value": 'NIQUIA'}, {"label": "NUTIBARA", "value": 'NUTIBARA'},
                                 {"label": "ORFELINATO", "value": 'ORFELINATO'},
                                 {"label": "PAJARITO", "value": 'PAJARITO'},
                                 {"label": "PALENQUE", "value": 'PALENQUE'}, {"label": "PALMITAS", "value": 'PALMITAS'},
                                 {"label": "PAN DE AZUCAR", "value": 'PAN DE AZUCAR'},
                                 {"label": "PARAISO", "value": 'PARAISO'},
                                 {"label": "PARIS", "value": 'PARIS'},
                                 {"label": "PARQUE MONTANA", "value": 'PARQUE MONTANA'},
                                 {"label": "PEDREGAL", "value": 'PEDREGAL'},
                                 {"label": "PEDREGAL ALTO", "value": 'PEDREGAL ALTO'},
                                 {"label": "PEDREGAL BAJO", "value": 'PEDREGAL BAJO'},
                                 {"label": "PICACHO", "value": 'PICACHO'},
                                 {"label": "PINOS", "value": 'PINOS'}, {"label": "PINOS 2", "value": 'PINOS 2'},
                                 {"label": "PINOS 3", "value": 'PINOS 3'}, {"label": "PINUELA", "value": 'PINUELA'},
                                 {"label": "POPULAR", "value": 'POPULAR'}, {"label": "POPULAR 2", "value": 'POPULAR 2'},
                                 {"label": "PORVENIR", "value": 'PORVENIR'},
                                 {"label": "POTRERITO", "value": 'POTRERITO'},
                                 {"label": "PRIMAVERA", "value": 'PRIMAVERA'},
                                 {"label": "PUEBLO VIEJO", "value": 'PUEBLO VIEJO'},
                                 {"label": "SABANETA", "value": 'SABANETA'},
                                 {"label": "SALVATORIANO", "value": 'SALVATORIANO'},
                                 {"label": "SAN ANTONIO DE PRADO", "value": 'SAN ANTONIO DE PRADO'},
                                 {"label": "SAN CRISTOBAL", "value": 'SAN CRISTOBAL'},
                                 {"label": "SAN ESTEBAN", "value": 'SAN ESTEBAN'},
                                 {"label": "SAN RAFAEL", "value": 'SAN RAFAEL'},
                                 {"label": "SANTA CATALINA SUR", "value": 'SANTA CATALINA SUR'},
                                 {"label": "SANTA ELENA", "value": 'SANTA ELENA'},
                                 {"label": "SANTO DOMINGO", "value": 'SANTO DOMINGO'},
                                 {"label": "VERSALLES", "value": 'VERSALLES'},
                                 {"label": "VERSALLES 2", "value": 'VERSALLES 2'},
                                 {"label": "VILLA DEL SOCORRO", "value": 'VILLA DEL SOCORRO'},
                                 {"label": "VILLA HERMOSA", "value": 'VILLA HERMOSA'},
                                 {"label": "VILLA LINDA", "value": 'VILLA LINDA'},
                                 {"label": "VOLADOR CENTRO", "value": 'VOLADOR CENTRO'},
                                 {"label": "VOLADOR NORTE", "value": 'VOLADOR NORTE'},
                                 {"label": "YULIMAR", "value": 'YULIMAR'}, {"label": "FUERA_AS", "value": 'FUERA_AS'}],
                             multi=True,
                             value=[],  # 'YULIMAR'
                             clearable=False
                             ),

                dcc.Markdown('''
            ##### Clasificación del mapa
            ''', style={'text-align': 'left', 'padding': '0px 0px 0px 0px'}),

                dcc.RadioItems(
                    id='clasificacion',
                    options=[{'label': i, 'value': i} for i in
                             ['Densidad', 'Tratamiento', 'UsoDeSuelo', 'ClaseSuelo', 'Amenaza_Hidrologica',
                              'Amenaza_Mov']],
                    value='Densidad',
                    labelStyle={'display': 'block'}),

                dcc.Markdown('''
            ##### Nivel de transparencia
            ''', style={'text-align': 'left', 'padding': '0px 0px 0px 0px'}),

                dcc.Slider(id='my-slider',
                           min=0, max=1, step=0.1, value=0.4,
                           marks={
                               0: {'label': '0', 'style': {'color': '#77b0b1'}},
                               0.2: {'label': '0.2'}, 0.4: {'label': '0.4'}, 0.6: {'label': '0.6'},
                               0.8: {'label': '0.8'},
                               1: {'label': 'Sin Tranparencia', 'style': {'color': '#f50'}}
                           }, ),

                dcc.Markdown('''
            ##### Mapas de fondo
            ''', style={'text-align': 'left', 'padding': '0px 0px 0px 0px'}),

                dcc.RadioItems(
                    id='stylemap',
                    options=[{'label': i, 'value': i} for i in
                             ['carto-positron', 'streets', 'satellite', 'satellite-streets']],
                    value='carto-positron',
                    labelStyle={'display': 'block'}
                ),

                dcc.Markdown('''
            ###### Contacto:rmopython@gmail.com, movil+573017565982, abril/2021, Fuentedeinformación:(1)POTAMVA. 
            ''', style={'text-align': 'left', 'padding': '0px 0px 0px 0px'})

            ],
            style={'width': '23%', 'display': 'inline-block'}),

        html.Div([
            dcc.Graph(id='grafica0')
        ], style={'width': '75%', 'float': 'right', 'display': 'block'})

    ], style={
        'borderBottom': 'thin lightgrey solid',
        'backgroundColor': 'rgb(250, 250, 250)',
        'padding': '10px 5px'
    }),

])

@app.callback(
    Output('grafica0', 'figure'),
    [Input('slct_circuito', 'value'),
     Input('clasificacion', 'value'),
     Input('my-slider', 'value'),
     Input('stylemap', 'value')])

def update_graph(option_slctd_cir, option_slctd_clas, option_slctd_slider, option_slctd_style):

    df_potamva = pd.read_csv('https://raw.githubusercontent.com/rubertm/potamva/main/pot/AMVAcombinado.csv', sep=';')
    # , dtype={"Densidad": str, "Tratamiento": str, "UsoDeSuelo": str, "ClaseSuelo": str, "Amenaza_Hidrologica": str, "Ameneza_Mov": str})
    pp_AMVA = pd.read_csv('https://raw.githubusercontent.com/rubertm/potamva/main/pot/pp_AMVA.csv', sep=';')

    # geo_df = gpd.read_file('/content/drive/MyDrive/pot/AMVAcombinado.shp').to_crs("EPSG:4686")
    # geo_df2 = geo_df[geo_df['CIRCUITO']==option_slctd_cir]
    geo_df2 = geo_df[(geo_df.CIRCUITO.isin(option_slctd_cir))]

    # df_potamva2 = df_potamva[df_potamva['CIRCUITO']==option_slctd_cir]
    df_potamva2 = df_potamva[(df_potamva.CIRCUITO.isin(option_slctd_cir))]
    df_potamva2['text'] = 'Tratamiento: ' + df_potamva2['Tratamientotxt'] + '<br>' + \
                          'Uso del Suelo: ' + df_potamva2['UsoDeSuelotxt'] + '<br>' + \
                          'Clase de Suelo: ' + df_potamva2['ClaseSuelotxt'] + '<br>' + \
                          'Densidad viv/ha: ' + df_potamva2['DENS_X_HA'].astype(str)

    color = df_potamva2[option_slctd_clas]  # geo_df2[option_slctd_clas]

    pp_AMVA = pp_AMVA[(pp_AMVA.Circuito1.isin(option_slctd_cir)) | (pp_AMVA.Circuito2.isin(option_slctd_cir)) | (
        pp_AMVA.Circuito3.isin(option_slctd_cir)) |
                      (pp_AMVA.Circuito4.isin(option_slctd_cir)) | (pp_AMVA.Circuito5.isin(option_slctd_cir))]

    pp_AMVA['text'] = 'PP: ' + pp_AMVA['NOMBRE'] + '<br>' + \
                      'codigo: ' + pp_AMVA['CODIGO'] + '<br>' + \
                      'area_ha: ' + pp_AMVA['AREA_ha'].astype(str) + '<br>' + \
                      'total viviendas: ' + pp_AMVA['N_VIVIENDA'].astype(str) + '<br>' + \
                      'fecha entrada: ' + pp_AMVA['ANO'].astype(str) + '<br>' + \
                      '2030: ' + pp_AMVA['2030'].astype(str) + '<br>' + \
                      '2040: ' + pp_AMVA['2040'].astype(str) + '<br>' + \
                      '2050: ' + pp_AMVA['2050'].astype(str)

    if option_slctd_clas == 'Densidad':
        tickvals_n = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
        ticktext_t = ['0', '1-10viv/ha', '11-30viv/ha', '31-50viv/ha', '51-100viv/ha', '101-120viv/ha', '121-200viv/ha',
                      '201-300viv/ha', '301-400viv/ha', '-9999']
    elif option_slctd_clas == 'Tratamiento':
        tickvals_n = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']
        ticktext_t = ['API', 'Conservacion', 'Consolidacion', 'Consolidacion SubUrbana', 'Desarrollo',
                      'Generacion de actividades forestales', 'Mejoramiento Integral',
                      'Preservacion activa', 'Preservacion estricta', 'Recuperacion', 'Redesarrollo', 'Renovacion',
                      'Restauracion de Act. Rurales', 'Sin Dato']
    elif option_slctd_clas == 'UsoDeSuelo':
        tickvals_n = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']
        ticktext_t = ['Actividad multiple', 'Agropecuario', 'Comercial', 'Industrial', 'Mineria', 'Oficial',
                      'Residencial', 'Via',
                      'Zona verde rural', 'Zona verde urbano', 'Sin Dato']
    elif option_slctd_clas == 'ClaseSuelo':
        tickvals_n = ['1', '2', '3', '4', '5']
        ticktext_t = ['Expansion', 'Rural', 'Suburbano', 'Urbano', 'Sin Dato']
    elif option_slctd_clas == 'Amenaza_Hidrologica':
        tickvals_n = ['1', '2', '3']
        ticktext_t = ['Avenida Torrencial', 'Inundacion', 'Sin Dato']
    else:
        tickvals_n = ['1', '2', '3', '4']
        ticktext_t = ['Alta', 'Media', 'Muy-Alta', 'Sin Dato']

    #style = option_slctd_style
    #token = 'pk.eyJ1Ijoicm1vcHl0aG9uIiwiYSI6ImNrbmZ6MGZyMDF3Yncyd2s4ODVoMmR1Z3EifQ.FCGeYHLeHwjRkksgEyIrSw'

    fig = px.choropleth_mapbox(data_frame=df_potamva2, geojson=geo_df2.geometry, color=color,
                               locations=df_potamva2.OBJECTID, hover_name=df_potamva2.text,
                               opacity=option_slctd_slider
                               )
    fig.add_trace(go.Choroplethmapbox(geojson=js_pp_AMVA_dash0, locations=pp_AMVA.ID,
                                      marker=go.choroplethmapbox.Marker(opacity=0.5),
                                      colorscale='gray', z=pp_AMVA['ID2'],
                                      text=pp_AMVA['text'], hovertemplate="<b>%{text}</b><br>" + "<extra></extra>",
                                      marker_line_width=3, autocolorscale=False, showscale=False,
                                      name='Planes Parciales',
                                      marker_line_color='#0DF9FF', showlegend=True))  #  visible=visible ))

    fig.update_layout(mapbox_style=option_slctd_style, mapbox_zoom=10,
                      mapbox_center={'lat': 6.24, 'lon': -75.58},
        mapbox_accesstoken='pk.eyJ1Ijoicm1vcHl0aG9uIiwiYSI6ImNrbmZ6MGZyMDF3Yncyd2s4ODVoMmR1Z3EifQ.FCGeYHLeHwjRkksgEyIrSw',
                    coloraxis_showscale=True, width=950, height=600,
                    margin={"r": 10, "t": 10, "l": 10, "b": 10},
                coloraxis_colorbar=dict(title=option_slctd_clas, titleside='top',
                                        titlefont=dict(size=14, family='Arial, sans-serif'),
                                        thicknessmode='fraction',
                                len=0.6, lenmode='fraction', outlinewidth=1, showticklabels=True, y=0.6,
                                        tickvals=tickvals_n,
                                        ticktext=ticktext_t)
                      )

    return fig
# ------------------------------------------------------------------
if __name__ == '__main__':
    app.run_server(debug=True)

# app.run_server(mode='inline')
# app.run_server(mode='inline', port=8030)