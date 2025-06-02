import json
from django.shortcuts import render
import os


def remedy_compare(request):
    # Path to your JSON file (adjust the path as needed)
    json_file_path = os.path.join(os.path.dirname(__file__), 'organon.json')

    # Load JSON data
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # Extract medicine names
    remedy_names = list(data.keys())

    # Initialize context with default values
    context = {
        'remedy_names': remedy_names,
        'symptoms': {},
        'selected_remedies': [],
        'selected_symptom': '',
        'symptom_options': {
            'description': False,
            'mind': False,
            'head': False,
            'eyes': False,
            'ears': False,
            'nose': False,
            'mouth': False,
            'throat': False,
            'stomach': False,
            'abdomen': False,
            'rectum': False,
            'urinary': False,
            'male': False,
            'female': False,
            'respiratory': False,
            'back': False,
            'extremities': False,
            'sleep': False,
            'fever': False,
            'skin': False,
            'modalities': False,
            'relationship': False,
            'compare': False,
            'dose': False
        }
    }

    if request.method == 'POST':
        # Get selected remedies
        selected_remedies = [
            request.POST.get('remedy1'),
            request.POST.get('remedy2'),
            request.POST.get('remedy3'),
            request.POST.get('remedy4')
        ]
        # Remove empty selections
        selected_remedies = [r for r in selected_remedies if r]
        context['selected_remedies'] = selected_remedies

        # Get selected symptom
        selected_symptom = request.POST.get('symptom', '')
        context['selected_symptom'] = selected_symptom

        # Update which symptom option is selected
        if selected_symptom in context['symptom_options']:
            context['symptom_options'][selected_symptom] = True

        # Extract symptoms for selected remedies
        symptoms = {}
        for name in selected_remedies:
            if name in data:
                symptoms[name] = {
                    'description': data[name].get('description', ''),
                    'mind': data[name].get('mind', ''),
                    'head': data[name].get('head', ''),
                    'eyes': data[name].get('eyes', ''),
                    'ears': data[name].get('ears', ''),
                    'nose': data[name].get('nose', ''),
                    'mouth': data[name].get('mouth', ''),
                    'throat': data[name].get('throat', ''),
                    'stomach': data[name].get('stomach', ''),
                    'abdomen': data[name].get('abdomen', ''),
                    'rectum': data[name].get('rectum', ''),
                    'urinary': data[name].get('urinary', ''),
                    'male': data[name].get('male', ''),
                    'female': data[name].get('female', ''),
                    'respiratory': data[name].get('respiratory', ''),
                    'back': data[name].get('back', ''),
                    'extremities': data[name].get('extremities', ''),
                    'sleep': data[name].get('sleep', ''),
                    'fever': data[name].get('fever', ''),
                    'skin': data[name].get('skin', ''),
                    'modalities': data[name].get('modalities', ''),
                    'relationship': data[name].get('relationship', ''),
                    'compare': data[name].get('compare', ''),
                    'dose': data[name].get('dose', '')
                }
        context['symptoms'] = symptoms

    return render(request, 'app/base.html', context)
