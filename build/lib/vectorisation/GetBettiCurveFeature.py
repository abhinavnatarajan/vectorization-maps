import numpy as np
from gudhi import representations

__all__ = ["GetBettiCurveFeature"]

def GetBettiCurveFeature(barcode, res=100):

    if(np.size(barcode) > 0):
        bettiCurve = representations.vector_methods.BettiCurve(resolution=res)
        feature_vector = bettiCurve.fit_transform([barcode])[0]
    else:
    	feature_vector = np.zeros(res)
        
    return feature_vector