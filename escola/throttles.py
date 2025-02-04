from rest_framework import throttling

class MatriculaAnonRateThrottle(throttling.AnonRateThrottle):
    rate = '5/days'