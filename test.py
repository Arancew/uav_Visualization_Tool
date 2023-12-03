from pyproj import Proj, transform

def convert_coordinates(lon, lat):
    # 定义源坐标系（WGS 84，经纬度坐标系）
    source_crs = Proj(init='epsg:4326')

    # 定义目标坐标系（Web Mercator，3857坐标系）
    target_crs = Proj(init='epsg:3857')

    # 转换坐标
    x, y = transform(source_crs, target_crs, lon, lat)

    return x, y

# 输入经纬度坐标
longitude = 108.91184002161002
latitude = 34.24450601666008

# 转换为3857坐标系
x, y = convert_coordinates(longitude, latitude)

print(f"经度: {longitude}, 纬度: {latitude} 在3857坐标系中的坐标为 x: {x}, y: {y}")
