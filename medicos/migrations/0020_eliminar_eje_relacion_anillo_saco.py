from django.db import migrations

def eliminar_eje_relacion_anillo_saco(apps, schema_editor):
    EjeCriterio = apps.get_model('medicos', 'EjeCriterio')
    CriterioClinico = apps.get_model('medicos', 'CriterioClinico')
    CriterioSocial = apps.get_model('medicos', 'CriterioSocial')

    # Buscar el eje por descripcion exacta
    eje = EjeCriterio.objects.filter(descripcion='Relación anillo / saco').first()
    if eje:
        # Eliminar criterios clínicos asociados
        CriterioClinico.objects.filter(eje=eje).delete()
        # Eliminar criterios sociales asociados
        CriterioSocial.objects.filter(eje=eje).delete()
        # Eliminar el eje
        eje.delete()

class Migration(migrations.Migration):
    dependencies = [
        ('medicos', '0019_alter_paciente_correo_alter_paciente_direccion_and_more'),
    ]
    operations = [
        migrations.RunPython(eliminar_eje_relacion_anillo_saco),
    ]
