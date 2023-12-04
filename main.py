import csv

from utils import data_process,result_show2

if __name__ == '__main__':
    input_data='after_process.txt'
    map_box_path=r"D:\code\uav_ponit\UAV_load\data\mapbox.tif"
    pix_data_path="pix_data.txt"
    print("data_process")
    data_process(input_data,map_box_path,pix_data_path)
    print("show")
    result_show2(map_box_path,pix_data_path)