#!/usr/bin/env python
# -*- coding: utf-8 -*-
from werkzeug.security import generate_password_hash
import sqlite3
import random


def random_telphone(count=11):
    """
        随机生成XX位的手机号码

        :param count: 手机号长度，默认为11位
        :return: phone_number  生成的手机号
    """
    str = ['139', '138', '137', '136', '135', '134', '159', '158', '157', '150', '151', '152', '188', '187', '182', '183', '184', '178', '130', '131', '132', '156', '155', '186', '185', '176', '133', '153', '189', '180', '181', '177']
    str1 = '0123456789'
    phone_number = random.choice(str)+''.join(random.choice(str1) for i in range(count-3))
    return phone_number

def random_name():
    # 删减部分小众姓氏
    firstName = "赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻水云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳鲍史唐费岑薛雷贺倪汤滕殷罗毕郝邬安常乐于时傅卞齐康伍余元卜顾孟平" \
                "黄和穆萧尹姚邵湛汪祁毛禹狄米贝明臧计成戴宋茅庞熊纪舒屈项祝董粱杜阮席季麻强贾路娄危江童颜郭梅盛林刁钟徐邱骆高夏蔡田胡凌霍万柯卢莫房缪干解应宗丁宣邓郁单杭洪包诸左石崔吉" \
                "龚程邢滑裴陆荣翁荀羊甄家封芮储靳邴松井富乌焦巴弓牧隗山谷车侯伊宁仇祖武符刘景詹束龙叶幸司韶黎乔苍双闻莘劳逄姬冉宰桂牛寿通边燕冀尚农温庄晏瞿茹习鱼容向古戈终居衡步都耿满弘国文东殴沃曾关红游盖益桓公晋楚闫"
    # 百家姓姓氏
    # firstName = "赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许何吕施张孔曹严华金魏陶姜戚谢邹喻柏水窦章云苏潘葛奚范彭郎鲁韦昌马苗凤花方俞任袁柳酆鲍史唐费廉岑薛雷贺倪汤滕殷罗毕郝邬安常乐于时傅皮卞齐康伍余元卜顾孟平" \
    #             "黄和穆萧尹姚邵湛汪祁毛禹狄米贝明臧计伏成戴谈宋茅庞熊纪舒屈项祝董粱杜阮蓝闵席季麻强贾路娄危江童颜郭梅盛林刁钟徐邱骆高夏蔡田樊胡凌霍虞万支柯昝管卢莫经房裘缪干解应宗丁宣贲邓郁单杭洪包诸左石崔吉钮" \
    #             "龚程嵇邢滑裴陆荣翁荀羊於惠甄麴家封芮羿储靳汲邴糜松井段富巫乌焦巴弓牧隗山谷车侯宓蓬全郗班仰秋仲伊宫宁仇栾暴甘钭厉戎祖武符刘景詹束龙叶幸司韶郜黎蓟薄印宿白怀蒲邰从鄂索咸籍赖卓蔺屠蒙池乔阴欎胥能苍" \
    #             "双闻莘党翟谭贡劳逄姬申扶堵冉宰郦雍舄璩桑桂濮牛寿通边扈燕冀郏浦尚农温别庄晏柴瞿阎充慕连茹习宦艾鱼容向古易慎戈廖庾终暨居衡步都耿满弘匡国文寇广禄阙东殴殳沃利蔚越夔隆师巩厍聂晁勾敖融冷訾辛阚那简饶空" \
    #             "曾毋沙乜养鞠须丰巢关蒯相查後荆红游竺权逯盖益桓公晋楚闫法汝鄢涂钦归海帅缑亢况后有琴梁丘左丘商牟佘佴伯赏南宫墨哈谯笪年爱阳佟言福百家姓终"
    # 百家姓中双姓氏
    firstName2="万俟司马上官欧阳夏侯诸葛闻人东方赫连皇甫尉迟公羊澹台公冶宗政濮阳淳于单于太叔申屠公孙仲孙轩辕令狐钟离宇文长孙慕容鲜于闾丘司徒司空亓官司寇仉督子颛孙端木巫马公西漆雕乐正壤驷公良拓跋夹谷宰父谷梁段干百里东郭南门呼延羊舌微生梁丘左丘东门西门南宫南宫"
    # 女孩名字
    girl = '秀娟英华慧巧美娜静淑惠珠翠雅芝玉萍红娥玲芬芳燕彩春菊兰凤洁梅琳素云莲真环雪荣爱妹霞香月莺媛艳瑞凡佳嘉琼勤珍贞莉桂娣叶璧璐娅琦晶妍茜秋珊莎锦黛青倩婷姣婉娴瑾颖露瑶怡婵雁蓓纨仪荷丹蓉眉君琴蕊薇菁梦岚苑婕馨瑗琰韵融园艺咏卿聪澜纯毓悦昭冰爽琬茗羽希宁欣飘育滢馥筠柔竹霭凝晓欢霄枫芸菲寒伊亚宜可姬舒影荔枝思丽'
    # 男孩名字
    boy = '伟刚勇毅俊峰强军平保东文辉力明永健世广志义兴良海山仁波宁贵福生龙元全国胜学祥才发武新利清飞彬富顺信子杰涛昌成康星光天达安岩中茂进林有坚和彪博诚先敬震振壮会思群豪心邦承乐绍功松善厚庆磊民友裕河哲江超浩亮政谦亨奇固之轮翰朗伯宏言若鸣朋斌梁栋维启克伦翔旭鹏泽晨辰士以建家致树炎德行时泰盛雄琛钧冠策腾楠榕风航弘'
    # 名
    name = '中笑贝凯歌易仁器义礼智信友上都卡被好无九加电金马钰玉忠孝'

    # 10%的机遇生成双数姓氏
    if random.choice(range(100))>10:
        firstName_name =firstName[random.choice(range(len(firstName)))]
    else:
        i = random.choice(range(len(firstName2)))
        firstName_name =firstName2[i:i+2]

    sex = random.choice(range(2))
    name_1 = ""

    # 生成并返回一个名字
    if sex > 0:
        girl_name = girl[random.choice(range(len(girl)))]
        if random.choice(range(2)) > 0:
            name_1 = name[random.choice(range(len(name)))]
        return {'name': firstName_name + name_1 + girl_name, 'gender': '女'}
    else:
        boy_name = boy[random.choice(range(len(boy)))]
        if random.choice(range(2)) > 0:
            name_1 = name[random.choice(range(len(name)))]
        return {'name': firstName_name + name_1 + boy_name, 'gender': '男'}

