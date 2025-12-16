# Shapes from town table
#
# Nov '25

# Setup

import geopandas as gpd
import matplotlib.pyplot as plt

from sqlalchemy import create_engine

# Database connection (TODO: Own DB not nyc)
db_connection_url = "postgresql://postgres@localhost:5432/nyc"
con = create_engine(db_connection_url)

# Query
# Select geom not ST_AsText(geom)

#sql = """SELECT name, geom
#         FROM town
#         WHERE name = 'Shops'"""

#sql = """SELECT name, geom
#         FROM town
#         WHERE name = 'Railway'"""

#sql = """SELECT name, geom
#         FROM town
#         WHERE name = 'Trees'"""

#sql = """SELECT name, geom
#         FROM town
#         WHERE name = 'Roads'"""

sql = """SELECT name, geom
         FROM town
         WHERE name = 'Houses'"""

# Read into GeoDataFrame
gdf = gpd.read_postgis(sql, con)
print(gdf)

# Plot
fig, ax = plt.subplots()
gdf.plot(ax=ax, color='green', edgecolor='black')
plt.title('Shapes from Town Table')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.savefig('shapes_from_town.png')
