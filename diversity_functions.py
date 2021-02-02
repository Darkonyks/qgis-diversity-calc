
import math

def dc_summarizePoly(poly, lyrPoint, fldCpecies):

    dctPoly = {}

    # loop thru all the points that intersects the polygons bounding box
    for obs in lyrPoint.getFeatures(poly.geometry().boundingBox()):
        # check to see if the point is actually in the polygon
        if poly.geometry().contains(obs.geometry()):
            # get the name of the species as a string variable
            sSpecies = obs.attribute(fldCpecies)
            # check to see if the species already has an entry in the dictinary
            if sSpecies in dctPoly.keys():
                # if it does increase the count to 1
                dctPoly[sSpecies] += 1
            else:
                # if there is no entry for the species, create it and set its
                # initial value to 1
                dctPoly[sSpecies] = 1
    return dctPoly


def dc_MergeDictionaries(dMain, cat, dPoly):
    # check to see if the category exists in the dMain dictionary
    if cat in dMain.keys():
        # if it does then loop thru the summary data in dPoly
        for species, obs in dPoly.items():
            # check if there is already an entry for the species in the category
            if species in dMain[cat].keys():
                # if there is than add the numbe of the observations in the summary data
                dMain[cat][species] += obs
            else:
                dMain[cat][species] = obs
    else:
        dMain[cat] = dPoly

    return dMain


def dc_richness(dict):

    return len(dict)


def dc_shannons(dict):

    total = sum(dict.values())
    shannons = 0

    for count in dict.values():
        prop = count/total

        shannons += prop*math.log(prop)
    return abs(shannons)


def dc_simpsons(dict):
    total = sum(dict.values())
    simpsons = 0

    for count in dict.values():
        prop = count/total

        simpsons += prop*prop
    return simpsons


def dc_evennes(dict):

    max = math.log(dc_richness(dict))
    return dc_shannons(dict)/max


def dc_resultString(dict):
    result = ""
    for category, summary in dict.items():
        result += "{}: {}   {:2.3f}   {:2.3f}   {:2.3f}\n".format(category, dc_richness(
            summary), dc_shannons(summary), dc_simpsons(summary), dc_evennes(summary))
    return result
