"""
author:魏振东
date：20200331
func：腾讯优图人脸识别
"""
import TencentYoutuyun
import os
from tencent.Draw import Draw
from opdata.opexcel import Operatingexcel

# 输入路径返回有效数据
def youtu(image_path):
    appid = '10151047'
    secret_id = 'AKID59AA4pi1Sis5GIS2tdCe1b7W2T2asTjr'
    secret_key = 'N5mMxsiO6zjIk7Kj3DIPPLG4mOvOjvpk'
    userid = '924271966'
    end_point = TencentYoutuyun.conf.API_YOUTU_END_POINT  # 优图开放平台
    youtu = TencentYoutuyun.YouTu(appid, secret_id, secret_key, userid, end_point)

    req = youtu.DetectFace(image_path=image_path, mode=0, data_type=0)
    return req

# 以字典形式返回有效数据，以及所有图片的长度
def youtu_face():
    # 获取所有文件名称
    imgs = os.listdir("img")
    dic_face = {}
    # 分析人脸，并把人脸数据存储到字典中
    for i in imgs:
        path = "img/{0}".format(i)
        req = youtu(path)
        if req["face"] != [] and req["face"][0] != {}:
            dic_face.setdefault("人脸", []).append(req)
    return dic_face["人脸"],len(imgs)

# gender	Int	性别[0/(female)~100(male)]
def data_gender(list):
    female = 0
    male = 0
    for i in list:
        if int(i)>=50:
            male = male + 1
        else:
            female = female + 1
    return female,male

# glasses	Int	眼镜[0不戴眼镜 1戴眼镜 2戴墨镜] 注：替代原glass（Bool）字段
def data_glasses(list):
    glasses0 = 0
    glasses1 = 0
    glasses2 = 0
    for i in list:
        if int(i)==0:
            glasses0 =  glasses0 + 1
        elif int(i)==0:
            glasses1 = glasses1 + 1
        else:
            glasses2 = glasses2 + 1
    return glasses0,glasses1,glasses2


if __name__ == '__main__':
    d = Draw
    og = Operatingexcel()
    dic_face,len_img = youtu_face()

    """"下载一些图片，包括人像，动物，花朵还有你自己的相片，编程实现识别识别人像，统计人像图片的个数，用饼状图表示占比。"""
    attr = ['人像', '非人像']
    value = [len(dic_face), len_img-len(dic_face)]
    d.drawpie(attr, value,"人像比例")


    # 因为每次分析数据比较麻烦，所以吧数据保存到excel中
    # dict = {}
    # for i in dic_face:
    #     dict.setdefault("性别", []).append(i["face"][0]["gender"])
    #     dict.setdefault("年龄", []).append(i["face"][0]["age"])
    #     dict.setdefault("微笑", []).append(i["face"][0]["expression"])
    #     dict.setdefault("魅力", []).append(i["face"][0]["beauty"])
    #     dict.setdefault("眼镜", []).append(i["face"][0]["glasses"])
    # print(dict)
    # 保存到文件中
    # og.set_excel_dic(dict, "统计信息.xlsx", 0, 0)

    """"对文件夹中的人像图片，测颜值、是否带帽子、戴眼镜等属性并输出。"""
    dicc = og.get_excel_dic("统计信息.xlsx", "Sheet1")

    """性别比例饼状图"""
    female,male = data_gender(dicc["性别"])
    attr = ['female', 'male']
    value = [female, male]
    d.drawpie(attr, value,"男女比例饼状图")

    """"年龄折线图"""
    l = [str(x) for x in range(len(dicc["年龄"]))]
    d.drawline(list1=dicc["年龄"],list4=l,name="年龄折线图")

    """微笑人数饼图"""
    female,male = data_gender(dicc["微笑"])
    attr = ['笑', '不笑']
    value = [female, male]
    d.drawpie(attr, value,"微笑人数饼图")

    """魅力值折线图"""
    l = [str(x) for x in range(len(dicc["魅力"]))]
    d.drawline(list1=dicc["魅力"],list4=l,name="魅力值")

    """"眼镜饼状图"""
    glasses0,glasses1,glasses2 = data_glasses(dicc["眼镜"])
    attr = ['不戴眼镜', '戴眼镜', '戴墨镜']
    value = [glasses0,glasses1,glasses2]
    d.drawpie(attr, value,"眼镜饼状图")