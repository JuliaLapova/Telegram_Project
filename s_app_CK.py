import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")

# Создаем DataFrame с данными и дополнительной строкой заголовков
columns = [
    "ConfigId", 
    #"num", 
    "projectname", 
    "TurnName", 
    "StepName", 
    #"interior", 
    #"bystep", 
    #"byinterior", 
    "RowName", 
    "bu_column", 
    "location_column", 
    "sort_num"
]

# Добавляем вторую строку заголовков
multi_index = pd.MultiIndex.from_tuples(
    [(col, col) for col in columns],
    names=["Наименование", "Подробное наименование"]
)

# Создаем DataFrame с данными
data = {
    # "ConfigId": [6, 5, 2, 9, 8, 6, 6, 6, 6, 6, 6],
    "ConfigName": ['Проекты МО', 'Проекты МО', 'Страна', 'Проекты МО(Нежилое)', 'Проекты Москвы(Нежилое)', 'Проекты МО', 'Проекты МО', 'Проекты МО', 'Проекты МО', 'Проекты МО', 'Проекты МО'],
    "projectname": ["ЛЮБЕРЦЫ", "ЛЮБЕРЦЫ", "ЛЮБЕРЦЫ", "ЛЮБЕРЦЫ", "ЛЮБЕРЦЫ", "ТОМИЛИНО", "ТОМИЛИНО", "ТОМИЛИНО", "ТОМИЛИНО", "ТОМИЛИНО", "ТОМИЛИНО"],
    "TurnName": ["6 очередь", "6 очередь", "6 очередь", "7 очередь", "7 очередь", "3 очередь", "3 очередь", "4 очередь", "4 очередь", "4 очередь", "5 очередь"],
    "StepName": ["1 этап", "2 этап", "3 этап", "1 этап", "2 этап", "1 этап", "2 этап", "1 этап", "2 этап", "3 этап", "1 этап"],
    #"interior": [None, None, None, None, None, None, None, None, None, None, None],
    #"bystep": [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    #"byinterior": [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    "RowName": ["ЛЮБЕРЦЫ 6.1", "ЛЮБЕРЦЫ 6.2", "ЛЮБЕРЦЫ 6.3", "ЛЮБЕРЦЫ 7.1", "ЛЮБЕРЦЫ 7.2", "ТОМИЛИНО 3.1", "ТОМИЛИНО 3.2", "ТОМИЛИНО 4.1", "ТОМИЛИНО 4.2", "ТОМИЛИНО 4.3", "ТОМИЛИНО 5.1"],
    "bu_column": ["БЮ МО"] * 11,
    "location_column": ["МО"] * 11,
    "sort_num": [1000, 1000, 1000, 1000, 1000, 2000, 2000, 2000, 2000, 2000, 2000]
}

df = pd.DataFrame(data)

# Отображаем отфильтрованную таблицу в Streamlit
st.subheader("Сервис для редактирования справочника 'ЦК Проекты' для отчета 'ЦК CRM'")

st.markdown("[Описание в конфлюенс](https://wiki.samoletgroup.ru/pages/viewpage.action?pageId=450200680)")

# Поля ввода для добавления новой строки в одну строку
cols = st.columns(8)
new_config_id = cols[0].selectbox("Группа проектов", options=["Проекты МО", "Страна", "Проекты МО(Нежилое)", "Проекты Москвы(Нежилое)"], help="Группа проектов. Используется для фильтра по проектам.")
#new_num = cols[1].text_input("num", help="Введите номер")
new_projectname = cols[1].selectbox("Проект как в CRM", options=["NOVA", "Квартал Домашний", "Химки Парк", "Квартал Торики"], help="Выберите проект из справочника проектов CRM. Проекта может не быть в CRM, даже если внесены планы.")
new_turnname = cols[2].selectbox("Очередь", options=[f"{i} очередь" for i in range(1, 21)], help="Укажите номер очереди.")
new_stepname = cols[3].selectbox("Этап", options=["Пусто"] + [f"{i} этап" for i in range(1, 11)], help="Укажите номер этапа или оставьте поле пустым.")
#new_interior = cols[5].text_input("interior", help="Введите название интерьера")
#new_bystep = cols[6].text_input("bystep", help="Введите номер по этапу")
#new_byinterior = cols[7].text_input("byinterior", help="Введите номер по интерьеру")
new_rowname = cols[4].text_input("Наименование в отчете", help="Укажите наименование так, как оно должно отображаться в отчете.")
new_bu_column = cols[5].selectbox("Бизнес-Юнит", options=["БЮ МО", "БЮ Москва", "Москва", "Страна"], help="Укажите Бизнес-Юнит.")
new_location_column = cols[6].text_input("Регион", help="Укажите регион.")
new_sort_num = cols[7].text_input("Сортировка", help="Введите номер сортировки, для регулирования местоположения строки в отчете.")

