# use (django) frameworks library
# write (python manage.py runserver) at terminal to start server
# write (python mange.py startapp (app_name)) to start new app
# to add new main path use-> path('products/', include('products.urls') at main project urls
# then add a new function at section's views -> products\views
# after that add the path for this function at section's urls -> products\urls -> path('new', views.new)
# write your new model at section's model -> products\model
# at model you define new class and its variables
# to add database to sqlite write (python manage.py makemigrations) at the terminal
# then to initialize it write (python manage.py migrate) at terminal then open it in dp browser for sqlite
# use (python manage.py createsuperuser) at terminal to create an admin
