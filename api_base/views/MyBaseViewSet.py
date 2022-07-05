from rest_framework.viewsets import ModelViewSet


class MyBaseViewSet(ModelViewSet):
    serializer_class = None
    pagination_class = None
    permission_map = {

    }
    serializer_map = {

    }

    def get_permissions(self):
        return [permission() for permission in self.permission_map.get(self.action, self.permission_classes)]

    def get_serializer_class(self):
        return self.serializer_map.get(self.action, self.serializer_class)
