import unittest
from Dev_Core import Item, Hub


class TestItem(unittest.TestCase):
    def test_item_id(self):
        '''Проверка того что у разных Items разные id'''
        item1 = Item('товар1', 'описание товара1', "01.01.2025", "белый, вкусный, сладкий")
        item2 = Item('tovar2', 'opisanie tovara2', '02012025', 'кислый, твердый, вкусный')
        self.assertNotEquals(item1._id, item2._id)
        #pass # Реализуйте проверку того что у разных Items разные id

    def test_len(self):
        '''Проверка того что при добавлении тэгов меняется значение len(item)'''
        item3 = Item('товар1', 'описание товара1', "01.01.2025", "белый, вкусный, сладкий")
        item3.add_tag('дорого')
        self.assertEqual(len(item3), 4)

        #pass # Реализуйте проверку того что при добавлении тэгов меняется значение len(item)

    def test_equal_tags(self):
        '''Проверка того что если к предмету добавить два идентичных тега - их колчество будет один'''
        pass # Реализуйте проверку того что если к предмету добавить два идентичных тега - их колчество будет один
        item3 = Item('товар1', 'описание товара1', "01.01.2025", "белый, вкусный, сладкий")
        item3.add_tag('белый')
        self.assertEqual(len(item3), 3)

    def test_str(self):
        '''Проверка __str__'''
        item3 = Item('товар1', 'описание товара1', "01.01.2025", "белый, вкусный, сладкий")
        self.assertEqual(str(item3), 'товар1')

    def test_is_tagged(self):
        item3 = Item('товар1', 'описание товара1', "01.01.2025", "белый, вкусный, сладкий")
        self.assertTrue(item3.is_tagged)

class TestHub(unittest.TestCase):
    def test_hub_singleton(self):
        '''Проверка того что hub - синглтон' # небольшая документация к тесту'''
        hub1 = Hub('01.01.2025', 'Store$1')
        hub2 = Hub('02.01.2025', 'Store$3')
        self.assertTrue(hub1 is hub2)

    def test_len(self):
        '''Проверка того что при добавлении предметов меняется значение len(item)'''
        hub1 = Hub('01.01.2025', 'Store$1')
        item1 = Item('Tovar1', 'Descryption1', '01.01.2025','tag1, tag2, tag3')
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

    def test_find_by_tags(self):
        hub1 = Hub('01.01.2025', 'Store$1')
        item1 = Item('Tovar1', 'Descryption1', '01.01.2025', 'tag1, tag2, tag3')
        item2 = Item('Tovar2', 'Descryption2', '02.01.2025', 'tag1, tag2, tag3, tag4')
        item3 = Item('Tovar3', 'Descryption3', '03.01.2025', 'tag5, tag6, tag7, tag8')
        item4 = Item('Tovar4', 'Descryption4', '04.01.2025', 'tag1, tag9, tag10, tag11')
        hub1.add_item(item1)
        hub1.add_item(item2)
        hub1.add_item(item3)
        hub1.add_item(item4)
        self.assertEqual(hub1.find_by_tags(['tag1', 'tag2']), 'qwe')


if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)




