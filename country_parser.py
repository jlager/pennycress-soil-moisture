import os
import json
import numpy as np

def load_countries(json_path: str) -> dict:

    # load polygons
    with open(json_path, 'r') as f:
        country_data = json.load(f)

    # extract country polygons
    country_poly = {}
    for i in range(len(country_data)):

        # get name, update dict
        country_name = country_data[i]['fields']['name']
        if country_name not in country_poly:
            country_poly[country_name] = []

        # get polygons, if inhomogeneous shape, loop through
        poly = country_data[i]['fields']['geo_shape']['coordinates']
        poly = np.array(poly, dtype=object) # support ragged arrays
        poly = np.squeeze(poly) # remove singleton dimensions
        if poly.ndim > 1: # if 2D, then it's a polygon, store and continue
            country_poly[country_name].append(poly.astype(float))
            continue
        for p in poly: # otherwise loop through the list of polygons
            p = np.squeeze(np.array(p, dtype=object))
            if p.ndim > 1: # if 2D, then it's a polygon, store and continue
                country_poly[country_name].append(p.astype(float))
                continue
            for q in p: # otherwise loop through the list of points
                q = np.squeeze(np.array(q, dtype=object))
                country_poly[country_name].append(q.astype(float))

    # flip lng/lat to lat/lng
    for c in country_poly.keys():
        for i in range(len(country_poly[c])):
            country_poly[c][i] = np.fliplr(country_poly[c][i])

    return country_poly