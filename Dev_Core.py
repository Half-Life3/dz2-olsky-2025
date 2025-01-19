import uuid
from datetime import datetime
from webbrowser import Error


class Item:
    '''
Item (класс предметов, хранящихся на складе)
Item должен иметь уникальный _id, наиминование, описание, дату, в которую он должен быть отправлен а так же множество тегов _tags.
Должен поддерживать добавление и удаление тегов. (В нашей задаче теги это просто строки ненулевой длинны, например "Хрупкий", "Скоропортящийся" и т.д.)
    '''
    _id: str
    name: str
    discryption: str
    dispatch_time: str
    _tags: set[str]
    _cost: int

    def add_tag(self, tag: str):
        return self._tags.add(tag)

    def rm_tag(self, tag: str):
        return self._tags.remove(tag)

    def __init__(self, name: str, discryption: str, dispatch_time: str, tags: str, cost=100):
        # Для Item убедитесь что id всё время генерируется новый
        self._id = uuid.uuid4().hex
        self.name = name
        self.discryption = discryption
        self.dispatch_time = dispatch_time
        self._tags = set(tags.split(", "))
        self._cost = cost

    def __str__(self):
        # Реализацию __str__ продумайте сами, учитывая то что вам может потребоваться знать про эти объекты для дальнейшей работы с ними
        return self.name

    def __repr__(self):
        # Для Item в __repr__ в строку включите первые 3 (или меньше) тега из _tags и его id
        if len(self._tags) >= 3:
            return f"Item: {self._id} with tags:{list(self._tags)[:3]}"
        else:
            return f"Item: {self._id} with tags:{list(self._tags)[:len(self._tags)]}"

    def __len__(self) -> int:
        # Для Item функция len(item) должна возвращать количество тегов этого предмета
        return len(self._tags)

    @property
    def cost(self):
        return self._cost

    @cost.setter
    def cost(self, value):
        if value < 0:
            raise ValueError('Cost cannot be negative')
        self._cost = value

    def __lt__(self, other):
        """Сравнивает товары по количесву*цена"""
        if self.item._cost < other.item._cost:
            return True
        else:
            return False

    def get_id(self):
        return self._id

    def is_tagged(self, tag: str) -> bool:
        return tag in self._tags

    def __getitem__(self, position):
        sorted_item = sorted(self.stacks, key=lambda x: self.stacks[position].item.cost)
        return f"{position + 1} is the {sorted_item[position]}"

    def add_tags(self, tags: str):
        tags = list(tags.split(", "))
        for tag in tags:
            self._tags.add(tag)

    def rm_tags(self, tags: str):
        tags = list(tags.split(", "))
        for tag in tags:
            self._tags.remove(tag)

    def copy(self):
        '''метод copy(self), который возвращает новый item с таким же описанием, ценой и именем, но с другим id'''
        new_item = Item(self.name, self.discryption, self.dispatch_time, str(self._tags), self._cost)
        return new_item


