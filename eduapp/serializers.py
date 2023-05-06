""" from rest_framework import serializers
class MySerializer(serializers.Serializer):
    field1 = serializers.CharField(max_length=100)
    field2 = serializers.IntegerField()

    def validate_field2(self, value):
        if value < 0:
            raise serializers.ValidationError("Field2 cannot be negative")
        return value

    def to_internal_value(self, data):
        # Convert the string 'true' or 'false' to a boolean value
        data['field3'] = data.get('field3', '').lower() == 'true'
        return super().to_internal_value(data)
 """