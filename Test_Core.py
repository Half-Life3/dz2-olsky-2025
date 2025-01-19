import unittest
from pprint import pprint

from Dev_Core import Item, Hub


class TestItem(unittest.TestCase):
    def test_item_id(self):
        '''Проверка того что у разных Items разные id'''
        item1 = Item('товар1', 'описание товара1', "01.01.2025", "белый, вкусный, сладкий")
        item2 = Item('tovar2', 'opisanie tovara2', '02012025', 'кислый, твердый, вкусный')
        self.assertNotEqual(item1._id, item2._id)
        # pass # Реализуйте проверку того что у разных Items разные id

    def test_len(self):
        '''Проверка того что при добавлении тэгов меняется значение len(item)'''
        item3 = Item('товар1', 'описание товара1', "01.01.2025", "белый, вкусный, сладкий")
        item3.add_tag('дорого')
        self.assertEqual(len(item3), 4)

        # pass # Реализуйте проверку того что при добавлении тэгов меняется значение len(item)

    def test_equal_tags(self):
        '''Проверка того что если к предмету добавить два идентичных тега - их колчество будет один'''
        pass  # Реализуйте проверку того что если к предмету добавить два идентичных тега - их колчество будет один
        item3 = Item('товар1', 'описание товара1', "01.01.2025", "белый, вкусный, сладкий")
        item3.add_tag('белый')
        self.assertEqual(len(item3), 3)

    def test_str(self):
        '''Проверка __str__'''
        item3 = Item('товар1', 'описание товара1', "01.01.2025", "белый, вкусный, сладкий")
        self.assertEqual(str(item3), 'товар1')

    def test_is_tagged(self):
        item3 = Item('товар1', 'описание товара1', "01.01.2025", "белый, вкусный, сладкий")
        self.assertTrue(item3.is_tagged('вкусный'))

    def test_repr(self):
        item3 = Item('товар1', 'описание товара1', "01.01.2025", "вкусный")
        self.assertEqual(str(item3.__repr__()), f"Item: {item3._id} with tags:['вкусный']")

    def test_get_cost(self):
        item3 = Item('товар1', 'описание товара1', "01.01.2025", "белый, вкусный")
        self.assertEqual(item3.cost, 100)

    def test_set_cost_positive(self):
        item3 = Item('товар1', 'описание товара1', "01.01.2025", "белый, вкусный")
        item3.cost = 101
        self.assertEqual(item3.cost, 101)

    def test_set_cost_negative(self):
        item3 = Item('товар1', 'описание товара1', "01.01.2025", "белый, вкусный")
        with self.assertRaises(ValueError) as context:
            item3.cost = -300
        self.assertEqual(str(context.exception), "Cost cannot be negative")

    def test_add_tags(self):
        item3 = Item('товар1', 'описание товара1', "01.01.2025", "белый, вкусный")
        item3.add_tags('tag1, tag2, белый')
        self.assertEqual(item3._tags, {'tag1', 'tag2', 'белый', 'вкусный'})

    def test_rm_tags(self):
        item3 = Item('товар1', 'описание товара1', "01.01.2025", "белый, вкусный")
        item3.rm_tags('белый')
        self.assertEqual(item3._tags, {'вкусный'})

    def test_copy(self):
        item3 = Item('товар1', 'описание товара1', "01.01.2025", "белый, вкусный")
        item3_copy = item3.copy()
        self.assertEqual(item3.name, item3_copy.name)
        self.assertEqual(item3.discryption, item3_copy.discryption)
        self.assertEqual(item3.dispatch_time, item3_copy.dispatch_time)
        self.assertEqual(item3.cost, item3_copy.cost)