class Hub:
    """
Hub (синглтон, класс объекта нашего склада)
Hub должен поддерживать обращение к предметам по индексам и иметь метод добавления предмета в лист _items,
поле _date с датой в любом формате, а так же быть синглтоном (при любом вызове Hub() возвращается один и тот же инстантс объекта)
    """
    _items: list[Item]
    _date: str
    hub_name: str
    _hub_instance = None

    def add_item(self, item):
        # Измените метод add_item(item) так чтобы он проверял что item действительно является типом Item или его наследником
        if isinstance(item, Item):
            self._items.append(item)
        else:
            raise TypeError("item должен быть экземпляром класса Item или его наследником")

    def __new__(cls, *args, **kwargs):
        # Сделать синглтон
        if cls._hub_instance is None:
            cls._hub_instance = super().__new__(cls)
        return cls._hub_instance

    def __init__(self, date, hub_name):
        self._items: list[Item] = []
        self._date = date
        self.hub_name = hub_name

    def __str__(self):
        # Реализацию __str__ продумайте сами, учитывая то что вам может потребоваться знать про эти объекты для дальнейшей работы с ними
        return self.hub_name

    def __repr__(self):
        # Для Hub в __repr__ в строку включите первые 3 (или меньше) предмета из _items
        if len(self._items) >= 3:
            return f"Hub: {self.hub_name} with items:{self._items[0:3]}"
        else:
            f"Hub: {self.hub_name} with items:{self._items[0:len(self._items)]}"

    def __len__(self):
        # Для Hub функция len(hub) должна возвращать количество предметов на данный момент
        return len(self._items)

    def __getitem__(self, position):
        if 0 <= position < len(self._items):
            return self._items[position]
        else:
            raise IndexError('Бу! Испугался? Ты не бойся')

    def find_by_id(self, item_id) -> str:
        for item in self._items:
            if item_id == item.get_id():
                return f"{self._items.index(item)},{item}"
        return '-1'

    def find_by_tags(self, tags: list) -> list:
        '''Реализуйте метод find_by_tags([tags]), который возвращает контейнер, который содержит все предметы из items у который есть ВСЕ теги из tags
        (для этого будет полезно сделать метод в Items is_tagged(tag) и/или реализуйте в нём итератор по тегам, чтобы не лезть в протектед поле _tags)'''
        result_list = []
        for item in self._items:
            for i in range(len(tags)):
                if item.is_tagged(tags[i]) and i == len(tags) - 1:
                    result_list.append(item)
                elif item.is_tagged(tags[i]):
                    continue
                else:
                    break
        return result_list

    def rm_item(self, i):
        '''Реализуйте метод rm_item(i) который удаляет item с id=i если i это число, или удаляет item=i если i это Item.'''
        if type(i) == str:
            for item in self._items:
                if item.get_id() == i:
                    self._items.remove(item)
        elif type(i) == Item:
            self._items.remove(i)
        else:
            raise TypeError('Неверный тип данных для удаления итема')

    def drop_items(self, items: list):
        """Так же полезным будет метод drop_items(items), который уберает вообще все товары из Hub, которые содержатся в items"""
        for item in items:
            if item in self._items:
                self._items.remove(item)

    def clear(self):
        """Из утилит так же может быть полезен clear() который полностью отчистит весь контейнер _items"""
        items = self._items.copy()
        for item in items:
            self._items.remove(item)
        if len(self) != 0:
            raise Exception("That's was an error")

    @property
    def date(self):
        """Реализуйте метод set_date() и get_date() (или реализуйте поле _date через property) для установки даты в хабе"""
        return self._date

    @date.setter
    def date(self, date):
        date_obj = datetime.strptime(date, "%d.%m.%Y")
        if date_obj.year < 2000:
            raise ValueError('Дата раньше 2000 года')
        self._date = date

    def find_by_date(self, date1, date2=None):
        """Реализуйте метод find_by_date(), который возвращает лист всех Item, подходящих по дате. Реализуйте его таким образом,
        что если в метод передаётся только одна дата, то возвращаются все items с датой раньше или равной ей, а если передаётся две даты,
        тогда все items с датой в этом промежутке (для этого можно использовать *args и смотреть сколько аргументов в явном виде передали).
        В случае если передали слишком много параметров - бросайте ошибку"""
        result_items = []
        date1_obj = datetime.strptime(date1, "%d.%m.%Y")
        if date2:
            date2_obj = datetime.strptime(date2, "%d.%m.%Y")
            for item in self._items:
                date_check_obj = datetime.strptime(item.dispatch_time, "%d.%m.%Y")
                if date1_obj <= date_check_obj <= date2_obj:
                    result_items.append(item)
        else:
            for item in self._items:
                date_check_obj = datetime.strptime(item.dispatch_time, "%d.%m.%Y")
                if date1_obj >= date_check_obj:
                    result_items.append(item)

        return result_items

    def find_most_valuable(self, amount = 1):
        """Добавьте метод find_most_valuable(amount=1) который вернёт первые amount самых дорогих предметов на складе.
        Если предметов на складе меньше чем amount - верните их все"""
        sorted_items = sorted(self._items, key=lambda item: item.cost, reverse=True)
        if amount < len(self._items):
            return sorted_items[:amount]
        else:
            return sorted_items