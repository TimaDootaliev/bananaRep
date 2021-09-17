from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


""" 
Статусы: (открытый, закрытый, черновик) 
каждый вариант выбора представляется в виде кортежа(tuple) из двух элементов (ключ - хранится в БД, 
текст - используется для отображения данных) 
"""
STATUS_CHOICES = (
    ('open', 'Открытое'),
    ('closed', 'Закрытое'),
    ('draft', 'Черновик'),
)


class Publication(models.Model):
    """ Классы, которые наследуются от models.Model являются моделями, то есть отвечают за связь с БД через ORM.
    В БД будет создана таблица с указанными полями """
    title = models.CharField('Заголовок', max_length=255)
    # CharField - VARCHAR(), обязательное свойство max_length
    text = models.TextField('Описание')
    # TextField - TEXT
    status = models.CharField('Статус', max_length=10, choices=STATUS_CHOICES)
    # choices - жестко ограниченные варианты выбора, т.е. никакие иные значениея не принимаются
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             related_name='pubs', verbose_name='Автор')
    """ ForeignKey - поле для свзязи с другой моделью. Обязательное свойство: модель, on_delete - определяет, 
    что произойдет с объявлением, если удалить из БД """
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    """ DateTimeField - TIMESTAMP, auto_now_add - время задается при добавлении записи, 
    auto_now - время задается при изменении записи """
    updated_at = models.DateTimeField('Дата обновления', auto_now=True)

    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'

    def __str__(self):
        return self.title


class Comment(models.Model):
    publication = models.ForeignKey(Publication,
                                    on_delete=models.CASCADE,
                                    related_name='comments', verbose_name='Объявление')
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='comments', verbose_name='Автор')
    text = models.TextField('Текст')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return f'{self.publication} --> {self.user}'
 # TODO: операции в SELECT - загуглить


