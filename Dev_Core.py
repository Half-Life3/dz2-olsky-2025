import uuid

class Item:
    '''
Item (класс предметов, хранящихся на складе)
Item должен иметь уникальный _id, наиминование, описание, дату, в которую он должен быть отправлен а так же множество тегов _tags. Должен поддерживать добавление и удаление тегов. (В нашей задаче теги это просто строки ненулевой длинны, например "Хрупкий", "Скоропортящийся" и т.д.)
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

    def __init__(self, name: str, discryption: str, dispatch_time: str, tags: str, cost = 100):
        #Для Item убедитесь что id всё время генерируется новый
        self._id = uuid.uuid4().hex
        self.name = name
        self.discryption = discryption
        self.dispatch_time = dispatch_time
        self._tags = set(tags.split(","))
        self._cost = cost

    def __str__(self):
        #Реализацию __str__ продумайте сами, учитывая то что вам может потребоваться знать про эти объекты для дальнейшей работы с ними
        return self.name

    def __repr__(self):
        #Для Item в __repr__ в строку включите первые 3 (или меньше) тега из _tags и его id
        if len(self._tags) >= 3:
            return f"Item: {self._id} with tags:{self._tags[:3]}"
        else:
            return f"Item: {self._id} with tags:{self._tags[:len(self._tags)]}"

    def __len__(self) -> int:
        #Для Item функция len(item) должна возвращать количество тегов этого предмета
        return len(self._tags)

    def set_cost(self, cost: int):
        self._cost = cost
        return f'Значение cost изменено на {cost}'

    def get_cost(self) -> int:
        return self._cost

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
        return f"{position + 1} is the {sorted_stacks[position]}"

class Hub:
    """
Hub (синглтон, класс объекта нашего склада)
Hub должен поддерживать обращение к предметам по индексам и иметь метод добавления предмета в лист _items, поле _date с датой в любом формате, а так же быть синглтоном (при любом вызове Hub() возвращается один и тот же инстантс объекта)
    """
    _items: list[Item]
    _date: str
    hub_name: str
    _hub_instance = None

    def add_item(self, item):
        return self._items.append(item)
    # [i] -> item

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
        #Для Hub в __repr__ в строку включите первые 3 (или меньше) предмета из _items
        if len(self._items) >= 3:
            return f"Hub: {self.hub_name} with items:{self._items[0:3]}"
        else: f"Hub: {self.hub_name} with items:{self._items[0:len(self._items)]}"


    def __len__(self):
        # Для Hub функция len(hub) должна возвращать количество предметов на данный момент
        return len(self._items)

    def __getitem__(self, position):
        if 0 <= position < len(self._items):
            return self._items[position]
        else: raise IndexError('Бу! Испугался? Ты не бойся')

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
            for i in range(len(item._tags)):
                if item.is_tagged(tags[i]):
                    result_list.append(item)
        return result_list
