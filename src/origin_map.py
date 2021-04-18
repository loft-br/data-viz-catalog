import requests
import pandas as pd
import folium

# url to request meshes of Brazilian macro-regions in geojson format using IBGE API v3
meshes_url = 'https://servicodados.ibge.gov.br/api/v3/malhas/paises/BR?formato=application/vnd.geo+json&qualidade=maxima&intrarregiao=regiao'
meshes_data = requests.get(meshes_url).json()

# url to request information of Brazilian macro-regions using IBGE API v1
regions_url = 'https://servicodados.ibge.gov.br/api/v1/localidades/regioes'
regions_data = requests.get(regions_url, headers=headers).json()

# url to request centroids of Brazilian macro-regions using IBGE API v3
centroids_url = 'https://servicodados.ibge.gov.br/api/v3/malhas/paises/BR/metadados?intrarregiao=regiao'
centroids_data = requests.get(centroids_url).json()

meshes_ids = []
regions_ids = []
regions_names = []
regions_codes = []

# code area (id) information about meshes
for feature in meshes_data['features']:
    meshes_ids.append(str(feature['properties']['codarea']))

meshes_ids.sort()

# id and other information about Federative Units
for region in regions_data:
    regions_ids.append( str(region['id']))
    regions_names.append(region['nome'])
    regions_codes.append(region['sigla'])

regions_ids.sort()

# validate if ids match
meshes_ids == regions_ids

regions = pd.DataFrame({'id': regions_ids, 'nome': regions_names, 'sigla': regions_codes})
regions.set_index('id', inplace=True)

# retrieving centroid data
for region in centroids_data: 
    centroid = region['centroide']
    lat = centroid['latitude']
    lon = centroid['longitude']
    cod = str(region['id'])
    
    regions.loc[cod,'lat'] = lat
    regions.loc[cod,'lon'] = lon

regions.reset_index(inplace=True)

regions["percentage"] = [0, 9.5, 71, 5, 5]


#plotting a folium map
brazil_centroid = (-10.7437,-53.0758)

m = folium.Map(
    location=brazil_centroid,
    zoom_start=4,
    tiles='cartodbpositron'
)

choropleth = folium.Choropleth(
    geo_data=meshes_data,
    data=regions,
    bins = [0, 4, 8, 9, 12, 16, 60, 70, 80],
    columns=['id', 'percentage'],
    key_on='feature.properties.codarea',
    fill_color='YlOrRd',
    fill_opacity=0.9,
    name=" % de Origem por região do Brasil"
)

#hide colormap bar
for key in choropleth._children:
    if key.startswith('color_map'):
        del(choropleth._children[key])
        
choropleth.add_to(m)

#adding labels and circle markers
for index, row in regions.iterrows():
    location = list((row['lat'], row['lon']))
    popup = folium.Popup(f"<b>{row['nome']}</b> <br>{str(row['percentage'])}%", show= True)
    folium.Circle(
        location = location, 
        radius= row['percentage']*9000, 
        weight=10, 
        color = "#f26233", 
        fill=False,
        popup = popup
      ).add_to(m)

#creating the abroad marker
location_outside = list((-10.7437,-30.0758))
popup = folium.Popup("<b>Outros países</b> <br>9.5%", show= True)
folium.Circle(
        location = location_outside, 
        radius= 9.5*9000, 
        weight=10, 
        color = "#f26233", 
        fill=False,
        popup = popup
      ).add_to(m)

folium.LayerControl().add_to(m)

loc = 'Origem de Nascimento por região do Brasil e outros países (em %)'
title_html = '''
             <h3 align="center" style="font-size:16px"><b>{}</b></h3>
             '''.format(loc)   
m.get_root().html.add_child(folium.Element(title_html))

m.save("map.html")

# display an interactive html map - requires ipython or jupyter notebook
#m