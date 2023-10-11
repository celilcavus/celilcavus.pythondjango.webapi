from rest_framework import serializers
from haberler.models import Makale



class MakaleSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    yazar= serializers.CharField(max_length=150)
    baslik= serializers.CharField(max_length=120)
    aciklama = serializers.CharField(max_length=200)
    metin= serializers.CharField()
    sehir= serializers.CharField(max_length=120)
    yayimlama_tarihi= serializers.DateField()
    aktif= serializers.BooleanField(default=True)
    yaratilma_tarihi= serializers.DateTimeField(read_only=True)
    guncellenme_tarihi= serializers.DateTimeField(read_only=True)

    def create(self,validated_data):
        print(validated_data)
        return Makale.objects.create(**validated_data)
    
    def update(self,instance,validated_data):
        instance.yazar = validated_data.get('yazar',instance.yazar)
        instance.baslik = validated_data.get('baslik',instance.baslik)
        instance.aciklama = validated_data.get('aciklama',instance.aciklama)
        instance.metin = validated_data.get('metin',instance.metin)
        instance.sehir = validated_data.get('sehir',instance.sehir)
        instance.yayimlama_tarihi = validated_data.get('yayimlama_tarihi',instance.yayimlama_tarihi)
        instance.aktif = validated_data.get('aktif',instance.aktif)
        instance.yaratilma_tarihi = validated_data.get('yaratilma_tarihi',instance.yaratilma_tarihi)
        instance.guncellenme_tarihi = validated_data.get('guncellenme_tarihi',instance.guncellenme_tarihi)

        instance.save()
        return instance

    def delete(self,pk):
        try:
            findmakale = Makale.objects.get(pk=pk)
            Makale.objects.delete(findmakale)
            Makale.save()
        except Exception:
            print('Silme işlemi başarisiz')

