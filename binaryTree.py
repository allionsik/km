class EmptyNode:
    """
    Класс, представляющий пустой узел в бинарном дереве.
    
    Пустой узел используется для обозначения отсутствия левого или правого потомка у узла.
    """
    
    def __repr__(self):
        """
        Возвращает строковое представление пустого узла.
        
        Возвращает:
            str: Символ '*', обозначающий пустой узел.
        """

        return '*'
    
    def insert(self, value):
        """
        Вставляет значение в дерево, создавая новый узел.
        
        Аргументы:
            value: Значение, которое нужно вставить в дерево.
        
        Возвращает:
            BinaryNode: Новый узел с вставленным значением.
        """

        return BinaryNode(EmptyNode(), value, EmptyNode())
    
    def __len__(self):
        """
        Возвращает количество узлов в поддереве.
        
        Возвращает:
            int: 0, так как пустой узел не имеет потомков.
        """

        return 0

    def lcr(self):
        """
        Выполняет центрированный обход пустого узла.
        
        Возвращает:
            list: Пустой список, так как узел пустой.
        """

        return []

    def min(self):
        """
        Возвращает минимальное значение в поддереве.
        
        Raises:
            ValueError: Если дерево пустое и минимальное значение не определено.
        """

        raise ValueError("Минимальное значение не определено для пустого дерева")

    def max(self):
        """
        Возвращает максимальное значение в поддереве.
        
        Raises:
            ValueError: Если дерево пустое и максимальное значение не определено.
        """

        raise ValueError("Максимальное значение не определено для пустого дерева")

class BinaryNode:
    """
    Класс, представляющий узел в бинарном дереве поиска.
    
    Узел содержит значение и ссылки на левого и правого потомков.
    """
    
    def __init__(self, left, value, right):
        """
        Инициализирует узел с заданными потомками и значением.
        
        Аргументы:
            left (BinaryNode или EmptyNode): Левый потомок.
            value: Значение узла.
            right (BinaryNode или EmptyNode): Правый потомок.
        """

        self.left = left    
        self.value = value  
        self.right = right  
        
    def __repr__(self):
        """
        Возвращает строковое представление узла.
        
        Возвращает:
            str: Строковое представление узла в формате (left, value, right).
        """

        return f'({self.left}, {self.value}, {self.right})'
    
    def insert(self, value):
        """
        Вставляет значение в правильное место в дереве.
        
        Аргументы:
            value: Значение, которое нужно вставить.
        
        Возвращает:
            BinaryNode: Текущий узел с обновленными потомками.
        """

        if value < self.value:
            self.left = self.left.insert(value)
        else:
            self.right = self.right.insert(value)
        return self
    
    def __len__(self):
        """
        Возвращает количество узлов в поддереве.
        
        Возвращает:
            int: Количество узлов в поддереве.
        """
        
        return 1 + len(self.left) + len(self.right)

    def lcr(self):
        """
        Выполняет центрированный обход поддерева.
        
        Возвращает:
            list: Список значений в порядке центрированного обхода.
        """

        result = []
        result.extend(self.left.lcr())
        result.append(self.value)
        result.extend(self.right.lcr())
        return result

    def min(self):
        """
        Возвращает минимальное значение в поддереве.
        
        Возвращает:
            int или float: Минимальное значение в поддереве.
        """

        if isinstance(self.left, EmptyNode):
            return self.value
        else:
            return self.left.min()

    def max(self):
        """
        Возвращает максимальное значение в поддереве.
        
        Возвращает:
            int или float: Максимальное значение в поддереве.
        """

        if isinstance(self.right, EmptyNode):
            return self.value
        else:
            return self.right.max()

class BinaryTree:
    """
    Класс, представляющий бинарное дерево поиска.
    
    Дерево содержит методы для вставки, обхода и поиска минимального и максимального значений.
    """
    
    def __init__(self):
        """
        Инициализирует пустое бинарное дерево.
        
        Tree is initially empty.
        """

        self.root = EmptyNode()
        
    def __repr__(self):
        """
        Возвращает строковое представление дерева.
        
        Возвращает:
            str: Строковое представление дерева.
        """

        return repr(self.root)
    
    def insert(self, value):
        """
        Вставляет значение в дерево.
        
        Аргументы:
            value: Значение, которое нужно вставить.
        """

        self.root = self.root.insert(value)
    
    def __len__(self):
        """
        Возвращает количество узлов в дереве.
        
        Возвращает:
            int: Количество узлов в дереве.
        """

        return len(self.root)

    def lcr(self):
        """
        Выполняет центрированный обход дерева.
        
        Возвращает:
            list: Список значений в порядке центрированного обхода.
        """

        return self.root.lcr()

    def min(self):
        """
        Возвращает минимальное значение в дереве.
        
        Возвращает:
            int или float: Минимальное значение в дереве.
        
        Raises:
            ValueError: Если дерево пустое.
        """

        if isinstance(self.root, EmptyNode):
            raise ValueError("Минимальное значение не определено для пустого дерева")
        return self.root.min()

    def max(self):
        """
        Возвращает максимальное значение в дереве.
        
        Возвращает:
            int или float: Максимальное значение в дереве.
        
        Raises:
            ValueError: Если дерево пустое.
        """

        if isinstance(self.root, EmptyNode):
            raise ValueError("Максимальное значение не определено для пустого дерева")
        return self.root.max()