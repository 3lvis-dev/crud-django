from django.shortcuts import render, get_object_or_404, redirect
from person.form import FormPerson
from person.models import Person

def home(request):
    no_persons = Person.objects.count()
    persons = Person.objects.order_by('id')
    return render(request, 'index.html', {
        'no_persons': no_persons,
        'persons': persons
    })



# CREATE Method
def person_new(request):
    if request.method == 'POST':
        person_form = FormPerson(request.POST)
        if person_form.is_valid():
            person_form.save()
            return redirect('index')
    else:
        person_form = FormPerson()

    return render(request, 'new.html', {'person_form': person_form})


# READ Method
def personDetail(request, id):
    person = get_object_or_404(Person, pk=id)
    return render(request, 'detail.html', {
        'person': person
    })



# UPDATE Method
def person_edit(request, id):
    person = get_object_or_404(Person, pk=id)
    if request.method == 'POST':
        person_form = FormPerson(request.POST, instance=person)
        if person_form.is_valid():
            person_form.save()
            return redirect('index')
    else:
        person_form = FormPerson(instance=person)

    return render(request, 'edit.html', {'person_form': person_form})



# DELETE Method
def person_delete(request, id):
    person = get_object_or_404(Person, pk=id)

    if person:
        person.delete()
    return redirect('index')