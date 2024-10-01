


def introspection_info(obj):
    # Получение типа объекта
    type_of_object = type(obj)

    # Получение атрибутов объекта
    attributes = dir(obj)

    # Получение методов объекта
    methods = [method for method in dir(obj) if callable(getattr(obj, method))]

    # Получение модуля, к которому принадлежит объект
    module = getattr(obj, '__module__', None)

    # Дополнительная информация об объекте по типу
    additional_info = {
        "str": lambda s: f"'{s}'",
        "int": lambda i: str(i),
        "float": lambda f: str(f),
        "complex": lambda c: str(c),
        "list": lambda l: f"[{','.join(map(str, l))}]",
        "tuple": lambda t: f"({','.join(map(str, t))})",
        "dict": lambda d: f"{{{','.join(': '.join((k, v)) for k, v in d.items())}}}"
    }

    try:
        additional_info[type(obj)](obj)
    except KeyError:
        pass

    return {
        "type": type_of_object.__name__,
        "attributes": attributes,
        "methods": methods,
        "module": module,
        **additional_info
    }


# Пример использования
number_info = introspection_info(42)
print(number_info)


