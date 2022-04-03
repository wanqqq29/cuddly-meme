# -*- coding: utf-8 -*-

import pandas as pd
from pandas.core.frame import DataFrame
import hanlp, joblib
from sklearn.ensemble import AdaBoostClassifier
from sklearn import metrics

# 调用hanlp进行分词
hanlp.pretrained.tok.ALL
tok = hanlp.load(hanlp.pretrained.tok.COARSE_ELECTRA_SMALL_ZH)
# 并行处理，将长评论进行分句同时处理
# 第一级管道分句，第二级管道分词和去停用词：
Hanlp = hanlp.pipeline().append(hanlp.utils.rules.split_sentence).append(tok).append(
    lambda sents: remove_stop_words(sents, '../stop.txt'))


# 加载停用词词典
def load_file(filepath):
    with open(filepath, 'r', encoding="utf-8") as f:
        contents = f.readlines()
    result = []
    for content in contents:
        result.append(content.strip())
    return result


# 去除停用词并做特殊处理
def remove_stop_words(text, filepath):
    result = []
    str = ''
    dic = load_file(filepath)
    for k in text:
        for i in k:
            if i not in dic:
                result.append(i)
    ## 对否定词“不、太”做特殊处理，把它与后面的词拼接
    while '不' in result:
        index = result.index('不')
        if index == len(result) - 1:
            break
        result[index:index + 2] = [''.join(result[index:index + 2])]
    # while '太' in result:
    #     index = result.index('太')
    #     if index == len(result) - 1:
    #         break
    #     result[index:index + 2] = [''.join(result[index:index + 2])]
    # while '酒店' in result:
    #     index = result.index('酒店')
    #     if index == len(result) - 1:
    #         break
    #     result[index:index + 2] = [''.join(result[index:index + 2])]
    # while '房间' in result:
    #     index = result.index('房间')
    #     if index == len(result) - 1:
    #         break
    #     result[index:index + 2] = [''.join(result[index:index + 2])]
    # while '住宿' in result:
    #     index = result.index('住宿')
    #     if index == len(result) - 1:
    #         break
    #     result[index:index + 2] = [''.join(result[index:index + 2])]
    # while '旅行社' in result:
    #     index = result.index('旅行社')
    #     if index == len(result) - 1:
    #         break
    #     result[index:index + 2] = [''.join(result[index:index + 2])]
    # while '导游' in result:
    #     index = result.index('导游')
    #     if index == len(result) - 1:
    #         break
    #     result[index:index + 2] = [''.join(result[index:index + 2])]
    # while '吃' in result:
    #     index = result.index('吃')
    #     if index == len(result) - 1:
    #         break
    #     result[index:index + 2] = [''.join(result[index:index + 2])]
    # while '没有' in result:
    #     index = result.index('没有')
    #     if index == len(result) - 1:
    #         break
    #     result[index:index + 2] = [''.join(result[index:index + 2])]

    str = " ".join(result)

    return str


def load_corpus(aaa):
    """
    df批处理
    """
    data = []
    for line in aaa:
        content = Hanlp(line)
        data.append(content)
    return data


def load_text(aaa):
    """
    df批处理
    """
    # 并行处理，将长评论进行分句同时处理
    # 第一级管道分句，第二级管道分词和去停用词：
    data = []
    content = Hanlp(aaa)
    data.append(content)
    return data


def 训练():
    df = pd.read_csv('../csv/test_label.csv')
    df['content'] = load_corpus(df['content'])
    df_train = df.sample(frac=0.8, replace=False, random_state=0, axis=0)
    df_test = df[~df.index.isin(df_train.index)]
    vec = joblib.load('../model/clf_vec.m')
    x_train = vec.fit_transform(df_train['content'])
    y_train = df_train['score']
    x_test = vec.transform(df_test['content'])
    y_test = df_test['score']
    clf = joblib.load('../model/clf_model6000.m')
    bdt = AdaBoostClassifier(clf, algorithm='SAMME.R', n_estimators=1000, learning_rate=0.46)
    bdt.fit(x_train, y_train)
    predictions = bdt.predict(x_test)
    print(metrics.classification_report(y_test, predictions))
    print('准确率:', metrics.accuracy_score(y_test, predictions))
    API_test(vec,bdt,array)

def API(content):
    vec = joblib.load('../model/boost_vec.m')
    bdt = joblib.load('../model/boost.m')
    pre = bdt.predict(vec.transform(load_text(content))).tolist()
    yy_pre = bdt.predict_proba(vec.transform(load_text(content)))
    print(pre[0],yy_pre)
    return pre[0]


def API2(content):
    vec = joblib.load('../model/boost_vec.m')
    bdt = joblib.load('../model/boost.m')
    df = DataFrame({'content': content})
    data = vec.transform(df['content'])
    pre = bdt.predict(data)
    yy_pre = bdt.predict_proba(data)
    print(pre, yy_pre)
    return pre

def API_test(vecc,bdtt,content):
    vec = vecc
    bdt = bdtt
    df = DataFrame({'content': content})
    data = vec.transform(df['content'])
    pre = bdt.predict(data)
    yy_pre = bdt.predict_proba(data)
    print(pre, yy_pre)
    return pre

