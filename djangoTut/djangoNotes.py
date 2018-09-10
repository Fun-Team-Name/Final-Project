Django Notes
=============
Structure
    URLS (urls.py)
    View (views.py)
    Model (models.py)

Sending the request to the right view (urls.py)
    list called urlpatterns
        contains a list of path('<url>',<model>.<function>)
        or re_path(r'<regEx to match url>' <model>.<function>)
        use \<<type>:<name>\> in url to capture values

Handling the request (views.py)
    view functions take in HttpRequest object as a parameter
    from django.http import HttpResponse
    return HttpResponse('...')

Defining data models (models.py)
    Python objects called models
    Django handels talking to DB

    Def of model
        refference: https://docs.djangoproject.com/en/2.1/ref/models/fields/
        from django.db import models

        class <Class name>(models.Model):
            <field name> = models.<field type>(<peramiters>)
            ...

Querying data (views.py)
    filter:
        <model>.objects.filter(<field>__exact="<what to match>")

    create HttpResponse:
        from django.shortcuts import render
        render(<HttpRequest>, '<url>', <context>)
        # combines specific HTML Template and data
        ex:
            from django.shortcuts import render
            from .models import Team
            def index(request):
                list_teams = Team.objects.filter(team_level__exact="U09")
                context = {'youngest_teams': list_teams}
                return render(request, '/best/index.html', context)

Rendering data (HTML templates)
    use {% <python code> %} to imject python code into HTML

Make new virtual environment:
    in command line: mkvirtualenv <name of env>

    some commands:
        deactivate — Exit out of the current Python virtual environment
        workon — List available virtual environments
        workon name_of_environment — Activate the specified Python virtual environment
        rmvirtualenv name_of_environment — Remove the specified environment.

Databse migration
    in directory that has manage.py run: (must do every time models change)
        python3 manage.py makemigrations
        python3 manage.py migrate

Run server using:
    python3 manage.py runserver

mySQL:
    tell mySQL to read changes: FLUSH PRIVILEGES;
    Allow remote access: sudo ufw allow mysql
    start the mySQL server: systemctl start mysql
    launch shell (as root): /usr/bin/mysql -u root -p

    change pasword for root user:
        UPDATE mysql.user SET Password = PASSWORD('<new password>') WHERE User = 'root';

    view users:
        SELECT User, Host, authentication_string FROM mysql.user;

    create database:
        CREATE DATABASE <Databse name>;

    add user:
        INSERT INTO mysql.user (User,Host,authentication_string,ssl_cipher,x509_issuer,x509_subject)
        VALUES('<username>','localhost',PASSWORD('<password>'),'','','');

    grant PRIVILEGES to user:
        GRANT ALL PRIVILEGES ON <database>.* to <username>@localhost;

    SHOW DATABASES;

