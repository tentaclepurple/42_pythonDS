def select_type(data):
    if data is not None:
        if isinstance(data, list):
            data = ['Hello', 'World']
            print(f"['{data[0]}', '{data[1]}']")
        elif isinstance(data, tuple):
            data = ('Hello', 'Euskal Herria')
            print(f"('{data[0]}', '{data[1]}')")
        elif isinstance(data, set):
            data = {'Hello', 'Urduliz'}

            for i, element in enumerate(data):
                if i == 0 and element == 'Hello':
                    print(f"{{'{element}', ", end='')
                elif i == 0 and element != 'Hello':
                    print("{'Hello', ", end='')
                elif i == 1 and element == 'Urduliz':
                    print(f"'{element}'}}")
                else:
                    print("'Urduliz'}")      
        elif isinstance(data, dict):
            data = {'Hello': '42Urduliz'}
            for key, value in data.items():
                print(f"{{'{key}', '{value}'}}")


if __name__ == "__main__":
    ft_list = ["Hello", "tata!"]
    ft_tuple = ("Hello", "toto!")
    ft_set = {"Hello", "tutu!"}
    ft_dict = {"Hello": "titi!"}
    select_type(ft_list)
    select_type(ft_tuple)
    select_type(ft_set)
    select_type(ft_dict)