def random_student(sid):
    t = random_name()
    name, gender = t['name'], t['gender']
    department = random.choice((
        '理学部', '信息与工程科学部', '人文学部', '社会科学学部', '经济与管理学部',
    ))
    if department == '理学部':
        faculty = random.choice((
            '数学科学学院', '物理学院', '化学与分子工程学院', '生命科学学院', '城市与环境学院', '地球与空间科学学院', '心理与认知科学学院', '建筑与景观设计学院',
        ))
    elif department == '信息与工程科学部':
        faculty = random.choice((
            '信息科学技术学院', '工学院', '王选计算机研究所', '软件与微电子学院', '环境科学与工程学院', '软件工程国家工程研究中心', '材料科学与工程学院',
        ))
    elif department == '人文学部':
        faculty = random.choice((
            '中国语言文学系历史学系', '考古文博学院哲学系（宗教学系）', '外国语学院艺术学院', '对外汉语教育学院', '歌剧研究院',
        ))
    elif department == '社会科学学部':
        faculty = random.choice((
            '国际关系学院', '法学院信息管理系', '社会学系政府管理学院', '马克思主义学院', '教育学院新闻与传播学院', '体育教研部',
        ))
    elif department == '经济与管理学部':
        faculty = random.choice((
            '经济学院', '光华管理学院', '人口研究所', '国家发展研究院'
        ))

    if department == '理学部':
        major = random.choice((
            '数学与应用数学', '信息与计算科学', '数理基础科学', '物理学', '应用物理学', '核物理', '声学', '化学', '应用化学', '化学生物学',
            '分子科学与工程', '天文学', '地理科学', '自然地理与资源环境', '人文地理与城乡规划', '地理信息科学', '大气科学', '应用气象学', '海洋科学',
            '海洋技术', '海洋资源与环境', '军事海洋学', '地球物理学', '空间科学与技术', '地质学', '地球化学', '地球信息科学与技术', '古生物学',
            '生物科学', '生物技术', '生物信息学', '生态学', '心理学', '应用心理学', '统计学类', '应用统计学',
        ))
    elif department == '信息与工程科学部':
        major = random.choice((
            '计算机科学与技术', '软件工程', '网络工程', '信息安全', '物联网工程', '数字媒体技术', '智能科学与技术', '空间信息与数字技术', '电子与计算机工程',
            '电子信息工程', '电子科学与技术', '通信工程', '微电子科学与工程', '光电信息科学与工程', '信息工程', '广播电视工程', '水声工程', '电子封装技术',
            '集成电路设计与集成系统', '医学信息工程', '电磁场与无线技术', '电波传播与天线', '电子信息科学与技术', '电信工程及管理', '应用电子技术教育',
        ))
    elif department == '人文学部':
        major = random.choice((
            '历史学', '世界史', '考古学', '文物与博物馆学', '文物保护技术', '外国语言与外国历史', '教育学', '科学教育', '人文教育', '教育技术学',
            '艺术教育', '学前教育', '小学教育', '特殊教育', '华文教育', '汉语言文学', '汉语言', '汉语国际教育', '中国少数民族语言文学', '古典文献学',
            '应用语言学', '秘书学', '英语', '俄语', '德语', '法语', '西班牙语', '阿拉伯语', '日语', '波斯语', '朝鲜语', '菲律宾语', '梵语巴利语',
            '印度尼西亚语', '印地语', '柬埔寨语', '老挝语', '缅甸语', '马来语', '蒙古语', '僧伽罗语', '泰语', '乌尔都语', '希伯来语', '越南语',
            '豪萨语', '斯瓦希里语', '阿尔巴尼亚语', '保加利亚语', '波兰语', '捷克语', '斯洛伐克语', '罗马尼亚语', '葡萄牙语', '瑞典语', '塞尔维亚语',
            '土耳其语', '希腊语', '匈牙利语', '意大利语', '泰米尔语', '普什图语', '世界语', '孟加拉语', '尼泊尔语', '克罗地亚语', '荷兰语', '芬兰语',
            '乌克兰语', '挪威语', '丹麦语', '冰岛语', '爱尔兰语', '拉脱维亚语', '立陶宛语', '斯洛文尼亚语', '爱沙尼亚语', '马耳他语', '哈萨克语',
            '乌兹别克语', '祖鲁语', '拉丁语', '翻译', '商务英语', '新闻学', '广播电视学', '广告学', '传播学', '编辑出版学', '网络与新媒体', '数字出版',
        ))
    elif department == '社会科学学部':
        major = random.choice((
            '社会学', '社会工作', '人类学', '女性学', '家政学',
        ))
    elif department == '经济与管理学部':
        major = random.choice((
            '经济学', '经济统计学', '国民经济管理', '资源与环境经济学', '商务经济学', '能源经济', '财政学', '税收学', '金融学', '金融工程', '保险学',
            '投资学', '金融数学', '信用管理', '经济与金融', '国际经济与贸易', '贸易经济', '管理科学', '信息管理与信息系统', '工程管理', '房地产开发与管理',
            '工程造价', '保密管理', '工商管理', '市场营销', '会计学', '财务管理', '国际商务', '人力资源管理', '审计学', '资产评估', '物业管理',
            '文化产业管理', '劳动关系', '体育经济与管理', '财务会计教育', '市场营销教育', '农林经济管理', '农村区域发展', '公共事业管理', '行政管理',
            '劳动与社会保障', '土地资源管理', '城市管理', '海关管理', '交通管理', '海事管理', '公共关系学', '电子商务', '电子商务及法律'
        ))
    _class = str(random.choice(range(1, 13)))

    return (sid, name, gender, department, faculty, major, _class)

