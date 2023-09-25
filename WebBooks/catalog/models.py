from django.db import models
from django.urls import reverse
from django.conf import settings



class Genre(models.Model):
# Поле (или множество полей)
    name = models.CharField(max_length=200,
                            help_text="Введите жанр книги",
                            verbose_name="Жанр книги")
    def __str__(self):
        return self.name



class Language(models.Model):
    name = models.CharField(max_length=20,
                            help_text='Введите язык книги',
                            verbose_name='Язык')
    def __str__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=20,
                            help_text='Введите наименование издательства',
                            verbose_name='Издательство')
    def __str__(self):
        return self.name




class Author(models.Model):
    first_name = models.CharField(max_length=100,
                                  help_text='Введите имя автора',
                                  verbose_name='Имя')
    last_name = models.CharField(max_length=100,
                                 help_text='Введите фамилию автора',
                                 verbose_name='Фамилия')
    date_of_birth = models.DateField(help_text='Ввежите дату рождения',
                                         verbose_name='Дата рождения',
                                         null=True, blank=True)
    about = models.TextField(help_text='Введите сведения об авторе',
                             verbose_name='Сведения об авторе')
    photo = models.ImageField(upload_to='images',
                              help_text='Введите фото автора',
                              verbose_name='Фото автора',
                              null=True, blank=True)
    def __str__(self):
        return self.last_name


class Book(models.Model):
    title = models.CharField(max_length=200,
                             help_text='Введте название книги',
                             verbose_name='Название книги')
    genre = models.ForeignKey('Genre',
                              on_delete=models.CASCADE,
                              help_text='Выберите жанр книги',
                              verbose_name='Каскад книги', null=True)
    language = models.ForeignKey('Language',
                                 on_delete=models.CASCADE,
                                 help_text='Введите язык книги',
                                 verbose_name='Язык')
    piblisher = models.ForeignKey('Publisher',
                                  on_delete=models.CASCADE,
                                  help_text='Введите наименование издательства',
                                  verbose_name='Издательство',
                                  )
    year = models.CharField(max_length=4,
                            help_text='Введите год издания',
                            verbose_name='Год издания')
    author = models.ManyToManyField('Author',
                                    help_text='Выберите автора (авторов) книги',
                                    verbose_name='Автор (авторы) книги ')
    summary = models.TextField('Summary',
                               help_text='Введите краткое содержание книги',
                               verbose_name='Аннотация книги')
    isbn = models.CharField(max_length=13,
                            help_text='Должно содержать 13 символов',
                            verbose_name= 'ISBN книги')
    price = models.DecimalField(decimal_places=2, max_length=7,
                                help_text='Введите цену книги',
                                verbose_name='Цена (руб.)')
    photo = models.ImageField(upload_to='images',
                              help_text='Введите изображение обложки',
                              verbose_name='Изображение обложки')



    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # Возвращает URL-aдpec для доступа к
        # определенному экземпляру книги
        return reverse('book-detail', args=[str(self.id)])



class Status(models.Model):
    name = models.CharField(max_length=20,
                            help_tехt="Введите статус экземпляра книги",
                            verbose_name="Cтaтyc экземпляра книги")
    def __str__(self):
        return self.name




class Bookinstance(models.Model):
    book = models.ForeignKey('Book',
                            on_delete=models.CASCADE, null=True)
    inv_nom = models.CharField(max_length=20,
                            null=True,
                            hеlр_tехt="Введите инвентарный номер экземпляра",
                            verbose_name= "Инвентарный номер")
    status = models.ForeignKey('Status',
                            on_delete=models.CASCADE,
                            null=True,
                            hеlр_tехt='Изменить состояние экземпляра',
                            verbose_name="Cтaтyc экземпляра книги")
    due_back = models.DateField(null=True, blank=True,
                            help_text='Введите конец срока статуса',
                            verbose_name='Дaтa окончания статуса')

# Метаданные
class Meta:
    ordering = ["due_back"]
def str (self) :
    return '%s %s %s' % (self.inv_nom, self.book, self.status)





# 388