# Проверка выбора проекта
if new_projectname == "Химки Парк":
    st.error("По этому проекту не добавлено ни одного объекта недвижимости в CRM. Нужно завести хотя бы один объект.")

# Кнопка для добавления новой строки
if st.button("Добавить строку"):
    new_row = {
        "ConfigId": new_config_id,
     #   "num": new_num,
        "projectname": new_projectname,
        "TurnName": new_turnname,
        "StepName": new_stepname,
      #  "interior": new_interior,
      #  "bystep": new_bystep,
      #  "byinterior": new_byinterior,
        "RowName": new_rowname,
        "bu_column": new_bu_column,
        "location_column": new_location_column,
        "sort_num": new_sort_num
    }
    df = df.append(new_row, ignore_index=True)
    st.success("Строка добавлена!")
    st.dataframe(df, use_container_width=True)

# Фильтры для таблицы в одной строке
filter_cols = st.columns(4)
configname_filter = filter_cols[0].selectbox("Фильтр по Группе", options=["Все"] + list(df["ConfigName"].unique()))
projectname_filter = filter_cols[1].selectbox("Фильтр по Названию Проекта", options=["Все"] + list(df["projectname"].unique()))
turnname_filter = filter_cols[2].selectbox("Фильтр по Очереди", options=["Все"] + list(df["TurnName"].unique()))
stepname_filter = filter_cols[3].selectbox("Фильтр по Этапу", options=["Все"] + list(df["StepName"].unique()))

# Применение фильтров
filtered_df = df
if configname_filter != "Все":
    filtered_df = filtered_df[filtered_df["ConfigName"] == configname_filter]
if projectname_filter != "Все":
    filtered_df = filtered_df[filtered_df["projectname"] == projectname_filter]
if turnname_filter != "Все":
    filtered_df = filtered_df[filtered_df["TurnName"] == turnname_filter]
if stepname_filter != "Все":
    filtered_df = filtered_df[filtered_df["StepName"] == stepname_filter]


# Кнопка для удаления выбранных строк после фильтров
if st.button("Удалить выбранные строки"):
    if configname_filter != "Все":
        df = df[df["ConfigName"] != configname_filter]
    if projectname_filter != "Все":
        df = df[df["projectname"] != projectname_filter]
    if turnname_filter != "Все":
        df = df[df["TurnName"] != turnname_filter]
    if stepname_filter != "Все":
        df = df[df["StepName"] != stepname_filter]
    st.success("Выбранные строки удалены!")
    st.dataframe(df, use_container_width=True)


# Создаем копию DataFrame с переименованными заголовками для отображения
renamed_df = filtered_df.rename(columns={
    "ConfigName": "Группа проектов",
    "projectname": "Название проекта",
    "TurnName": "Очередь",
    "StepName": "Этап",
    "RowName": "Наименование в отчете",
    "bu_column": "Бизнес-Юнит",
    "location_column": "Регион",
    "sort_num": "Сортировка"
})

# Отображаем отфильтрованную таблицу с новыми заголовками в Streamlit 
st.subheader("Справочник ЦК Проекты")
st.dataframe(renamed_df, use_container_width=True)

# Добавляем кнопку для скачивания Excel файла
if st.button("Скачать Excel"):
    # Создаем Excel файл
    import xlsxwriter

    # Создаем Excel файл
    workbook = xlsxwriter.Workbook('projects_table.xlsx')
    worksheet = workbook.add_worksheet('Projects')



