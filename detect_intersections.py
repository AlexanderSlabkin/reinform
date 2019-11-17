project = QgsProject.instance()
planshety = QgsVectorLayer('/home/alexander/Programming/QGIS/planshety/planshety.shp',
                           'Planshety layer', 'ogr')
zoni = QgsVectorLayer('/home/alexander/Programming/QGIS/zoni.shp',
                      'Zoni layer', 'ogr')
caps = zoni.dataProvider().capabilities()

if not planshety.isValid() and zoni.isValid():
    print('Layer failed to load!')

if project.count() is 0:
    crs = QgsCoordinateReferenceSystem(4326, QgsCoordinateReferenceSystem.EpsgCrsId)
    planshety.setCrs(crs)
    zoni.setCrs(crs)
    project.addMapLayers((zoni, planshety))

features = zoni.getFeatures()
rectangles = planshety.getFeatures()

for i in features:
    all_planshets = []
    for k in rectangles:
        rectangle = k.geometry()
        if rectangle.intersects(i.geometry()):
            all_planshets.append(k['planshet'])

    string = ', '.join(all_planshets)
    if caps & QgsVectorDataProvider.ChangeAttributeValues:
        attrs = {1: string}
        zoni.dataProvider().changeAttributeValues({i.id(): attrs})
