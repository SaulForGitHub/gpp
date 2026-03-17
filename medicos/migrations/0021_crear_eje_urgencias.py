from django.db import migrations
from django.db.models import Max

def crear_eje_urgencias(apps, schema_editor):
    EjeCriterio = apps.get_model('medicos', 'EjeCriterio')
    CriterioClinico = apps.get_model('medicos', 'CriterioClinico')
    User = apps.get_model('auth', 'User')
    try:
        creador = User.objects.get(username="strik")
    except User.DoesNotExist:
        creador = None

    # Obtener el mayor valor de orden actual
    ultimo_orden = EjeCriterio.objects.aggregate(max_orden=Max('orden'))['max_orden'] or 0
    nuevo_orden = ultimo_orden + 1

    # Crear el nuevo eje
    eje = EjeCriterio.objects.create(
        tipo='Clínico',
        descripcion='Consulta en servicio de urgencias',
        orden=nuevo_orden,
        creado_por=creador,
        actualizado_por=None,
    )

    # Crear los criterios asociados
    CriterioClinico.objects.create(
        eje=eje,
        descripcion='No',
        max_dias=0,
        puntaje=0,
        orden=1,
        creado_por=creador,
        actualizado_por=None,
    )
    CriterioClinico.objects.create(
        eje=eje,
        descripcion='Si',
        max_dias=180,
        puntaje=1,
        orden=2,
        creado_por=creador,
        actualizado_por=None,
    )

class Migration(migrations.Migration):
    dependencies = [
        ('medicos', '0020_eliminar_eje_relacion_anillo_saco'),
    ]
    operations = [
        migrations.RunPython(crear_eje_urgencias),
    ]
