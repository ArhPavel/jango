from django.core.management.base import BaseCommand
from catalog.models import Product, Category

class Command(BaseCommand):
    help = 'Удаляет старые данные и добавляет новые тестовые продукты и категории в базу данных'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.MIGRATE_HEADING('--- Запуск очистки и наполнения базы данных ---'))

        self.stdout.write('Удаление старых данных...')
        Product.objects.all().delete()
        Category.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Все старые продукты и категории успешно удалены!'))


        self.stdout.write('\nДобавление новых тестовых данных...')

        # 1. Создаем категории
        fruits_cat, _ = Category.objects.get_or_create(
            name='Фрукты',
            defaults={'description': 'Свежие и сочные фрукты'}
        )
        veg_cat, _ = Category.objects.get_or_create(
            name='овощи',
            defaults={'description': 'Свежие овощи прямо с грядки'}
        )
        chem_cat, _ = Category.objects.get_or_create(
            name='бытовая химия',
            defaults={'description': 'Товары для дома и чистоты'}
        )


        products_list = [
            {'name': 'Слива', 'category': fruits_cat, 'price': 250.00, 'description': 'Сладкая спелая слива'},
            {'name': 'Яблоко', 'category': fruits_cat, 'price': 120.50, 'description': 'Хрустящие красные яблоки'},
            {'name': 'Огурец', 'category': veg_cat, 'price': 180.50, 'description': 'Грунтовые огурцы'},
            {'name': 'Помидор', 'category': veg_cat, 'price': 220.00, 'description': 'Томаты на ветке'},
            {'name': 'Стиральный порошок', 'category': chem_cat, 'price': 450.99, 'description': 'Для белого и цветного белья'},
        ]

        
        for product_data in products_list:
            product, created = Product.objects.get_or_create(**product_data)
            if created:
                self.stdout.write(self.style.SUCCESS(
                    f'Успешно добавлен продукт: {product.name} ({product.category.name})'
                ))
            else:
                self.stdout.write(self.style.WARNING(
                    f'Продукт уже существует: {product.name}'
                ))

        self.stdout.write(self.style.MIGRATE_LABEL('\n=== База данных успешно обновлена! ==='))
