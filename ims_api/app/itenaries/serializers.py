from rest_framework import serializers
from ims_api.app.itenaries.models import Itenary


class ItenarySerializer(serializers.ModelSerializer):
    """
    Serializer class for an itenary
    """
    name = serializers.CharField(
        # validators=[],
        required=True,
        error_messages={
            "required": "You must provide the name of the itenary you want to create",
            "blank": "Itenary name field cannot be left empty"
        }
    )

    class Meta:
        model = Itenary
        fields = ('id', 'name', 'thumbnail', 'company_id', 'created_at',
                    'updated_at', 'deleted', 'deleted_at' )
