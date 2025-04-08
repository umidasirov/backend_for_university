from django.shortcuts import render, redirect
from .forms import FileUploadForm
from .models import Mymodel

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            # Сохраняем форму, и данные попадут в базу данных
            form.save()
            return redirect('success_url')  # После сохранения можно перенаправить на другую страницу
    else:
        form = FileUploadForm()

    return render(request, 'index.html', {'form': form})
def success_page(request):
    files = Mymodel.objects.all()
    return render(request, 'success.html',{'model':files})  # Страница успеха


def delete_file(request, file_id):
    # Находим файл по ID и удаляем его
    file_to_delete = Mymodel.objects.get(id=file_id)

    # Удаляем файл из файловой системы (если используете FileField)
    file_to_delete.file.delete()

    # Удаляем запись из базы данных
    file_to_delete.delete()

    # Перенаправляем пользователя обратно на страницу с файлом
    return redirect('success_url')  # или перезапустите страницу, если 'success_url' это ваш маршрут