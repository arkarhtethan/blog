from rest_framework.routers import DefaultRouter
from .viewset import PostModelVeiwSet
router = DefaultRouter()

router.register('posts',PostModelVeiwSet,base_name="posts")