from process import time_now, Con_MySQL
import csv


def extract_type():
    mysql = Con_MySQL(database='amap_api', user='denny', password='123456', host='192.168.10.31', port=3306)
    cur_mysql = mysql.cursor()
    select_mysql = "SELECT typecode,type,COUNT(*) AS num FROM guangzhou_pois GROUP BY typecode ORDER BY num DESC;"
    cur_mysql.execute(select_mysql)
    with open('guangzhou_poi_type.csv', 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        # 写入columns_name
        writer.writerow(['index', 'typecode', 'type', 'count'])
        index = 0
        for data in cur_mysql.fetchall():
            index += 1
            writer.writerow([index, data[0].replace("'", ""), data[1].replace("'", ""), data[2]])
            print(index, data[2], data[0].replace("'", ""), data[1].replace("'", ""))


if __name__ == '__main__':
    extract_type()