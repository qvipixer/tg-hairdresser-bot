import aiogram.utils.markdown as fmt

# Разметка для Услуг
msg_services = fmt.text(
    fmt.text("Модельные мужские стрижки (с укладкой и без)"),
    fmt.text("Детские модельные стрижки"),
    fmt.text("Стрижка бороды, чёлки, висков и усов"),
    fmt.text("Стрижки наголо"),
    fmt.text("Женские модельные стрижки на любую длину волос (с укладкой и без)"),
    fmt.text("Различные виды окрашивания"),
    fmt.text("Мелирование и колорирование на любую длину волос"),
    fmt.text("Лечение волос"),
    fmt.text("Торжественные укладки"),
    fmt.text("Вечерние прически"),
    sep="\n",
)

# Разметка для Мастеров
msg_masters = fmt.text(
    fmt.text("Парикмакер Инга"),
    fmt.text("Специализация:"),
    fmt.text("- Коммерческие современные укладки"),
    fmt.text("- Окрашивание в различных техниках, в особенности total blonde, "),
    fmt.text("оттенки тёплых направлений цвета, рыжие"),
    fmt.text("- создание формы прически при помощи стрижки"),
    fmt.text("- перманентная укладка волос"),
    fmt.text("Стаж:"),
    fmt.text("- 9 лет"),
    fmt.text("- Более 3500 довольных гостей"),
    sep="\n",
)

# Разметка для Контактов
msg_contacts = fmt.text(
    fmt.text("+375291234567"),
    sep="\n",
)

# Разметка для Консультация
msg_consult = fmt.text(
    fmt.text("Консультация"),
    sep="\n",
)
