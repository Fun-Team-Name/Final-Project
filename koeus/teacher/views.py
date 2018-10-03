from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, redirect
#from teacher.forms import AddToClass
from teacher.forms import signupForm
from teacher.models import AccountManager
from teacher.models import Account
from django.contrib.auth.forms import AuthenticationForm

'''
@permission_required('teacher.manageStudents')
def renew_book_librarian(request, pk):
    # If this is a POST request then process the Form data
    if request.method == 'POST':

        # Create a form instance and populate it with data from the request (binding):
        form = AddToClass(request.POST)

        # Check if the form is valid:
        if AddToClass.is_valid():
            # process the data in form.cleaned_data as required (here we just write it to the model due_back field)
            book_instance.due_back = book_renewal_form.cleaned_data['renewal_date']
            book_instance.save()

            # redirect to a new URL:
            return HttpResponseRedirect(reverse('all-borrowed') )

    # If this is a GET (or any other method) create the default form.
    else:
        proposed_renewal_date = datetime.date.today() + datetime.timedelta(weeks=3)
        book_renewal_form = RenewBookForm(initial={'renewal_date': proposed_renewal_date})

    context = {
        'form': book_renewal_form,
        'book_instance': book_instance,
    }

    return render(request, 'catalog/book_renew_librarian.html', context)
'''

def teacherHome(request):
	return render(request, 'teacherHome.html', {})

def teacher_login(request):
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            return render(request, 'teacherHome.html', {})
        else:
            form = AuthenticationForm()
        return render(request, 'registration/login.html',{'form':form})


# def signup(request):
# 	form = signupForm(request.POST or None)
# 	if form.is_valid():
# 		email = form.cleaned_data.get('email')
# 		password = form.cleaned_data.get('password2')
# 		firstName = form.cleaned_data.get('firstName')
# 		lastName = form.cleaned_data.get('lastName')
# 		#form.save()
# 		Account.objects.create_user(email=email, password=password, firstName=firstName, lastName=lastName)
# 		return redirect('login')
# 	return render(request, 'registration/signup0.html', {'form':form})

def signup(request):
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            return render(request, 'registration/login.html', {'form':form})
        else:
            form = AuthenticationForm()
        return render(request, 'registration/signup0.html',{'form':form})
