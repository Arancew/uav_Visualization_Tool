import csv

from utils import data_process,result_show2

if __name__ == '__main__':

    file_name='res2.csv'
    after_name='after_process.txt'
    map_box_path=r"D:\code\uav_ponit\UAV_load\data\mapbox.tif"
    pix_data_path="pix_data.txt"
    #根据你数据的类型，提取出对应的经纬度信息
    #input=res.txt
    fw=open(after_name,'w')
    # with open(file_name, 'r') as f:
    #     while True:
    #         s = f.readline()
    #         if s == '':
    #             break
    #         data,_ = s.split('},')
    #         data=eval(data+'}')
    #         data=data['locate']
    #         fw.write("{},{}\n".format(data[0], data[1]))
    #input 为csv
    with open(file_name, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            long = row['lon']
            lat=row['lat']
            long=eval(long)/1e7
            lat=eval(lat)/1e7
            (lat,long)
            fw.write("{},{}\n".format(lat,long))
    fw.close()
    print("data_process")
    data_process(after_name,map_box_path,pix_data_path)
    print("show")
    result_show2(map_box_path,pix_data_path)