main_menutab         = types.ReplyKeyboardMarkup(row_width=4, resize_keyboard=True, one_time_keyboard=True)
box_type         = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True, one_time_keyboard=True)
marshmallow_type         = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
zefir_type         = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
marshmallow_tastetab   = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True, one_time_keyboard=True)
zefir_1_2  = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True, one_time_keyboard=True)
zefir_1_2_3 = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True, one_time_keyboard=True)
zefir_tastetab = types.ReplyKeyboardMarkup(row_width=3, resize_keyboard=True, one_time_keyboard=True)

Buy           = types.KeyboardButton(text='Зробити замовлення')
Registration           = types.KeyboardButton(text='Реєстрація')
Entrance           = types.KeyboardButton(text='Увійти')
Track           = types.KeyboardButton(text='Відслідкувати')

Marshmallow           = types.KeyboardButton(text='Маршмелоу')
Zefir           = types.KeyboardButton(text='Зефір')
Box_mix           = types.KeyboardButton(text='Бокс-мікс')

Marshmallow1           = types.KeyboardButton(text='Маршмелоу квадратні в прозорому пакуванні (5грншт)')
Marshmallow2           = types.KeyboardButton(text='Маршмелоу в коробці 16шт - 350г (100грн)')
Marshmallow3           = types.KeyboardButton(text='Маршмелоу-лапки 100г (50грн)')
Marshmallow4           = types.KeyboardButton(text='Маршмелоу ваніль 100г (30грн)')

Zefir1           = types.KeyboardButton(text='3шт - 45грн')
Zefir2           = types.KeyboardButton(text='9шт - 135грн')
Zefir3           = types.KeyboardButton(text='15шт - 225грн')

Marshmallow1           = types.KeyboardButton(text='банан-шоколад')
Marshmallow2           = types.KeyboardButton(text='вишня-шоколад')
Marshmallow3           = types.KeyboardButton(text='вишня-арахісова паста')
Marshmallow4           = types.KeyboardButton(text='чорниця-лаванда')
Marshmallow5           = types.KeyboardButton(text='мята-шоколад')
Marshmallow6           = types.KeyboardButton(text='ваніль-мигдаль')

Zefir_1  = types.KeyboardButton(text='1')
Zefir_2  = types.KeyboardButton(text='2')

Zefir__1 = types.KeyboardButton(text='1')
Zefir__2 = types.KeyboardButton(text='2')
Zefir__3 = types.KeyboardButton(text='3')

zefir_tastetab1 = types.KeyboardButton(text='яблуко')
zefir_tastetab2 = types.KeyboardButton(text='полуниця')
zefir_tastetab3 = types.KeyboardButton(text='смородина')
zefir_tastetab4 = types.KeyboardButton(text='банан')
zefir_tastetab5 = types.KeyboardButton(text='вишня')
zefir_tastetab6 = types.KeyboardButton(text='лимон-кокос')
zefir_tastetab7 = types.KeyboardButton(text='лимон-імбир')
zefir_tastetab8 = types.KeyboardButton(text='пряний мандарин')
zefir_tastetab9 = types.KeyboardButton(text='апельсин-ваніль')
zefir_tastetab10 = types.KeyboardButton(text='лайм-мята')
zefir_tastetab11 = types.KeyboardButton(text='слива-грецький горіх')
zefir_tastetab12 = types.KeyboardButton(text='банан-полуниця')
zefir_tastetab13 = types.KeyboardButton(text='полуниця-кокос')
zefir_tastetab14 = types.KeyboardButton(text='снікерс')
zefir_tastetab15 = types.KeyboardButton(text='кава-шоколад')
zefir_tastetab16 = types.KeyboardButton(text='банан-шоколад')
zefir_tastetab17 = types.KeyboardButton(text='глінтвейн')
zefir_tastetab18 = types.KeyboardButton(text='полуниця-шампанське')

main_menutab.add(Buy, Registration, Entrance, Track)
box_type.add(Marshmallow, Zefir, Box_mix)
marshmallow_type.add(Marshmallow1, Marshmallow2, Marshmallow3, Marshmallow4)
zefir_type.add(Zefir1, Zefir2, Zefir3)
marshmallow_tastetab.add(Marshmallow1, Marshmallow2, Marshmallow3, Marshmallow4, Marshmallow5, Marshmallow6)
zefir_1_2.add(Zefir_1, Zefir_2)
zefir_1_2_3.add(Zefir__1, Zefir__2, Zefir__3)
zefir_tastetab.add(zefir_tastetab1, zefir_tastetab2, zefir_tastetab3, zefir_tastetab4, zefir_tastetab5, zefir_tastetab6, zefir_tastetab7, zefir_tastetab8, zefir_tastetab9, zefir_tastetab10, zefir_tastetab11, zefir_tastetab12, zefir_tastetab13, zefir_tastetab14, zefir_tastetab15, zefir_tastetab16, zefir_tastetab17, zefir_tastetab18)