def random_leave(sid):
    state = random.choice(('待审批', '已撤回', '审批中', '已驳回', '待销假', '已完成'))
    return (sid, state)

def create_teacher(connection, start_tid, end_tid, role):
    if start_tid < 100000 or end_tid > 199999:
        raise ValueError('教师编号 [100000, 199999]')

    for id in range(start_tid, end_tid):
        user = random_name()
        user['id'] = id
        user['password'] = generate_password_hash('1')
        with connection:
            # 生成
            connection.execute(
                'INSERT INTO teacher(tid,name,gender) VALUES(?,?,?)',
                (user['id'], user['name'], user['gender'])
            )
            # 注册
            connection.execute(
                'INSERT INTO role(rid,password,role) VALUES(?,?,?)',
                (user['id'], user['password'], role)
            )

def create_student(connection, start_sid, end_sid):
    if start_sid < 2000000000 or end_sid > 2999999999:
        raise ValueError('学生编号 [2000000000, 2999999999]')

    stu = role = []
    for id in range(start_sid, end_sid):
        s = random_student(id)
        stu.append(s)
        role.append((s[0], generate_password_hash('1'), '学生'))
    with connection:
        # 生成
        connection.executemany(
            'INSERT INTO student(sid,name,gender,department,faculty,major,class) VALUES(?,?,?,?,?,?,?)', stu
        )
        # 注册
        connection.executemany(
            'INSERT INTO role(rid,password,role) VALUES(?,?,?)', role
        )

def create_leave(connection, start_sid, end_sid):
    return
    if start_sid < 2000000000 or end_sid > 2999999999:
        raise ValueError('学生编号 [2000000000, 2999999999]')
    leaves = []
    for id in range(start_sid, end_sid):
        leave = random_leave(id)
        leaves.append()
    with connection:
        connection.executemany(
            'INSERT INTO leave(sid,state,category,apply_datetime,start_datetime,end_datetime,reason) VALUES(?,?,?,?,?,?,?)',
            leaves
        )

def update_telphone(connection, start_tid, end_tid):
    tel = []
    for id in range(start_tid, end_tid):
        tel.append((random_telphone(), id))
    with connection:
        connection.executemany('UPDATE teacher set telphone=? WHERE tid=?', tel)


def main():
    connection = sqlite3.connect('./db/data.db')
    try:
        # # 生成辅导员信息
        # create_teacher(connection, 100000, 100040, '辅导员')
        # # 生成教务处信息
        # create_teacher(connection, 100041, 100060, '教务处')
        # # 生成考勤人员信息
        # create_teacher(connection, 100061, 100080, '考勤')
        # # 生成学生信息
        # create_student(connection, 2000001001, 2000001200)
        # 生成请假条信息
        create_leave(connection, 2000000000, 2000001000)
        # # 更新教师电话号码
        # update_telphone(connection, 100000, 100080)
    except Exception as e:
        print(e)
    finally:
        connection.close()


if __name__ == '__main__':
    main()