models

    def in app's models.py. Subclasses of django.db.models.Model

    fields:
        when declaring with function like CharField(), you can pass arguements
        ex:
            help_text: Provides a text label for HTML forms (e.g. in the admin site), as described above.
            verbose_name: A human-readable name for the field used in field labels. If not specified, Django will infer the default verbose name from the field name.
            default: The default value for the field. This can be a value or a callable object, in which case the object will be called every time a new record is created.
            null: If True, Django will store blank values as NULL in the database for fields where this is appropriate (a CharField will instead store an empty string). The default is False.
            blank: If True, the field is allowed to be blank in your forms. The default is False, which means that Django's form validation will force you to enter a value. This is often used with null=True , because if you're going to allow blank values, you also want the database to be able to represent them appropriately.
            choices: A group of choices for this field. If this is provided, the default corresponding form widget will be a select box with these choices instead of the standard text field.
            primary_key: If True, sets the current field as the primary key for the model (A primary key is a special database column designated to uniquely identify all the different table records). If no field is specified as the primary key then Django will automatically add a field for this purpose.

            full list here: https://docs.djangoproject.com/en/2.0/ref/models/fields/#field-options

        common field types:
            CharField is used to define short-to-mid sized fixed-length strings. You must specify the max_length of the data to be stored.
            TextField is used for large arbitrary-length strings. You may specify a max_length for the field, but this is used only when the field is displayed in forms (it is not enforced at the database level).
            IntegerField is a field for storing integer (whole number) values, and for validating entered values as integers in forms.
            DateField and DateTimeField are used for storing/representing dates and date/time information (as Python datetime.date in and datetime.datetime objects, respectively). These fields can additionally declare the (mutually exclusive) parameters auto_now=True (to set the field to the current date every time the model is saved), auto_now_add (to only set the date when the model is first created) , and default (to set a default date that can be overridden by the user).
            EmailField is used to store and validate email addresses.
            FileField and ImageField are used to upload files and images respectively (the ImageField simply adds additional validation that the uploaded file is an image). These have parameters to define how and where the uploaded files are stored.
            AutoField is a special type of IntegerField that automatically increments. A primary key of this type is automatically added to your model if you don’t explicitly specify one.
            ForeignKey is used to specify a one-to-many relationship to another database model (e.g. a car has one manufacturer, but a manufacturer can make many cars). The "one" side of the relationship is the model that contains the key.
            ManyToManyField is used to specify a many-to-many relationship (e.g. a book can have several genres, and each genre can contain several books). In our library app we will use these very similarly to ForeignKeys, but they can be used in more complicated ways to describe the relationships between groups. These have the parameter on_delete to define what happens when the associated record is deleted (e.g. a value of models.SET_NULL would simply set the value to NULL).

            full list here: https://docs.djangoproject.com/en/2.0/ref/models/fields/#field-types

    metadata:
        inside model declare class Meta
            class Meta:
                ordering = ['-my_field_name']

        specify default ordering using a list of field names assigned to ordering.
        prepend - to reverse order

        full is of metadata options: https://docs.djangoproject.com/en/2.0/ref/models/options/

    methods:
        minimally have __str__() method to return a human readable string of the object

        also common to have  get_absolute_url()
        ex:
            def get_absolute_url(self):
                """Returns the url to access a particular instance of the model."""
                return reverse('model-detail-view', args=[str(self.id)])

Model management:
    create a new record:
        <var name> = <model name>(<field name> = "<instance name>")

    save to databsed
        <var name>.save()

    # priamry_key field given automatically. id field set to 1 for first instance

    use objects atribute to match criteria
        <var name> = <model>.objects.<criteria>()

        <criteria>
            filter(<field>__<match type>=<target>) # .count() to return number
                match types: https://docs.djangoproject.com/en/2.0/ref/models/querysets/#field-lookups

            to index through field to get to desiered subfield use __:
                <field>: genre__name

    in models.py
        class <model name>(models.Model):
            <field name> = models.<field constructor>(<parameters>)

            <functions>

    field constructors:
        https://docs.djangoproject.com/en/2.1/ref/models/fields/#field-types

    field ex:
        ManyToManyField: "book can have multiple genres and a genre can have many books"
        ForeignKey: " each book will only have one author, but an author may have many books"
        UUIDField:  is used for the id field to set it as the primary_key for this
            model. This type of field allocates a globally unique value for each instance (one for every book you can find in the library).

Admin site:
    in */locallibrary/catalog/admin.py
        from django.contrib import admin
        from catalog.models import <List of models>

        admin.site.register(<model>) # for each model you want to import

    python3 manage.py createsuperuser

    python3 manage.py runserver
        then navigate to http://127.0.0.1:8000/admin/

    admin site customization: https://docs.djangoproject.com/en/2.0/ref/contrib/admin/

    to change how model displayed in admin site, define a Model admin class:
        https://docs.djangoproject.com/en/dev/ref/contrib/admin/#modeladmin-objects

    fieldsets: group field in admin
        in admin.py in admin calss
            fieldsets = (
                (<title>, {
                    'fields':('<field1>', '<field2>', ...)
                }),
                ...
            )