class TestHub(unittest.TestCase):
    def test_hub_singleton(self):
        '''Проверка того что hub - синглтон' # небольшая документация к тесту'''
        hub1 = Hub('01.01.2025', 'Store$1')
        hub2 = Hub('02.01.2025', 'Store$3')
        self.assertTrue(hub1 is hub2)

    def test_len(self):
        '''Проверка того что при добавлении предметов меняется значение len(item)'''
        hub1 = Hub('01.01.2025', 'Store$1')
        item1 = Item('Tovar1', 'Descryption1', '01.01.2025', 'tag1, tag2, tag3')
        item2 = Item('Tovar2', 'Descryption2', '01.01.2025', 'tag1, tag2, tag3, tag4')
        hub1.add_item(item1)
        hub1.add_item(item2)
        self.assertEqual(len(hub1), 2)

    def test_getitem(self):
        hub1 = Hub('01.01.2025', 'Store$1')
        item1 = Item('Tovar1', 'Descryption1', '01.01.2025', 'tag1, tag2, tag3')
        item2 = Item('Tovar2', 'Descryption2', '01.01.2025', 'tag1, tag2, tag3, tag4')
        hub1.add_item(item1)
        hub1.add_item(item2)
        self.assertEqual(hub1[0], item1)
        self.assertEqual(hub1[1], item2)

    def test_getitem_negative(self):
        hub1 = Hub('01.01.2025', 'Store$1')
        item1 = Item('Tovar1', 'Descryption1', '01.01.2025', 'tag1, tag2, tag3')
        item2 = Item('Tovar2', 'Descryption2', '01.01.2025', 'tag1, tag2, tag3, tag4')
        hub1.add_item(item1)
        hub1.add_item(item2)
        self.assertNotEqual(hub1[0], item2)

    def test_find_by_id(self):
        hub1 = Hub('01.01.2025', 'Store$1')
        item1 = Item('Tovar1', 'Descryption1', '01.01.2025', 'tag1, tag2, tag3')
        item2 = Item('Tovar2', 'Descryption2', '01.01.2025', 'tag1, tag2, tag3, tag4')
        hub1.add_item(item1)
        hub1.add_item(item2)
        self.assertEqual(hub1.find_by_id(hub1[0].get_id()), '0,Tovar1')

    def test_find_by_id_negative(self):
        hub1 = Hub('01.01.2025', 'Store$1')
        item1 = Item('Tovar1', 'Descryption1', '01.01.2025', 'tag1, tag2, tag3')
        item2 = Item('Tovar2', 'Descryption2', '01.01.2025', 'tag1, tag2, tag3, tag4')
        hub1.add_item(item1)
        hub1.add_item(item2)
        self.assertEqual(hub1.find_by_id('123'), '-1')

    def test_find_by_tags_hard(self):
        hub1 = Hub('01.01.2025', 'Store$1')
        item1 = Item('Tovar1', 'Descryption1', '01.01.2025', 'tag1, tag2, tag3')
        item2 = Item('Tovar2', 'Descryption2', '02.01.2025', 'tag1, tag2, tag3, tag4')
        item3 = Item('Tovar3', 'Descryption3', '03.01.2025', 'tag5, tag6, tag7, tag2')
        item4 = Item('Tovar4', 'Descryption4', '04.01.2025', 'tag1, tag9, tag2, tag11')
        hub1.add_item(item1)
        hub1.add_item(item2)
        hub1.add_item(item3)
        hub1.add_item(item4)
        result_list = [item1, item2, item4]
        self.assertEqual(hub1.find_by_tags(['tag1', 'tag2']), result_list)

    def test_find_by_tags_easy(self):
        hub1 = Hub('01.01.2025', 'Store$1')
        item1 = Item('Tovar1', 'Descryption1', '01.01.2025', 'tag1, tag2')
        item2 = Item('Tovar2', 'Descryption2', '02.01.2025', 'tag2, tag3')
        hub1.add_item(item1)
        hub1.add_item(item2)
        result_list = [item1]
        self.assertEqual(hub1.find_by_tags(['tag1', 'tag2']), result_list)

    def test_rm_item_type_item(self):
        hub1 = Hub('01.01.2025', 'Store$1')
        item1 = Item('Tovar1', 'Descryption1', '01.01.2025', 'tag1, tag2')
        item2 = Item('Tovar2', 'Descryption2', '02.01.2025', 'tag2, tag3')
        hub1.add_item(item1)
        hub1.add_item(item2)
        hub1.rm_item(item1._id)
        self.assertEqual(hub1.__len__(), 1)

    def test_rm_item_type_id(self):
        hub1 = Hub('01.01.2025', 'Store$1')
        item1 = Item('Tovar1', 'Descryption1', '01.01.2025', 'tag1, tag2')
        item2 = Item('Tovar2', 'Descryption2', '02.01.2025', 'tag2, tag3')
        hub1.add_item(item1)
        hub1.add_item(item2)
        hub1.rm_item(item1)
        self.assertEqual(hub1.__len__(), 1)

    def test_drop_items(self):
        hub1 = Hub('01.01.2025', 'Store$1')
        item1 = Item('Tovar1', 'Descryption1', '01.01.2025', 'tag1, tag2')
        item2 = Item('Tovar2', 'Descryption2', '02.01.2025', 'tag2, tag3')
        item3 = Item('Tovar3', 'Descryption3', '02.01.2025', 'tag2, tag3')
        hub1.add_item(item1)
        hub1.add_item(item2)
        hub1.add_item(item3)
        hub1.drop_items([item1, item2])
        self.assertEqual(len(hub1), 1)

    def test_clear(self):
        hub1 = Hub('01.01.2025', 'Store$1')
        item1 = Item('Tovar1', 'Descryption1', '01.01.2025', 'tag1, tag2')
        item2 = Item('Tovar2', 'Descryption2', '02.01.2025', 'tag2, tag3')
        hub1.add_item(item1)
        hub1.add_item(item2)
        hub1.clear()
        self.assertEqual(len(hub1), 0)

    def test_get_date(self):
        hub1 = Hub('01.01.2025', 'Store$1')
        item1 = Item('Tovar1', 'Descryption1', '01.01.2025', 'tag1, tag2')
        item2 = Item('Tovar2', 'Descryption2', '02.01.2025', 'tag2, tag3')
        hub1.add_item(item1)
        hub1.add_item(item2)
        self.assertEqual(hub1.date, hub1._date)

    def test_set_date_positive(self):
        hub1 = Hub('01.01.2025', 'Store$1')
        item1 = Item('Tovar1', 'Descryption1', '01.01.2025', 'tag1, tag2')
        item2 = Item('Tovar2', 'Descryption2', '02.01.2025', 'tag2, tag3')
        hub1.add_item(item1)
        hub1.add_item(item2)
        hub1.date = '02.02.2022'
        self.assertEqual(hub1.date, '02.02.2022')

    def test_set_date_negative(self):
        hub1 = Hub('01.01.2025', 'Store$1')
        item1 = Item('Tovar1', 'Descryption1', '01.01.2025', 'tag1, tag2')
        item2 = Item('Tovar2', 'Descryption2', '02.01.2025', 'tag2, tag3')
        hub1.add_item(item1)
        hub1.add_item(item2)
        with self.assertRaises(ValueError) as context:
            hub1.date = '02.02.1122'
        self.assertEqual(str(context.exception), "Дата раньше 2000 года")

    def test_find_by_date_1arg(self):
        hub1 = Hub('01.01.2025', 'Store$1')
        item1 = Item('Tovar1', 'Descryption1', '01.01.2025', 'tag1, tag2')
        item2 = Item('Tovar2', 'Descryption2', '02.01.2025', 'tag2, tag3')
        item3 = Item('Tovar3', 'Descryption2', '03.01.2025', 'tag2, tag3')
        hub1.add_item(item1)
        hub1.add_item(item2)
        hub1.add_item(item3)
        self.assertEqual(hub1.find_by_date('02.01.2025'), [item1, item2])

    def test_find_by_date_2args(self):
        hub1 = Hub('01.01.2025', 'Store$1')
        item1 = Item('Tovar1', 'Descryption1', '01.01.2025', 'tag1, tag2')
        item2 = Item('Tovar2', 'Descryption2', '02.01.2025', 'tag2, tag3')
        item3 = Item('Tovar3', 'Descryption2', '03.01.2025', 'tag2, tag3')
        hub1.add_item(item1)
        hub1.add_item(item2)
        hub1.add_item(item3)
        self.assertEqual(hub1.find_by_date('02.01.2025', '03.01.2025'), [item2, item3])

    def test_add_item(self):
        hub1 = Hub('01.01.2025', 'Store$1')
        item1 = Item('Tovar1', 'Descryption1', '01.01.2025', 'tag1, tag2')
        item2 = Item('Tovar2', 'Descryption2', '02.01.2025', 'tag2, tag3')
        item3 = Item('Tovar3', 'Descryption2', '03.01.2025', 'tag2, tag3')
        hub1.add_item(item1)
        hub1.add_item(item2)
        hub1.add_item(item3)
        self.assertEqual(len(hub1), 3)

    def test_add_item_negative(self):
        hub1 = Hub('01.01.2025', 'Store$1')
        with self.assertRaises(TypeError) as context:
            hub1.add_item(123)
        self.assertEqual(str(context.exception), "item должен быть экземпляром класса Item или его наследником")

    def test_most_valuable_positive(self):
        hub1 = Hub('01.01.2025', 'Store$1')
        item1 = Item('Tovar1', 'Descryption1', '01.01.2025', 'tag1, tag2')
        item2 = Item('Tovar2', 'Descryption2', '02.01.2025', 'tag2, tag3')
        item3 = Item('Tovar3', 'Descryption2', '03.01.2025', 'tag2, tag3')
        hub1.add_item(item1)
        hub1.add_item(item2)
        hub1.add_item(item3)
        item1.cost = 100
        item2.cost = 102
        item3.cost = 101
        self.assertEqual(hub1.find_most_valuable(), [item2])

    def test_most_valuable_negative(self):
        hub1 = Hub('01.01.2025', 'Store$1')
        item1 = Item('Tovar1', 'Descryption1', '01.01.2025', 'tag1, tag2')
        item2 = Item('Tovar2', 'Descryption2', '02.01.2025', 'tag2, tag3')
        item3 = Item('Tovar3', 'Descryption2', '03.01.2025', 'tag2, tag3')
        hub1.add_item(item1)
        hub1.add_item(item2)
        hub1.add_item(item3)
        item1.cost = 100
        item2.cost = 102
        item3.cost = 101
        result_items = hub1.find_most_valuable(4)
        self.assertEqual(result_items[0], item2)
        self.assertEqual(result_items[1], item3)
        self.assertEqual(result_items[2], item1)


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
