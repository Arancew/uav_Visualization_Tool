import cv2
import rasterio

# 打开TIF图像文件
'''
读取一张tif地图，通过像素坐标来获取对应的经纬度信息。
'''
import pyproj
class read_tif:
    def __init__(self,path):
        self.tif_path = path
        self.src=rasterio.open(self.tif_path)
        # 创建EPSG:3857和EPSG:4326（WGS84）坐标系的转换器
        crs3857 = pyproj.CRS("EPSG:3857")
        crs4326 = pyproj.CRS("EPSG:4326")
        # 创建转换器
        self.transformer = pyproj.Transformer.from_crs(crs3857, crs4326, always_xy=True)
    def a4326_to_3857(self,longitude,latitude):
        wgs84 = pyproj.CRS("EPSG:4326")
        web_mercator = pyproj.CRS("EPSG:3857")
        transformer = pyproj.Transformer.from_crs(wgs84, web_mercator, always_xy=True)

        x, y = transformer.transform(longitude, latitude)
        return x,y

    def a3857_to_4326(self,longitude,latitude):
        wgs84 = pyproj.CRS("EPSG:4326")
        web_mercator = pyproj.CRS("EPSG:3857")
        transformer = pyproj.Transformer.from_crs(web_mercator,wgs84, always_xy=True)

        x, y = transformer.transform(longitude, latitude)
        return x,y

    def get_locate(self,x,y):
        lon, lat = self.src.xy(x, y)
        # print(lon,lat)
        return self.transformer.transform(lon,lat)

def result_show2(img_path,data_path):
    start_x = 0
    start_y = 0
    img = cv2.imread(img_path)  # 读取图片
    last = ""
    i = 0
    for line in open(data_path,'r'):
        str_splite = line.split(',')
        cv2.circle(img, (int(str_splite[0]) - start_x, int(str_splite[1]) - start_y), 10, (150, 255, 0), -1)
        if last == "":
            pass
        else:
            cv2.line(img, (int(last[0]) - start_x, int(last[1]) - start_y),
                     (int(str_splite[0]) - start_x, int(str_splite[1]) - start_y), (150, 255, 0), 3)
        last = str_splite
        img_tangle = img.copy()

        cv2.namedWindow("img2", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("img2", 1100, 950)
        cv2.imshow('img2', img_tangle)
        cv2.waitKey(100)

        i += 1

    cv2.waitKey(20000)
    # cv2.imshow('img',img)
    # cv2.waitKey(0)
    cv2.imwrite(r'result.jpg', img)
def data_process(input_data,map_box_path,pix_data_path):
    '''
    :param
    input_data
    输入是一个txt文件路径，其中包含了经纬度：
    例如：
    34.2445358,108.9119574
    34.244536,108.911957
    34.2445361,108.9119566
    34.2445364,108.9119563
    34.2445366,108.9119561
    34.2445371,108.9119558
    34.2445381,108.9119554
    34.2445395,108.9119555
    :return:
    对应经纬度在遥感地图的像素坐标 ，保存在pix_data.txt文件夹中
    例如：
    2391,2440
    2391,2440
    2391,2440
    2391,2440
    2391,2440
    2390,2440
    2390,2440
    2389,2440
    2389,2440
    2389,2440
    '''
    source_tif=read_tif(map_box_path)
    fw=open(pix_data_path,'w')
    f=open(input_data,'r')
    while True:
        s=f.readline()
        print(s)
        if s=='\n' or s=='':
            break
        lat,long=s.split(',')
        long=eval(long)
        lat=eval(lat)
        print(f"经度: {long}, 纬度: {lat}")
        a_,b_=source_tif.a4326_to_3857(long, lat)
        x,y = source_tif.src.index(a_,b_)
        print(x,y)
        fw.write("{},{}\n".format(x,y))
# if __name__=='__main__':
    # file_name='res2.csv'
    # after_name='after_process.txt'
    # map_box_path=r"D:\code\uav_ponit\UAV_load\data\mapbox.tif"
    # pix_data_path="pix_data.txt"
    # data_process(after_name, map_box_path, pix_data_path)