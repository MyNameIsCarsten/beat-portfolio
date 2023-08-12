from django.shortcuts import render
from .models import Beat
from django.db.models import Min
from catalog_app.fill_database import mp3_path, get_bpm_key

def home(request):
  # Ausgewählte Objekte aus Datenbank holen
  all_items = Beat.objects.all()
  keys = Beat.objects.values('key').distinct()
  min_bpm = Beat.objects.filter().order_by('bpm').first().bpm
  max_bpm = Beat.objects.filter().order_by('bpm').last().bpm
  mid_bpm = round((min_bpm + max_bpm) / 2, 0)
  context = {
    'all_items': all_items,
    'keys': keys,
    'min_bpm': min_bpm,
    'max_bpm': max_bpm,
    'mid_bpm': mid_bpm
  }


  if request.method == 'POST':
    print(request.POST)
    if 'key' in request.POST:

      filter_value = request.POST['key']

      # Ausgewählte Objekte aus Datenbank holen
      context['all_items'] = Beat.objects.filter(key=filter_value).values()

    elif 'delete_all' in request.POST:
      # Delete all objetcs
      Beat.objects.all().delete()

      # Ausgewählte Objekte aus Datenbank holen
      all_items = Beat.objects.all()
      keys = Beat.objects.values('key').distinct()
      context = {
        'all_items': all_items,
        'keys': keys
      }

    elif 'filter_bpm' in request.POST:

      # Ausgewählte Objekte aus Datenbank holen
      all_items = Beat.objects.all()
      keys = Beat.objects.values('key').distinct()
      min_bpm = Beat.objects.filter().order_by('bpm').first().bpm
      max_bpm = Beat.objects.filter().order_by('bpm').last().bpm
      mid_bpm = round((min_bpm + max_bpm) / 2, 0)

      context = {
        'all_items': all_items,
        'keys': keys,
        'min_bpm': min_bpm,
        'max_bpm': max_bpm,
        'mid_bpm': mid_bpm
      }
      print(context)

    else:
      folder_path = request.POST['path']
      #folder_path = "D:\Dropbox\Beats\ProfessionalStuff\Beatstars\Afro Beats"
      beat_list = mp3_path(folder_path)

      # Neue Objekte erstellen
      for beat in beat_list:
        try:
          number, bpm, key, name, full_path = get_bpm_key(beat, folder_path)
          Beat.objects.create(number=number, bpm=bpm, key=key, name=name, full_path=full_path)
        except:
          pass

      # Alle Objekte aus Datenbank holen
      all_items = Beat.objects.all()
      keys = Beat.objects.values('key').distinct()
      context = {
        'all_items': all_items,
        'keys' : keys
      }
  else:
    # Alle Objekte aus Datenbank holen
    all_items = Beat.objects.all()
    keys = Beat.objects.values('key').distinct()

    min_bpm = Beat.objects.filter().order_by('bpm').first().bpm
    max_bpm = Beat.objects.filter().order_by('bpm').last().bpm
    mid_bpm = round((min_bpm + max_bpm)/2, 0)

    context = {
      'all_items': all_items,
      'keys': keys,
      'min_bpm': min_bpm,
      'max_bpm': max_bpm,
      'mid_bpm': mid_bpm
    }
  print(context['keys'])
  return render(request, "catalog_app/home.html", context)