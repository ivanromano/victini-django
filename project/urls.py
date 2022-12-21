from rest_framework import routers
from .api import ProjectViewSets

router = routers.DefaultRouter()

router.register('api/proyects', ProjectViewSets, 'proyects')

urlpatterns = router.urls # no equivocarse de nombre