if __name__ == '__main__':
    array = [
        '1.安排住宿酒店离市区都很远，环境也不足五星标准，行程团餐很难吃2.第四天下午去大理，没有提前告诉我高铁票号，小孩出行用的是户口薄，需要有票号才能取，我到了高铁站工作人员告诉我要票号，我问导游她竟然不知道，还要再去问公司，折腾了好久，另外15：55发车的高铁，13点就把我们送到高铁站，足足等了3小时3.住的酒店离昆明高铁南站只有10分钟路程，为什么让我们昆明站下再坐1小时车到酒店？浪费时间订了那么多次携程，这次的体验差到爆',
        '整个行程几乎都是在交通工具上，坐动车，坐船，坐大巴车，真正玩的时间就半天。第二天回武汉的动车票是晚上9点半的，回到武汉都晚上12点过了，太晚了。行程无任何亮点，都是5个小景点，连神龙架的招牌神农祭坛都不在行程中，来回武汉花了将近一天的时间，景区参观加起来不到3小时，有种被忽悠的感觉，别人问我都不好意思说去过神龙架还有不包伙食的，要交35元每人每餐，第一餐就是船上的食堂盒饭，菜很差，吃完之后盘子就放那种 ** * 桶里。晚上和第二天中午在木鱼镇一个食堂吃的，还过的去，住的神龙山庄酒店还可以，酒店早餐也可以。乘船有2层，一层大厅免费的，但靠窗的位置一桌100元，二楼一桌180元。同样的行程，同一个团的，在途牛网预订的就要便宜几十元。携程就是贵。',
        '旅游团按排的太差，导游讲解不尽责尽力，随便讲一下，不跟团讲解，自己在门口休息，不???导游客如何烧香拜佛，一个非常不称职的导游!',
        '时间安排成问题，各种等待，各种坑。早上五点起来说滑雪场排队。可等导游等了2个多小时。导游素质成问题。因为没有吃40 / 人的团餐。被安排到比别人差的酒店。气愤。',
        '非常差，这是我跟过最差的团', '额，说点啥子好捏，其它的不说，导游的在车上说的一些话反正一定伤到人的心了，，为什么给5星的，因为我也做过服务行业，我确实不忍心，在我眼里只有一星跟五星。',
        '行程安排紧凑，导游热情客气，家庭出游带父母小孩非常合适，能照顾到老人的感受和身体，酒店住的碧桂园，风景不错。张家界和天门山景色优美值得前来游玩',
        '旅行很愉快导游照顾很周到风景很美的一路很顺利导游安排的很妥当过程很快乐也很省事感谢导游的用心安排',
        '导游武阿哥，途中那个男的人很好，服务热情❤️，从接团到散团我们的问题都比较多，因为第一次来湖南吖，想了解的也比较多，问题也是特别多????，大晚上给他打电话还耐心解答，十分感谢你的耐心????✌️。本次出游很满意????????????']
    # 训练()
    API("槟榔谷，顾名思义，这是一个以槟榔树为主题且以观赏休闲为目的的一个景区，作为一个标准的旅友客观的评价一下槟榔谷这个景区，以下属于个人观点，不喜勿喷： （这是逛槟榔谷的最大意义之一，这属于非物质文化遗产了，实话说，奶奶们真的是在织布，但是这不对外销售，这是自己织布自己使用，当然，高价格也可以协商购买，但是对于我一个无产阶级来说，这个东西对我不实用，现在的工厂的产物对我来说已经足够啦，我对手工的作品也没有什么很大的执念，所以我不明白，一件Gucci的手工毛衣可以卖得辣么贵，辣么贵，心疼我这种无产阶级。） 吃：小吃街，里面有海南算是比较特色的小吃，但是我作为海南本土人，兴趣不大，但内地来的朋友们买了菠萝饭，他们觉得还挺好吃的；我们还吃了菠萝，都知道景点的实物都比较贵，但是这里的菠萝虽然贵，但是很甜；还有一个蜂蜜炒椰子肉，那个真的很贵，但是好好吃，可以试吃，朋友们要买，所以我全程都在吃，请尽情的鄙视我吧，我不介意。 喝：请自行准备喝的水，作为一个不喝饮料（饮料只喝椰子水，觉得好作）的我，携带了两瓶矿泉水，小吃街里面有卖饮料，怕麻烦的可以自行去购买哈！ 住：无（我们没住，所以不知道，不怕远的话住山上的度假酒店区感觉还是不错的，我们是从君澜下来的，还行吧!前天晚上住的，没有在槟榔谷这一带住） 行：其实行这一块才是写这篇攻略的最大亮点，嘿嘿，前面的都是铺垫，铺垫。 现在开始进入主题；当我们驾驶车从“呀诺达”到“槟榔谷”的时候，感觉槟榔谷的停车位很给力耶，剩下多少车位一目了然，感觉停个车都好感动。当我们抵达槟榔谷的时候已经是下午2:30左右了，所以要制定一个完美游览计划，我们在槟榔谷的游玩路线是：门口步行直达演出的地点（大概快快步行的话大概需要18-22分钟左右的样子），因为我们看的是2:50的表演，看完演出出来再出来观光。（取票-看表演-观光-返回海口），这个地方一般不会作为主流旅游景点的，因为开大会所以到这里待了几天。这个博鳌亚洲论坛会场自2001年在琼海博鳌开展第一届会议以来，就已经作为博鳌亚洲论坛永久会址，大门口有万国国旗，里面有各种别墅作为住宿酒店，和会场相隔甚远，需要电瓶车接驳。")

    API2(array)
