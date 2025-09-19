from .models import PageView, ClickEvent
from rest_framework import serializers


class PageViewSerializer(serializers.ModelSerializer):
    user_info = serializers.SerializerMethodField()

    class Meta:
        model = PageView
        fields = [
            "id",
            "user_info",
            "page_url",
            "timestamp",
            "session_id",
            "referrer_url",
            "user_agent",
            "ip_address",
        ]
        read_only_fields = ["id", "timestamp", "user_info"]

    def get_user_info(self, obj):
        return obj.get_user_info()
    

class ClickEventSerializer(serializers.ModelSerializer):
    user_info = serializers.SerializerMethodField()

    class Meta:
        model = ClickEvent
        fields = [
            "id",
            "user_info",
            "element_id",
            "page_url",
            "timestamp",
            "session_id",
            "referrer_url",
            "user_agent",
        ]
        read_only_fields = ["id", "timestamp", "user_info"]

    def get_user_info(self, obj):
        return obj.get_user_info()