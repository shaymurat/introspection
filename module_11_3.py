import inspect


def introspection_info(obj):
    '''возвращает словарь содержащий тип, модуль, атрибуты и методы объекта'''
    info = {'type': type(obj).__name__,
            'attributes': [],
            'methods': []}

    for name in dir(obj):
        if callable(getattr(obj, name)):
            info['methods'].append(name)
        else:
            info['attributes'].append(name)

    obj_module = inspect.getmodule(obj)
    if obj_module is None:
        info['module'] = __name__
    else:
        info['module'] = obj_module.__name__

    return info


if __name__ == '__main__':
    from pprint import pprint

    print('*'*20, 42, '*'*20)
    pprint(introspection_info(42), compact=True)
    print()

    print('*'*20, 'introspection_info', '*'*20)
    pprint(introspection_info(introspection_info), compact=True)
    print()

    import humanity
    den = humanity.Human('Денис', 22)
    print('*'*20, 'den', '*'*20)
    pprint(introspection_info(den), compact=True)
    print()

    print('*'*20, 'float', '*'*20)
    pprint(introspection_info(float), compact=True)
